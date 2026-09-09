# Delete a consumer from a consent group

Source: https://developers.webexconnect.io/reference/delete_v1-groups-groupid-members-4
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:31:46+00:00



## API reference metadata

These are source metadata and examples. `api.auth` is ReadMe metadata; verify authentication in the documented headers/security scheme.

```json
{
  "method": "delete",
  "url": "",
  "auth": "required",
  "params": [],
  "results": {
    "codes": []
  },
  "apiSetting": "6a675233ec1c893d8a7f684c"
}
```

## OpenAPI operation and component schemas

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "Contact Policy API",
    "description": "This document describes the IMImobile Contact Policy REST API",
    "version": "@project.version@ <@git.commit.id.describe-short@>"
  },
  "servers": [
    {
      "url": "https://{your_connecttenant_apidomain }",
      "description": "Enter your own API host",
      "variables": {
        "customerHost": {
          "default": "example.com",
          "description": "Your base domain (e.g., api.mycompany.com)"
        }
      }
    }
  ],
  "security": [
    {
      "ProfileKey": []
    },
    {
      "JWT-Authentication": []
    }
  ],
  "path": "/v1/groups/{groupId}/members",
  "method": "delete",
  "path_parameters": [
    {
      "$ref": "#/components/parameters/groupId"
    }
  ],
  "operation": {
    "tags": [
      "Consumers"
    ],
    "summary": "Delete a consumer from a consent group",
    "description": "Use this method for deleting a consent record from the specified group. Identify the consumer by `address`, by `alternateAddress` (WhatsApp only), or by both; at least one is required. *Note-  Replace {your_connecttenant_apidomain } in the URL with your hostname to try this API with your environment. See [Know your endpoint page.](https://developers.webexconnect.io/reference/endpoints)*",
    "parameters": [
      {
        "name": "address",
        "in": "query",
        "required": false,
        "description": "The specific URL encoded address of the consumer which needs to be deleted. Either `address` or `alternateAddress` is required.",
        "example": "%2012125551212",
        "schema": {
          "$ref": "#/components/schemas/Address"
        }
      },
      {
        "name": "channel",
        "in": "query",
        "required": false,
        "description": "If specified, will delete consent of the particular channel.",
        "schema": {
          "$ref": "#/components/schemas/Channel"
        }
      },
      {
        "$ref": "#/components/parameters/alternateAddress"
      }
    ],
    "responses": {
      "200": {
        "description": "The consent has been deleted. Returns the deleted consent record(s).",
        "content": {
          "application/json": {
            "schema": {
              "type": "array",
              "minItems": 1,
              "items": {
                "$ref": "#/components/schemas/ConsumerConsent"
              }
            }
          }
        }
      },
      "404": {
        "$ref": "#/components/responses/404GroupNotFound"
      }
    }
  },
  "components": {
    "parameters": {
      "groupId": {
        "in": "path",
        "name": "groupId",
        "required": true,
        "schema": {
          "$ref": "#/components/schemas/GroupId"
        }
      },
      "consentStatus": {
        "in": "query",
        "name": "consent",
        "description": "If specified, filters results by the consumer's opted in/out status",
        "example": true,
        "schema": {
          "type": "boolean"
        }
      },
      "alternateAddress": {
        "in": "query",
        "name": "alternateAddress",
        "required": false,
        "description": "WhatsApp-only consumer identifier (BSUID). Requires channel=whatsapp and the WhatsApp BSUID feature flag enabled; must match the configured format, else 400.\n",
        "schema": {
          "$ref": "#/components/schemas/AlternateAddress"
        }
      },
      "responseFormat": {
        "in": "query",
        "name": "format",
        "description": "Response content-type.",
        "example": "CSV",
        "schema": {
          "type": "string",
          "default": "JSON",
          "enum": [
            "CSV",
            "JSON"
          ]
        }
      },
      "continuationToken": {
        "in": "query",
        "name": "continuationToken",
        "description": "The continuation token returned in a previouse request that specifies the next page of results to retrieve.",
        "example": "WR6J8u9fDH3YB9up6OmVWw",
        "required": false,
        "schema": {
          "$ref": "#/components/headers/X-cp-continuation-token"
        }
      },
      "pageSize": {
        "in": "query",
        "name": "pageSize",
        "description": "The amount of results to return with the next page.",
        "example": 50,
        "required": false,
        "schema": {
          "type": "integer",
          "default": 50,
          "maximum": 1000
        }
      }
    },
    "schemas": {
      "GroupDefinition": {
        "type": "object",
        "description": "Description of a group and its senders",
        "properties": {
          "groupId": {
            "$ref": "#/components/schemas/GroupId"
          },
          "tenantId": {
            "$ref": "#/components/schemas/TenantId"
          },
          "created": {
            "$ref": "#/components/schemas/IsoDate"
          },
          "lastUpdated": {
            "$ref": "#/components/schemas/IsoDate"
          },
          "maxFrequencies": {
            "$ref": "#/components/schemas/MaxFrequencies"
          },
          "name": {
            "type": "string",
            "description": "The name of the group.",
            "example": "StoreCo Consent Group",
            "minLength": 1,
            "maxLength": 120
          },
          "description": {
            "type": "string",
            "description": "A text description for this consent group.",
            "example": "StoreCo Sale Campaign"
          },
          "senders": {
            "type": "array",
            "description": "Array of allowed sending addresses for this consent group to send from.",
            "minItems": 1,
            "maxItems": 10,
            "items": {
              "$ref": "#/components/schemas/ChannelAddress"
            }
          },
          "groupDefault": {
            "$ref": "#/components/schemas/GroupDefault"
          },
          "createdBy": {
            "type": "string",
            "description": "Identity to track the creator of the group.",
            "example": "username@imi.com"
          },
          "status": {
            "$ref": "#/components/schemas/GroupStatus"
          }
        }
      },
      "GroupId": {
        "description": "Unique ID of group",
        "type": "string",
        "example": "YNN--jY3ehD73SJ6"
      },
      "MaxFrequency": {
        "description": "Describes the maximum frequency of contacts for a given channel over a given period of time.",
        "type": "object",
        "required": [
          "maxCount",
          "period",
          "channel"
        ],
        "properties": {
          "maxCount": {
            "type": "integer",
            "description": "The maximum number of contacts for a unit of time.",
            "minimum": 1,
            "maximum": 5000,
            "example": 100
          },
          "period": {
            "type": "string",
            "description": "The unit of time based on the UTC calendar the maximum count applies to.",
            "example": "DAY",
            "enum": [
              "DAY",
              "WEEK",
              "MONTH"
            ]
          },
          "channel": {
            "$ref": "#/components/schemas/Channel"
          }
        }
      },
      "MaxFrequencyResponse": {
        "allOf": [
          {
            "$ref": "#/components/schemas/MaxFrequency"
          },
          {
            "type": "object",
            "required": [
              "count"
            ],
            "properties": {
              "count": {
                "description": "The current frequency counter for this consumer for the specified period and channel.",
                "type": "integer",
                "example": 25,
                "minimum": 0
              }
            }
          }
        ]
      },
      "Name": {
        "type": "string",
        "description": "The unique name of the group.",
        "example": "StoreCo Consent Group",
        "minLength": 1,
        "maxLength": 128
      },
      "MaxFrequencies": {
        "description": "Array of objects describing the maximum frequency of contacts for a given channel over a given period of time.",
        "type": "array",
        "minItems": 0,
        "maxItems": 10,
        "items": {
          "$ref": "#/components/schemas/MaxFrequency"
        }
      },
      "TenantId": {
        "type": "string",
        "description": "A tenant id.",
        "example": 1050
      },
      "ChannelAddress": {
        "type": "object",
        "required": [
          "channel",
          "address"
        ],
        "properties": {
          "channel": {
            "$ref": "#/components/schemas/Channel"
          },
          "address": {
            "$ref": "#/components/schemas/Address"
          }
        }
      },
      "Sender": {
        "type": "object",
        "required": [
          "channel"
        ],
        "properties": {
          "channel": {
            "$ref": "#/components/schemas/Channel"
          },
          "address": {
            "$ref": "#/components/schemas/Address"
          }
        }
      },
      "GroupDefault": {
        "type": "string",
        "description": "The default control type for addresses to be contacted.",
        "example": "ALLOWLIST",
        "enum": [
          "ALLOWLIST",
          "DENYLIST"
        ]
      },
      "GroupStatus": {
        "type": "string",
        "description": "The state of the group to indicate if currently active or updatable.",
        "example": "ENABLED",
        "enum": [
          "ENABLED",
          "DISABLED"
        ]
      },
      "ConsentFields": {
        "type": "object",
        "required": [
          "consent",
          "reason"
        ],
        "properties": {
          "consent": {
            "type": "boolean",
            "description": "Value indicating whether the consumer approves or disapproves of communication",
            "example": true
          },
          "reason": {
            "type": "string",
            "description": "Free form text value indicating an arbitrary comment about this record",
            "example": "Sample comment"
          },
          "expires": {
            "$ref": "#/components/schemas/IsoDate"
          },
          "alternateAddress": {
            "allOf": [
              {
                "$ref": "#/components/schemas/AlternateAddress"
              }
            ],
            "description": "WhatsApp-only consumer identifier (BSUID). When the WhatsApp BSUID feature flag is enabled and `channel=whatsapp`, `address` may be omitted provided this `alternateAddress` is supplied. Rejected with 400 for non-WhatsApp channels or when the feature flag is disabled.\n"
          },
          "replaceAlternateAddress": {
            "type": "boolean",
            "default": false,
            "writeOnly": true,
            "description": "WhatsApp-only overwrite flag. When `true`, the supplied `alternateAddress` overwrites the existing `alternateAddress` on the consent record. Requires `channel=whatsapp` and a non-empty `alternateAddress`; the API returns 400 otherwise. Ignored when the WhatsApp BSUID feature flag is disabled. Write-only: accepted on requests but never emitted in responses.\n",
            "example": false
          }
        }
      },
      "ConsumerConsent": {
        "allOf": [
          {
            "$ref": "#/components/schemas/ChannelAddress"
          },
          {
            "$ref": "#/components/schemas/ConsentFields"
          }
        ]
      },
      "ConsentRequest": {
        "description": "Consumer identity and the desired consent value. For `channel=whatsapp` either `address` or `alternateAddress` is required (both may be supplied, and `alternateAddress` / `replaceAlternateAddress` apply to WhatsApp only); for all other channels `address` is required and `alternateAddress` is not applicable.\n",
        "allOf": [
          {
            "type": "object",
            "required": [
              "channel"
            ],
            "properties": {
              "channel": {
                "$ref": "#/components/schemas/Channel"
              },
              "address": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/Address"
                  }
                ],
                "description": "Address for communications sent on this channel. Required for all channels except `whatsapp`, where it may be omitted provided `alternateAddress` is supplied.\n"
              }
            }
          },
          {
            "$ref": "#/components/schemas/ConsentFields"
          }
        ],
        "if": {
          "required": [
            "channel"
          ],
          "properties": {
            "channel": {
              "const": "whatsapp"
            }
          }
        },
        "then": {
          "anyOf": [
            {
              "required": [
                "address"
              ]
            },
            {
              "required": [
                "alternateAddress"
              ]
            }
          ]
        },
        "else": {
          "required": [
            "address"
          ]
        }
      },
      "AddOrUpdateConsentRequest": {
        "description": "Consumer identity and the desired consent value. For `channel=whatsapp` either `address` or `alternateAddress` is required (and `alternateAddress` / `replaceAlternateAddress` apply to WhatsApp only); for all other channels `address` is required and `alternateAddress` is not applicable.\n",
        "allOf": [
          {
            "$ref": "#/components/schemas/ConsentRequest"
          },
          {
            "type": "object",
            "properties": {
              "metadata": {
                "$ref": "#/components/schemas/Metadata"
              }
            }
          }
        ]
      },
      "Address": {
        "type": "string",
        "description": "Address for communications sent on this channel.",
        "example": "+12125551212"
      },
      "AlternateAddress": {
        "type": "string",
        "description": "WhatsApp-only consumer identifier (BSUID). Valid only for channel=whatsapp and only accepted when the WhatsApp BSUID feature flag is enabled; must match the configured BSUID format. Requests violating these rules return 400.\n",
        "example": "US.1234567890123456"
      },
      "Channel": {
        "type": "string",
        "description": "A channel of communication",
        "example": "whatsapp",
        "enum": [
          "email",
          "text",
          "voice",
          "whatsapp"
        ]
      },
      "IsoDate": {
        "type": "string",
        "description": "ISO8601 formatted date and time",
        "example": "2020-07-13T21:21:32Z"
      },
      "Metadata": {
        "type": "object",
        "title": "metadata",
        "description": "Optional fields to store extra data along with the consent change request",
        "properties": {
          "keyword": {
            "type": "string",
            "description": "Any arbitrary keyword associated with the consent change request.",
            "example": "Demo"
          },
          "campaign": {
            "type": "string",
            "description": "An identifier of the campaign that is associated with the consent change request.",
            "example": "Demo Broadcast"
          },
          "source": {
            "type": "string",
            "description": "The source that prompted the consent change.",
            "example": "Magazine"
          },
          "messageBody": {
            "type": "string",
            "description": "The message received from the consumer that prompted the change in consent.",
            "example": "yes"
          }
        }
      },
      "NotificationSubscription": {
        "type": "object",
        "required": [
          "callbackUrl"
        ],
        "description": "Defines the properties related to a notification subscription.",
        "properties": {
          "calbackUrl": {
            "type": "string",
            "description": "The URL that will get the callback",
            "example": "https://webhook.example.com/notify"
          },
          "authId": {
            "type": "integer",
            "description": "The ID to be used for making the callback. If not provided, the callback will proceed without authorization. To obtain an authorization ID, add an authorization under the Assets -> Integrations section. A unique authorization ID will be generated and displayed on the Authorization listing page, which must be included in this API call.",
            "example": 1234
          }
        }
      }
    },
    "headers": {
      "X-cp-continuation-token": {
        "schema": {
          "type": "string",
          "description": "An arbitrary stateless token returned with paginated results. It can be used as a\nquery parameter to get the next page of results. If the token is not present, there is not another page of data.\n"
        }
      }
    },
    "responses": {
      "404GroupNotFound": {
        "description": "Invalid or unknown group ID."
      },
      "410GroupDeleted": {
        "description": "The group has been deleted."
      }
    },
    "securitySchemes": {
      "ProfileKey": {
        "type": "http",
        "scheme": "bearer",
        "bearerFormat": "ProfileKey",
        "description": "Default API authentication method that uses a profile key assigned to a tenant through the connect\nplatform under the Tenant settings.\n\nExample: `0ca67aa4-c800-463f-8180-54412c5f4f4f`\n"
      },
      "JWT-Authentication": {
        "type": "http",
        "scheme": "bearer",
        "bearerFormat": "JWT",
        "description": "JWT Token **DEPRECATED**: Use ProfileKey authentication instead.\n\nAn example decoded JWT token body accepted by the application looks like the following:\n\n```javascript\n{\n    \"tenantid\": \"example-tenant-id\", // The ID of a tenant associated with the request.\n    \"roleId\": 1,                     // The ID of the users role where 1=read only, 2=read write, 3=full access.\n    \"iss\": \"IMI\",                    // Identifier of the JWT's issuing service.\n    \"iat\": 1611723014,               // Unix Timestamp in seconds specifying the issued at date.\n    \"exp\": 1611723614                // Unix Timestamp in seconds specifying the expiration date.\n    \"username\": \"jsmith\"             // The username associated with the request (optional field).\n}\n```\n"
      }
    }
  }
}
```
