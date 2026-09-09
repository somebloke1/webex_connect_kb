- Leverage Single Sign-On (SSO) for user authentication. <<prodname>> supports SSO using SAML 2.0.

  - In case, you wish to continue using password-based authentication, encourage users to set up a strong password and update it regularly. <<prodname>> password policy requiress atleast one uppercase letter, one special character, one numeric character, and at-least 8 characters in total for setting up a password.

- Leverage role-based access control when adding new users to your <<prodname>> tenant

- Don't use group email addresses for user access, and use an active email id that's regularly accessed to not miss out on any platform alerts and notifications sent by <<prodname>>. 

- If you're not using SSO, make sure to delete user accounts from within <<prodname>> when a user leaves your organization.

- Provide Decrypt Access permission only to authorized users as it can potentially be used to see sensitive customer data.

- Rotate your service keys and JSON Web Tokens regularly. We do provide an option to generate a new service key or JSON Web Tokens before phasing out the old credentials. Refer API tab within Service Dashboard for more information.

- Configure [IP Address Allowlist](https://help.webexconnect.io/v6.20.0/docs/tenant-settings#ip-address-allowlist) for tenants that need to restrict API access to trusted networks. Tenant Owners can add IPv4 addresses or CIDR ranges from Tenant Settings. When entries are configured, API traffic that does not originate from those entries is rejected.

- Opt for Monitoring (i.e., User Audit) add-on to get visibility into user actions across the platform. Please note that the audit trail will only be visible to Owner user role.

- Use features such as Service Locking and Logbooks Locking to avoid accidental, unintended, or unauthorized edits to services and logbooks.

> 🚧 
> 
> Please note that we do not recommend pinning certificates as out certificates may change from time to time leading to connection termination causing your application functionality to break.