# Update the issues agent config for a session (Beta)
> Source: [Original LangChain documentation](https://docs.langchain.com/langsmith/smith-api/issues-agent/update-the-issues-agent-config-for-a-session-beta)
/langsmith/langsmith-platform-openapi.json patch /api/v1/platform/sessions/{session_id}/issues-agent
**Beta:** This endpoint is in active development and may change without notice.

Patches the agent config. All side effects (clearing fix fields when
the GitHub repo changes, setting agent_overview_repo_id) happen in a
single CRUD transaction. Omitted fields are left unchanged.
