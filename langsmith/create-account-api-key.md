---
title: "Create an account and API key"
description: "To get started with LangSmith, you need to create an account. You can sign up for a free account in the LangSmith UI. LangSmith supports sign in with Google, GitHub, and email."
source: "https://docs.langchain.com/langsmith/create-account-api-key"
category: "docs"
tags: [docs, langsmith, create-account-api-key]
---

# Create an account and API key

To get started with LangSmith, you need to create an account. You can sign up for a free account in the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-create-account-api-key). LangSmith supports sign in with Google, GitHub, and email.

## API keys

LangSmith supports two types of API keys. You can use both types of token to authenticate requests to the LangSmith API, but they have different use cases:

* [**Personal Access Tokens (PATs)**](administration-overview.md#personal-access-tokens-pats) inherit the permissions of the user who created them. Use PATs for personal scripts or tools.
* [**Service keys**](administration-overview.md#service-keys) scope to specific [workspaces](administration-overview.md#workspaces) or the entire [organization](administration-overview.md#organizations). Use service keys for applications and production services.

To log [traces](observability-concepts.md#traces) and run [evaluations](evaluation.md) with LangSmith, create an API key to authenticate your requests.

### Open API Keys settings
Navigate to the [**Settings** page](https://smith.langchain.com/settings) and select the **API Keys** section.

### Configure the key type
For service keys, choose between an organization-scoped and workspace-scoped key. If the key is workspace-scoped, you must specify the workspaces.

[Enterprise](pricing-plans.md) users can also [assign specific workspace roles](administration-overview.md#workspace-roles-rbac) to service keys, which adjusts their permissions independently of any user.

### Set expiration
Set the key's expiration. The key becomes unusable after the number of days chosen, or never, if that is selected.

### Create the key
Click **Create API Key.** LangSmith will display the API key only once, so make sure to copy it and store it in a safe place.

> [!TIP]
> [Enterprise](pricing-plans.md) Organization Admins can edit the [role](administration-overview.md#workspace-roles-rbac) on an existing service key without rotating the key. On the [**Settings** page](https://smith.langchain.com/settings) **API Keys** section, switch to the **Service** tab and click any service key row to open the edit dialog. Update the workspace role (and, for organization-scoped keys, the org role) and click **Save**. The key string itself is unchanged.

## Deactivate or delete a personal access token

Deactivation temporarily stops a PAT from authenticating; deletion permanently removes it. Deactivate a token when you need to keep its record and reactivate it later.

Members can deactivate, reactivate, and delete their own PATs. [Organization Admins](rbac.md#organization-admin) and [Organization Operators](rbac.md#organization-operator) can also manage every member's PATs.

| Action         | Effect                                                                                               | Reversible                                                  |
| -------------- | ---------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| **Deactivate** | Stops authentication and keeps the record, owner, and last use visible with a **Deactivated** badge. | Yes. Select **Reactivate key** to use the same token again. |
| **Reactivate** | Allows authentication again with the same token and its original expiration date.                    | Yes. Deactivate the token again at any time.                |
| **Delete**     | Permanently removes the token and its record.                                                        | No. Create a new token if you need access again.            |

Deactivation does not change a token's expiration date, and **Reactivate key** is unavailable once that date has passed. Create a new token instead.

To deactivate or delete a PAT:

1. Go to [**Settings**](https://smith.langchain.com/settings) > **API Keys** and open the **Personal** tab.
2. Find the token under **My keys**. To manage another member's token, switch to **All members**.
3. In the **Actions** column, select **Deactivate key** or **Delete key**. Each action opens its own confirmation dialog.
4. Type the token's description, which the dialog displays. For a token with no description, type the short key from the **Key** column instead.
5. Select **Deactivate** or **Delete** to confirm. A success notification confirms the action.

To reactivate a deactivated PAT, select **Reactivate key** in the **Actions** column. Reactivation takes one click, without a confirmation dialog, and displays a success notification.

Authentication results are cached, so a deactivated or deleted token stops working within a minute rather than instantly. A reactivated token may remain unusable until a cached rejection expires.

[Audit logs](audit-logs.md) record deactivation as `revoke_personal_access_token` and reactivation as `reinstate_personal_access_token`.

Service keys can only be deleted, not deactivated. Open the **Service** tab and select **Delete key** in the **Actions** column, then confirm with the typed description that deleting a PAT requires.

## Configure the SDK

Install the SDK for your language:

#### Python
**pip**

```bash
pip install langsmith
```

**uv**

```bash
uv add langsmith
```

#### TypeScript
```bash
npm install langsmith
```

For full details, refer to the [Python SDK](smith-python-sdk.md) or [JS/TS SDK](smith-js-ts-sdk.md) reference.

Then, set your API key and enable tracing:

```bash
export LANGSMITH_API_KEY=<your-api-key>
export LANGSMITH_TRACING=true
```

You may also need the following additional environment variables:

* `LANGSMITH_ENDPOINT` controls which LangSmith server the SDK sends data to. It defaults to `https://api.smith.langchain.com` (GCP US). Set it only if you are on a different deployment. For regional SaaS, set it to the API URL for your region:

  <table>
    <thead>
      <tr>
        <th>Region</th>

        <th>
          {protocol_0 === false ? "Host" : "URL"}
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td>GCP US</td>

        <td>
          <code>
            {`${protocol_0 === false ? "" : "https://"}${prefix_0 || "api.smith"}.langchain.com${suffix_0 || ""}`}
          </code>
        </td>
      </tr>

      <tr>
        <td>GCP EU</td>

        <td>
          <code>
            {`${protocol_0 === false ? "" : "https://"}eu.${prefix_0 || "api.smith"}.langchain.com${suffix_0 || ""}`}
          </code>
        </td>
      </tr>

      <tr>
        <td>GCP APAC</td>

        <td>
          <code>
            {`${protocol_0 === false ? "" : "https://"}apac.${prefix_0 || "api.smith"}.langchain.com${suffix_0 || ""}`}
          </code>
        </td>
      </tr>

      <tr>
        <td>AWS US</td>

        <td>
          <code>
            {`${protocol_0 === false ? "" : "https://"}aws.${prefix_0 || "api.smith"}.langchain.com${suffix_0 || ""}`}
          </code>
        </td>
      </tr>
    </tbody>
  </table>

* `LANGSMITH_WORKSPACE_ID` is required only if your API key is scoped to more than one [workspace](administration-overview.md#workspaces). Find your Workspace ID on the [**Settings** page](https://smith.langchain.com/settings) under **General**:

  `LANGSMITH_WORKSPACE_ID=`

To reuse endpoint, API key, and workspace settings across local shells or remote runtimes, refer to [Profile configuration](profile-configuration.md).

## Use API keys outside of the SDK

See [instructions for managing your organization via API](manage-organization-by-api.md).

***

> [!NOTE]
> [Connect these docs](../use-these-docs.md) to your agent of choice via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/create-account-api-key.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
