import { mkdir, writeFile } from "node:fs/promises";
import { createHash, randomUUID } from "node:crypto";
import path from "node:path";

import type { SandboxMode, ThreadOptions } from "@openai/codex-sdk";
import type { CodexRunRequest, CodexRunResult } from "./types.js";

interface CodexThreadLike {
  id?: string;
  run(prompt: string): Promise<unknown>;
}

interface CodexClientLike {
  startThread(options?: ThreadOptions): CodexThreadLike;
  resumeThread(threadId: string, options?: ThreadOptions): CodexThreadLike;
}

export type CodexClientFactory = () => Promise<CodexClientLike>;

export interface RunCodexDeps {
  createCodexClient?: CodexClientFactory;
  now?: () => Date;
  runId?: () => string;
}

export function getDefaultLogRoot(): string {
  const userProfile = process.env.USERPROFILE ?? process.env.HOME ?? process.cwd();
  return path.join(
    userProfile,
    "OneDrive",
    "Documents",
    "Financial Agent Reports",
    "_sdk_runs",
  );
}

export function formatRunTimestamp(date: Date): string {
  const pad = (value: number) => String(value).padStart(2, "0");
  return `${date.getFullYear()}-${pad(date.getMonth() + 1)}-${pad(date.getDate())} ${pad(
    date.getHours(),
  )}${pad(date.getMinutes())}${pad(date.getSeconds())}`;
}

export function buildRunLogDir(
  request: Pick<CodexRunRequest, "logRoot">,
  date: Date,
  runId = randomUUID().slice(0, 8),
): string {
  const ms = String(date.getMilliseconds()).padStart(3, "0");
  return path.join(request.logRoot ?? getDefaultLogRoot(), `${formatRunTimestamp(date)}-${ms}-${runId}`);
}

export function extractFinalResponse(result: unknown): string {
  if (typeof result === "string") {
    return result;
  }
  if (result && typeof result === "object") {
    const record = result as Record<string, unknown>;
    for (const key of ["finalResponse", "final_response", "output", "text"]) {
      if (typeof record[key] === "string") {
        return record[key];
      }
    }
    return JSON.stringify(record, null, 2);
  }
  return String(result ?? "");
}

export function extractThreadId(thread: CodexThreadLike, result: unknown, fallback?: string): string | undefined {
  if (typeof thread.id === "string" && thread.id.length > 0) {
    return thread.id;
  }
  if (result && typeof result === "object") {
    const record = result as Record<string, unknown>;
    if (typeof record.threadId === "string") {
      return record.threadId;
    }
    if (typeof record.thread_id === "string") {
      return record.thread_id;
    }
  }
  return fallback;
}

export function extractSavedReportPath(finalResponse: string): string | undefined {
  const match = finalResponse.match(/[A-Z]:\\[^\r\n*?"<>|]+\\investment_report\.md/i);
  return match?.[0];
}

export function buildThreadOptions(request: Pick<CodexRunRequest, "workspace" | "sandbox">): ThreadOptions {
  const sandboxMap: Record<NonNullable<CodexRunRequest["sandbox"]>, SandboxMode> = {
    read_only: "read-only",
    workspace_write: "workspace-write",
    full_access: "danger-full-access",
  };
  return {
    ...(request.workspace ? { workingDirectory: request.workspace } : {}),
    ...(request.sandbox ? { sandboxMode: sandboxMap[request.sandbox] } : {}),
  };
}

export function sha256Text(text: string): string {
  return createHash("sha256").update(text, "utf8").digest("hex");
}

async function createDefaultCodexClient(): Promise<CodexClientLike> {
  const module = await import("@openai/codex-sdk");
  const Codex = module.Codex as new () => CodexClientLike;
  return new Codex();
}

async function writeRunLog(
  request: CodexRunRequest,
  result: CodexRunResult,
  logDir: string,
  startedAt: Date,
): Promise<void> {
  await mkdir(logDir, { recursive: true });
  const manifest = {
    startedAt: startedAt.toISOString(),
    completedAt: new Date().toISOString(),
    live: request.live,
    workspace: request.workspace ?? process.cwd(),
    sandbox: request.sandbox,
    threadId: result.threadId,
    status: result.status,
    savedReportPath: result.savedReportPath,
    promptRedacted: "<redacted>",
    promptSha256: sha256Text(request.prompt),
    promptLength: request.prompt.length,
  };
  await writeFile(path.join(logDir, "run_manifest.json"), `${JSON.stringify(manifest, null, 2)}\n`, "utf8");
  if (result.finalResponse) {
    await writeFile(path.join(logDir, "final_response.md"), result.finalResponse, "utf8");
  }
  if (result.error) {
    await writeFile(path.join(logDir, "error.md"), result.error, "utf8");
  }
}

export async function runCodex(request: CodexRunRequest, deps: RunCodexDeps = {}): Promise<CodexRunResult> {
  if (!request.prompt.trim()) {
    return { status: "failed", error: "Missing required prompt." };
  }
  if (request.mode === "run" && request.threadId) {
    return { status: "failed", error: "codex:run does not accept threadId; use codex:resume instead." };
  }
  if (request.mode === "resume" && !request.threadId) {
    return { status: "failed", error: "codex:resume requires threadId." };
  }

  if (!request.live) {
    return {
      status: "dry_run",
      threadId: request.threadId,
      finalResponse: `Dry run only. No Codex SDK thread was started.\n\nPrompt:\n${request.prompt}`,
    };
  }

  const startedAt = deps.now?.() ?? new Date();
  const logDir = buildRunLogDir(request, startedAt, deps.runId?.());

  try {
    const client = await (deps.createCodexClient ?? createDefaultCodexClient)();
    const threadOptions = buildThreadOptions(request);
    const thread = request.mode === "resume"
      ? client.resumeThread(request.threadId!, threadOptions)
      : client.startThread(threadOptions);
    const rawResult = await thread.run(request.prompt);
    const finalResponse = extractFinalResponse(rawResult);
    const result: CodexRunResult = {
      status: "completed",
      threadId: extractThreadId(thread, rawResult, request.threadId),
      finalResponse,
      logDir,
      savedReportPath: extractSavedReportPath(finalResponse),
    };
    await writeRunLog(request, result, logDir, startedAt);
    return result;
  } catch (error) {
    const errorMessage = error instanceof Error ? `${error.name}: ${error.message}` : String(error);
    const result: CodexRunResult = {
      status: "failed",
      threadId: request.threadId,
      logDir,
      error: errorMessage,
    };
    await writeRunLog(request, result, logDir, startedAt);
    return result;
  }
}
