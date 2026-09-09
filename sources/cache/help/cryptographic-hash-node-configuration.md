# Cryptographic Hash

Source: https://help.webexconnect.io/docs/cryptographic-hash-node-configuration
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:28:54+00:00

Cryptographic hash allows you to generate one-way hash of plain string using one of the supported algorithms. You can apply salt as an additional security. 



![Cryptographic Hash Node](https://files.readme.io/80e8484-Screenshot_2019-04-18_at_7.09.43_PM.png)




## Node Configuration

All the parameters and input fields that you need to define within the node window are explained below.



| Input Variables | Output Variables | Node Outcomes  |
| --- | --- | --- |
| ### Hashing algorithmSelect a Hashing algorithm to generate hash. We support four hashing algorithms.  <br>  <br>- SHA-256: This algorithm generates a unique, fixed size 256-bit (32-byte) hash<br>- SHA-512: This algorithm generates a unique, fixed size 512-bit (64-byte) hashPlain Text: Enter an input variable or plain text to be hashed  <br>  <br>Apply Salt: Select this checkbox, if you wish to configure additional security to the encrypted string .Salt is random data that is added to the string before it is passed to the hash function.  <br>  <br>Salt type: Select the type of Salt data you wish to add tot he string.Supported salt values include text ,base64 and Hex.You can also generate random value during runtime by selecting Autogenerate Salt.  <br>  <br>Salt value: Data that must be added to string to be hashed is provided here. | hash.output: Generated hash is stored in this variable  <br>  <br>hash.salt | onSuccess: Hash generated successfully.  <br>  <br>onError: Hash generation failed because of invalid input. |

