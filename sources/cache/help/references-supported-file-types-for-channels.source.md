## Apple Messages for Business

| Media       | Supported Content Types - Outbound                                            | Supported Content Types - Inbound                                             |
| :---------- | :---------------------------------------------------------------------------- | :---------------------------------------------------------------------------- |
| audio       | mp4, amr, wav                                                                 | amr                                                                           |
| application | pdf, msword, xls, xlsx, vnd.ms-powerpoint, text/plain, ics, usdz, caf, pkpass | pdf, msword, xls, xlsx, vnd.ms-powerpoint, text/plain, ics, usdz, caf, pkpass |
| image       | jpeg, jpg, png, heic                                                          | jpeg, jpg, png, heic                                                          |
| video       | mp4                                                                           | quicktime                                                                     |

## Email

| Media       | Supported Content Types - Outbound | Supported Content Types - Inbound |
| :---------- | :--------------------------------- | :-------------------------------- |
| image       | jpg, png, svg, bmp, gif, heic      | jpg, png, svg, bmp, gif, heic     |
| audio       | mp3, amr                           | mp3, amr                          |
| video       | 3gp, avi, mp4                      | 3gp, avi, mp4                     |
| application | doc, docx, ppt, pptx, pdf, txt     | doc, docx, ppt, pptx, pdf, txt    |
| mail        |                                    | msg, eml                          |

## Instagram (Deprecated)

| Media | Supported Content Types - Outbound           | Supported Content Types - Inbound |
| :---- | :------------------------------------------- | :-------------------------------- |
| Image | .jpg, .png, .ico, .bmp, sticker (Like heart) | .jpg, .png, .ico, .bmp, .gif      |

## Facebook Messenger

| Media       | Supported Content Types - Outbound   | Supported Content Types - Inbound    |
| :---------- | :----------------------------------- | :----------------------------------- |
| image       | jpg, gif, webp, png, bmp             | jpg, gif, webp, png, bmp             |
| audio       | mp3, amr, m4a                        | mp3, amr                             |
| video       | mp4, mov, m4v, 3gp, flv              | mp4, mov, m4v, 3gp, flv              |
| application | pdf, doc, docx, ppt, pptx, xls, xlsx | pdf, doc, docx, ppt, pptx, xls, xlsx |

## In-App Messaging / Live Chat

