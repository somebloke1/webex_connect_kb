# Single Sign-On (SSO) Using SAML

Source: https://help.webexconnect.io/docs/single-sign-on-settings
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:36+00:00

The Webex Connect platform supports web-based Single Sign-On (SSO) using the Security Assertion Markup Language (SAML). This feature allows Webex Connect enterprise clients to enable their employees to log in seamlessly using their existing organizational credentials.

Single Sign-On (SSO) is an integrated feature of Webex Connect and must be set up to allow users to authenticate via their organizational credentials. Please contact your account manager to assist with enabling the SSO feature for your organization.

> 📘 SSO for tenant Owner
> 
> Owner can login via SSO or password depending on the SSO configurations.

Only an owner can configure the SSO settings and enable SSO for various users.

## Prerequisites

You must have the Identity provider details like IDP (Identity Provider) login URL, Entity ID, and IDP certificate for successful user invitation. Also, make sure that the users' email addresses are present in IDP. The '.cer' certificate files will be accepted for both, Identity Provider Certificate, and the Assertion Decryption Certificate.

Obtain the following assertion data from the Webex Connect service provider:

| Attributes             | Values                 | Description                      |
| :--------------------- | :--------------------- | :------------------------------- |
| mobileno               | user.telephonenumber   | The telephone number of the user |
| loginid                | user.userprincipalname | The email ID of the user         |
| firstname              | user.displayname       | The first name of the user       |
| Unique User Identifier | user.mail              | The email ID of the user         |

> 📘 Attributes in assertion data
> 
> The attributes are case-sensitive and should be entered in the displayed cases above.

## SSO Settings

To configure the SSO settings, follow the steps given below:

1. Navigate to **Settings** > **Single Sign-On Settings**.
2. Select from the following options under **Log-in Settings**. The settings you select here are applicable to all users across the platform, except for the owner.
   - **Allow login with password** - this option allows users to log in using an email ID and password-based basic authentication.
   - **Allow login with Single-sign on (SSO)** - this option allows users to log in using their existing organizational (Identity provider) credentials as per single sign-on configurations.

> 📘 
> 
> If you select both the options, you can choose how each user logs in individually.

3. Select the **Default Authentication For New Users**. The available options are **SSO** and **Password**. The option you select here will be the default login mechanism for all the new users created from now on.



![SSO Settings - Part 1](https://files.readme.io/b52161102574f92501f454a59cf6f6fc257c67e74b82f6e43d14f4e91f4da3d3-Single-Sign-On_1.png)






![SSO Settings - Part 2](https://files.readme.io/1a6b52fae0711a76a22ada45bff9dabf5b7df4e48bb796dddae6ace28cf26bca-Single-Sign-On_2.png)




4. Select the **SAML Version** that the identity provider uses.
5. Provide the **Identity Provider Login URL**. This is the URL to which Webex Connect sends a SAML request to start the login sequence.
6. Provide the Entity ID. This is the unique URL that identifies your SAML Identity Provider (IDP). This entity ID must be the same as the `<saml:issuer>` attribute in the SAML assertion. You will get this URL at both the IDP end as well as at the service provider end but you would need to use only one of these URLs and use the same URL at both places.
7. Select a file for the **Identity Provider Certificate**.
8. Select the **Request Signature Method**. This is the hashing algorithm for encrypted requests. The supported methods are _RSA-SHA1_ and _RSA-SHA256_.
9. Assertion Decryption Certificate (Optional): If the identity provider encrypts SAML assertions, upload the decryption certificate here.
10. Authentication Context Requirements:  Provide the list of Allowed Authentication Context values (`SAML AuthnContextClassRef`) that Webex Connect will include in the authentication request to the Identity Provider (IdP). This setting is mandatory and is pre-populated by default for both existing and new tenants with:  
    `urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport`
    - You can add up to 5 values.
    - Only full URN values are accepted. Values without the urn: prefix are not supported and will be rejected.
    - Ensure the selected values are supported by your IdP. Unsupported values may cause authentication to fail based on IdP policy.  
      Example values:  
      `urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport`  
      `urn:oasis:names:tc:SAML:2.0:ac:classes:Password`.
11. Provide **Webex ConnectService Provider Details**. These details are required to configure the federated authentication, a single sign-on method that uses SAML assertions sent to an Webex Connect endpoint.

- **Assertion Customer Service URL** - the URL that the identity provider uses to verify SAML messages from Webex Connect.
- **Identifier** - the unique identifier for your tenant. Use it as `entity id` in the identity provider configuration.

11. Click **Save** to save the configuration details.

## Inviting New Users

After you have configured the SSO settings, when you invite new users, an email will be sent for the invitation. If you have selected SSO as the default option, the new users do not need to create a password. The name and phone number of such users are captured during their first login.

> 📘 Password Reset
> 
> The password reset option is not applicable for users who are configured to login with SSO.

## Password vs SSO

The following image illustrates how login works for existing and new users with password and SSO:



![Image illustrating login processes for existing and new users with password and SSO](https://files.readme.io/f0c64f6-sso-table.png)




## Testing your SSO configuration

Webex Connect allows you to test your SSO configuration by simply clicking a Test button after you have configured the SSO settings. Enter the Login Email ID of the user for whom you have enabled and want to test the SSO option for. 

> 📘 Note
> 
> The '**Allow login with SSO**' option should be selected to test SSO.

Follow the below steps to test SSO:

1. Click **Allow login with Single Sign-on (SSO)**.
2. Select **SSO** from 'Default for New Users' option to enable SSO for the new users.
3. Configure Required Settings as mentioned in the Configuring SAML Single Sign-On procedure above.
4. Click **Test**.  
   The Test Single Sign-On page appears.



![Test SSO](https://files.readme.io/49dcc8d6c964a568412f3e5b38b46fe2f1a03787308fc9b999b98e59d1062a6d-Single-Sign-On_2.png)




5. Enter your **Test Email ID** (see below).  
   The entered user ID should match with the user’s records provided to the IDP (Identity Provider) in order to successfully login.
6. Click **Test**.



![Test Single Sign-On](https://files.readme.io/c5c12743ce07bd704b8638ed93dafbeed244b58103a8bd344648de7399f7eb2e-2025-03-28_11-27-20.jpg)




The user will be directed to the login page of the entered ‘Identity Provider’s Login URL’. In case of a successful login, the user will be provided a ‘test session’ with Webex Connect.  

In case, entered data do not match (e.g. due to the wrong id), an error message is thrown as received from IDP.  For example:  



![Screenshot displaying error message for mismatched data due to wrong ID, as received from IDP.](https://files.readme.io/c48d17c-errormsg.png)




## Remote Log-off for SSO

Webex Connect has introduced Remote Logout functionality which allows a user that is active on multiple platforms/products to logout at once from everywhere simply from a single platform.

In order to enable remote logout, you need to provide “Remote Logout URL” under the SAML Settings on the Single Sign-On Settings page.

Remote logout URL is used to terminate session at IDP's end when the user logs out of Webex Connect(SP).”

On successful logout from Webex Connect for SSO enabled users, a session termination request is sent on remote logout URL.

Remote logout URL is used to terminate session at IDP end when user logs out of Webex Connect(SP).

Webex Connect (SP) will not delete any other active SP's session (other than Webex Connect when SSO user logouts of Webex Connect) and IDP should take action to delete other SP's sessions to achieve Single Logout.