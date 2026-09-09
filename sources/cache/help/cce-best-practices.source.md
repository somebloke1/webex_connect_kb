**Configuring Retry Logic for Pre-built Integration Nodes or 3rd Party API Calls**

There isn't any implicit retrial built into various integration nodes offered by <<prodname>> (such as Contact Centre Enterprise, Zendesk, etc). At the moment if an API call made by <<prodname>> pre-built integration nodes or HTTP Request node to the integrated system or any third-party API call fails, the node transitions to the node outcome that corresponds to API call failure without any retries. Retry logic should be built within flows depending on the use case and requirements.

**Tenant Time Zone and Date Time Format Settings**

Configure the [Tenant TimeZone](https://help.imiconnect.io/docs/tenant-settings) and Date Format Settings for your tenant as per your region/preference.

**Enable Attachment Support within Contact Center Enterprise**

  * Please ensure that you have enabled the ability to receive attachments within Contact Center Enterprise.

**Security Best Practices**

  * Follow the ‘Principle of Least Privilege’ and leverage [role-based access control (RBAC)](https://help.imiconnect.io/docs/user-roles-and-hierarchy) to limit user access to relevant features and capabilities
  *  Once the set-up is complete, use the [Service Locking Feature](https://help.imiconnect.io/docs/service-settings) to avoid unintended/accidental changes to your flows

**Flow Configuration Best Practices**

  * Do not configure high timeout values while making use of HTTP request node and Delay node when using these nodes as it can lead to delayed processing of concurrent flow threads.
  * Do not configure never-ending loops as such mistakes can lead to concurrency thresholds causing new event processing to stop.

**Descriptive Logs for Debugging**

You must enable the Descriptive Logs option under the flow settings to capture node execution details. Please note that this feature is suggested to be used only during initial flow set-up and troubleshooting. Enabling this feature in production mode can impact your tenant performance.

**Groups and Teams**

For the <<prodname>> and Contact Center Enterprise integration flows, we recommend you to use the Client level services, and not configure assets or flows for these integrations at a Group or Team level.

**Configuring authorizations for Contact Center Enterprise integration nodes**

While there is no limit on the number of authorizations you can configure for a node, we recommend configuring one authorization for one type of node and reusing the same authorization configuration across flows.

**<<prodname>> Services used for Contact Center Enterprise Flows**

It is recommended that you use the service locking feature to avoid accidental changes or deletion of services or flows. Also, the service keys should not be changed for these services as it would lead to integration not working. If such changes are made, reverting to the original stage will not be possible.

**Messenger Get Started Configuration**

We recommend you to not enable the **Get Started** button on the Messenger app configuration screen under Assets --> Apps section when using <<prodname>> for supporting Messenger for Contact Center Enterprise.