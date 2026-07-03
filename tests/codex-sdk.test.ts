import assert from "node:assert/strict";
import { mkdtemp, readFile, rm, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import path from "node:path";
import test from "node:test";

import { parseArgs, runDoctor } from "../src/codex-sdk/cli.js";
import { buildThreadOptions, getDefaultLogRoot, runCodex } from "../src/codex-sdk/runner.js";

test("parseArgs defaults to live and preserves prompt", () => {
  const parsed = parseArgs(["run", "--prompt", "AGENT: Microsoft for 3 years"]);
  assert.equal(parsed.command, "run");
  assert.equal(parsed.request?.live, true);
  assert.equal(parsed.request?.prompt, "AGENT: Microsoft for 3 years");
});

test("parseArgs reads prompt from file", async () => {
  const tempDir = await mkdtemp(path.join(tmpdir(), "codex-sdk-args-"));
  try {
    const promptPath = path.join(tempDir, "prompt.txt");
    await writeFile(promptPath, "AGENT: Microsoft for 3 years\n", "utf8");
    const parsed = parseArgs(["run", "--prompt-file", promptPath]);
    assert.equal(parsed.request?.prompt, "AGENT: Microsoft for 3 years\n");
    assert.equal(parsed.request?.live, true);
  } finally {
    await rm(tempDir, { recursive: true, force: true });
  }
});

test("parseArgs strips UTF-8 BOM from prompt file", async () => {
  const tempDir = await mkdtemp(path.join(tmpdir(), "codex-sdk-args-"));
  try {
    const promptPath = path.join(tempDir, "prompt-with-bom.txt");
    await writeFile(promptPath, "\ufeffQUICK: Microsoft", "utf8");
    const parsed = parseArgs(["run", "--prompt-file", promptPath]);
    assert.equal(parsed.request?.prompt, "QUICK: Microsoft");
  } finally {
    await rm(tempDir, { recursive: true, force: true });
  }
});

test("parseArgs rejects prompt and prompt-file together", () => {
  assert.throws(
    () => parseArgs(["run", "--prompt", "QUICK: Microsoft", "--prompt-file", "prompt.txt"]),
    /either --prompt or --prompt-file/,
  );
});

test("parseArgs requires thread id for resume", () => {
  assert.throws(() => parseArgs(["resume", "--prompt", "continue"]), /requires --thread-id/);
});

test("parseArgs rejects thread id on run", () => {
  assert.throws(
    () => parseArgs(["run", "--prompt", "continue", "--thread-id", "thread-existing"]),
    /does not accept --thread-id/,
  );
});

test("non-live Codex SDK request is rejected", async () => {
  const result = await runCodex({ mode: "run", prompt: "QUICK: Microsoft", live: false });
  assert.equal(result.status, "failed");
  assert.match(result.error ?? "", /live-only/);
  assert.equal(result.logDir, undefined);
});

test("parseArgs rejects disabled dry-run flag", () => {
  assert.throws(
    () => parseArgs(["run", "--prompt", "QUICK: Microsoft", "--dry-run"]),
    /dry-run is disabled/,
  );
});

test("live run starts a new thread and passes prompt without changing it", async () => {
  const logRoot = await mkdtemp(path.join(tmpdir(), "codex-sdk-test-"));
  const prompt = "AGENT: Microsoft for 3 years, no current position";
  try {
    const result = await runCodex(
      { mode: "run", prompt, live: true, logRoot },
      {
        now: () => new Date("2026-07-02T10:11:12Z"),
        runId: () => "testid01",
        createCodexClient: async () => ({
          startThread: () => ({
            id: "thread-new",
            run: async (receivedPrompt: string) => {
              assert.equal(receivedPrompt, prompt);
              return { finalResponse: "completed" };
            },
          }),
          resumeThread: () => {
            throw new Error("resumeThread should not be used without --thread-id.");
          },
        }),
      },
    );
    assert.equal(result.status, "completed");
    assert.equal(result.threadId, "thread-new");
    assert.ok(result.logDir?.startsWith(logRoot));
    assert.match(result.logDir ?? "", /-\d{3}-testid01$/);
    const manifest = JSON.parse(await readFile(path.join(result.logDir!, "run_manifest.json"), "utf8")) as {
      promptRedacted: string;
      promptSha256: string;
      promptLength: number;
      status: string;
    };
    assert.equal(manifest.promptRedacted, "<redacted>");
    assert.equal(manifest.promptLength, prompt.length);
    assert.match(manifest.promptSha256, /^[a-f0-9]{64}$/);
    assert.equal(manifest.status, "completed");
  } finally {
    await rm(logRoot, { recursive: true, force: true });
  }
});

test("workspace and sandbox are passed to Codex SDK thread options", () => {
  assert.deepEqual(buildThreadOptions({ workspace: "C:\\repo", sandbox: "workspace_write" }), {
    workingDirectory: "C:\\repo",
    sandboxMode: "workspace-write",
  });
  assert.deepEqual(buildThreadOptions({ sandbox: "full_access" }), {
    sandboxMode: "danger-full-access",
  });
});

test("resume run uses resumeThread only when threadId is provided", async () => {
  const logRoot = await mkdtemp(path.join(tmpdir(), "codex-sdk-test-"));
  try {
    const result = await runCodex(
      {
        mode: "resume",
        prompt: "continue",
        live: true,
        threadId: "thread-existing",
        logRoot,
        workspace: "C:\\workspace",
        sandbox: "read_only",
      },
      {
        now: () => new Date("2026-07-02T10:11:12Z"),
        runId: () => "testid02",
        createCodexClient: async () => ({
          startThread: () => {
            throw new Error("startThread should not be used for resume.");
          },
          resumeThread: (threadId: string, options) => {
            assert.equal(threadId, "thread-existing");
            assert.deepEqual(options, { workingDirectory: "C:\\workspace", sandboxMode: "read-only" });
            return {
              id: threadId,
              run: async () => "resumed",
            };
          },
        }),
      },
    );
    assert.equal(result.status, "completed");
    assert.equal(result.threadId, "thread-existing");
  } finally {
    await rm(logRoot, { recursive: true, force: true });
  }
});

test("default log root is outside the repository", () => {
  assert.equal(path.resolve(getDefaultLogRoot()).toLowerCase().startsWith(path.resolve(process.cwd()).toLowerCase()), false);
});

test("doctor checks current repository basics", async () => {
  const result = await runDoctor(process.cwd());
  assert.equal(result.ok, true);
});
