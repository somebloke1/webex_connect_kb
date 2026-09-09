## Role-Based Access Control (RBAC)

User management provides a way to control user access (based on the roles) and is the ability to onboard and off-board users across the platform. You can define users and groups and provide the required permissions using user management. The users of the <<prodname>> platform are uniquely identified by their email address.

> 📘 Managing Users
> 
> - Tenant 'Owner' is the user role with highest level of access. If you're a partner helping a client go live with their services on <<prodname>>, it is best to assign the Owner rights to the individuals who would need access to features such as Single Sign On (SSO) Configuration, Tenant Time Zone Settings, and platform usage audit trail for monitoring purposes.
> - Users with **Owner** and/or **Full Access** roles can add/delete users and edit the permissions of the existing users. Editing the permissions includes revoking access. Only **Owner** level users can add another user in "Owner" role. Once a user has been added in "Owner" role, their access level cannot be changed or revoked in a self-serve mode. You will need to reach out to Webex Connect support to make a change in their access level. 
> - By default, the Service Key and JWT Authentication Tokens are masked. Only **Owners**, **Full Access Users**, and **Limited Access Users** can see the Service Key and JWT Authentication Tokens by clicking the Show Icon (eye icon) next to these credentials.

> 📘 Note
> 
> The same email ID of a user can be added to multiple tenants. The user will be able to take up different roles in each of these tenants. 
> 
> For example, [Tim@serviceprovider.com](mailto:Tim@serviceprovider.com) can have the role A (Owner) in tenant Q, and he/she can have role B (Full access) in tenant Z.

The users' access to assets varies depending on the user's hierarchy. Users, also known as _teammates_, can exist at tenant/client-level, group-level. or a team-level.

## User Roles

The following table mentions about the platform features for which default access is provided or not provided for various roles.

| Feature Name                          | Owner                                       | Full Access User   | Limited Access | Read Only | Restricted |
| :------------------------------------ | :------------------------------------------ | :----------------- | :------------- | :-------- | :--------- |
| Profile Key                           | Yes                                         | Yes                | No             | No        | No         |
| Service Key/JWT Token                 | Yes                                         | Yes                | No             | No        | No         |
| SSO Configuration                     | Yes                                         | No                 | No             | No        | No         |
| Invite Other Users                    | Yes                                         | Yes                | No             | No        | No         |
| Revoke User Access                    | Yes (Except other Owners)                   | Yes (Except Owner) | No             | No        | No         |
| Change User Roles                     | Yes (Except other Owners)                   | Yes (Except Owner) | No             | No        | No         |
| Change Tenant TimeZone or Date Format | Yes                                         | No                 | No             | No        | No         |
| Provide Decrypt Access to Other Users | Yes                                         | No                 | No             | No        | No         |
| Create New Services                   | Yes                                         | Yes                | Yes            | No        | No         |
| View Existing Services                | Yes                                         | Yes                | Yes            | Yes       | No         |
| Get Numbers                           | Yes                                         | Yes                | Yes            | No        | No         |
| Configure New App Assets              | Yes                                         | Yes                | Yes            | No        | No         |
| Share App Assets with Groups          | Yes                                         | Yes                | Yes            | No        | No         |
| Add Integrations                      | Yes                                         | Yes                | Yes            | No        | No         |
| Access Monitoring (Audit Trail)       | Yes (if this add-on has been subscribed to) | No                 | No             | No        | No         |
| Add Group(s)                          | Yes                                         | No                 | No             | No        | No         |
| Add Team(s)                           | Yes                                         | No                 | No             | No        | No         |
| Access Reports                        | Yes                                         | Yes                | Yes            | Yes       | No         |
| Access Debug Console                  | Yes                                         | Yes                | Yes            | Yes       | No         |
| Download Export Logs                  | Yes                                         | Yes                | Yes            | Yes       | No         |
| Schedule Export Logs                  | Yes                                         | No                 | No             | No        | No         |

The platform has users at the following hierarchy levels:

- **Tenant/Client** - users at this level have access to all the assets.  
  The users set up at Tenant level can switch to the group/team level to see the assets at that level. The access rights depend on the role of the user.
