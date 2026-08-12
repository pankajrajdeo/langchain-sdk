> ## Documentation Index
> Fetch the complete documentation index at: https://docs.langchain.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Johnsnowlabs integrations

> Integrate with Johnsnowlabs using LangChain Python.

Gain access to the [johnsnowlabs](https://www.johnsnowlabs.com/) ecosystem of enterprise NLP libraries
with over 21.000 enterprise NLP models in over 200 languages with the open source `johnsnowlabs` library.
For all 24.000+ models, see the [John Snow Labs Model Models Hub](https://nlp.johnsnowlabs.com/models)

## Installation and setup

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install johnsnowlabs
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add johnsnowlabs
  ```
</CodeGroup>

To \[install enterprise features]\([https://nlp.johnsnowlabs.com/docs/en/jsl/install\_licensed\_quick](https://nlp.johnsnowlabs.com/docs/en/jsl/install_licensed_quick), run:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
# for more details see https://nlp.johnsnowlabs.com/docs/en/jsl/install_licensed_quick
nlp.install()
```

You can embed your queries and documents with either `gpu`,`cpu`,`apple_silicon`,`aarch` based optimized binaries.
By default cpu binaries are used.
Once a session is started, you must restart your notebook to switch between GPU or CPU, or changes will not take effect.

## Embed query with CPU:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
document = "foo bar"
embedding = JohnSnowLabsEmbeddings('embed_sentence.bert')
output = embedding.embed_query(document)
```

## Embed query with GPU:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
document = "foo bar"
embedding = JohnSnowLabsEmbeddings('embed_sentence.bert','gpu')
output = embedding.embed_query(document)
```

## Embed query with apple silicon (M1,M2,etc..):

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
documents = ["foo bar", 'bar foo']
embedding = JohnSnowLabsEmbeddings('embed_sentence.bert','apple_silicon')
output = embedding.embed_query(document)
```

## Embed query with AARCH:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
documents = ["foo bar", 'bar foo']
embedding = JohnSnowLabsEmbeddings('embed_sentence.bert','aarch')
output = embedding.embed_query(document)
```

## Embed document with CPU:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
documents = ["foo bar", 'bar foo']
embedding = JohnSnowLabsEmbeddings('embed_sentence.bert','gpu')
output = embedding.embed_documents(documents)
```

## Embed document with GPU:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
documents = ["foo bar", 'bar foo']
embedding = JohnSnowLabsEmbeddings('embed_sentence.bert','gpu')
output = embedding.embed_documents(documents)
```

## Embed document with apple silicon (M1,M2,etc..):

````python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
```python
documents = ["foo bar", 'bar foo']
embedding = JohnSnowLabsEmbeddings('embed_sentence.bert','apple_silicon')
output = embedding.embed_documents(documents)
````

## Embed Document with AARCH:

````python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
```python
documents = ["foo bar", 'bar foo']
embedding = JohnSnowLabsEmbeddings('embed_sentence.bert','aarch')
output = embedding.embed_documents(documents)
````

Models are loaded with [nlp.load](https://nlp.johnsnowlabs.com/docs/en/jsl/load_api) and spark session is started with [nlp.start()](https://nlp.johnsnowlabs.com/docs/en/jsl/start-a-sparksession) under the hood.

***

<div className="source-links">
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/johnsnowlabs.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
