---
title: "reference/python/langgraph/pregel/_checkpoint"
description: "Index of 20 pages and 0 subdirectories under reference/python/langgraph/pregel/_checkpoint."
category: "index"
tags: [index, reference, python, langgraph, pregel, checkpoint]
---

# reference/python/langgraph/pregel/_checkpoint

20 pages here.

## Files

- [GetNextVersion](GetNextVersion.md) - View source on GitHub
- [LATEST_VERSION](LATEST_VERSION.md) - View source on GitHub
- [achannels_from_checkpoint](achannels_from_checkpoint.md) - Async version of channels_from_checkpoint. See docstring there.
- [acheckpoint_superseded](acheckpoint_superseded.md) - Async checkpoint_superseded.
- [channels_from_checkpoint](channels_from_checkpoint.md) - Hydrate channels from a checkpoint.
- [checkpoint_superseded](checkpoint_superseded.md) - Whether the thread has moved past saved, the checkpoint config addressed.
- [copy_checkpoint](copy_checkpoint.md) - View source on GitHub
- [create_checkpoint](create_checkpoint.md) - Build a new Checkpoint from the previous one and live channel state.
- [create_checkpoint_plan_for_update_state_api](create_checkpoint_plan_for_update_state_api.md) - Return (channels_to_snapshot, metadata) for an update_state head.
- [create_metadata_for_update_state_api](create_metadata_for_update_state_api.md) - Advance counters_since_delta_snapshot for update_state on a non-fresh thread.
- [delta_channels_overwritten](delta_channels_overwritten.md) - Return the names of the DeltaChannels that writes set with an Overwrite.
- [delta_channels_to_snapshot](delta_channels_to_snapshot.md) - Return the set of DeltaChannel names that should snapshot now.
- [delta_channels_with_pending_writes](delta_channels_with_pending_writes.md) - DeltaChannels a branch starting from this checkpoint must snapshot.
- [empty_checkpoint](empty_checkpoint.md) - View source on GitHub
- [exit_delta_late_task_id](exit_delta_late_task_id.md) - Synthetic task id for exit-mode writes of a superstep after the anchor's own.
- [exit_delta_task_id](exit_delta_task_id.md) - Synthetic task id for exit-mode DeltaChannel writes.
- [get_delta_channels_from_all_channels](get_delta_channels_from_all_channels.md) - DeltaChannels to snapshot on the first update_state of a fresh thread: the ones it wrote, as the rest have no version and nothing to store.
- [get_updated_channels_from_tasks](get_updated_channels_from_tasks.md) - Channel names written by an update_state superstep (excluding PUSH).
- [put_writes_accepts_task_path](put_writes_accepts_task_path.md) - Whether a saver's put_writes or aput_writes takes task_path.
- [versions_seen_without_bumps](versions_seen_without_bumps.md) - versions_seen as the nodes read it: an entry a bump advanced goes back to the version the node really read, or away if it never read one.