[block:parameters]
{
  "data": {
    "h-0": "Media",
    "h-1": "Supported Types - Outbound",
    "h-2": "Supported Types - Inbound",
    "0-0": "image",
    "0-1": "jpeg, png, gif  \nsvg",
    "0-2": "jpeg, png, gif",
    "1-0": "audio",
    "1-1": "mp3, wav, ogg, opus, aac, 3gp, mkv",
    "1-2": "mp3, wav",
    "2-0": "video",
    "2-1": "mp4, mkv, avi, mov, mpeg, 3gp",
    "2-2": "mp4",
    "3-0": "application",
    "3-1": "pdf,  doc, ppt, pptx, xlsx, xls,  \ntxt, csv",
    "3-2": "pdf, doc, ppt, pptx, xlsx, xls,  \ncsv"
  },
  "cols": 3,
  "rows": 4,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


## MMS

[block:parameters]
{
  "data": {
    "h-0": "Media Type",
    "h-1": "File Extension",
    "h-2": "Maximum File Size",
    "0-0": "Overall MMS payload size",
    "0-1": "",
    "0-2": "750 KB",
    "1-0": "Image",
    "1-1": "The URL must be publicly accessible and end with one of the following file types:  \n.jpg = image/jpg, image/jpeg  \n.png = image/png  \n.gif = image/gif",
    "1-2": "750 KB",
    "2-0": "Audio",
    "2-1": "The URL must be publicly accessible and end with one of the following file types:  \n.mp3 = audio/mp3, audio/mpeg",
    "2-2": "750 KB",
    "3-0": "Video",
    "3-1": "The URL must be publicly accessible and end with one of the following file types:  \n.mp4 = video/mp4",
    "3-2": "750 KB",
    "4-0": "Excel",
    "4-1": ".xlsx, xls = application/excel",
    "4-2": "750 KB",
    "5-0": "Calendar",
    "5-1": ".ics, .ical, .ifb, .icalendar = text/calendar  ",
    "5-2": "750 KB",
    "6-0": "Contact",
    "6-1": " .vcf,  \n.vcard = text/vcard, text/v-card, text/x-vcard",
    "6-2": "750 KB",
    "7-0": "Pdf",
    "7-1": ".pdf = application/pdf, application/x-pdf",
    "7-2": "750 KB",
    "8-0": "Text",
    "8-1": "text/plain",
    "8-2": "750 KB"
  },
  "cols": 3,
  "rows": 9,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


## Push Notifications

| Media | Supported Content Types |
| :---- | :---------------------- |
| image | jpg, png                |

## RCS

| Media    | Supported Content Types                 |
| :------- | :-------------------------------------- |
| image    | apng,gif, x-icon, jpeg, jpg, png        |
| document | pdf                                     |
| audio    | mpeg, mp4, ogg, oga, webm,mp3,mpg,mpeg4 |
| video    | 3gpp, mpeg, ogg, webm, x-m4v, ms-asf    |

## SMS

| Media | Supported Content Type |
| :---- | :--------------------- |
| NA    | NA                     |

## Voice

| Media | Supported Content Types | Supported Format                                                                    |
| :---- | :---------------------- | :---------------------------------------------------------------------------------- |
| audio | .wav                    | RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, stereo 8000 Hz        |
| audio | .Mp3                    | Audio file with ID3 version 2.3.0MPEG ADTS, layer III, v1, 224 kbps, 32 kHz, Stereo |

In case of URL, we support.wav

| Feature             | Supported Content Types | Supported Format                                                                |
| :------------------ | :---------------------- | :------------------------------------------------------------------------------ |
| Pre-uploaded prompt | .mp3                    | RIFF (little-endian) data, WAVE  audio, Microsoft PCM, 16 bit, stereo 8000 Hz   |
|                     | .wav                    | Audio file with ID3 version 2.3.0MPEG ADTS, layer III, 224 kbps, 32 kHz, Stereo |
|                     | .wav                    | Linear PCM, sampling rate: 8000/16000 Hz, bits/sample: 16                       |
|                     |                         | 128/256 kbps                                                                    |
|                     |                         | G711 A-law, sampling rate 8000/16000 Hz, bits/sample: 8                         |
|                     |                         | 64/128 kbps                                                                     |
|                     |                         | G711 U-law, sampling rate 8000/16000 Hz, bits/sample: 8                         |
|                     |                         | 64/128 kbps                                                                     |

| Codecs                                                    | Bit Rate     |
| :-------------------------------------------------------- | :----------- |
| Linear PCM, sampling rate: 8000/16000 Hz, bits/sample: 16 | 128/256 kbps |
| G711 A-Law, sampling rate 8000/16000 Hz, bits/sample: 8   | 64/128 kbps  |
| G711 U-Law, sampling rate 8000/16000 Hz, bits/sample: 8   | 64/128 kbps  |

## WhatsApp

[block:parameters]
{
  "data": {
    "h-0": "Media Type",
    "h-1": "Supported via Send node (in Media Message Type)",
    "h-2": "Supported via Messaging API v1 (in Media Message Type)",
    "h-3": "Supported via Send Node and Messaging API v1 for Template Message Type",
    "h-4": "Maximum Size",
    "0-0": "audio",
    "0-1": "AAC, AMR, MPEG, OGG  \n  \nNote: For OGG MIME Type, only media codec supported by WhatsApp is OPUS. Also, OPUS MIME Type is no longer supported by WhatsApp.",
    "0-2": "audio/aac, audio/mp4, audio/mpeg, audio/amr, audio/ogg (only opus codecs, base audio/ogg is not supported)",
    "0-3": "Audio is not supported via Templates.",
    "0-4": "16 MB",
    "1-0": "Document",
    "1-1": "TXT, PDF, PPT, DOC, DOC(X), PPT(X), XLS(X)",
    "1-2": "text/plain, application/pdf, application/vnd.ms-powerpoint, application/msword, application/vnd.ms-excel, application/vnd.openxmlformats-officedocument.wordprocessingml.document, application/vnd.openxmlformats-officedocument.presentationml.presentation, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    "1-3": "TXT, PDF, PPT, DOC, DOC(X), PPT(X), XLS(X)",
    "1-4": "100 MB",
    "2-0": "image",
    "2-1": "JPEG, PNG",
    "2-2": "image/jpeg, image/png  \n  \nImages must be 8-bit, RGB or RGBA",
    "2-3": "JPEG, PNG",
    "2-4": "5 MB",
    "3-0": "video",
    "3-1": "3GPP, MP4  \n  \nNote:  \nOnly H.264 video codec and AAC audio codec is supported.  \nWhatsApp support videos with a single audio stream or no audio stream.",
    "3-2": "video/mp4, video/3gp  \n  \nNote:  \nOnly H.264 video codec and AAC audio codec is supported.  \nWe support videos with a single or no audio stream.",
    "3-3": "3GPP, MP4  \n  \nNote:  \nOnly H.264 video codec and AAC audio codec is supported.  \nWhatsApp support videos with a single or no audio stream.",
    "3-4": "16 MB",
    "4-0": "Sticker",
    "4-1": "WEBP",
    "4-2": "image/webp",
    "4-3": "NA",
    "4-4": "Static stickers: 100KB  \n  \nAnimated stickers: 500KB"
  },
  "cols": 5,
  "rows": 5,
  "align": [
    "left",
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


<br />

> 👍 WhatsApp Media Best Practices
> 
> - While uploading the media and setting the mime-type make sure you are following the [guidelines](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Configuring_server_MIME_types#how_to_set_up_your_server_to_send_the_correct_mime_types) mentioned in the documentation.
> - The publicly accessible URL used while configuring the message must end in the same file format set under the 'File MIME type'. It should not have any geo-restriction and should be accessible from a server located within USA premises.
> - Supported incoming media message mime-types are identical to outbound message media mime-types in Send node and Messaging API. The mime-type of the incoming media message can be captured as part of the following: 
>   - Start node and Receive node output variable i.e., "**whatsApp.mimetype**", 
>   - Outbound webhooks, Debug logs and Export logs with JSON path "**attachments.mime_type**"
> - WebP is a modern image format that provides superior lossless compression and creates smaller and richer images that makes web faster. The source libraries to use for converting an image to WebP file-format are available at [An image format for the Web](https://developers.google.com/speed/webp). You can also use various third-party converters publicly available to convert images to WebP file-format.

## Custom Node Integration

| Feature     | File type                      |
| :---------- | :----------------------------- |
| Custom Node | Only SVG image files supported |

## Event Scheduler

| Media                 | Supported Content Types |
| :-------------------- | :---------------------- |
| Text                  | .txt                    |
| Excel                 | .xlsx                   |
| Comma Separated Value | .csv                    |

## Channel Asset Set-Up

| Channel                  | Media | Supported Content Types |
| :----------------------- | :---- | :---------------------- |
| RCS asset creation       | image | jpg,png                 |
| WhatsAppp asset creation | image | jpg, png                |