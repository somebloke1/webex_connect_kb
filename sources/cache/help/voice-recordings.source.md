All the recordings from voice flows and APIs will be accessible on the **Voice Recordings** page. 

- **Flows**: Includes recordings from the **Call Patch **and **Record **nodes.
- **V1 API**: Includes both the full call recording and individual action-level recordings (e.g., Play, Record, Call Patch, and Call Transfer).

Using the **Settings**, you can backup or store the voice recordings on FTP/SFTP/S3 servers.	

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/f3829f21d389a4a52938cc5c4a34acf3f0b5f2915e9b8393623f4892da614f30-2025-07-25_12-51-46.png",
        "",
        "Screenshot for Voice Recordings page"
      ],
      "align": "center",
      "border": true,
      "caption": "Voice Recordings"
    }
  ]
}
[/block]


Listen to and download recordings of a flow. These recordings will be available for 30 days from the generation date.​

You can now provide an email/a notify URL to get notifications on the file exports scheduled on Voice Recordings. The notification is triggered at the end of each export cycle, relaying the outcome of the file export process.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/2c60807-image.png",
        null,
        "Screenshot of Flow Recordings"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Flow Recordings"
    }
  ]
}
[/block]


To access the recordings:

1. Go to the **Tools** > **Voice Recordings**.
2. Navigate to the **Settings** tab.
3. Select the **File Destination**.
4. For **none**, enable the required voice recordings. Only the enabled voice recordings will be saved to the configured location.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/b258f1a-image.png",
        null,
        "Screenshot of Recordings Settings"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Recordings Settings"
    }
  ]
}
[/block]


5. For FTP, enter the following details and enable the required voice recordings. Only the enabled voice recordings will be saved to the configured location.  
   (i) **User Name** - the user name used to login to the FTP server  
   (ii) **Password** - the password used to login to the FTP server  
   (iii) **Host Name** - the hostname of the FTP server  
   (iv) **Path Name** - the folder path on the FTP server  
   (v) **Port Name** - the port number for the FTP server.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/0665686-ftp-settings.png",
        "ftp-settings.png",
        "Screenshot of FTP Server Settings"
      ],
      "align": "center",
      "caption": "Screenshot of FTP Server Settings"
    }
  ]
}
[/block]


> 📘 Note
> 
> The FTP feature is no longer supported for new configurations, because Data sent via FTP is vulnerable to sniffing, spoofing, and brute force attacks, among other basic attack methods.
> 
> The feature will work as is for the existing customers.

6. For SFTP, enter the following details and enable the required voice recordings. Only the enabled voice recordings will be saved to the configured location.  
   (i) **User Name** - the user name used to login to the SFTP server  
   (ii) **Password** - the password used to login to the SFTP server  
   (iii) **Host Name** - the hostname of the SFTP server  
   (iv) **Path Name** - the folder path on the SFTP server  
   (v) **Port Name** - the port number for the SFTP server.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/c245f00-image.png",
        null,
        "Screenshot of SFTP Settings"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of SFTP Settings"
    }
  ]
}
[/block]


> 📘 Note
> 
> You can upload the private key (example: AWS based Open SSH key files like rsa512.ppk, rsa256.ppk, ecdsa521.ppk, ecdsa384.ppk, ecdsa256.ppk, ed25519.ppk, ECDSAprivate.ppk, EDDSA255private.ppk) for SFTP configuration, when you select the File Destination as SFTP using the **Upload** button.

7. For S3, enter the following details and enable the required voice recordings. Only the enabled voice recordings will be saved to the configured location.
   1. **User Name** - the user name used to login to the Amazon Simple Storage Service (S3) console.
   2. **Bucket Name** - the unique DNS compliant for your new bucket. A bucket consists of file folders or store objects.
   3. **Access Key** - the access key used to login to the S3 console.
   4. **Secret Key** - the secret key used to login to the S3 console.
   5. **Region** - the region of the S3 console.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/d6f71a3-image.png",
        null,
        "S3 Console Settings"
      ],
      "align": "center",
      "border": true,
      "caption": "S3 Console Settings"
    }
  ]
}
[/block]


8. Enter a URL for **File Export Notify URL**, to which a notification is sent when a new log file is generated. If an invalid URL is passed in API request or via a variable, then such request will not be considered eligible for retries.
9. Enter an email address for **Notify on Email**, to which a notification is sent when a new log file is generated.
10. Click **Save**.  
    The selected voice recordings are backed up to the configured location on a daily basis.