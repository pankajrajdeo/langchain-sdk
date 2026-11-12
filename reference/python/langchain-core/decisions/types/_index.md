---
title: "reference/python/langchain-core/decisions/types"
description: "Index of 16 pages and 12 subdirectories under reference/python/langchain-core/decisions/types."
category: "index"
tags: [index, reference, python, langchain-core, decisions, types]
---

# reference/python/langchain-core/decisions/types

16 pages here, 62 pages including subdirectories.

## Directories

- [Box/](Box/_index.md) - 3 pages
- [BoxAnswer/](BoxAnswer/_index.md) - 3 pages
- [BoxCoordinates/](BoxCoordinates/_index.md) - 4 pages
- [Choice/](Choice/_index.md) - 4 pages
- [ChoiceAnswer/](ChoiceAnswer/_index.md) - 4 pages
- [ClassifierRequest/](ClassifierRequest/_index.md) - 2 pages
- [ClassifierResponse/](ClassifierResponse/_index.md) - 8 pages
- [Noul/](Noul/_index.md) - 4 pages
- [NoulAnswer/](NoulAnswer/_index.md) - 2 pages
- [NoulCriteria/](NoulCriteria/_index.md) - 3 pages
- [Score/](Score/_index.md) - 4 pages
- [ScoreAnswer/](ScoreAnswer/_index.md) - 5 pages

## Files

- [Answer](Answer.md) - A discriminated union of answers returned by decision models.
- [Box](Box.md) - Locate what the instructions describe in an image in the state.
- [BoxAnswer](BoxAnswer.md) - Location of what a Box question describes.
- [BoxCoordinates](BoxCoordinates.md) - Edges of a box as fractions of the image height and width, from 0 to 1.
- [Choice](Choice.md) - Select one label from a fixed set of alternatives.
- [ChoiceAnswer](ChoiceAnswer.md) - Selected Choice label with its probability distribution and confidence.
- [ClassifierRequest](ClassifierRequest.md) - Complete input for one decision model invocation.
- [ClassifierResponse](ClassifierResponse.md) - Typed answers and metadata returned from one classification request.
- [Content](Content.md) - Type Alias in langchain_core
- [Noul](Noul.md) - Ask a binary question and receive the probability that its answer is yes.
- [NoulAnswer](NoulAnswer.md) - Probability that a Noul question's answer is yes.
- [NoulCriteria](NoulCriteria.md) - Optional descriptions for the two outcomes of a Noul question.
- [Question](Question.md) - A discriminated union of question types accepted by decision models.
- [Score](Score.md) - Evaluate state against an ordered rubric.
- [ScoreAnswer](ScoreAnswer.md) - Expected Score value with its rubric, distribution, and confidence.
- [State](State.md) - Type Alias in langchain_core
