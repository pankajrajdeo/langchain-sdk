# Automatically run evaluators on experiments
> Source: [Original LangChain documentation](https://docs.langchain.com/langsmith/bind-evaluator-to-dataset)
LangSmith supports two ways to grade experiments created via the SDK:

* **Programmatically**, by specifying evaluators in your code (see [How to evaluate an LLM application](https://docs.langchain.com/langsmith/evaluate-llm-application) for details)
* By **binding evaluators to a dataset** in the UI. This will automatically run the evaluators on any new experiments created, in addition to any evaluators you've set up via the SDK. This is useful when you're iterating on your application (target function), and have a standard set of evaluators you want to run for all experiments.

## Configuring an evaluator on a dataset

1. In the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-bind-evaluator-to-dataset), select a dataset.
2. Click the **Evaluators** tab.
3. Click **+ Evaluator** to open the **Add Evaluator** panel.
4. Choose one of the following:
   * **Create from scratch**: Build a new [LLM-as-a-Judge](https://docs.langchain.com/langsmith/llm-as-judge), [Code](https://docs.langchain.com/langsmith/online-evaluations-code), or [Composite](https://docs.langchain.com/langsmith/composite-evaluators-ui) evaluator, or select **From labeled data** to create an LLM-as-a-judge evaluator [aligned to human feedback](https://docs.langchain.com/langsmith/improve-judge-evaluator-feedback).
   * **Attach an existing evaluator**: Select an evaluator already in your workspace to reuse it.
   * **Create from a template**: Start from a ready-made evaluator.

> [!NOTE]
> When you configure an evaluator for a dataset, it will only affect the experiment runs that are created after the evaluator is configured. It will not affect the evaluation of experiment runs that were created before the evaluator was configured.

## LLM-as-a-judge evaluators

The process for binding evaluators to a dataset is very similar to the process for configuring an LLM-as-a-judge evaluator in the Playground. View instructions for [configuring an LLM-as-a-judge evaluator in the Playground.](https://docs.langchain.com/langsmith/llm-as-judge?mode=ui)

## Custom code evaluators

The process for binding a code evaluators to a dataset is very similar to the process for configuring a code evaluator in online evaluation. View instruction for [configuring code evaluators](https://docs.langchain.com/langsmith/online-evaluations-code).

The only difference between configuring a code evaluator in online evaluation and binding a code evaluator to a dataset is that the custom code evaluator can reference outputs that are part of the dataset's `Example`.

For custom code evaluators bound to a dataset, the evaluator function takes in two arguments:

* A `Run` ([reference](https://docs.langchain.com/langsmith/run-data-format)). This represents the new run in your experiment. For example, if you ran an experiment via SDK, this would contain the input/output from your chain or model you are testing.
* An `Example` ([reference](https://docs.langchain.com/langsmith/example-data-format)). This represents the reference example in your dataset that the chain or model you are testing uses. The `inputs` to the Run and Example should be the same. If your Example has a reference `outputs`, then you can use this to compare to the run's output for scoring.

The code below shows an example of a simple evaluator function that checks that the outputs exactly equal the reference outputs.

```python
import numpy as np

def perform_eval(run, example):
    # run is a Run object
    # example is an Example object
    output = run['outputs']['output']
    ref_output = example['outputs']['outputs']
    output_match = np.array_equal(output, ref_output)

    return { "exact_match": output_match }
```

```javascript
function perform_eval(run, example) {
    // run is a Run object
    // example is an Example object
    const output = run.outputs.output;
    const refOutput = example.outputs.outputs;

    // Deep equality check for arrays/objects
    const outputMatch = JSON.stringify(output) === JSON.stringify(refOutput);

    return { "exact_match": outputMatch };
}
```

## Next steps

* Analyze your experiment results in the [experiments tab](https://docs.langchain.com/langsmith/analyze-an-experiment)
* Compare your experiment results in the [comparison view](https://docs.langchain.com/langsmith/compare-experiment-results)

***

> [!NOTE]
> [Connect these docs](https://docs.langchain.com/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/bind-evaluator-to-dataset.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
