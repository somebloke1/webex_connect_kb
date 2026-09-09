# mTLS Configuration for Outbound Webhooks

Source: https://help.webexconnect.io/docs/mtls-configuration-for-outbound-webhooks
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:06+00:00

mTLS (Mutual Transport Layer Security) is a security protocol that ensures both parties in a communication (for example, a client and a server, such as Webex Connect and an external system) authenticate each other before establishing a secure connection.

This provides step-by-step instructions for configuring mTLS on outbound webhooks in Webex Connect.

Follow these steps to configure mTLS on the Outbound Webhook:

1. Navigate to **Assets > Integrations**.
2. Click **Add Integration > Outbound Webhook**.
3. Select the **Add mTLS Certificate (optional)** checkbox to enable mTLS for secure webhook configuration. Adding mTLS uses certificates to authenticate both the client and the server.

   

![Add mTLS Certificate](https://files.readme.io/70ad8f5c02208a20f1ea290818b118db08ee0a19dd8b057dc90b5a4e49cbe534-image.png)


4. After selecting **Add mTLS Certificate (optional)**, the "Configure Trust Store Certificate" appears.

   

![Configure Trust Store Certificate](https://files.readme.io/29825b5f8e8dec918cf413ed8847cd3fa7572fee0bf0fe0b93160ed04aded344-image.png)


5. Click **+Add New** to add a new certificate. Only one certificate can be added. You can upload only .p12 or JKS certificates.

   

![Upload mTLS Certificate](https://files.readme.io/9ca3cf15b2d4b1beaed14feab171e808ed756d5f09b773f49bab046a45e53703-image.png)


6. Select **Browse Certificate (required)**, choose the server certificate. **Select File Format (required)** and enter the **Store Password**. You can upload only .p12 or .jks certificates.
7. Click **Validate**. A valid certificate shows the **Valid Till** expiry and the **Identifier**.

   

![Validate Certificate](https://files.readme.io/d4e2eb76a178e6d28200ee654db5e0f7db03cbd99356d84beb72b7ad767a85e3-image.png)


8. Upon validating a certificate, install this client certificate (and intermediate Certificate Authority (CA), if applicable) in your server’s trust store. Configure your server to require client certificate validation to authenticate webhook requests from Webex Connect. Keep both the Active and New certificates installed on your server until the old certificate expires to ensure uninterrupted webhook delivery. After installing the client certificate, click **Test** to verify that the connection is established successfully.

   

![Download & Test Button Appears on the Certificate](https://files.readme.io/ce73631c95b0bff408cd40906b29c57b5f725878b39b34be4da74a48e418d724-image.png)



> 📘 Note
> 
> Add mTLS certificate is not available by default. To enable this for your tenant, please contact your account manager.