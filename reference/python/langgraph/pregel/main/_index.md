---
title: "reference/python/langgraph/pregel/main"
description: "Index of 46 pages and 2 subdirectories under reference/python/langgraph/pregel/main."
category: "index"
tags: [index, reference, python, langgraph, pregel, main]
---

# reference/python/langgraph/pregel/main

46 pages here, 112 pages including subdirectories.

## Directories

- [NodeBuilder/](NodeBuilder/_index.md) - 10 pages
- [Pregel/](Pregel/_index.md) - 56 pages

## Files

- [NodeBuilder](NodeBuilder.md) - - subscribe_only() - subscribe_to() - read_from() - do() - write_to() - meta() - add_retry_policies() - add_cache_policy() - set_timeout() - build()
- [Pregel](Pregel.md) - Pregel manages the runtime behavior for LangGraph applications.
- [achannels_from_checkpoint](achannels_from_checkpoint.md) - Async version of channels_from_checkpoint. See docstring there.
- [acheckpoint_superseded](acheckpoint_superseded.md) - Async checkpoint_superseded.
- [apply_writes](apply_writes.md) - Apply writes from a set of tasks (usually the tasks from a Pregel step) to the checkpoint and channels, and return managed values writes to be applied externally.
- [channels_from_checkpoint](channels_from_checkpoint.md) - Hydrate channels from a checkpoint.
- [checkpoint_superseded](checkpoint_superseded.md) - Whether the thread has moved past saved, the checkpoint config addressed.
- [coerce_timeout_policy](coerce_timeout_policy.md) - Normalize a timeout value to positive-second policy fields.
- [coerce_to_runnable](coerce_to_runnable.md) - Coerce a runnable-like object into a Runnable.
- [copy_checkpoint](copy_checkpoint.md) - View source on GitHub
- [create_checkpoint](create_checkpoint.md) - Build a new Checkpoint from the previous one and live channel state.
- [create_checkpoint_plan_for_update_state_api](create_checkpoint_plan_for_update_state_api.md) - Return (channels_to_snapshot, metadata) for an update_state head.
- [create_error_message](create_error_message.md) - View source on GitHub
- [create_model](create_model.md) - Create a pydantic model with the given field definitions.
- [delta_channels_overwritten](delta_channels_overwritten.md) - Return the names of the DeltaChannels that writes set with an Overwrite.
- [delta_channels_with_pending_writes](delta_channels_with_pending_writes.md) - DeltaChannels a branch starting from this checkpoint must snapshot.
- [draw_graph](draw_graph.md) - Get the graph for this Pregel instance.
- [empty_checkpoint](empty_checkpoint.md) - View source on GitHub
- [ensure_config](ensure_config.md) - Return a config with all keys, merging any provided configs.
- [ensure_message_ids](ensure_message_ids.md) - Give the messages written to DeltaChannels stable ids.
- [ensure_valid_checkpointer](ensure_valid_checkpointer.md) - View source on GitHub
- [get_async_graph_callback_manager_for_config](get_async_graph_callback_manager_for_config.md) - Build an async graph lifecycle callback manager from a runnable config.
- [get_bolded_text](get_bolded_text.md) - Get bolded text.
- [get_colored_text](get_colored_text.md) - Get colored text.
- [get_config](get_config.md) - View source on GitHub
- [get_new_channel_versions](get_new_channel_versions.md) - Get subset of current_versions that are newer than previous_versions.
- [get_sync_graph_callback_manager_for_config](get_sync_graph_callback_manager_for_config.md) - Build a sync graph lifecycle callback manager from a runnable config.
- [get_updated_channels_from_tasks](get_updated_channels_from_tasks.md) - Channel names written by an update_state superstep (excluding PUSH).
- [identifier](identifier.md) - Return the module and name of an object.
- [local_read](local_read.md) - Function injected under CONFIG_KEY_READ in task config, to read current state. Used by conditional edges to read a copy of the state with reflecting the writes from that node only.
- [map_input](map_input.md) - Map input chunk to a sequence of pending writes in the form (channel, value).
- [merge_configs](merge_configs.md) - Merge multiple configs into one.
- [patch_checkpoint_map](patch_checkpoint_map.md) - View source on GitHub
- [patch_config](patch_config.md) - Patch a config with new values.
- [patch_configurable](patch_configurable.md) - View source on GitHub
- [prepare_next_tasks](prepare_next_tasks.md) - Prepare the set of tasks that will make up the next Pregel step.
- [put_writes_accepts_task_path](put_writes_accepts_task_path.md) - Whether a saver's put_writes or aput_writes takes task_path.
- [read_channels](read_channels.md) - View source on GitHub
- [read_task_statuses](read_task_statuses.md) - Return the status of every task that has recorded writes, keyed by task id.
- [recast_checkpoint_ns](recast_checkpoint_ns.md) - Remove task IDs from checkpoint namespace.
- [task_path_str](task_path_str.md) - Generate a string representation of the task path.
- [tasks_w_writes](tasks_w_writes.md) - Apply writes / subgraph states to tasks to be returned in a StateSnapshot.
- [validate_graph](validate_graph.md) - View source on GitHub
- [validate_keys](validate_keys.md) - View source on GitHub
- [validate_timeout_supported](validate_timeout_supported.md) - View source on GitHub
- [versions_seen_without_bumps](versions_seen_without_bumps.md) - versions_seen as the nodes read it: an entry a bump advanced goes back to the version the node really read, or away if it never read one.
