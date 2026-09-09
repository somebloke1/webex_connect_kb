**How Does Webex Connect cleans up the Inactive Profiles**

With the Platform release v6.7.0 and Legacy SDKs (Android v2.20.5 & iOS v2.19.7), and Modular SDKs (Android v3.0.0 & iOS v3.0.0) and JavaScript SDK v1.6.0, we have introduced a new feature which removes inactive app profiles.

Profiles are deemed active by way of a heartbeat mechanism that is sent by our SDK to our backend systems. By default, a profile is deemed inactive if no heartbeat has been detected within a 40 day period. The SDK will send a heartbeat if at least 15 days has passed since the last heartbeat was sent.

The inactivity period is configurable, at the app asset level, to a maximum of 365 days. Contact our support team if you wish to change the inactivity period.

When a profile is deemed inactive, the platform will delete the profile data from our backend systems, and the SDKs will reset it's registration state. Therefore, applications must check the SDK registration state and re-register as required.

**What will happen to profiles that existed before the introduction of the clean up feature?**

Our system will not consider an existing profile as inactive until the first heartbeat has been received from the SDKs. Therefore, there will be no impact on existing profiles until a user installs a version of your app that includes the new SDKS.

**What if a user has uninstalled the app, how will these profiles be cleaned up?**

At this time, those profiles will not be deleted and will remain within our system. We are working on a process to remove these profiles at a future date. In the meantime, you can remove these profiles by calling our Delete Device Profile API.

**What happens to a user profile when the system receives an “Unregistered” error from Firebase Cloud Messaging (FCM)?**

- When the system receives an “Unregistered” error from FCM, it checks which messaging channels are enabled on the profile:
  - Push + Live Chat/In-App enabled: the profile is not deleted, so Live Chat/In-App messages can still be delivered.
  - Only Push enabled: the profile is deleted. And the user needs to register again.
- **MAD counting (30-day window)**:
  - If a profile is deleted due to an “Unregistered” error, that deletion is tracked for the next 30 days.
  - If the same user ID and the same device ID register again within those 30 days, it is counted as a MAD only once (it will not be counted again for the same user+device pair within that 30-day window).