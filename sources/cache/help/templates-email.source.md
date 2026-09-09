<<prodname>> offers an intuitive drag and drop email composer to configure email templates. <<prodname>> supports two types of email templates:

**Full Templates** - A single email template comprising all key email components including header, body, and footer.

**Partial Templates** - Multiple partial templates can be combined to form a complete template. This feature is useful when you want to configure multiple email templates with common elements. E.g., A logistics company may have a series of email templates to inform customers about the order status at various stages. Typically the header and footer of all these emails will be the same while the body content will vary for each email template. Partial templates feature can be used in such situations by configuring partial email templates for each of the email header, email body, and email footer. These parts can be combined at run time to create full emailers.

- Partial templates are reusable blocks that you can use across various emails.
- Any change made to a partial template applies to all the emails that use the partial template.
- <<prodname>> allows you to **Test** partial email templates by clicking on the action dropdown for partial email templates under **Tools** -> **Templates** section. Once clicked, you will be able to select anywhere between two to ten partial email templates and test them in combination. Partials will be rendered in the order of selection.

## Configure a New Template

Steps to configure a new email template:

1. Go to **Tools** > **Templates**.
2. Click **Add New Template**.
3. Enter a **Name** for the template. Only lower case letters and underscores are allowed in this field. Do not use spaces in the template name.
4. Select the **Channel** as _Email_.
5. Enter a **Reference ID** for the template. For example, Brand Marketing. This can be used to reference the template in Send Email node when using Dynamic Template selection option.
6. Select the Template Type - **Full Template** or **Partial Template**. 
7. Enter a **Subject** for the template.

   [block:image]{"images":[{"image":["https://files.readme.io/990e3c06cf514d6a6360e08dd782446659f8ee0b2b6b3926dc151059d3fe25b4-edc1b23-Email_Template_Configuration.png","","Screenshot of Creating a New Email Template"],"align":"center","border":true,"caption":"Creating a New Email Template"}]}[/block]
8. Click **Save**.

> 📘 Email Subject
> 
> The character limit for Email Subject Lines in a template is 998 characters.

9. Click **Save & Next**. The Email Composer screen appears.

   [block:image]{"images":[{"image":["https://files.readme.io/06211eb56aa5c31d3953148720b4ce580f6bca0e487b0332681bd8f49d757219-daa62c9-Templates_Email_Composer_Email_Composer_Window.png","","Screenshot for Email Composer"],"align":"center","border":true,"caption":"Email Composer\n\n| Feature                | Description                                                                                                                                                                  |\n| :--------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |\n| 1\\.**HTML View**       | To view the HTML code of the composed Email template.                                                                                                                        |\n| 2\\.**Mobile View**     | To view how the composed email template will look on a mobile device.                                                                                                        |\n| 3\\.**Desktop View**    | To view how the composed email template will look on a desktop device.                                                                                                       |\n| 4. **Grids**           | To view the margin, paddings and outline of the building blocks.                                                                                                             |\n| 5\\.**Download**        | To download the composed email template in HTML format.                                                                                                                      |\n| 6. ** Save & Exit**    | To save the email template design and close the composer screen.                                                                                                             |\n| 7. **Building Blocks** | It contains all the building blocks to design a email template.                                                                                                              |\n| 8. **Style Palette**   | It contains all the style elements that can be used to change the properties such as margins and paddings,borders,background colour for building blocks and page background. |\n| 9. **Design Canvas**   | It is the work area that holds the design of the email template.                                                                                                             |"}]}[/block]
10. On the **Style Palette**, click on the **Global **tab. Set the required colors to apply background color for a page and a default background color for all Building Blocks.

    [block:image]{"images":[{"image":["https://files.readme.io/f2d3c2c0d3a39c15ba7f3585b0c0045bf4dd197b30eb76b53e6c06a1397c3422-3.png","","Screenshot of Applying Background Colour using Style Palette"],"align":"center","border":true,"caption":"Applying Background Colour using Style Palette"}]}[/block]
