# API - WxEngage standalone

Source: https://help.webexconnect.io/docs/api
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:28+00:00

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
    "text": "Hi there",
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
    "text": "Hi there",
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