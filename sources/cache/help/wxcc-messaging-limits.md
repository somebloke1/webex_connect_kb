# Messaging Limits - WXCC

Source: https://help.webexconnect.io/docs/wxcc-messaging-limits
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:14+00:00

> ❗️ Accessing Messaging Limit
> 
> Please note this metric cannot be accessed for your phone number within WhatsApp app 'Account/Number Updates' section at this moment.

Messaging limits determine the maximum number of business-initiated conversations you can initiate using each of your phone numbers in a rolling 24-hour period. A business-initiated conversation begins when the first template message is delivered to a customer and ends 24 hours later.

Business phone numbers without an [approved display name](https://developers.facebook.com/micro_site/url/?click_from_context_menu=true&country=noam&destination=https%3A%2F%2Fwww.facebook.com%2Fbusiness%2Fhelp%2F338047025165344&event_type=click&last_nav_impression_id=0z90BGKEcON6K0dnh&max_percent_page_viewed=100&max_viewport_height_px=711&max_viewport_width_px=1440&orig_http_referrer=https%3A%2F%2Fdevelopers.facebook.com%2Fdocs%2Fwhatsapp%2Fmessaging-limits&orig_request_uri=https%3A%2F%2Fdevelopers.facebook.com%2Fajax%2Fdocs%2Fnav%2F%3Fpath1%3Dwhatsapp%26path2%3Dmessaging-limits&region=noam&scrolled=true&session_id=1qrYGA9BbUNeXpA6l&site=developers) are limited to 250 business-initiated conversations in a rolling 24-hour period. This includes all business phone numbers of an unverified business, since these numbers cannot receive display name approval until the business is verified.

Business phone numbers with a connected status and approved display name can initiate conversations with the following number of unique customers in a rolling 24-hour period:

- 1K unique customer
- 10K unique customers
- 100K unique customers
- An unlimited number of unique customers

## How to increase the Messaging limit

Messaging limits can be increased to the following:

- 1K business-initiated conversations
- 10K business-initiated conversations
- 100K business-initiated conversations
- An unlimited number of business-initiated conversations

You can increase your messaging limit to 1K on your own using the following methods. Higher limits, however, can only be achieved through [automatic scaling](https://developers.facebook.com/docs/whatsapp/messaging-limits#automatic-scaling), which happens after your limit has been increased to 1K.

Note that in order for your business phone number to be eligible for an increase, it must have a [connected status](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers#phone-number-status), and if your business phone number has a [low quality rating](https://www.facebook.com/business/help/896873687365001), it may continue to be limited to 250 business-initiated conversations until its quality rating improves.

## Open 1K Conversations in 30 Days

Open 1,000 or more business-initiated conversations in a 30-day moving period using templates with a [high quality rating](https://www.facebook.com/business/help/896873687365001). Once you reach this threshold, WhatsApp will analyze your [messaging quality](https://developers.facebook.com/docs/whatsapp/messaging-limits#messaging-quality) to determine if your messaging activity warrants an increase in your messaging limit. Based on this analysis, WhatsApp will then either [approve](https://developers.facebook.com/docs/whatsapp/messaging-limits#increase-approvals) or [deny](https://developers.facebook.com/docs/whatsapp/messaging-limits#increase-denials) an increase.

> 📘 Note
> 
> You can reach out to the support contact and request a messaging tier upgrade if you have completed business or identity verification or reached the 1K limit in the 30-day threshold, but you are still limited to 250 business-initiated discussions.

## Automatic Scaling

Once you have reached the 1K business-initiated conversations limit, each time you open a business-initiated conversation, WhatsApp will determine if your limit should be increased according to the following criteria:

- Your business phone number is [connected](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers#phone-number-status).
- Your business phone number quality rating is Medium or High.
- In the last 7 days, your business phone number has been used to open X or more business-initiated conversations, where X is the business phone number's current messaging limit, divided by 2.

If your business phone number meets all conditions, WhatsApp will increase its limit by one level, 24 hours later. If its quality rating has been set to Flagged for the last 7 days, WhatsApp will decrease its limit by one level immediately.

> 🚧 Quality Rating and Messaging Limit
> 
> If you meet these requirements but your business phone number has a low quality rating, you may continue to be limited to 250 business-initiated conversations until its quality rating improves. Please refer to [this](https://help.imiconnect.io/edit/about-your-whatsapp-business-phone-numbers-quality-rating) page for more details.

If you reach your messaging limit, you can initiate more conversations as soon as one or more active conversations end. For example:



![Screenshot displaying the messaging limit of 1000 business initiated conversations](https://files.readme.io/8753a1f-2024-03-05_11-56-38.jpg)

