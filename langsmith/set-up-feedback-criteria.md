# Set up feedback criteria
> Source: [Original LangChain documentation](https://docs.langchain.com/langsmith/set-up-feedback-criteria)
> [!TIP]
> **Recommended Reading**
>
> Before diving into this content, it might be helpful to read the following:
>
> * [Conceptual guide on tracing and feedback](observability-concepts.md)
> * [Reference guide on feedback data format](feedback-data-format.md)

Feedback criteria are represented in the application as feedback tags. For human feedback, you can set up new feedback criteria as continuous feedback or categorical feedback.

> [!NOTE]
> You can also manage feedback configs programmatically with the SDK. Refer to [Manage feedback & annotation queues programmatically](annotation-queues-sdk.md).

> [!TIP]
> For free-form acceptance criteria a reviewer writes per-run (rather than a fixed set of rubric scores), refer to [Use assertions](assertions.md).

To set up a new feedback criteria, follow [this link](https://smith.langchain.com/settings/workspaces/feedbacks) to view all existing tags for your workspace, then click **New Tag**.

## Continuous feedback

For continuous feedback, you can enter a feedback tag name, then select a minimum and maximum value. Every value, including floating-point numbers, within this range will be accepted as feedback scores.

> **Image:** [Cont feedback](set-up-feedback-criteria.md)

## Categorical feedback

For categorical feedback, you can enter a feedback tag name, then add a list of categories, each category mapping to a score. When you provide feedback, you can select one of these categories as the feedback score.
Both the category label and the score will be logged as feedback in `value` and `score` fields, respectively.

> **Image:** [Cat feedback](set-up-feedback-criteria.md)

***

> [!NOTE]
> [Connect these docs](https://docs.langchain.com/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/set-up-feedback-criteria.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
