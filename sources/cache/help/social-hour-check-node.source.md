The Social Hour Check node enables you to configure the permissible hours within which you can deliver a message to the user. Some countries allow delivery of messages like marketing information/order delivery updates during a specific time period only. It is important to configure social hours in such scenarios, where you can check for the permissible time range before you deliver the message to the users.<br>

When you configure the Social Hour Check node, the node checks if the request falls within the social hour range before proceeding further. If the request falls in the non-social hour period, you can take one of the two paths:

- **Wait for next available social hours **- In this case, <<prodname>> waits at this node until the next social hour window opens (based on your configuration) again at which stage the processing is resumed. You would choose this option for requirements such as sending a proactive notification for an upcoming appointment later in the week or month.

- **Branch requests not in social hour** - In this case, an alternative path is taken (based on your flow configuration) for handling the requests that fall outside of social hour window. You would choose this option for sending out of office auto-responders to customers who have reached out for live agent support outside of contact center operating hours.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/eb52008-Social.jpg",
        "Social.jpg",
        "Screenshot of Social Hour Check Node."
      ],
      "align": "center",
      "caption": "Social Hour Check Node"
    }
  ]
}
[/block]


Social hours play an important role in ensuring that you do not disturb the users at the wrong time of the day. You can configure working hours for your business, holidays, and special days using the Social Hour Check node. You can also set exceptions to the social hours. For example, if your normal working hours are from 9 AM to 6 PM, you can configure an exception of 1 PM to 2 PM as the lunch hour.<br>

## Node Configuration

Double-click the node to open the configuration window. Perform the following steps to configure the node:

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/a7c5974-Social_Hour_Check.jpg",
        "",
        "Screenshot of Social Hour Check Node Configuration Page"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Social Hour Check Node Configuration Page"
    }
  ]
}
[/block]


1. Choose a **Social Hours Policy**.
   - **Wait for next available social hours** - if the message originates outside of the configured social hours, the flow waits till the next available social hour slot to deliver the message.
   - **Branch requests not in social hours** - the request goes to an error edge.
2. Select **Add additional delay** and enter the **Delay (in minutes)** if you want the flow to wait for more time apart from the configured social hours.
3. Configure the social hours. You can configure the social hours for the entire week (by default, Monday to Friday) or individual days of the week with varied timings.
   - Enable the **Customize by Day** option if you want to set the social hours for specific days of the week or different time on different days and select the required days.
   - Enter the **From** and **To** time in 24-hour format.
   - Select **Set social hours exception** if you want to exclude specified duration from the social hours.
   - Click **Add New** to add more exceptions. You can add multiple exceptions.
   - Click the **Calendar** icon, pick a date, and click **Add** to add any holidays that you want to include as non-social hours. Repeat this step for all the holidays that you would like to add. If you mark a specific day as a holiday, it overwrites the social hours configured earlier for that day.
   - Select the **Time Zone (of the request)**. This time zone is applied to the configured social hours.

You can use Dynamic Timezone functionality in Social Hours that enables it to automatically analyze the acceptable social hours while sending a message or call in the selected time zone.

The Dynamic Timezone allows timezone parameters to be entered during the run-time (earlier only static parameters were supported). 

- To enable the dynamic timezone, “Select Dynamic Time Zone” option from the timezone drop-down.  
  A text box will appear.
- Enter the parameters.
- Click **Save**.  
  The Dynamic Timezone has been enabled and will allow you to enter timezone code during the runtime (See the below list for predefined timezone codes).

