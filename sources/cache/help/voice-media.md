# Voice Media

Source: https://help.webexconnect.io/docs/voice-media
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:32+00:00

Voice media is the repository of different voice files and folders segmented in business and language hierarchy. This feature allows you to create folders and upload voice media files into the folders. 

These files are used in Flow Builder to create single or multi-language voice flows. You can map the same media across multiple languages within the same flow without needing to create a separate flow for each language. As the media files are segregated into different folders, you can easily select necessary files while creating voice flows. You can create local language folders within the main folder. If you delete a folder, subsequently all the files and folders in the folder also get deleted.

The standard followed is [ISO 639-1](https://en.wikipedia.org/wiki/Language_localisation). 

To add voice media, follow the steps given below:

1. Navigate to **Tools** > **Voice Media**.
2. Click **Add Folder**, provide a name for the folder and click **Save**. The new folder appears on the **Voice Media** page.



![Screenshot of Voice Media Page](https://files.readme.io/b494e02-Voice.jpg)




3. Click the folder to which you want to add the media files.
4. Click **Add Language Folder**, select the required language and click **Save**. A folder gets created with the selected language.

> 📘 Note
> 
> You must add folders for all the languages that you require. Each folder corresponds only to a single language.



![Screenshot of Main Folder Navigation](https://files.readme.io/aa9c6cb-Voice1.jpg)




5. Click the language folder to which you want to add the media.
6. Click **Add New** and select:  
   (i) _Upload_ - browse and select a file from the local computer.

> 📘 Media File Type and Size
> 
> - The supported media file types are MP3 and WAV.
> - The file size to upload is limited to 10MB.

   (ii) _Record A Clip_ - enter a Recording Name and click Next. Select the **Country** from the drop-down list, dial the number provided on the screen and enter the **PIN** when prompted to record a clip. The set of pre-configured numbers for each country appears when you select the country.

   (iii) _Synthesize Using TTS_ - provide a name for the media, message, voice type, and language to synthesize TTS from the provide message.



![Screenshot of Synthesize using TTS](https://files.readme.io/5bb0801-Voice.jpg)




> 📘 Note
> 
> Starting from 6.5.0, the Standard option in the Voice Type dropdown is not available as Azure is deprecating the standard voice from August 2024. Please note that TTS API should not be used with voice type as Standard.