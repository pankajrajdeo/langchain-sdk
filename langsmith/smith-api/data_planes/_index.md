---
title: "langsmith/smith-api/data_planes"
description: "Index of 5 pages and 0 subdirectories under langsmith/smith-api/data_planes."
category: "index"
tags: [index, langsmith, smith-api, data_planes]
---

# langsmith/smith-api/data_planes

5 pages here.

## Files

- [Create a new data plane](create-a-new-data-plane.md) - Creates a new data plane object. Persists the rendered data plane spec, and returns 202 with the data plane in status=requested. Requires BYOC enabled org and org admin. The cloud of the control...
- [Delete a data plane](delete-a-data-plane.md) - Verifies that the stored customer AWS role has delete permissions, that the stored Azure subscription is reachable, or that the stored GCP provisioner service account can be impersonated. Then...
- [Get a data plane](get-a-data-plane.md) - Returns a data plane and its saved provisioning settings in any lifecycle state. Requires BYOC and organization:infrastructure:read.
- [List data planes for the current organization](list-data-planes-for-the-current-organization.md) - Returns up to 50 data planes owned by the caller's organization across all lifecycle states. Sorted by status priority (active first), then newest first. Requires BYOC to be enabled for the org.
- [Update data plane settings](update-data-plane-settings.md) - Update specific settings for a data plane owned by the caller's organization.
