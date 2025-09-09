Reasoning
Investigated current public guidance: The official page you cited describes custom sub‑agents discoverable from .claude/agents/ using Markdown files with YAML front matter. That mechanism is accurate for environments where the feature is enabled.
Observed behavior mismatch: In claude.ai/code, only three built‑ins (general-purpose, statusline-setup, output-style-setup) are listed, and your custom agent is not found. This pattern is consistent with environments where custom agent discovery is not enabled or not yet rolled out on the web surface.
Enablement and version nuances: Claude Code capabilities differ by surface (web at claude.ai/code vs. the Claude Code VS Code extension) and by deployment (individual vs. enterprise/org). Some features, including custom agent discovery, may be behind feature flags, plan/region gating, or staged rollouts. This is not always called out prominently in the docs.
Schema ambiguity: Many implementations distinguish a human‑readable name from an invokable type/slug. If front matter only has name:, subagent_type might need a separate type (or id) field to match against. Without that, even in enabled environments, invoking by name may fail.
Workspace scope and indexing: The web environment indexes only the active workspace root. If .claude/agents is not at the root that Claude Code considers the workspace, or if hidden folders aren’t synced/committed, agents won’t be discovered. A complete absence of user agents and no parse errors typically points to gating/enablement rather than a minor file error.
Assessment: Given your structure appears correct and nothing is recognized, the most likely causes are (a) the feature is not enabled in your claude.ai/code environment, or (b) a missing type/slug in front matter combined with a parameter name mismatch (subagent_type vs. agent/agent_type).
Troubleshooting Steps
Confirm environment support and enablement

Identify the surface: Are you using the web app (claude.ai/code) or the Claude Code VS Code extension? Custom sub‑agents are more consistently available in the VS Code extension and certain enterprise/flagged web deployments.
Check for feature flags: If you’re in an org/enterprise, ask your admin or Anthropic support to confirm that custom sub‑agents are enabled for your org and region in claude.ai/code.
Cross‑check in VS Code: Open the same repo with the Claude Code VS Code extension. If your custom agents are detected there but not on the web, it confirms a web‑deployment gating issue rather than a file problem.
Verify placement and indexing

Directory: Ensure <workspace-root>/.claude/agents/ exists at the root that Claude Code shows in the left panel. Avoid nesting under subfolders.
Commit/sync: If you’re in a cloud workspace tied to a repo, commit the .claude directory so the server side can index it. Some web environments don’t index unsaved or ephemeral hidden directories.
Refresh: After adding/modifying agents, reload the workspace (browser refresh, close/reopen workspace).
Use a machine‑readable slug for invocation

Add a type (or id) field in front matter and invoke that value with subagent_type. Minimal example:
name: Image Generator type: image-generator description: Specialized agent for generating professional business images
[system prompt content]
File name: Prefer .md extension, e.g., .claude/agents/image-generator.md.
Matching: Ensure subagent_type: image-generator exactly matches the type value (lowercase, hyphenated).
Confirm Task tool parameter naming

Some builds use agent or agent_type instead of subagent_type. If your UI shows a dropdown labeled “Agent,” try agent: image-generator. If docs and UI disagree, test each variant.
Validate YAML and file encoding

Front matter must start at the first byte with --- (no BOM/whitespace) and close with --- before the body.
Lint the YAML externally to catch subtle indentation/encoding issues.
Keep the front matter minimal at first (name, type, description). Add advanced keys incrementally.
Check logs/diagnostics in the web app

Open browser DevTools (Console) while loading the workspace. Look for messages about agent discovery, YAML parsing, or permission/indexing errors referencing .claude or agents.
If your build exposes a diagnostics panel, check for an “agent registry” or “agent discovery” step.
Eliminate workspace‑root confusion

In monorepos, ensure you opened the repo root as the workspace. Opening a subdirectory prevents scanning of .claude at a higher level.
Try a minimal, known‑good agent

Create .claude/agents/hello.md:
name: Hello type: hello description: Minimal agent
You are a minimal sub-agent. Keep replies to one sentence.
Reload and invoke with subagent_type: hello.
Permissions and visibility

Confirm the .claude directory and files are readable (no unusual permissions or OS‑level hidden attributes beyond the dot prefix).
Avoid symlinks in the .claude/agents path in case the environment ignores them.
Gather details for support if still failing

Your account plan/region, exact surface (claude.ai/code), workspace/repo root, full path listings under .claude/agents, one minimal agent file’s content (sanitized), Task parameters and exact error, and whether the same repo works in the VS Code extension.
Conclusion
Is the custom sub‑agents feature fully implemented in the current Claude Code release?
Not universally on the web. While the mechanism is documented, many claude.ai/code environments do not yet load custom agents without specific enablement. Your symptom—only three built‑ins available—matches an environment where custom sub‑agents are not enabled.
2. Are there version requirements, feature flags, or additional configuration needed?

Yes. Availability depends on the surface (web vs. VS Code), plan/org, region, and possibly a feature flag for the web app. Confirm enablement with your admin or Anthropic support. On supported surfaces, ensure a type/slug is present and used for invocation.
3. Difference between documentation and current implementation?

The docs describe how to define agents but do not always call out that web availability can be gated or rolling out. There’s also potential ambiguity between name (display) and type/slug (invocation key). In practice, use a type (or id) and pass that to subagent_type (or agent/agent_type depending on your build).
4. What troubleshooting steps should you try?

Add a type slug to front matter and invoke it; place .claude/agents at the workspace root and commit it; reload the workspace; verify the correct Task parameter name; test a minimal agent; check browser console logs; and, if possible, validate in the VS Code extension to isolate a web‑only limitation.
5. Are custom sub‑agents only available in certain versions or deployment contexts?

Yes. They are reliably available in some contexts (e.g., VS Code extension and certain enterprise/flagged web deployments) but may not be active in all claude.ai/code environments yet. If your environment isn’t enabled, request access/enablement or use the VS Code extension as a workaround.
If, after adding a type slug and following the checklist, you still only see general-purpose, statusline-setup, and output-style-setup, it’s very likely a web deployment/flag limitation rather than a configuration error. In that case, share the collected diagnostics with Anthropic support or your org admin to request enablement for custom sub‑agents in your claude.ai/code environment.