import { existsSync, readFileSync } from "node:fs";
import path from "node:path";
import process from "node:process";
import { fileURLToPath } from "node:url";

import { getDefaultLogRoot, runCodex } from "./runner.js";
import type { CodexRunRequest, CodexSandbox, DoctorResult } from "./types.js";

interface ParsedCli {
  command: "run" | "resume" | "doctor" | "help";
  request?: CodexRunRequest;
}

const SANDBOX_VALUES = new Set<CodexSandbox>(["read_only", "workspace_write", "full_access"]);

export function parseArgs(argv: string[]): ParsedCli {
  const [rawCommand, ...rest] = argv;
  const command = rawCommand === "resume" || rawCommand === "doctor" || rawCommand === "help" ? rawCommand : "run";
  const args = rawCommand && command === rawCommand ? rest : argv;

  if (command === "doctor" || command === "help") {
    return { command };
  }

  let prompt = "";
  let promptFile: string | undefined;
  let live = true;
  let workspace: string | undefined;
  let sandbox: CodexSandbox | undefined;
  let threadId: string | undefined;
  let logRoot: string | undefined;

  for (let index = 0; index < args.length; index += 1) {
    const arg = args[index];
    const next = args[index + 1];

    switch (arg) {
      case "--prompt":
        if (!next) {
          throw new Error("--prompt requires a value.");
        }
        prompt = next;
        index += 1;
        break;
      case "--prompt-file":
        if (!next) {
          throw new Error("--prompt-file requires a value.");
        }
        promptFile = next;
        index += 1;
        break;
      case "--live":
        live = true;
        break;
      case "--dry-run":
        throw new Error("--dry-run is disabled; production Codex SDK execution is live-only.");
      case "--workspace":
        if (!next) {
          throw new Error("--workspace requires a value.");
        }
        workspace = next;
        index += 1;
        break;
      case "--sandbox":
        if (!next || !SANDBOX_VALUES.has(next as CodexSandbox)) {
          throw new Error("--sandbox must be read_only, workspace_write, or full_access.");
        }
        sandbox = next as CodexSandbox;
        index += 1;
        break;
      case "--thread-id":
        if (!next) {
          throw new Error("--thread-id requires a value.");
        }
        threadId = next;
        index += 1;
        break;
      case "--log-root":
        if (!next) {
          throw new Error("--log-root requires a value.");
        }
        logRoot = next;
        index += 1;
        break;
      default:
        throw new Error(`Unknown argument: ${arg}`);
    }
  }

  if (prompt && promptFile) {
    throw new Error("Use either --prompt or --prompt-file, not both.");
  }
  if (promptFile) {
    prompt = readFileSync(promptFile, "utf8");
    if (prompt.charCodeAt(0) === 0xfeff) {
      prompt = prompt.slice(1);
    }
  }
  if (!prompt) {
    throw new Error("--prompt or --prompt-file is required.");
  }
  if (command === "run" && threadId) {
    throw new Error("codex:run does not accept --thread-id; use codex:resume.");
  }
  if (command === "resume" && !threadId) {
    throw new Error("codex:resume requires --thread-id.");
  }

  return {
    command,
    request: {
      mode: command,
      prompt,
      live,
      workspace,
      sandbox,
      threadId,
      logRoot,
    },
  };
}

export async function runDoctor(cwd = process.cwd()): Promise<DoctorResult> {
  let packageScriptsOk = false;
  let packageScriptsDetail = "package.json not found";
  const packagePath = path.join(cwd, "package.json");
  if (existsSync(packagePath)) {
    try {
      const packageJson = JSON.parse(readFileSync(packagePath, "utf8")) as {
        scripts?: Record<string, string>;
      };
      const scripts = packageJson.scripts ?? {};
      const requiredScripts = ["build", "test", "codex:run", "codex:resume", "codex:doctor"];
      packageScriptsOk = requiredScripts.every((script) => script in scripts);
      packageScriptsDetail = requiredScripts.filter((script) => !(script in scripts)).join(", ") || "all required scripts present";
    } catch (error) {
      packageScriptsDetail = error instanceof Error ? error.message : String(error);
    }
  }

  let sdkImportOk = false;
  let sdkImportDetail = "";
  try {
    await import("@openai/codex-sdk");
    sdkImportOk = true;
  } catch (error) {
    sdkImportDetail = error instanceof Error ? error.message : String(error);
  }

  const checks = [
    {
      name: "Node.js >= 18",
      ok: Number.parseInt(process.versions.node.split(".")[0] ?? "0", 10) >= 18,
      detail: process.version,
    },
    { name: "AGENTS.md exists", ok: existsSync(path.join(cwd, "AGENTS.md")) },
    { name: "PROJECT_STATE.md exists", ok: existsSync(path.join(cwd, "PROJECT_STATE.md")) },
    { name: ".codex/config.toml exists", ok: existsSync(path.join(cwd, ".codex", "config.toml")) },
    { name: ".codex/agents directory exists", ok: existsSync(path.join(cwd, ".codex", "agents")) },
    {
      name: "default SDK run log root is outside repository",
      ok: !path.resolve(getDefaultLogRoot()).toLowerCase().startsWith(path.resolve(cwd).toLowerCase()),
      detail: getDefaultLogRoot(),
    },
    {
      name: "package scripts include Codex SDK commands",
      ok: packageScriptsOk,
      detail: packageScriptsDetail,
    },
    {
      name: "built Codex SDK CLI exists",
      ok: existsSync(path.join(cwd, "dist", "src", "codex-sdk", "cli.js")),
    },
    {
      name: "@openai/codex-sdk import works",
      ok: sdkImportOk,
      detail: sdkImportDetail,
    },
  ];
  return { ok: checks.every((check) => check.ok), checks };
}

export function usage(): string {
  return [
    "Codex SDK control layer",
    "",
    "Examples:",
    '  npm.cmd run codex:run -- --prompt "AGENT: Microsoft for 3 years, no current position" --live',
    '  npm.cmd run codex:run -- --prompt-file ".\\prompt.txt" --live',
    '  npm.cmd run codex:run -- --prompt "QUICK: Microsoft" --live',
    '  npm.cmd run codex:resume -- --thread-id "<id>" --prompt "continue" --live',
    "",
    "Default mode is live-only production execution. --dry-run is disabled.",
  ].join("\n");
}

async function main(): Promise<void> {
  try {
    const parsed = parseArgs(process.argv.slice(2));
    if (parsed.command === "help") {
      console.log(usage());
      return;
    }
    if (parsed.command === "doctor") {
      const result = await runDoctor();
      console.log(JSON.stringify(result, null, 2));
      process.exitCode = result.ok ? 0 : 1;
      return;
    }
    if (!parsed.request) {
      throw new Error("Missing run request.");
    }
    const result = await runCodex(parsed.request);
    console.log(JSON.stringify(result, null, 2));
    process.exitCode = result.status === "failed" ? 1 : 0;
  } catch (error) {
    console.error(error instanceof Error ? error.message : String(error));
    console.error("");
    console.error(usage());
    process.exitCode = 1;
  }
}

if (process.argv[1] && fileURLToPath(import.meta.url) === path.resolve(process.argv[1])) {
  void main();
}