> 📘 Note:
> 
> The time zones configured in the Social Hour node are based on the 2025 [IANA](https://data.iana.org/time-zones/tzdb-2025b/) time zone file. All existing tenants currently use this 2025 file for time zone and Daylight-Saving Time (DST) calculations. Tenants wishing to update to the latest IANA time zone data must submit an operations ticket to request this change. This process ensures stability for existing tenants while allowing controlled updates to latest DST rules.

**Timezone Codes**

The following are the list of codes for different timezones:

Europe/Andorra  
Asia/Dubai  
Asia/Kabul  
America/Antigua  
America/Anguilla  
Europe/Tirane  
Asia/Yerevan  
Africa/Luanda  
Antarctica/McMurdo  
Antarctica/Casey  
Antarctica/Davis  
Antarctica/DumontDUrville  
Antarctica/Mawson  
Antarctica/Palmer  
Antarctica/Rothera  
Antarctica/Syowa  
Antarctica/Troll  
Antarctica/Vostok  
America/Argentina/Buenos_Aires  
America/Argentina/Cordoba  
America/Argentina/Salta  
America/Argentina/Jujuy  
America/Argentina/Tucuman  
America/Argentina/Catamarca  
America/Argentina/La_Rioja  
America/Argentina/San_Juan  
America/Argentina/Mendoza  
America/Argentina/San_Luis  
America/Argentina/Rio_Gallegos  
America/Argentina/Ushuaia  
Pacific/Pago_Pago  
Europe/Vienna  
Australia/Lord_Howe  
Antarctica/Macquarie  
Australia/Hobart  
Australia/Currie  
Australia/Melbourne  
Australia/Sydney  
Australia/Broken_Hill  
Australia/Brisbane  
Australia/Lindeman  
Australia/Adelaide  
Australia/Darwin  
Australia/Perth  
Australia/Eucla  
America/Aruba  
Europe/Mariehamn  
Asia/Baku  
Europe/Sarajevo  
America/Barbados  
Asia/Dhaka  
Europe/Brussels  
Africa/Ouagadougou  
Europe/Sofia  
Asia/Bahrain  
Africa/Bujumbura  
Africa/Porto-Novo  
America/St_Barthelemy  
Atlantic/Bermuda  
Asia/Brunei  
America/La_Paz  
America/Kralendijk  
America/Noronha  
America/Belem  
America/Fortaleza  
America/Recife  
America/Araguaina  
America/Maceio  
America/Bahia  
America/Sao_Paulo  
America/Campo_Grande  
America/Cuiaba  
America/Santarem  
America/Porto_Velho  
America/Boa_Vista  
America/Manaus  
America/Eirunepe  
America/Rio_Branco  
America/Nassau  
Asia/Thimphu  
Africa/Gaborone  
Europe/Minsk  
America/Belize  
America/St_Johns  
America/Halifax  
America/Glace_Bay  
America/Moncton  
America/Goose_Bay  
America/Blanc-Sablon  
America/Toronto  
America/Nipigon  
America/Thunder_Bay  
America/Iqaluit  
America/Pangnirtung  
America/Atikokan  
America/Winnipeg  
America/Rainy_River  
America/Resolute  
America/Rankin_Inlet  
America/Regina  
America/Swift_Current  
America/Edmonton  
America/Cambridge_Bay  
America/Yellowknife  
America/Inuvik  
America/Creston  
America/Dawson_Creek  
America/Fort_Nelson  
America/Vancouver  
America/Whitehorse  
America/Dawson  
Indian/Cocos  
"Africa/Kinshasa  
Africa/Lubumbashi  
Africa/Bangui  
Africa/Brazzaville  
Europe/Zurich  
Africa/Abidjan  
Pacific/Rarotonga  
America/Santiago  
America/Punta_Arenas  
Pacific/Easter  
Africa/Douala  
Asia/Shanghai  
Asia/Urumqi  
America/Bogota  
America/Costa_Rica  
America/Havana  
Atlantic/Cape_Verde  
America/Curacao  
Indian/Christmas  
Asia/Nicosia  
Asia/Famagusta  
Europe/Prague  
Europe/Berlin  
Europe/Busingen  
Africa/Djibouti  
Europe/Copenhagen  
America/Dominica  
America/Santo_Domingo  
Africa/Algiers  
America/Guayaquil  
Pacific/Galapagos  
Europe/Tallinn  
Africa/Cairo  
Africa/El_Aaiun  
Africa/Asmara  
Europe/Madrid  
Africa/Ceuta  
Atlantic/Canary  
Africa/Addis_Ababa  
Europe/Helsinki  
Pacific/Fiji  
Atlantic/Stanley  
Pacific/Chuuk  
Pacific/Pohnpei  
Pacific/Kosrae  
Atlantic/Faroe  
Europe/Paris  
Africa/Libreville  
Europe/London  
America/Grenada  
Asia/Tbilisi  
America/Cayenne  
Europe/Guernsey  
Africa/Accra  
Europe/Gibraltar  
America/Godthab  
America/Danmarkshavn  
America/Scoresbysund  
America/Thule  
Africa/Banjul  
Africa/Conakry  
America/Guadeloupe  
Africa/Malabo  
Europe/Athens  
Atlantic/South_Georgia  
America/Guatemala  
Pacific/Guam  
Africa/Bissau  
America/Guyana  
Asia/Hong_Kong  
America/Tegucigalpa  
Europe/Zagreb  
America/Port-au-Prince  
Europe/Budapest  
Asia/Jakarta  
Asia/Pontianak  
Asia/Makassar  
Asia/Jayapura  
Europe/Dublin  
Asia/Jerusalem  
Europe/Isle_of_Man  
Asia/Kolkata  
ndian/Chagos  
Asia/Baghdad  
Asia/Tehran  
Atlantic/Reykjavik  
Europe/Rome  
Europe/Jersey  
America/Jamaica  
Asia/Amman  
Asia/Tokyo  
Africa/Nairobi  
Asia/Bishkek  
Asia/Phnom_Penh  
Pacific/Tarawa  
Pacific/Enderbury  
Pacific/Kiritimati  
Indian/Comoro  
America/St_Kitts  
Asia/Pyongyang  
Asia/Seoul  
Asia/Kuwait  
America/Cayman  
Asia/Almaty  
Asia/Qyzylorda  
Asia/Qostanay  
Asia/Aqtobe  
Asia/Aqtau  
Asia/Atyrau  
Asia/Oral  
Asia/Vientiane  
Asia/Beirut  
America/St_Lucia  
Europe/Vaduz  
Asia/Colombo  
Africa/Monrovia  
Africa/Maseru  
Europe/Vilnius  
Europe/Luxembourg  
Europe/Riga  
Africa/Tripoli  
Africa/Casablanca  
Europe/Monaco  
Europe/Chisinau  
Europe/Podgorica  
America/Marigot  
Indian/Antananarivo  
Pacific/Majuro  
Pacific/Kwajalein  
Europe/Skopje  
Africa/Bamako  
Asia/Yangon  
Asia/Ulaanbaatar  
Asia/Hovd  
Asia/Choibalsan  
Asia/Macau  
Pacific/Saipan  
America/Martinique  
Africa/Nouakchott  
America/Montserrat  
Europe/Malta  
Indian/Mauritius  
Indian/Maldives  
Africa/Blantyre  
America/Mexico_City  
America/Cancun  
America/Merida  
America/Monterrey  
America/Matamoros  
America/Mazatlán  
America/Chihuahua  
America/Ojinaga  
America/Hermosillo  
America/Tijuana  
America/Bahia_Banderas  
Asia/Kuala_Lumpur  
Asia/Kuching  
Africa/Maputo  
Africa/Windhoek  
Pacific/Noumea  
Africa/Niamey  
Pacific/Norfolk  
Africa/Lagos  
America/Managua  
Europe/Amsterdam  
Europe/Oslo  
Asia/Kathmandu  
Pacific/Nauru  
Pacific/Niue  
Pacific/Auckland  
Pacific/Chatham  
Asia/Muscat  
America/Panama  
America/Lima  
Pacific/Tahiti  
Pacific/Marquesas  
Pacific/Gambier  
Pacific/Port_Moresby  
Pacific/Bougainville  
Asia/Manila  
Asia/Karachi  
Europe/Warsaw  
America/Miquelon  
Pacific/Pitcairn  
America/Puerto_Rico  
Asia/Gaza  
Asia/Hebron  
Europe/Lisbon  
Atlantic/Madeira  
Atlantic/Azores  
Pacific/Palau  
America/Asuncion  
Asia/Qatar  
Indian/Reunion  
Europe/Bucharest  
Europe/Belgrade  
Europe/Kaliningrad  
Europe/Moscow  
Europe/Simferopol  
Europe/Kirov  
Europe/Astrakhan  
Europe/Volgograd  
Europe/Saratov  
Europe/Ulyanovsk  
Europe/Samara  
Asia/Yekaterinburg  
Asia/Omsk  
Asia/Novosibirsk  
Asia/Barnaul  
Asia/Tomsk  
Asia/Novokuznetsk  
Asia/Krasnoyarsk  
Asia/Irkutsk  
Asia/Chita  
Asia/Yakutsk  
Asia/Khandyga  
Asia/Vladivostok  
Asia/Ust-Nera  
Asia/Magadan  
Asia/Sakhalin  
Asia/Srednekolymsk  
Asia/Kamchatka  
Asia/Anadyr  
Africa/Kigali  
Asia/Riyadh  
Pacific/Guadalcanal  
Indian/Mahe  
Africa/Khartoum  
Europe/Stockholm  
Asia/Singapore  
Atlantic/St_Helena  
Europe/Ljubljana  
Arctic/Longyearbyen  
Europe/Bratislava  
Africa/Freetown  
Europe/San_Marino  
Africa/Dakar  
Africa/Mogadishu  
America/Paramaribo  
Africa/Juba  
Africa/Sao_Tome  
America/El_Salvador  
America/Lower_Princes  
Asia/Damascus  
Africa/Mbabane  
America/Grand_Turk  
Africa/Ndjamena  
Indian/Kerguelen  
Africa/Lome  
Asia/Bangkok  
Asia/Dushanbe  
Pacific/Fakaofo  
Asia/Dili  
Asia/Ashgabat  
Africa/Tunis  
Pacific/Tongatapu  
Europe/Istanbul  
America/Port_of_Spain  
Pacific/Funafuti  
Asia/Taipei  
Africa/Dar_es_Salaam  
Europe/Kiev  
Europe/Uzhgorod  
Europe/Zaporozhye  
Africa/Kampala  
Pacific/Midway  
Pacific/Wake  
America/New_York  
America/Detroit  
America/Kentucky/Louisville  
America/Kentucky/Monticello  
America/Indiana/Indianapolis  
America/Indiana/Vincennes  
America/Indiana/Winamac  
America/Indiana/Marengo  
America/Indiana/Petersburg  
America/Indiana/Vevay  
America/Chicago  
America/Indiana/Tell_City  
America/Indiana/Knox  
America/Menominee  
America/North_Dakota/Center  
America/North_Dakota/New_Salem  
America/North_Dakota/Beulah  
America/Denver  
America/Boise  
America/Phoenix  
America/Los_Angeles  
America/Anchorage  
America/Juneau  
America/Sitka  
America/Metlakatla  
America/Yakutat  
America/Nome  
America/Adak  
Pacific/Honolulu  
America/Montevideo  
Asia/Samarkand  
Asia/Tashkent  
Europe/Vatican  
America/St_Vincent  
America/Caracas  
America/Tortola  
America/St_Thomas  
Asia/Ho_Chi_Minh  
Pacific/Efate  
"Pacific/Wallis  
Pacific/Apia  
Asia/Aden  
Indian/Mayotte  
Africa/Johannesburg  
Africa/Lusaka  
Africa/Harare

In case the entered time zone code is not the accepted value, it will generate an error outcome (Refer below image):

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/36c6db3-Social_Hour_Check1.jpg",
        "social hour_erroroutcome.png",
        "Screenshot of Node Outcomes"
      ],
      "align": "center",
      "sizing": "300px",
      "border": true,
      "caption": "Node Outcomes"
    }
  ]
}
[/block]


