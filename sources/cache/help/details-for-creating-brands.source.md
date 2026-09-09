Creating a brand in the 10DLC requires accurate company and tax information to ensure proper verification and avoid carrier rejections. This guide explains all fields in the Brand Creation form, categorized by organization type, and provides practical instructions for completion.

## Brand/Company Details

[block:parameters]
{
  "data": {
    "h-0": "Field Name",
    "h-1": "Mandatory/Optional ",
    "h-2": "Instruction",
    "0-0": "Legal Company Name",
    "0-1": "Mandatory",
    "0-2": "Must exactly match your official registration and tax records. For U.S. entities, ensure consistency with IRS registration.",
    "1-0": "Brand Name",
    "1-1": "Mandatory",
    "1-2": "The display or operating name of your brand. Can be the same as Legal Company Name.",
    "2-0": "Country of Registration",
    "2-1": "Mandatory",
    "2-2": "Select the country where your company is legally registered.",
    "3-0": "Type of Organization",
    "3-1": "Mandatory",
    "3-2": "Select the type of legal form of your organization.  \nOptions:  \nGovernment,  \nNon-Profit Organization,  \nPrivate Company,  \nPublicly Traded Company,"
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


## Tax Details

[block:parameters]
{
  "data": {
    "h-0": "Field Name",
    "h-1": "Mandatory/Optional",
    "h-2": "Instruction",
    "0-0": "Tax Number / EIN / ID",
    "0-1": "Mandatory",
    "0-2": "United States: Enter IRS-issued 9-digit EIN.  \nCanada: Enter the first 9 digits of your Business Number (BN).  \nEU/APAC/Other: Enter VAT ID or corporate registration number.",
    "1-0": "Tax Number Issuing Country",
    "1-1": "Mandatory",
    "1-2": "Select the country that issued your Tax Number/ ID/ EIN",
    "2-0": "DUNS, GIIN, or LEI Number",
    "2-1": "Optional",
    "2-2": "Enter if applicable. Used for global business identification."
  },
  "cols": 3,
  "rows": 3,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


Refer to the section “[How to enter the correct Tax ID?](#how-to-enter-the-correct-tax-id)” for more detailed instructions.

## Business Details / Stocks and Business Details

| Field Name     | Mandatory/Optional                   | Instruction                                                                                                                    |
| :------------- | :----------------------------------- | :----------------------------------------------------------------------------------------------------------------------------- |
| Vertical Type  | Mandatory for all Organization types | Select the industry/vertical that best represents your business (e.g., Healthcare, Retail, Education, or Government Services). |
| Reference ID   | Optional                             | Unique identifier (ID for your client within the CSP database).                                                                |
| Stock Symbol   | Mandatory for Public Companies only  | Enter the official trading ticker (e.g., AAPL for Apple).                                                                      |
| Stock Exchange | Mandatory for Public Companies only  | Select from a list of recognized stock exchanges (e.g., NASDAQ, NYSE).                                                         |

## Company Contact & Address

| Field Name             | Mandatory                           | Instruction                                                       |
| :--------------------- | :---------------------------------- | :---------------------------------------------------------------- |
| Address                | Mandatory                           | Street, locality, and area. Must match tax registration records.  |
| City                   | Mandatory                           | Enter registered office city.                                     |
| State                  | Mandatory for (U.S.)                | Select from the dropdown.                                         |
| Zipcode                | Mandatory                           | Use the official postal/ZIP code.                                 |
| Country                | Mandatory                           | Pre-fills based on registration but can be adjusted.              |
| Website                | Mandatory                           | Enter the company’s official domain. It must be valid and active. |
| Support Email Address  | Mandatory                           | Dedicated support contact for customer inquiries.                 |
| Support Phone Number   | Mandatory                           | Use an active phone number for the customer support phone number. |
| Business Email Address | Mandatory for Public Companies only | Additional business contact email.                                |

## Reseller Information

| Field Name                | Mandatory/Optional | Instruction                                                                                                                  |
| :------------------------ | :----------------- | :--------------------------------------------------------------------------------------------------------------------------- |
| Are you a Cisco Reseller? | Yes / No           | Select "Yes" if you are an authorized reseller. A reseller ID will be generated and applied across all brands and campaigns. |

## Organization-Type Specific Requirements

| Organization Type                         | Mandatory Fields                                                                                                                                            |
| :---------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Government                                | Legal company name, Country of registration, EIN/Tax ID, Address, Vertical, Website, Contact details.                                                       |
| Non-Profit Organization                   | Legal company name, Country of registration, EIN/Tax ID, Address, Vertical, Contact details. Must be officially registered as NON PROFIT.                   |
| Private Company                           | Legal company name, Country of registration, EIN/Tax ID, Address, Vertical, Contact details.                                                                |
| Publicly Traded Company                   | Legal company name, Country of registration, EIN/Tax ID, Vertical, Stock Symbol, Stock Exchange, Full Contact & Address details (including Business Email). |
| Sole Proprietor (Currently not supported) | DBA/Brand Name, Country of registration, Full Address, Reference ID, First & Last Name, Email, Telephone number.                                            |

## Best Practices for Completing the Form

- **Match Records Exactly**: Legal name, tax ID, and address must match government/IRS/corporate registry records.
- **Use Official Email**: Support and business email addresses should be professional domains (not free email services like Gmail/Yahoo).
- **Ensure Website Validity**: The provided website must resolve and represent the brand.
- **Organization Type Accuracy**: Select the correct organization type to avoid rejections.
- **Resellers**: If acting as a reseller, always mark correctly to ensure Campaign Registry ID linkage.

## Information for Different Organization Types

For creating brands for one of the 5 organizations, certain mandatory information has to be added or selected. The table below provides information on the information to be mapped against each type of organization while creating a brand:

[block:parameters]
{
  "data": {
    "h-0": "Organization",
    "h-1": "Mandatory Fields",
    "0-0": "Public Traded Company",
    "0-1": "**Brand/ Company Details**  \nLegal Company Name  \nBrand Name  \nCountry Of Registration  \n  \n**Tax Details**  \nTax Number/ID/EIN  \nTax Number Issuing Country  \n  \n**Stocks and Business Details**  \nStock Symbol  \nStock Exchange  \nVertical Type  \n  \n**Company Contact & Address**  \nAddress  \nCity  \nState  \nZipcode  \nCountry  \nWebsite  \nSupport Email Address  \nSupport Phone Number  \nBusiness Email Address  \n  \n**Reseller Information**",
    "1-0": "Private Company",
    "1-1": "**Brand/ Company Details**  \nLegal Company Name  \nBrand Name  \nCountry Of Registration  \n  \n**Tax Details**  \nTax Number/ID/EIN  \nTax Number Issuing Country  \n  \n**Business Details**  \nVertical Type  \n  \n**Company Contact & Address**  \nAddress  \nCity  \nState  \nZipcode  \nCountry  \nWebsite  \nSupport Email Address  \nSupport Phone Number  \n  \n**Reseller Information**",
    "2-0": "Non-profit organization",
    "2-1": "**Brand/ Company Details**  \nLegal Company Name  \nBrand Name  \nCountry Of Registration  \n  \n**Tax Details**  \nTax Number/ID/EIN  \nTax Number Issuing Country  \n  \n**Business Details**  \nVertical Type  \n  \n**Company Contact & Address**  \nAddress  \nCity  \nState  \nZipcode  \nCountry  \nWebsite  \nSupport Email Address  \nSupport Phone Number  \n  \n**Reseller Information**",
    "3-0": "Government",
    "3-1": "**Brand/ Company Details**  \nLegal Company Name  \nBrand Name  \nCountry Of Registration  \n  \n**Tax Details**  \nTax Number/ID/EIN  \n  \n**Business Details**  \nVertical Type  \n  \n**Company Contact & Address**  \nAddress  \nCity  \nState  \nZipcode  \nCountry  \nWebsite  \nSupport Email Address  \nSupport Phone Number  \n  \n**Reseller Information**"
  },
  "cols": 2,
  "rows": 4,
  "align": [
    "left",
    "left"
  ]
}
[/block]


## How to enter the correct Tax ID

The Tax ID number is used in conjunction with the company’s name, address, and other information to ensure that we perform a background investigation on the correct company. The following guidance will provide the best verification opportunity for your company.

**United States**

 If you are a US company or a foreign company with a US IRS Employer Identification Number (EIN), please enter that nine-digit number in the EIN field and ensure that your legal company name is consistent with your IRS registration and is properly spelled. The address you enter should also be the same as that used in registering with the IRS.

 **Canada**

 If your primary business registration is in Canada, please enter your Canadian Corporation Number, which may be federal or provincial. Please do NOT enter your business number or federal tax ID number, as that is not readily cross-referenced. As always, please ensure that your legal company name is consistent with your corporation registration and is properly spelled. The address you enter should also be the same as that used in registering with Corporations Canada.

- Alberta: Corporate Access Number 

- British Columbia: Requires an alpha prefix (BC)

- Quebec: Quebec Business Number

- Ontario: Federal Corporation Business Number (begins with two zeros, but remove leading zeros in admin to verify)

- Manitoba: Manitoba Corporation Number 

- Europe, Eastern Europe, North Atlantic, Middle East, South America, and APAC

Please enter the numeric portion of your VAT ID number. Automated VAT identification matching is currently optimized for the following list of countries. If your country is not on this list, please provide the primary corporation registration number or tax ID number for your country. 

| Country              | Country Abbreviation |
| :------------------- | :------------------- |
| Croatia              | HR                   |
| Hungary              | HU                   |
| Ireland              | IE                   |
| Italy                | IT                   |
| Lithuania            | LT                   |
| Luxembourg           | LU                   |
| Latvia               | LV                   |
| Malta                | MT                   |
| Netherlands          | NL                   |
| Norway               | NO                   |
| Poland               | PL                   |
| Portugal             | PT                   |
| Romania              | RO                   |
| Sweden               | SE                   |
| Slovenia             | SI                   |
| Slovakia             | SK                   |
| Northern Ireland     | XI                   |
| United Arab Emirates | AE                   |
| Australia            | AU                   |
| Belarus              | BY                   |
| Chile                | CL                   |
| Iceland              | IS                   |
| Malaysia             | MY                   |
| New Zealand          | NZ                   |
| Saudi Arabia         | SA                   |
| Singapore            | SG                   |
| Taiwan               | TW                   |