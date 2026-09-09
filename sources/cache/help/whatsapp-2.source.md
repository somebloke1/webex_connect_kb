## ➡️ Inbound Messages

```json text
{
    "aliasId": "6ee6ce94-9940-44a6-a017-d99ed4d97dd7",
    "direction": "inbound",
    "type": "text",
    "text": "Hi there, this is a sample inbound text containing credit card info: XXXX XXXX XXXX XXXX",
    "timestamp": "2019-08-24T14:15:22Z",
    "redacted": false
}
```
```json text-with-attachments
{
    "aliasId": "6ee6ce94-9940-44a6-a017-d99ed4d97dd7",
    "direction": "inbound",
    "type": "text-with-attachments",
    "text": "Hi there, this is a sample inbound text containing credit card info: XXXX XXXX XXXX XXXX",
    "attachments": [
        {
            "mimeType": "image/png",
            "fileName": "SampleImage.png",
            "fileUrl": "https://example.com/sample-image.png",
            "dropped": false
        },
        {
            "mimeType": "application/pdf",
            "fileName": "SampleFile.pdf",
            "fileUrl": "",
            "dropped": true
        }
    ],
    "timestamp": "2019-08-24T14:15:22Z",
    "redacted": false
}
```
```json attachments
{
    "aliasId": "6ee6ce94-9940-44a6-a017-d99ed4d97dd7",
    "direction": "inbound",
    "type": "attachments",
    "attachments": [
        {
            "mimeType": "image/png",
            "fileName": "SampleImage.png",
            "fileUrl": "https://example.com/sample-image.png",
            "dropped": false
        },
        {
            "mimeType": "application/pdf",
            "fileName": "SampleFile.pdf",
            "fileUrl": "",
            "dropped": true
        }
    ],
    "timestamp": "2019-08-24T14:15:22Z"
}
```
```json wab-interactive-response
{
    "aliasId": "6ee6ce94-9940-44a6-a017-d99ed4d97dd7",
    "direction": "inbound",
    "type": "wab-interactive-response",
    "wabInteractiveResponse": {
        "title": "Option 1",
        "identifier": "b0c75e59-3196-442d-9de5-bafaaa83b402"
    },
    "timestamp": "2019-08-24T14:15:22Z",
    "redacted": false
}
```

## ⬅️ Outbound Messages

```json text
{
    "aliasId": "6ee6ce94-9940-44a6-a017-d99ed4d97dd7",
    "direction": "outbound",
    "type": "text",
    "text": "Hi there, this is a sample outbound text containing credit card info: XXXX XXXX XXXX XXXX",
    "timestamp": "2019-08-24T14:15:22Z",
    "redacted": false,
    "attemptGwDelivery": true
}
```
```json text-with-attachments
{
    "aliasId": "6ee6ce94-9940-44a6-a017-d99ed4d97dd7",
    "direction": "outbound",
    "type": "text-with-attachments",
    "text": "Hi there, this is a sample outbound text containing credit card info: XXXX XXXX XXXX XXXX",
    "attachments": [
        {
            "mimeType": "image/png",
            "fileName": "SampleImage.png",
            "fileUrl": "https://example.com/sample-image.png",
            "dropped": false
        },
        {
            "mimeType": "application/pdf",
            "fileName": "SampleFile.pdf",
            "fileUrl": "",
            "dropped": true
        }
    ],
    "timestamp": "2019-08-24T14:15:22Z",
    "redacted": false,
    "attemptGwDelivery": true
}
```
```json attachments
{
    "aliasId": "6ee6ce94-9940-44a6-a017-d99ed4d97dd7",
    "direction": "outbound",
    "type": "attachments",
    "attachments": [
        {
            "mimeType": "image/png",
            "fileName": "SampleImage.png",
            "fileUrl": "https://example.com/sample-image.png",
            "dropped": false
        },
        {
            "mimeType": "application/pdf",
            "fileName": "SampleFile.pdf",
            "fileUrl": "",
            "dropped": true
        }
    ],
    "timestamp": "2019-08-24T14:15:22Z",
    "attemptGwDelivery": true
}
```
```json wab-buttons
{
    "aliasId": "6ee6ce94-9940-44a6-a017-d99ed4d97dd7",
    "direction": "outbound",
    "type": "wab-buttons",
    "wabButtons": {
        "header": {
            "type": "text",
            "text": "your text",
            "document": {
                "url": "your-media-url",
                "filename": "some-file-name"
            },
            "video": {
                "url": "your-media-url"
            },
            "image": {
                "url": "your-media-url"
            }
        },
        "body": {
            "text": "your-text-body-content"
        },
        "footer": {
            "text": "your-text-footer-content"
        },
        "action": {
            "buttons": [
                {
                    "type": "reply",
                    "reply": {
                        "id": "unique-postback-id",
                        "title": "First Button’s Title"
                    }
                },
                {
                    "type": "reply",
                    "reply": {
                        "id": "unique-postback-id",
                        "title": "Second Button’s Title"
                    }
                }
            ]
        }
    },
    "timestamp": "2019-08-24T14:15:22Z",
    "redacted": false,
    "attemptGwDelivery": true
}
```
```json wab-list
{
    "aliasId": "6ee6ce94-9940-44a6-a017-d99ed4d97dd7",
    "direction": "outbound",
    "type": "wab-list",
    "wabList": {
        "header": {
            "type": "text",
            "text": "your text"
        },
        "body": {
            "text": "your-text-body-content"
        },
        "footer": {
            "text": "your-text-footer-content"
        },
        "action": {
            "button": "cta-button-content",
            "sections": [
                {
                    "title": "section-title-content",
                    "rows": [
                        {
                            "id": "unique-row-identifier",
                            "title": "row-title-content",
                            "description": "row-description-content"
                        }
                    ]
                },
                {
                    "title": "section-title-content",
                    "rows": [
                        {
                            "id": "unique-row-identifier",
                            "title": "row-title-content",
                            "description": "row-description-content"
                        }
                    ]
                }
            ]
        }
    },
    "timestamp": "2019-08-24T14:15:22Z",
    "redacted": true,
    "attemptGwDelivery": true
}
```

## ↩️ Announcement

Announcements support markdown content. Refer to the cheat sheet below:

```json announcement
{
    "aliasId": "6ee6ce94-9940-44a6-a017-d99ed4d97dd7",
    "direction": "announcement",
    "type": "text",
    "text": "Sample **Announcement**",
    "timestamp": "2019-08-24T14:15:22Z"
}
```

## Markdown Cheat Sheet

| Formatting | Synax                                       |
| :--------- | :------------------------------------------ |
| Bold       | Embed within double star symbols (\*\*)     |
| Italics    | Embed within single underscore symbols (\_) |