## Input Variables

You can see a list of all the flow variables available for use within this node under the **Input Variables** pane. You can also search for a variable using the **Search** field.

You can see the list of variables that you explicitly create and configure for this node under the **Custom Variables** pane. You can also add a custom variable to the flow using the **Add New Custom Variable** button. For more information, see [Custom Variables](doc:variable-management#section-custom-variables).

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/3ce7c82-Social_Hour_Check3.jpg",
        "57ba897-socialhour_input_variables.png",
        "Screenshot of Input and Custom Variables."
      ],
      "align": "center",
      "border": true,
      "caption": "Input and Custom Variables"
    }
  ]
}
[/block]


## Output Variables

You can see the data that this node generates as output variables. These [variables](doc:variable-management) are available for use in subsequent nodes. The following are the standard output variables for the Social Hour Check node:

- **socialHour.timeToNext** - . 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/48e738f-Social_Hour_Check2.jpg",
        "Social Hour Check Output Variables.png",
        "Screenshot of Output Variables."
      ],
      "align": "center",
      "sizing": "300px",
      "border": true,
      "caption": "Output Variables"
    }
  ]
}
[/block]


## Node Outcomes

You can see the list of possible node outcomes for this node under this pane. You can customize the node labels using the **Edit** (pencil) icon. The node exits through one of the node edges corresponding to the outcome of the node.

