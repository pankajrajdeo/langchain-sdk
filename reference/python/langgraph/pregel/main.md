---
title: "main"
description: "- CACHE_NS_WRITES - CONF - CONFIG_KEY_CACHE - CONFIG_KEY_CHECKPOINT_ID - CONFIG_KEY_CHECKPOINT_NS - CONFIG_KEY_CHECKPOINTER - CONFIG_KEY_DURABILITY - CONFIG_KEY_NODE_FINISHED - CONFIG_KEY_READ -..."
source: "https://reference.langchain.com/python/langgraph/pregel/main"
category: "reference"
tags: [reference, langgraph, pregel, main]
---

# main

> **Module** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/main)

## Properties

- `CACHE_NS_WRITES`
- `CONF`
- `CONFIG_KEY_CACHE`
- `CONFIG_KEY_CHECKPOINT_ID`
- `CONFIG_KEY_CHECKPOINT_NS`
- `CONFIG_KEY_CHECKPOINTER`
- `CONFIG_KEY_DURABILITY`
- `CONFIG_KEY_NODE_FINISHED`
- `CONFIG_KEY_READ`
- `CONFIG_KEY_RUNNER_SUBMIT`
- `CONFIG_KEY_RUNTIME`
- `CONFIG_KEY_SEND`
- `CONFIG_KEY_STREAM`
- `CONFIG_KEY_STREAM_MESSAGES_V2`
- `CONFIG_KEY_TASK_ID`
- `CONFIG_KEY_THREAD_ID`
- `INPUT`
- `INTERRUPT`
- `NS_END`
- `NS_SEP`
- `NULL_TASK_ID`
- `PUSH`
- `TASKS`
- `MISSING`
- `END`
- `ManagedValueSpec`
- `DEFAULT_BOUND`
- `StreamChunk`
- `DEFAULT_RUNTIME`
- `All`
- `Durability`
- `StreamMode`
- `StreamPart`
- `ContextT`
- `InputT`
- `OutputT`
- `StateT`

## Methods

- [`ensure_config()`](https://reference.langchain.com/python/langgraph/pregel/main/ensure_config)
- [`merge_configs()`](https://reference.langchain.com/python/langgraph/pregel/main/merge_configs)
- [`patch_checkpoint_map()`](https://reference.langchain.com/python/langgraph/pregel/main/patch_checkpoint_map)
- [`patch_config()`](https://reference.langchain.com/python/langgraph/pregel/main/patch_config)
- [`patch_configurable()`](https://reference.langchain.com/python/langgraph/pregel/main/patch_configurable)
- [`recast_checkpoint_ns()`](https://reference.langchain.com/python/langgraph/pregel/main/recast_checkpoint_ns)
- [`create_model()`](https://reference.langchain.com/python/langgraph/pregel/main/create_model)
- [`coerce_to_runnable()`](https://reference.langchain.com/python/langgraph/pregel/main/coerce_to_runnable)
- [`coerce_timeout_policy()`](https://reference.langchain.com/python/langgraph/pregel/main/coerce_timeout_policy)
- [`get_async_graph_callback_manager_for_config()`](https://reference.langchain.com/python/langgraph/pregel/main/get_async_graph_callback_manager_for_config)
- [`get_sync_graph_callback_manager_for_config()`](https://reference.langchain.com/python/langgraph/pregel/main/get_sync_graph_callback_manager_for_config)
- [`get_config()`](https://reference.langchain.com/python/langgraph/pregel/main/get_config)
- [`create_error_message()`](https://reference.langchain.com/python/langgraph/pregel/main/create_error_message)
- [`apply_writes()`](https://reference.langchain.com/python/langgraph/pregel/main/apply_writes)
- [`local_read()`](https://reference.langchain.com/python/langgraph/pregel/main/local_read)
- [`prepare_next_tasks()`](https://reference.langchain.com/python/langgraph/pregel/main/prepare_next_tasks)
- [`task_path_str()`](https://reference.langchain.com/python/langgraph/pregel/main/task_path_str)
- [`identifier()`](https://reference.langchain.com/python/langgraph/pregel/main/identifier)
- [`achannels_from_checkpoint()`](https://reference.langchain.com/python/langgraph/pregel/main/achannels_from_checkpoint)
- [`acheckpoint_superseded()`](https://reference.langchain.com/python/langgraph/pregel/main/acheckpoint_superseded)
- [`channels_from_checkpoint()`](https://reference.langchain.com/python/langgraph/pregel/main/channels_from_checkpoint)
- [`checkpoint_superseded()`](https://reference.langchain.com/python/langgraph/pregel/main/checkpoint_superseded)
- [`copy_checkpoint()`](https://reference.langchain.com/python/langgraph/pregel/main/copy_checkpoint)
- [`create_checkpoint()`](https://reference.langchain.com/python/langgraph/pregel/main/create_checkpoint)
- [`create_checkpoint_plan_for_update_state_api()`](https://reference.langchain.com/python/langgraph/pregel/main/create_checkpoint_plan_for_update_state_api)
- [`delta_channels_overwritten()`](https://reference.langchain.com/python/langgraph/pregel/main/delta_channels_overwritten)
- [`delta_channels_with_pending_writes()`](https://reference.langchain.com/python/langgraph/pregel/main/delta_channels_with_pending_writes)
- [`empty_checkpoint()`](https://reference.langchain.com/python/langgraph/pregel/main/empty_checkpoint)
- [`get_updated_channels_from_tasks()`](https://reference.langchain.com/python/langgraph/pregel/main/get_updated_channels_from_tasks)
- [`put_writes_accepts_task_path()`](https://reference.langchain.com/python/langgraph/pregel/main/put_writes_accepts_task_path)
- [`versions_seen_without_bumps()`](https://reference.langchain.com/python/langgraph/pregel/main/versions_seen_without_bumps)
- [`draw_graph()`](https://reference.langchain.com/python/langgraph/pregel/main/draw_graph)
- [`map_input()`](https://reference.langchain.com/python/langgraph/pregel/main/map_input)
- [`read_channels()`](https://reference.langchain.com/python/langgraph/pregel/main/read_channels)
- [`ensure_message_ids()`](https://reference.langchain.com/python/langgraph/pregel/main/ensure_message_ids)
- [`read_task_statuses()`](https://reference.langchain.com/python/langgraph/pregel/main/read_task_statuses)
- [`get_new_channel_versions()`](https://reference.langchain.com/python/langgraph/pregel/main/get_new_channel_versions)
- [`validate_timeout_supported()`](https://reference.langchain.com/python/langgraph/pregel/main/validate_timeout_supported)
- [`validate_graph()`](https://reference.langchain.com/python/langgraph/pregel/main/validate_graph)
- [`validate_keys()`](https://reference.langchain.com/python/langgraph/pregel/main/validate_keys)
- [`get_bolded_text()`](https://reference.langchain.com/python/langgraph/pregel/main/get_bolded_text)
- [`get_colored_text()`](https://reference.langchain.com/python/langgraph/pregel/main/get_colored_text)
- [`tasks_w_writes()`](https://reference.langchain.com/python/langgraph/pregel/main/tasks_w_writes)
- [`ensure_valid_checkpointer()`](https://reference.langchain.com/python/langgraph/pregel/main/ensure_valid_checkpointer)

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/3521f08e21a7d89c28331191374bc85c11ecb6e2/libs/langgraph/langgraph/pregel/main.py)
