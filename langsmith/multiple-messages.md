# Test multi-turn conversations
> Source: [Original LangChain documentation](https://docs.langchain.com/langsmith/multiple-messages)
This how-to guide walks you through the various ways you can set up the Playground for multi-turn conversations, which will allow you to test different tool configurations and system prompts against longer threads of messages.

> **Image:** [Multiturn diagram](multiple-messages.md)

## From an existing run

First, ensure you have properly [traced](observability.md) a multi-turn conversation, and then navigate to your tracing project. Once you get to your tracing project simply open the run, select the LLM call, and open it in the Playground as follows:

> **Image:** [Multiturn from run](multiple-messages.md)

You can then edit the system prompt, tweak the tools and/or output schema and observe how the output of the multi-turn conversation changes.

## From a dataset

Before starting, make sure you have [set up your dataset](manage-datasets-in-application.md). Since you want to evaluate multi-turn conversations, make sure there is a key in your inputs that contains a list of messages.

Once you have created your dataset, head to the Playground and [load your dataset](manage-datasets-in-application.md#from-the-playground) to evaluate.

Then, add a messages list variable to your prompt, making sure to name it the same as the key in your inputs that contains the list of messages:

> **Image:** [Multiturn from dataset](multiple-messages.md)

When you run your prompt, the messages from each example will be added as a list in place of the 'Messages List' variable.

## Manually

There are two ways to manually create multi-turn conversations. The first way is by simply appending messages to the prompt:

> **Image:** [Multiturn manual](multiple-messages.md)

This is helpful for quick iteration, but is rigid since the multi-turn conversation is hardcoded. Instead, if you want your prompt to work with any multi-turn conversation you can add a 'Messages List' variable and add your multi-turn conversation there:

> **Image:** [Multiturn manual list](multiple-messages.md)

This allows you to just tweak the system prompt or the tools, while allowing any multi-turn conversation to take the place of the `Messages List` variable, allowing you to reuse this prompt across various runs.

## Next steps

Now that you know how to set up the Playground for multi-turn interactions, you can either manually inspect and judge the outputs, or you can [add evaluators](code-evaluator-ui.md) to classify results.

You can also read [these how-to guides](create-a-prompt.md) to learn more about how to use the Playground to run evaluations.

***

> [!NOTE]
> [Connect these docs](https://docs.langchain.com/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/multiple-messages.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
