# Save the agent overview for a session (Beta)
> Source: [Original LangChain documentation](https://docs.langchain.com/langsmith/smith-api/issues-agent/save-the-agent-overview-for-a-session-beta)
/langsmith/langsmith-platform-openapi.json patch /api/v1/platform/sessions/{session_id}/issues-agent/overview
**Beta:** This endpoint is in active development and may change without notice.

Saves the issues agent overview content server-side, creating or updating
the backing private Prompt Hub repo and linking it to the issues agent config.
