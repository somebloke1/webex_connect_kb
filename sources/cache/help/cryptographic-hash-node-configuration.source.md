Cryptographic hash allows you to generate one-way hash of plain string using one of the supported algorithms. You can apply salt as an additional security. 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/80e8484-Screenshot_2019-04-18_at_7.09.43_PM.png",
        "Screenshot 2019-04-18 at 7.09.43 PM.png",
        "Screenshot of Cryptographic Hash Node."
      ],
      "align": "center",
      "caption": "Cryptographic Hash Node"
    }
  ]
}
[/block]


## Node Configuration

All the parameters and input fields that you need to define within the node window are explained below.

[block:parameters]
{
  "data": {
    "h-0": "Input Variables",
    "h-1": "Output Variables",
    "h-2": "Node Outcomes ",
    "0-0": "### Hashing algorithmSelect a Hashing algorithm to generate hash. We support four hashing algorithms.  \n  \n- SHA-256: This algorithm generates a unique, fixed size 256-bit (32-byte) hash\n- SHA-512: This algorithm generates a unique, fixed size 512-bit (64-byte) hashPlain Text: Enter an input variable or plain text to be hashed  \n  \nApply Salt: Select this checkbox, if you wish to configure additional security to the encrypted string .Salt is random data that is added to the string before it is passed to the hash function.  \n  \nSalt type: Select the type of Salt data you wish to add tot he string.Supported salt values include text ,base64 and Hex.You can also generate random value during runtime by selecting Autogenerate Salt.  \n  \nSalt value: Data that must be added to string to be hashed is provided here.",
    "0-1": "hash.output: Generated hash is stored in this variable  \n  \nhash.salt",
    "0-2": "onSuccess: Hash generated successfully.  \n  \nonError: Hash generation failed because of invalid input."
  },
  "cols": 3,
  "rows": 1,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]