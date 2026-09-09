The Decryption node enables you to decrypt an encrypted text or a string into plain text using either:

- AWS-Key Management Service (AWS-KMS)
- <<prodname>> Decryption

Usage of Decryption node typically follows an encryption node earlier in the flow. Same Decryption method should be used in the Encryption and Decryption nodes. During decrypting a text or a string, you need to specify the same details, which you have configured while encrypting that text or string. 

Here is the node image:

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/fc94b07-Decryption.png",
        "Decryption.png",
        "Screenshot of Decryption Node."
      ],
      "align": "center",
      "border": true,
      "caption": "Decryption Node"
    }
  ]
}
[/block]


## Node Configuration

When you double-click the Decryption node, the Decryption screen appears with two tabs: Configuration and Transition Actions. The Configuration tab enables you to configure the decryption settings whereas the Transitions tab provides configuring the node on-enter/on-leave operations.

### Using AWS-KMS

To use AWS Key Management Service, you must have an account with AWS. We recommend creating this account in the region you want to have your data in. The details you would need include - Access Key, Secret key, AWS Region, Cyphertext Blob, Encryption Context Key and Value, and Grant Token.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/3858991-Decryption_Click_the_image_to_view_it_larger.png",
        "Decryption Click the image to view it larger.png",
        "Screenshot of Decryption Node Configuration Page."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Decryption Node Configuration Page."
    }
  ]
}
[/block]


Here is the description for the various config elements:

| Field                              | Description                                                                                                                                                                                                                                                              |
| :--------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Access Key and Secret Key          | These typically are the IAM user access credentials for your AWS KMS account. Copy these values from your AWS account.                                                                                                                                                   |
| AWS Region                         | This is the geographic area where your AWS KMS account is hosted. E.g., _us-west-2_ for AWS US West (Oregon). Refer [here](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html) for full list.                                     |
| Cyphertext Blob                    | Specify the encrypted text or string (or the variable that contains the text/string) that you wish to decrypt.                                                                                                                                                           |
| Encryption Context (Key and Value) | These are a set of non-secret key-value pairs. Providing encryption context makes the encryption request  bound cryptographically to the cipher-text.  The advantage with this is - same encryption context is required to decrypt (or decrypt and re-encrypt) the data. |
| Grant Token                        | Specify the **Grant Token**, which was created to provide temporary permissions.                                                                                                                                                                                         |

### Using <<prodname>> Decryption

Select <<prodname>> Decryption option from the Decryption Method dropdown and provide the following details:

| Field                   | Description                                                                     |
| :---------------------- | :------------------------------------------------------------------------------ |
| Text To Be Decrypted    | Enter the text or the variable that contains the text that you want to decrypt. |
| Store Decrypted Data In | Enter the variable in which you want to store the value of the decrypted text.  |