- **Group** - each tenant/client can have multiple groups or sub-accounts.  
  The sub-accounts represent various units/departments of a client. Sub-accounts are required to administer a set of users grouped by their function within the organization. This is an optional level in the hierarchy. Users at the group-level have access only to the assets created at that group-level. However, users at the group-level can switch down to the team-level to see the assets of the teams within that group. The access rights depend on the role of the user.
- **Team** - a sub-account can contain multiple teams which in-turn contain team members. This is an optional level in the hierarchy.  
  Users at the team-level have access only to the assets created at the team-level. They cannot see and access assets at other team-levels or at its parent group-level. The access rights depend on the role of the user.

### **Specific Permissions**

#### **Granular Access to Profile Key, ServiceKey, and JWT Token**:

Users with the ‘Owner’ and ‘Full Access’ roles will be able to view the following UI options in the ‘Permissions’ page of the platform:

- Profile API / Media access Key
- Service Key / JWT Token

In case of users with the ‘Owner’ role, the above options will be enabled by default and cannot be disabled. While, users with the ‘Full Access’ role can enable or disable these options in the UI.

> 📘 Permission Changes
> 
> The above change also impacts all the existing users and users whose roles are changed, such that accesses will either be revoked or retained based on the new permission settings above.  
> For example, if a user with ‘Restricted Access’ role previously had access to either of the options above, their access will now be revoked.
> 
> The role-based changes can be tracked in the user details of Audit Logs.

#### **Regenerate Profile Key**

Users only with the ‘Owner’ role can regenerate the profile key in the Services page of the platform with the ‘Regenerate Profile Key’ option. Users with all other roles (including Support access users) will view this option in the disabled state in the platform UI.

## Role synchronization between Control Hub and Webex Connect

For Webex Contact Center integrated tenants, user roles can synchronize between Control Hub and Webex Connect. The synchronized role depends on whether the user is a partner administrator, a Control Hub customer administrator, or an existing Webex Connect user.

### External Administrators for Partners in Webex Connect

| Users' privileges for External Administrator for Partners | Access levels in Webex Connect |
| --------------------------------------------------------- | ------------------------------ |
| External Administrator: Full Administrator                | Connect Full Access            |
| External Administrator: Provisioning Admin                | Connect Limited Access         |
| External Administrator: Read-only                         | Connect Read-only              |

### Control Hub users synchronize in Webex Connect

| Users' privileges in Control Hub           | Role allocated in Webex Connect |
| ------------------------------------------ | ------------------------------- |
| Customer Administrator: Full Administrator | Connect Tenant Owner            |
| Customer Contact Center Administrator      | Connect Tenant Owner            |
| Customer Administrator: Read-only          | Connect Read-only               |

### Connect users synchronize in Control Hub

| Users' privileges in Webex Connect | Role allocated in Control Hub              |
| ---------------------------------- | ------------------------------------------ |
| Connect Read-only                  | Customer Administrator: Read-only          |
| Connect Limited                    | Customer Administrator: Read-only          |
| Connect Full Access                | Customer Administrator: Full Administrator |
| Connect Tenant Owner               | Customer Administrator: Full Administrator |
| Connect Restricted Access          | Customer Administrator: Read-only          |

## Add Sub-accounts (Groups)

To add sub-accounts:

1. Click **Sub-accounts** in the **User Management** menu.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/1bab3552a20ca0cdb9a56fda21463a306b05c949bf373a2c2b417fc619969fbe-2025-03-28_14-13-21.jpg",
        "Subaccount.jpg",
        "Screenshot of User Management Menu"
      ],
      "align": "center",
      "border": true,
      "caption": "User Management Menu"
    }
  ]
}
[/block]


2. Go to the **Groups** tab and click **Add New Group**.
3. Provide a suitable **Name** and **Description** and click **Save**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/82991c7364f9e5728f930db6baeff2e56774c60681c3ef6c8e56ab02e9e6d087-2025-03-28_14-19-16.jpg",
        "Subgroup.jpg",
        "Screenshot of Add Group"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Add Group"
    }
  ]
}
[/block]


The specified group is created.

> 🚧 Deleting Sub-accounts (Groups)
> 
> Deleting sub-accounts is not supported currently.

## **Add/Edit Teams**

To add Teams:

1. Click **Sub-accounts** in the **User Management** menu.
2. Go to the **Teams** tab and click **Add New Team**.
3. Provide a suitable **Name** and **Description**.
4. Select a group in the **Groped Under** drop-down list box.
5. Click **Save**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/8fc181d13a2e72d8145fb0d71634c43dfa55515325b32e3e78f2ccfd94411050-2025-03-28_15-35-51.jpg",
        "Addteam.jpg",
        "Screenshot of Add Team to a Group"
      ],
      "align": "center",
      "border": true,
      "caption": "Add Team to a Group"
    }
  ]
}
[/block]


The specified team is created within the selected group.

> 🚧 Deleting Teams
> 
> Currently, the deletion of teams is not supported.

## **Add/Edit/Delete Teammates**

To add teammates:

1. Click **Teammates** in the **User Management** menu. You can see a list of the users at this hierarchy level.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/5b20c68-Administration_User_Roles_Teammates.png",
        "Administration User Roles Teammates.png",
        "Screenshot of  Teammates"
      ],
      "align": "center",
      "caption": "Screenshot of Teammates"
    }
  ]
}
[/block]


2. Enter the **Email ID** of the user.
3. Select the **Role** that you want to grant the user and click **Invite User**. For details about roles, see the [User Roles](https://help.imiconnect.io/docs/user-roles-and-hierarchy#user-roles) section.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/dc40acc-Administration_User_Roles_Add_Teammates.png",
        "Administration User Roles Add Teammates.png",
        "Screenshot of Adding Teammates"
      ],
      "align": "center",
      "caption": "Add Teammates"
    }
  ]
}
[/block]


4. Click **Edit** against the required user and update the role permission and data access for that user.
5. Click **Delete** against the user that you want to delete and confirm the action to delete the selected user.

## **Switch View**

You can switch from a tenant/client level to a group or team level using the **Switch View** menu item available in the **User Management** menu. If you are a user at a group-level, you can switch to the team-level.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/87fd19f-Switch_GroupsTeams.jpg",
        "Switch GroupsTeams.jpg",
        "Screenshot of Switch View Menu Item"
      ],
      "align": "center",
      "caption": "Switch View Menu Item"
    }
  ]
}
[/block]


## Hierarchy-based Feature Access

The following table provides an illustration of the availability of the assets between the users across a hierarchy. 'Created at' column refers to the level at which the Entity/Asset has been created or configured.

[block:parameters]
{
  "data": {
    "h-0": "Entity/Asset",
    "h-1": "Created At",
    "h-2": "Tenant/Client",
    "h-3": "Group",
    "h-4": "Team",
    "0-0": "Users",
    "0-1": "Tenant/Client",
    "0-2": "✅",
    "0-3": "❌",
    "0-4": "❌",
    "1-0": "",
    "1-1": "Group",
    "1-2": "❌",
    "1-3": "✅",
    "1-4": "❌",
    "2-0": "",
    "2-1": "Team",
    "2-2": "❌",
    "2-3": "❌",
    "2-4": "✅",
    "3-0": "Services",
    "3-1": "Tenant/Client",
    "3-2": "✅",
    "3-3": "❌",
    "3-4": "❌",
    "4-0": "",
    "4-1": "Group",
    "4-2": "❌",
    "4-3": "✅",
    "4-4": "❌",
    "5-0": "",
    "5-1": "Team",
    "5-2": "❌",
    "5-3": "✅  \nonly when switched <br>to the team-level",
    "5-4": "✅",
    "6-0": "Apps",
    "6-1": "Tenant/Client",
    "6-2": "✅",
    "6-3": "✅  \nonly when shared <br>with the group",
    "6-4": "✅  \nonly when shared with the team",
    "7-0": "",
    "7-1": "Group",
    "7-2": "❌",
    "7-3": "✅",
    "7-4": "✅  \nonly when shared with the team",
    "8-0": "",
    "8-1": "Team",
    "8-2": "❌",
    "8-3": "✅  \nonly when switched <br>to the team-level",
    "8-4": "✅",
    "9-0": "Integrations",
    "9-1": "Tenant/Client",
    "9-2": "✅",
    "9-3": "❌",
    "9-4": "❌",
    "10-0": "",
    "10-1": "Group",
    "10-2": "❌",
    "10-3": "✅",
    "10-4": "❌",
    "11-0": "",
    "11-1": "Team",
    "11-2": "❌",
    "11-3": "✅  \nonly when switched <br>to the team-level",
    "11-4": "✅"
  },
  "cols": 5,
  "rows": 12,
  "align": [
    "left",
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]