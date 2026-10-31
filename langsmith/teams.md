---
title: "Teams"
description: "Group organization members into teams, then give each team a role and access policies in the workspaces it can access."
source: "https://docs.langchain.com/langsmith/teams"
category: "docs"
tags: [docs, langsmith, teams]
---

# Teams

> Group organization members into teams, then give each team a role and access policies in the workspaces it can access.

A team is a group of organization members. You can give a team access to several workspaces, with a specific role in each. Team members who belong to those workspaces receive the team's role there. Teams build on [role-based access control (RBAC)](rbac.md) and [attribute-based access control (ABAC)](abac.md).

> [!NOTE]
>
> Teams are available for organizations on the [Enterprise plan](https://www.langchain.com/pricing) and for [self-hosted](self-hosted.md) deployments. [Contact our sales team](https://www.langchain.com/contact-sales) to learn more.

## Access rules

In a workspace, a user's permissions are the sum of their own [workspace role](rbac.md#workspace-roles) and the role of each team they belong to. [Access policies](abac.md) can come from those roles and from the teams themselves. A matching deny policy applies first and blocks access, whatever the roles allow. For the evaluation order, refer to [How ABAC works with RBAC](abac.md#how-abac-works-with-rbac).

A team's role applies only to members who belong to the workspace. Giving a team access does not add anyone to the workspace. To give a team member access, [add the user to the workspace](set-up-hierarchy.md#set-up-a-workspace) or [sync the team from your identity provider](#sync-team-members-from-your-identity-provider).

## Before you begin

* Ensure that [RBAC](rbac.md) and [ABAC](abac.md) are enabled for your organization. Without ABAC, team access policies have no effect.
* For self-hosted deployments, see below.

## Enable teams for self-hosted deployments

> [!NOTE]
>
> On [self-hosted](self-hosted.md) deployments, teams require Helm chart 0.18.0-rc.50 or later (application version 0.18.19rc1).

Use one of the following options to enable teams:

* **Enable for a specific organization**: Run the following against your LangSmith PostgreSQL database, replacing `<organization_id>` with the ID copied from the organization settings page in the UI:

```sql
  UPDATE organizations SET config = config || '{"can_use_teams": true}' WHERE id = '<organization_id>' AND NOT is_personal;
```

* **Enable for all organizations**: Add the following environment variable to `commonEnv` in your `values.yaml`:

```yaml
  DEFAULT_ORG_FEATURE_CAN_USE_TEAMS: "true"
```

To manage teams in the UI, also [enable ABAC](abac.md#enable-abac-for-self-hosted-deployments).

## Create a team

To create a team:

1. Navigate to Organization **Settings** > **Teams**.
2. Click **Create team**.
3. Enter a **Name** and, optionally, a **Description**.
4. (Optional) Add members, workspace access, and access policies. Refer to [Edit a team](#edit-a-team).
5. Click **Create team**.

Team names must be unique across the organization.

## Edit a team

To edit a team:

1. Navigate to Organization **Settings** > **Teams** and click the team.
2. Make your changes in **Members**, **Workspaces**, or **Access policies**.
3. Click **Update team**.

LangSmith saves the changes together. If one fails, LangSmith keeps the unsaved changes so you can retry them.

### Members

Click **+ Add member** to add organization members. To remove a member, click the remove icon on their row. A removed member loses the access the team gave them.

The section also lists the team's [workspace-only members](#add-workspace-only-members-and-policies), with a link to the workspace they were added in.

### Workspaces

Click **+ Grant workspace** and select a workspace to give the team's members a role there. The role defaults to [Workspace Viewer](rbac.md#workspace-viewer). You can select any built-in or [custom workspace role](rbac.md#custom-roles) instead, and change it later on the workspace's row.

To remove access, click the remove icon on the workspace's row and type the workspace name to confirm. Removing access also removes the team's workspace-only members and access policies in that workspace.

### Access policies

Click **+ Attach policy** to attach an [access policy](abac.md#access-policy-structure). The team's access policies apply to its members in every workspace the team can access.

To limit a team's policy to one workspace, attach it through the [API](#manage-teams-with-the-api) with `workspace_id` set. The team must have access to that workspace, and you must be a member of that workspace. The team dialog shows the workspace that such a policy applies in.

## Add workspace-only members and policies

In a workspace that a team can access, a [Workspace Admin](rbac.md#workspace-admin) can add members and access policies to the team for that workspace only. This lets a workspace's administrators manage access in their workspace without organization-level permissions.

Workspace-only members do not receive the team's role. They receive only the workspace-only access policies, and only in that workspace. Workspace-only access policies apply only to workspace-only members.

For example, the `Support` team has the [Workspace Editor](rbac.md#workspace-editor) role in `Production`. A Workspace Admin in `Production` can add more users to `Support` for that workspace only, and attach a policy that lets them read projects tagged `Environment=Development`.

To add workspace-only members or policies:

1. Navigate to the workspace's **Settings** > **Teams**. The page lists each team with access to the workspace.
2. Click a team.
3. Add or remove members, or attach or detach access policies.
4. Click **Update team**.

You can add only users who are members of the workspace. The team's name, description, members, and access policies appear as read-only.

## Delete a team

To delete a team, navigate to Organization **Settings** > **Teams**, click the delete icon on the team's row, and type the team name to confirm.

Deleting a team removes its members, workspace access, and access policies, including workspace-only members and policies.

A role that a team uses in a workspace cannot be deleted. Change the team's role or remove its workspace access first.

## Sync team members from your identity provider

Link a team to a group in your identity provider (IdP), and LangSmith sets the team's members from that group. Sync works with [SCIM](user-management.md#set-up-scim-for-your-organization) and [SSO Groups Sync](user-management.md#sso-groups-sync-alternative). Workspace-only members are not synced.

To sync a team:

1. Navigate to Organization **Settings** > **Teams** and click the team.
2. In **General**, enter the group's name in **IdP group**. For SCIM, enter the SCIM group's name. For SSO Groups Sync, enter a value from the [groups claim](user-management.md#sso-groups-sync-alternative).
3. Select **Sync members from the IdP group**.
4. Click **Update team**.

### Sync behavior

* **Matching**: A group matches when its name equals the team's IdP group, ignoring leading and trailing spaces. Matching is case-sensitive. Each IdP group can be linked to only one team.

* **Timing**: SSO Groups Sync updates a user's teams at each login and requires **Sync workspace/role assignments**. SCIM updates a user's teams when their SCIM groups change.

* **Membership**: A synced team's members are the users in the IdP group. A change you make in LangSmith lasts until that user's next sync.

* **Organization role**: When no `LS:` group sets a user's organization role, a team match sets it:

  * Through SSO Groups Sync, a new user joins the organization as an [Organization Viewer](rbac.md#organization-viewer). A user whose membership SSO Groups Sync manages is set to Organization Viewer. Other memberships, such as from an invite, keep their role.
  * Through SCIM, a user whose membership SCIM does not manage is set to [Organization User](rbac.md#organization-user), and SCIM manages the membership after that. This includes users with a higher role, such as Organization Admin.

* **Workspace membership**: Sync adds the user to each workspace the team can access. This membership has no role of its own. The user's access comes from the team's role. At the user's next sync, LangSmith removes the membership if no team has access to that workspace.

* **Login gate**: When **Require matching group to sign in** is enabled, a group that matches a synced team counts as a matching group. For SSO Groups Sync, this also requires **Sync workspace/role assignments**.

* **Sync disabled**: The team keeps its members, and you manage them in LangSmith.

## Permissions

The minimum built-in role for each action:

| Action | Minimum built-in role |
| - | - |
| View teams, members, and access policies | [Organization Viewer](rbac.md#organization-viewer) |
| Create, rename, or delete a team | [Organization Operator](rbac.md#organization-operator) |
| Add or remove members | Organization Operator |
| Give, change, or remove workspace access | Organization Operator |
| Attach or detach access policies | Organization Operator |
| View workspace-only members and policies | [Workspace Viewer](rbac.md#workspace-viewer) |
| Add or remove workspace-only members and policies | [Workspace Admin](rbac.md#workspace-admin) |

[Custom roles](rbac.md#custom-roles) can hold the `workspaces:teams:*` permissions. For the permission each action checks, refer to the [operations reference](organization-workspace-operations.md#workspace-teams).

## Manage teams with the API

The teams endpoints are under `/api/v1/platform/orgs/current/teams`. [Audit logs](audit-logs.md#tracked-operations-reference) record each change to a team.

## See also

* [Role-based access control](rbac.md)
* [Attribute-based access control](abac.md)
* [User management](user-management.md)
* [Organization and workspace operations reference](organization-workspace-operations.md)
* [Audit logs](audit-logs.md)

***

[Connect these docs](../use-these-docs.md) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/teams.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