[block:parameters]
{
  "data": {
    "h-0": "Node Edge",
    "h-1": "Node Event/Outcome",
    "0-0": "Success (green)  \n  \n**Note**: You can see this node edge only when you complete the node configuration.",
    "0-1": "\\* **onSuccess** - the flow exits through this node when it is a success.",
    "1-0": "Timeout (yellow/amber)",
    "1-1": "\\* **nextSocialHour** - the flow exits through this node outcome when the message originates outside the configured social hours. The flow then waits for the next social hour to deliver the message.",
    "2-0": "Error (red)",
    "2-1": "\\* **onError** - the flow exits through this node outcome when there is an error",
    "3-0": "",
    "3-1": "\\* **notInSocialHour** -This branch is executed when the transaction occurs outside the time window specified for social interaction in the Social Hour node."
  },
  "cols": 2,
  "rows": 4,
  "align": [
    "left",
    "left"
  ]
}
[/block]


See the [example](#section-example) for configuration details.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/4ef57e2-Social_Hour_Check1.jpg",
        "Social Hour Check Node outcomes.png",
        "Screenshot of Node Outcomes"
      ],
      "align": "center",
      "sizing": "300px",
      "border": true,
      "caption": "Node Outcomes"
    }
  ]
}
[/block]


## Transition Actions

Use this tab to configure the transition actions for <code>On-enter</code>/<code>On-leave</code> events. However, configuring transition actions is optional. For detailed instructions about configuring the transition actions, see [Node Transition Actions](doc:transition-actions).

### Example

A parcel delivery company wants to send updates to its users about the delivery status of their parcels. It uses the Social Hour Check node in its flow to check if it is the right hour to send updates. The company sends updates or messages only between 8 AM and 6 PM during the weekdays (except on a Wednesday) and 10 AM to 7 PM on the weekends. Any message that originates outside of these hours is queued and delivered in the next available social hour time slot. See the following configuration:

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/7d1df22-Social_Hour_Check4.jpg",
        "Social Hour Check Sample Configuration of Social Hours.png",
        "Screenshot of Sample Configuration of Social Hours."
      ],
      "align": "center",
      "sizing": "smart",
      "border": true,
      "caption": "Sample Configuration of Social Hours"
    }
  ]
}
[/block]