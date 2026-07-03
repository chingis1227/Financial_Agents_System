export type CodexRunStatus = "completed" | "failed";

export type CodexSandbox = "read_only" | "workspace_write" | "full_access";

export interface CodexRunRequest {
  mode: "run" | "resume";
  prompt: string;
  live: boolean;
  workspace?: string;
  sandbox?: CodexSandbox;
  threadId?: string;
  logRoot?: string;
}

export interface CodexRunResult {
  status: CodexRunStatus;
  threadId?: string;
  finalResponse?: string;
  logDir?: string;
  savedReportPath?: string;
  error?: string;
}

export interface DoctorResult {
  ok: boolean;
  checks: Array<{
    name: string;
    ok: boolean;
    detail?: string;
  }>;
}