11. From the **Building Blocks **palette, drag-&-drop the required block on the workspace. For more information, see [Building Blocks]\(#building Block Options) section.

    [block:image]{"images":[{"image":["https://files.readme.io/34039655a48cd075e78632f9076ee0a5fe66fb176786d3e7749c43da8a533d03-4.png","","Screenshot of Building Blocks"],"align":"center","border":true,"caption":"Building Blocks"}]}[/block]
12. On the Style Palette, click on Global tab and apply colors for page background and foreground. Click on the Building Block tab to apply styles to selected individual building blocks.

    - **Dark Mode Settings**: Use the Dark mode for text colour, text, blocks, etc. 
    - **Background**: Use this option to set a background color for the page.
    - **Foreground**: Use this option to set a default color for all building blocks. When a new block is added to the workspace, the selected background color will be applied automatically.
    - **Page Title**: Use this option to enter the meaningful text that is displayed on the browser tab when the email is viewed on a desktop browser.

      [block:image]{"images":[{"image":["https://files.readme.io/8967e7eceaaf35a719034caa9beec0152f3c05950d4582c298057d48702f3258-5.png","","Screenshot of Style Palete"],"align":"center","border":true,"caption":"Style Palette"}]}[/block]

      The text of the Page Title will be displayed on the browser:

      [block:image]{"images":[{"image":["https://files.readme.io/f8d0d218ebaac2f48280b96dbba6f1874e32be3a1aaa7c7b2f46b70c6d15ad04-6.png","","Screenshot of the page title"],"align":"center","border":true,"caption":"Page Title"}]}[/block]
13. When a text is selected in any building block, a toolbar is displayed to apply font type, text size, text color, text alignment, text height and so on. You can also add a URL to a highlighted text.

    [block:image]{"images":[{"image":["https://files.readme.io/d61c87969bbadbebaf35491f9060f0980c142e4e609a619459f3822b964706d0-7.png","","Screenshot of the Text Toolbar"],"align":"center","border":true,"caption":"Text Toolbar"}]}[/block]

    > 📘 Note
    > 
    > $(x) button on the toolbar is not operational, but it does accept manually entered values.
14. For Image building blocks within the style palette, you can select an image or add a link for Desktop and Mobile devices.
15. Click **Save & Exit **to save and close the email composer screen. The system auto-saves the content every 2 minutes.
16. If you want to close the template without saving the changes, click on **x**. When you open the template again, the system will give you the option to retrieve the unsaved changes or open the template in its last saved version.

## Building Block Options

The building blocks are grouped based on their similarity under different accordions. Every block has a copy, copy code to clipboard, move, and delete options.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/0ddcfcff9f07496f2b087472ff049e1ed06444712c417241cce24c7b6d5ceb09-2025-04-06_21-13-43.png",
        "",
        "Screenshot for Building Block Options"
      ],
      "align": "center",
      "border": true,
      "caption": "Building Block Options"
    }
  ]
}
[/block]


## Manage unsubscribe link in an email

1. Open the email composer.
2. Click **Add Layout**. The Layout Palette is displayed.
3. From the Layout menu, drag and drop the **Footer** element on the canvas.  
   A text block with default text with a unsubscribe hyperlink is displayed.
4. Click on **Unsubscribe** text; the rich text toolbar is displayed.

![](https://files.readme.io/544123a-Toolbar.png "Toolbar.png")

4. On the toolbar, click **insert link** icon to configure the **Unsubscribe** hyperlink.
5. Enter the hyperlink details. and click **OK**.  
   You are done with unsubscribe link creation.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/8b33fe2-Hyperlink.png",
        "Hyperlink.png",
        "Screenshot of adding the Link"
      ],
      "align": "center",
      "caption": "Screenshot of adding the Link"
    }
  ]
}
[/block]


| Label             | Description                                                                                            |
| :---------------- | :----------------------------------------------------------------------------------------------------- |
| URL               | Enter the  URL of the hyperlink.  This  URL will open when a user clicks  'unsubscribe'  in the email. |
| Link display text | This is the hyperlink text in the email.                                                               |
| Mouseover text    | The text to display when the user hovers the mouse on the hyperlinked text.                            |

## Add Layout (Palette)

The Layout Palette interface enables you to design a template by a simple **drag and drop**  interaction. You can edit images and content with the help of an inbuilt editor. Following are the template elements and cards available in the layout:

[block:parameters]
{
  "data": {
    "h-0": "Element",
    "h-1": "Description",
    "0-0": "Pre-Header",
    "0-1": "A preheader is the short summary text that follows the subject line when an email is viewed in the inbox.",
    "1-0": "Header",
    "1-1": "Allows you to add an introductory content.",
    "2-0": "Spacer",
    "2-1": "Allows you to add a space between two elements. Click the spacer element on the canvas to open the Style Palette.",
    "3-0": "Button",
    "3-1": "Allows you to place a clickable button.  \nDouble-click the button element to configure the button.",
    "4-0": "Button & Text",
    "4-1": "Allows you to add a button (in the right) and a text box beside the button.",
    "5-0": "Text",
    "5-1": "Allows you to add a paragraph text.",
    "6-0": "Conditional",
    "6-1": "Allows you to create a conditional email based on the conditional criteria with the help of a conditional builder.  \nPlease note that you cannot add more than 120 IF/ELSEIF conditions within an Email Template.",
    "7-0": "Table (Textual)",
    "7-1": "Allows you to add a table to the template.",
    "8-0": "Image",
    "8-1": "Allows you to add an image. The image is justified to the content on the template.",
    "9-0": "Image(100%)",
    "9-1": "Allows you to add an image. This image occupies the total width of the template.",
    "10-0": "Image & Text (15:85)",
    "10-1": "Allows you to add image and text. The image occupies 15% of the width and the text 85% of the width.",
    "11-0": "Image & Text (30/70)",
    "11-1": "Allows you to add image and text. The image occupies 30% of the width and the text 70% of the width.",
    "12-0": "Image & Text (50/50)",
    "12-1": "Allows you to add image and text. The image occupies 50% of the width and the text 50% of the width.",
    "13-0": "Text & Image (50/50)",
    "13-1": "Allows you to add text and image. The text occupies 50% of the width and the image 50% of the width.",
    "14-0": "Image & Text",
    "14-1": "Allows you to add an image and a caption to the image.",
    "15-0": "Two Images & Text Group",
    "15-1": "Allows you to add two images, a header, and text to each image.",
    "16-0": "Three Images & Text Group",
    "16-1": "Allows you to add three images, a header, and text to each image.",
    "17-0": "Two Images Group",
    "17-1": "Allows you to add two images side to side as a group.",
    "18-0": "Three Images Group",
    "18-1": "Allows you to add three image side to side as a group.",
    "19-0": "Social Follow",
    "19-1": "Allows you to add text and image, configure link for social media sharing.",
    "20-0": "Divider",
    "20-1": "Allow you to add a divider(horizontal space ) between two elements.",
    "21-0": "Footer",
    "21-1": "Allows you to add footer to the email."
  },
  "cols": 2,
  "rows": 22,
  "align": [
    "left",
    "left"
  ]
}
[/block]


[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/344d151-Templates_Email_Building_Blocks_in_the_Email_Composer.png",
        "Templates Email Building Blocks in the Email Composer.png",
        "Screenshot of Buildng Blocks in the Email Composer."
      ],
      "align": "center",
      "caption": "Screenshot of Building Blocks in the Email Composer"
    }
  ]
}
[/block]


## Style (Palette)

The Style Palette enables you to customize and format the elements blocks and cards used in the canvas area.

[block:parameters]
{
  "data": {
    "h-0": "Element",
    "h-1": "Description",
    "0-0": "Background Color",
    "0-1": "Allows you to set the background color of the text.  \n  \nNote: This option is displayed on selecting a text element.",
    "1-0": "Image Style",
    "1-1": "Allows you to set  image style (i.e Height in pixels and width in percentage)  \n  \nNote: This option is displayed on selecting an image element.",
    "2-0": "Border Style",
    "2-1": "Allows you to set the width, radius, and color of the selected text.",
    "3-0": "> Border width",
    "3-1": "Drag and drop to set the border with of the text box",
    "4-0": "> Border Radius",
    "4-1": "Drag and drop to set the radius of the text box",
    "5-0": "> Border Color",
    "5-1": "Allows you to set the border color of the text box",
    "6-0": "> Border  Style",
    "6-1": "Allows you to set the border style. Choose a style from the dropdown.",
    "7-0": "Padding & Margins",
    "7-1": "Allows you to set the margin and paddings for the text.",
    "8-0": "> Padding top",
    "8-1": "Drag to set at the text padding above the text.",
    "9-0": "> Padding right",
    "9-1": "Drag to set at the text padding-right to the text.",
    "10-0": "> Padding bottom",
    "10-1": "Drag to set at the text padding below the text.",
    "11-0": "> Padding left",
    "11-1": "Drag to set at the text padding-left to the text.",
    "12-0": "> Margin top",
    "12-1": "Drag to set the top margin of the element",
    "13-0": "> Margin right",
    "13-1": "Drag to set the right margin of the element",
    "14-0": "> Margin bottom",
    "14-1": "Drag to set the bottom margin of the element",
    "15-0": "> Margin left",
    "15-1": "Drag to set the left margin of the element"
  },
  "cols": 2,
  "rows": 16,
  "align": [
    "left",
    "left"
  ]
}
[/block]


[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/ce7c091-email_composer_style_palette.png",
        "email_composer_style_palette.png",
        "Screenshot of Style Palette on Email Composer"
      ],
      "align": "center",
      "caption": "Screenshot of Style Palette on Email Composer"
    }
  ]
}
[/block]


### Source Mode

In this mode, you can enhance or modify the HTML code that may have come from an external party. It helps the user customize the templates that cannot be done in graphical mode. All the edits in the source mode can be previewed, cleared, viewed, or saved.

Click the **Toggle Switch** to enable/disable the code window.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/599aeb7-email_composer_html_view.png",
        "email_composer_html_view.png",
        "Screenshot of HTMLview on Email Composer"
      ],
      "align": "center",
      "caption": "Screenshot of HTML View on Email Composer"
    }
  ]
}
[/block]