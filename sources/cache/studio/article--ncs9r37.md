# Webex AI Agent Studio Administration guide

Source: https://help.webex.com/article/ncs9r37
Documentation version: not specified by publisher
Source last modified: 2026-09-08T17:48:52.503Z
Retrieved: 2026-09-08T23:48:48+00:00

<a id="content"></a>

<a id="concept-template_47161120-d76a-489a-a2a8-e5a0cd63fa60"></a>

Webex AI Agent Studio is a sophisticated platform that is designed to create, manage, and deploy automated AI agents to fulfill customer service and support needs. Using artificial intelligence, AI agents provide automated assistance to customers before they interact with human agents. These agents support voice interactions with intonation, language understanding, and contextual awareness within conversations. Also, AI agents seamlessly and informatively handle digital channel interactions through text and online chat. Customers benefit from a concierge-like experience, receiving assistance with questions, information retrieval, and minimizing wait times.

<a id="section_mhv_lg1_1dc"></a>

### Key benefits for businesses

- **Efficiency & productivity**

  - Automates repetitive tasks, freeing human employees for strategic work.
  
  - Provides 24/7 availability, handling higher volumes and improving response times.
  
  - Improves accuracy in data processing, analysis, and reporting.

- **Cost savings**
  
  - Reduces labor costs through automation.
  
  - Optimizes resource allocation for greater efficiency.
  
  - Lowers operational costs by streamlining processes and preventing errors.

- **Enhanced decision-making**
  
  - Provides data-driven insights by analyzing large datasets.
  
  - Enables predictive analytics for anticipating future outcomes.
  
  - Improves risk management through identification and assessment.

- **Improved customer experience**
  
  - Personalizes interactions based on customer data.
  
  - Offers faster response times through AI-powered chatbots and virtual assistants.
  
  - Provides 24/7 customer support.

- **Scalability & flexibility**
  
  - Easily scales up or down to meet changing business needs.
  
  - Learns and adapts to new situations and information.

- **Competitive advantage**
  
  - Drives innovation and development of new products/services.
  
  - Increases efficiency for a competitive edge.

- **Employee Empowerment** 
  
  - Frees human potential for more creative and strategic work.
  
  - Enhances collaboration by providing data, insights, and support.

<a id="section_mgz_xq2_p3c"></a>

Table 1. Availability of Webex AI Agent
| Contact Center Solution | AI Agent Type |
| --- | --- |
| - Webex Contact Center<br>- Webex Contact Center Enterprise (WxCCE)<br>- Unified CCE (UCCE)<br>- Packaged CCE (PCCE)<br>- Unified CCX (UCCX)<br>  <br>   <br>  <br>  Unified CCX is currently available as an Alpha release. | Scripted AI Agent<br> <br>Autonomous AI Agent |

<a id="concept-template_14de745a-0b7b-467b-8d22-3c12249c96cc"></a>

### Understand AI agent types and examples

The following table provides a glimpse of AI agent types and their capabilities:

Table 2. AI agent types and their capabilities
| AI agent type | Purpose | How to set up? |
| --- | --- | --- |
| Autonomous | Autonomous agents work independently to fulfill the defined goals, reducing the need for continuous human intervention.<br>- They make decisions based on available information and predefined actions.<br>- They automate time-consuming or repetitive tasks.<br>- They access and use a knowledge base to deliver informative and accurate responses to user questions. | [Set up autonomous AI agent](https://help.webex.com/article/ncs9r37#concept-template_7f4b97c9-5d5e-49b5-a651-5293923e98f9) |
| Scripted | Scripted AI agents are programmed to follow a set of predefined rules and instructions.<br>- They perform specific tasks that are clearly defined and structured.<br>- They respond to questions based on a user-created training corpus, which is a collection of examples and answers. | [Set up scripted AI agent](https://help.webex.com/article/ncs9r37#concept-template_4777d368-bcf4-4e97-9b5d-9eb0db6b6393) |

<a id="section_vf3_rtd_xcc"></a>

#### Examples

Both autonomous and scripted AI agents apply to various use cases, depending on the specific requirements and desired capabilities. Some examples include:

- **Customer service**—Both autonomous and scripted agents can provide customer support, with autonomous agents offering more flexibility and understanding of natural language.

- **Virtual assistants**—Autonomous agents are well suited for virtual assistant roles as they can manage a wide range of tasks and offer more personalized interactions.

The choice between autonomous and scripted AI agents depend on the complexity of the tasks, the required level of autonomy, and the availability of training data.

<a id="concept-template_3f5db740-02c5-4c6e-a882-fce7fd503297"></a>

### Prerequisites

<a id="section_fp5_xn2_p3c"></a>

#### Webex Contact Center

- If an organization doesn't have an active contact center trial or subscription, partners can set up a contact center trial with the Webex AI agent feature. For more information, see [Webex Contact Center Self-Service Trials](https://help.webex.com/7eatkw) article.

- To sign up for subscription, customers need to purchase the AI Agent add-on for the Flex-3.0 Contact Center license. Based on entitlements, Webex Contact Center provisions AI Agent as one of its services for an organization. For more information about provisioning the Webex Contact Center, see [Get Started with Webex Contact Center](https://help.webex.com/nee1mb6).

<a id="section_jbs_yn2_p3c"></a>

#### Webex Contact Center Enterprise and Contact Center Enterprise

- Ensure that the following components are on release 15.0(1) ES202511 or later: Cisco Unified CVP, Cisco VVB, and Cloud Connect.

- To sign up for subscription, customers need to purchase the AI Agent add-on addon for Webex AI Agent in Cisco Commerce Workspace (CCW). See the Cisco Collaboration Flex Plan Contact Center Ordering Guide page at [https://www.cisco.com/c/en/us/products/collateral/customer-collaboration/collab-flex-3-contact-center-og.html](https://www.cisco.com/c/en/us/products/collateral/customer-collaboration/collab-flex-3-contact-center-og.html).

  Enable the hybrid organization setup, which integrates both cloud and on-premises environments with necessary entitlements. The ordering process involves selecting the appropriate AI Agent units under the Collaboration Flex 3.0 Contact Center Offering. Digital AI Agents also get activated as part of the voice subscription order. The voice AI Agent entitlement grants access to Webex AI Agent Studio, enabling you to design and create AI Agents tailored to your specific use case requirements.

  For details on how to configure AI Agents, see the Webex AI Agent chapter in the Cisco Unified Contact Center Enterprise Features Guide at [https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-feature-guides-list.html](https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-feature-guides-list.html) and the Cisco Packaged Contact Center Enterprise Features Guide at [https://www.cisco.com/c/en/us/support/contact-center/packaged-contact-center-enterprise-15-0-1/model.html](https://www.cisco.com/c/en/us/support/contact-center/packaged-contact-center-enterprise-15-0-1/model.html).

<a id="user-roles-and-permissions"></a>

### User roles and permissions

This section provides the details of the user roles and required permissions within an organization for accessing the AI Agent Studio application:

| Role | Customer organization | Partner organization | Any other organization |
| --- | --- | --- | --- |
| **Full Administrator** | Full access to AI Agent Studio, including management of transcript access for other users | Full access to AI Agent Studio, except sensitive information such as transcripts | Full access to AI Agent Studio, except sensitive information such as transcripts |
| **Contact Center Service Administrator** | Full access to AI Agent Studio, except sensitive information such as transcripts | Not applicable | Full access to AI Agent Studio except sensitive information such as transcripts |
| **Provisioning Administrator** | Not applicable | Full access to AI Agent Studio except, sensitive information such as transcripts | Not applicable |
| **Read-only Administrator** | Can't access the Webex Contact Center service on Control Hub | Read-only access to AI Agent Studio, except sensitive information such as transcripts | Read-only access to AI Agent Studio, except sensitive information such as transcripts |
| **Supervisor** | Read-only access to AI Agent Studio, except sensitive information such as transcripts | Not applicable | Not applicable |

Full administrators from the customer organization can access the Enterprise Profile. They use this to manage transcript access for themselves and other users in the organization. By default, no user has access to transcripts. Full administrators must explicitly grant this access to users in the organization.

<a id="section_oxm_h1m_nfc"></a>

#### Manage transcript access

As a full administrator, you can manage transcript access for users in your organization.

- Launch AI Agent Studio.
 
- Hover over the user icon in the bottom-left corner of the navigation menu and click **Enterprise Profile**.
 
- Click the **Teammates** tab to view the list of existing teammates.
 
- Click the **Modify** icon under **Actions**column.
 
- Enable the **Decrypt access** toggle to grant users access to transcripts.
 
- Click **Modify** to save the changes.

<a id="concept-template_ad62c8d0-c166-4c70-9fb9-4bb9ecdfc6ee"></a>

### Access Webex AI Agent Studio

To create your AI agents, you must sign in to the Webex AI Agent Studio application. You can sign in using the following ways:

<a id="section_ijc_bds_wcc"></a>

#### Sign-in from Control Hub

If you don’t see Webex AI Agent, contact Cisco Support to enable the corresponding feature flag.

- Sign in to [Control Hub](https://admin.webex.com).

- Select Services > Contact Center.

- From the Contact Center navigation pane, select Customer experience > AI Agent.

- Click Webex AI Agent to access the application.

This opens the Webex AI Agent Studio application in another browser tab, and you’re ready to configure your AI Agents.

Voice preview for AI agents is available only when you access Webex AI Agent Studio through Control Hub > Services > Contact Center, where voice channel interactions are supported.

<a id="section_vcz_gds_wcc"></a>

#### Sign-in from Webex Connect

To access the Webex AI Agent Studio application, you should have access to Webex Connect.

- Sign in to Webex Connect application using the tenant URL provided for your enterprise and credentials. 
  
  By default, the **Services** page appears as a home page.

  or

  Sign in to [Control Hub](https://admin.webex.com) and select Services **>** Contact Center. From the Contact Center navigation pane, select Tenant Settings **>** Digital. Select Webex Connect. The **Services** page appears as a home page.

- From the **App Tray** menu of the left navigation pane, click Webex AI Agent to access the application.
  
  The system opens the Webex AI Agent Studio application in another browser tab and you’re automatically signed-in to the application.

<a id="concept-template_edb134a0-96eb-41ab-94fa-b6baefef6b26"></a>

### Home page layout

Welcome to the Webex AI Agent Studio application. When you sign in, the home page displays the following layout:

- **Navigation bar**

  The navigation bar that appears on the left provides access to the following menus:

  - **Dashboard**—Displays a list of AI agents the user has access to, as granted by the enterprise administrator.
  
  - **Knowledge**—Shows the central knowledge repository or knowledge base, which serves as the brain for autonomous AI agents to respond to customer queries.
  
  - **Help**—Provides access to the Webex AI Agent Studio user guide on the Webex Help Center.
  
  - **Sign out**—Allows you to sign out of the Webex AI Agent Studio application.
 
- **User profile** 
  
  The user profile menu allows you to view your profile information, switch between UI themes, and sign out of the application. To change the theme, click Change Theme and choose your preferred option–Light, Dark, and System (default theme). The selected theme is instantly applied on all pages.

  The **Enterprise Profile**page contains information about the AI agent tenant.
 
- - The General tab displays the organizational timezone. Choose the required timezone from the drop-down menu. When you create a new agent, the chosen timezone appears in the agent profile page. See the [Update autonomous AI agent profile](https://help.webex.com/article/ncs9r37#task-template_5416be2f-b95e-4b80-bebc-3fa8201414bf) section for more details.
  
  - In the **Teammates** tab, you can view and manage the list of teammates who have access to the application.

    Full administrators from the customer organization can access the Enterprise Profile. They use this to manage transcript access for themselves and other users in the organization. By default, no user has access to transcripts. Full administrators must explicitly grant this access to users in the organization.

<a id="concept-template_4059e8c6-51fa-47f1-b510-9aafbe7ead1f"></a>

### Know your Dashboard

On the dashboard, the AI agents are represented by cards. Each card displays basic information, including the AI agent name, last updated by, last updated on, and the engine used for training the agent.

<a id="section_us5_zdw_ycc"></a>

#### Tasks on AI agent card

Hover over an AI agent card to view the following options:

- **Preview**—Click **Preview** to open the AI agent preview widget.

- **Ellipsis** icon—Click this icon to perform the following tasks:
  
  - **Copy Access token**—Copy the AI agent's access token for invoking the agent through APIs.
  
  - **Export**—Export the AI agent details (in JSON format) to your local folder.
  
  - **Delete**—Permanently delete the AI agent from the system.
  
  - **Pin**—Pin the AI agent to the first position on the dashboard, or unpin to move it back to its previous position.

<a id="section_qtq_llv_ycc"></a>

#### Create a new AI agent

You can create a new AI agent by using the **+ Create agent** option on the top-right corner of the dashboard. You can choose to use a predefined template or create an agent from scratch.

To know how to create scripted and autonomous AI agents, see the following sections:

- [Create an autonomous AI agent](https://help.webex.com/article/ncs9r37#task-template_cd5ff649-b94c-4546-82e9-6dac68310ab9)

- [Create a scripted AI agent](https://help.webex.com/article/ncs9r37#task-template_72a02c77-a182-4301-b588-235a042809a2)

You can create up to 100 AI agents, which includes both scripted and autonomous types.

<a id="section_grn_byz_zcc"></a>

#### Import AI agent

You can import an AI agent in JSON format from a list of available AI agents. First, ensure you’ve exported the AI agent in JSON format to your local folder. Follow these steps to import it:

- Click Import agent.

- Click **Upload** to upload the AI agent file (in JSON format) exported from the platform.

- In the **Agent name** field, enter the AI agent name.

- (Optional) In the **System ID**, edit the system-generated unique identifier.

- Click **Import**.

Your AI agent is now successfully imported to the Webex AI Agent Studio platform and is available on the dashboard.

<a id="section_iln_mmv_ycc"></a>

#### Keyword search

The platform provides robust search capabilities to help you easily locate and manage AI agents. You can perform keyword search using the agent name. Enter the agent name or a portion of the name in the search bar. The system displays a list of AI agents that match your search criteria.

<a id="section_wdz_kdw_ycc"></a>

#### Filter by agent type

In addition to keyword search, you can refine your search results by filtering based on the type of AI agent. Choose one of the agent type filters from the drop-down list—**Scripted**, **Autonomous**, and **All**.

<a id="content"></a>

<a id="concept-template_ce8bd9fd-6585-4353-9fda-57b22ee97c33"></a>

A knowledge base is a central repository of information for the Large Language Model (LLM)-powered AI agents. The AI agents use advanced AI and machine learning technologies to understand, process, and generate human-like text. The AI engine trains the AI agents using vast amount of data, enabling them to provide detailed and contextually relevant responses. Knowledge bases store the data necessary for the functioning of autonomous AI agents.

Create the required knowledge base for the AI agent that you're configuring.

Do not upload any of the following to the knowledge base:

- Payment Card Industry (PCI) data

- Personally Identifiable Information (PII)

- Protected Health Information (PHI)

- Any other sensitive, confidential, or regulated information

You’re responsible for making sure all content you upload complies with these requirements.

If you are accessing the Knowledge page for the first time, a disclaimer appears prompting about sensitive data described above. Click agree to proceed further.

<a id="create-knowledge-source-for-ai-agent"></a>

### Create knowledge source for AI agent

- Log in to the Webex AI Agent Studio platform.
 
- Click the Knowledge icon on the left navigation pane to navigate to the Knowledge page.

You can create and manage knowledge base sources from the knowledge page. Knowledge sources for autonomous AI agents can be files, articles, website sources. If you’re adding sources for the first time, the Knowledge page displays the following tiles:

- **Upload files**: Choose this option to upload files. See the [Upload files](https://help.webex.com/article/ncs9r37#upload-files) section.
 
- **Create an article**: Choose this option to create an article. See the [Create articles](https://help.webex.com/article/ncs9r37#create-an-article) section.
 
- **Extract website**: Choose this option to extract website content. See the [Extract websites](https://help.webex.com/article/ncs9r37#extract-website) section.

Click the required tile to create the appropriate knowledge base source. You can also use the Add source drop-down button on the upper right corner of the page to add knowledge base sources. Choose Files, Articles, or Websites as required.

After you create the knowledge base sources, configure the knowledge base for the AI agents.

<a id="upload-files"></a>

### Upload files

<a id="context_wlq_gjv_43c"></a>

You can upload files as knowledge sources for your agents. Files can be .xlsx, .xls, .csv, .pdf, .docx, .doc, txt.

|  |  |
| --- | --- |
| 1 | Choose Add source > Files. |
| 2 | On the Upload files page, drag and drop the files to the knowledge base. Alternatively, click Add File to add a file.<br> <br>Keep the file name as descriptive as possible. The file name is used as the source name within the knowledge base. |
| 3 | Click Process Files to process the uploaded files. Click Clear list to clear the files. You can also choose to Close and keep processing.<br> <br>When done, you can view the processed files in the Processed files tab.<br> <br>**Additional Processing Notes**<br> <br>- The maximum wait time for processing a file before it gets timed out is 2 hours (measured from the time the file got picked up for processing). However, there is no limit for the time the file remains in the queue.<br>- Image-processing support is available only for PDF files.<br> <br>See the guidelines and best practices when uploading files:<br> <br>The file is listed in the Sources page.<br>Access the knowledge sources page to perform the following tasks.<br>- Click the **Edit** icon under Controls to edit the file.<br>- Click the **Delete** icon under Controls to delete the source. |

What to do next

Map the uploaded file to the AI agent. See the [Configure knowledge base](https://help.webex.com/en-us/article/ncs9r37/Webex-AI-Agent-Studio-Administration-guide#task-template_9b7eb61b-facf-4467-902b-53276bd3723d) section in the Webex AI Agent Studio Administration Guide.

<a id="concept-template_2e240339-836b-4c09-bf61-fc19a362da73"></a>

### Best practices when uploading files

Follow these guidelines and best practices when uploading files to the Knowledge Base:

- You can add multiple files at a time.
 
- For each tenant, the following file upload restrictions apply:

  - Total storage limit: 2 GB per Knowledge Base.
  
  - Maximum number of files: 100 files per Knowledge Base.
  
  - Individual file size limit: 10 MB.
  
  - Individual text (.txt) file size limit: 2 MB.
  
  - PDF file size limit: In addition to the file size limit, a limit of 300 pages per PDF is also applicable.

<a id="section_y1n_4sc_jjc"></a>

#### Dos and Don'ts when uploading files with tabular data (all file types)

This section outlines best practices when uploading files with tabular data:

**Dos**

- Keep tables simple and well-formed with a single header row at the top.

- Keep each table row under 6,000 characters (headers and row values combined).
  
  If a file upload fails, ensure no row exceeds 6,000 characters.

- Use clear, descriptive column headers in tables (for example, `Customer Name`, `Order Date`) as these headers are used when extracting the data.

**Don'ts**

- Do not use merged cells or nested tables in tabular content as the structure is lost during extraction.

- Do not include a single very large free-text paragraph in one cell. Always adhere to the 6,000-character row limit.

<a id="section_jzt_2tc_jjc"></a>

#### Dos and Don'ts when uploading spreadsheet (.xlsx, .xls, .csv)

This section outlines best practices when uploading spreadsheets and CSV files:

**Dos**

- Keep one table per sheet.

- Keep the headers in the first row followed by data rows. This enables the system to process the header row accurately.

- Adhere to the total allowed character count in spreadsheet which is **3,000,000 characters**.

- Keep each row under 6,000 characters (including headers row and data row combined).
  
  If a file upload fails, ensure no row exceeds 6,000 characters.

**Don'ts**

- Do not include hidden sheets if they are not needed, as the system still reads and ingests these sheets.

- Do not create multiple tables in one sheet. The system consolidates all tables from a single Excel sheet into one unified table. Therefore, clean up the file before uploading.

If the system takes too long to process your Excel file, it may be because of the large amount of data in the file. Consider splitting the data across multiple files and uploading the individual files separately.

<a id="concept-template_0c131373-4110-4aeb-a3ba-240436d578d9"></a>

### Limitations

See the following limitations:

- **Formatting**: The system doesn't preserve document and cell formats (colors, fonts, styles, and conditional formatting).

- **Indexing**: Tables inside PDFs, webpages, and markdown files are indexed as plain text. This reduces retrieval precision for queries that target specific rows or columns.

- **Spreadsheets and CSV files**: If a single row exceeds the character limit, the system rejects the entire file. Additionally, the system doesn't preserve hyperlinks in CSV files.

- **PDF files**: The system doesn't preserve hyperlinks in PDF files.

- **Word files (.docx, .doc)**: The system doesn't preserve hyperlinks inside table cells.

<a id="create-an-article"></a>

### Create articles

|  |  |
| --- | --- |
| 1 | Choose Add source > Articles. |
| 2 | On the Write an article page, under Source details enter the Source name and provide a detailed Description. |
| 3 | Type the required information in the text editor. Format the text using the format options, as needed.<br> <br>**Important Considerations:** You cannot add tables in documents. |
| 4 | Click Add Source. |

<a id="result_fdg_fhv_jjc"></a>

The article is added to the Sources page.

Access the knowledge sources page to perform the following tasks.

- Click the **Edit** icon under Controls to edit the article.

- Click the **Delete** icon under Controls to delete the source.

<a id="postreq_aht_jkw_v3c"></a>

What to do next

Map the uploaded file to the AI agent. See the [Configure knowledge base](https://help.webex.com/en-us/article/ncs9r37/Webex-AI-Agent-Studio-Administration-guide#task-template_9b7eb61b-facf-4467-902b-53276bd3723d) section in the Webex AI Agent Studio Administration Guide.

<a id="extract-website"></a>

### Extract website

<a id="section_vwc_hgw_43c"></a>

You can add knowledge to your AI agents by extracting information from websites you own. Website extraction uses automated crawling techniques to browse the internet to find and download the relevant content from web pages and transform it into knowledge that your AI agents can access.

Crawling begins with the starting URL that you specify. Based on the depth and the page limits, the crawler application navigates from the home page, visits the websites, and fetches the required content based on the URL patterns and subdomain definitions.

<a id="section_htc_jgw_43c"></a>

#### How does the Cisco Webex AI agent web crawler identify itself

The Cisco Webex AI agent web crawler identifies itself using the User-Agent Header mechanism. Use the following information to configure your web server, WAF, CDN, or bot management system to ensure the crawler can access your site when authorized.

Every HTTP request from the crawler includes a custom **User-Agent** header, which typically follows one of these patterns:

**Standard format:**

```text
CiscoWebexAIAgentCrawler/1.0 
(+url/ai-agent-crawler-info; ask-aiagent@cisco.com)
```

**Browser-like string that includes the crawler identifier:**

```text
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) 
AppleWebKit/537.36 (KHTML, like Gecko; compatible; 
CiscoWebexAIAgentCrawler/1.0; +url/ai-agent-crawler-info; 
ask-aiagent@cisco.com) Chrome/145.0.0.0 Safari/537.36
```

**Key identifier for allowlisting:** CiscoWebexAIAgentCrawler/1.0

When configuring allowlists or bot detection rules, use this string (or a prefix match such as ‘CiscoWebexAIAgentCrawler’) to identify the crawler.

<a id="section_t5w_gfq_fjc"></a>

#### How does the web crawler work with robots.txt

The crawler respects robots.txt and identifies itself with the **User-Agent** token `CiscoWebexAIAgentCrawler`.

The crawler sends a browser-like User-Agent header in HTTP requests for compatibility [for example Mozilla/5.0 (...; CiscoWebexAIAgentCrawler/1.0; ...)], but uses the token `CiscoWebexAIAgentCrawler` for robots.txt rule matching. Please use this exact token in your `robots.txt` directives.

See the following examples:

**- To allow full access to the crawler**

```text
User-agent: CiscoWebexAIAgentCrawler
```

```text
Allow: /
```

**- To restrict the crawler to specific paths**

```text
User-agent: CiscoWebexAIAgentCrawler
Allow: /public/
Allow: /docs/
Disallow: /admin/
Disallow: /private/
```

**- To disallow the crawler entirely**

```text
User-agent: CiscoWebexAIAgentCrawler
Disallow: /
```

**- To allow this crawler only and block all others**

```text
User-agent: CiscoWebexAIAgentCrawler
Allow: /
User-agent: *
Disallow: /
```

**Important Considerations:**

- **Exclusive group matching**: If both a User-agent: `CiscoWebexAIAgentCrawler` group and a User-agent: * group exist, the crawler follows only the rules in its named group; * rules are ignored. To apply both, duplicate the relevant directives in the named group.

- **Blank required**: Separate user-agent groups with a blank line, otherwise parsers may merge them.

- **Case-insensitive**: User-agent tokens are matched case-insensitively, please use `CiscoWebexAIAgentCrawler` for clarity.

<a id="configuration-steps"></a>

### Create web URL knowledge source

<a id="prereq_kdp_1kw_43c"></a>

Before you begin

Before creating a web URL knowledge source, make sure you have:

- Access to publicly available websites that you own.

- An understanding of the website structure you want to crawl.

You can only use website extraction with publicly accessible information that you're legally permitted to access and process. Don't use this feature with:

- Payment card industry (PCI) data.

- Personally identifiable information (PII).

- Protected health information (PHI).

- Any sensitive, confidential, or regulated information.

By using this feature, you agree to comply with all applicable data protection laws, privacy regulations, and third-party rights. See the [Disclaimer](https://help.webex.com/en-us/article/gi2sms/Disclaimer) before configuring the web url source.

|  |  |
| --- | --- |
| 1 | Choose Add source > Websites. On the Extract Websites page, perform the configurations. |
| 2 | In the Source Details tab, enter the source name and a brief description about the source in the Description field. |
| 3 | In the Source Configuration section, define the following parameters:<br> <br>- Under Source:<br>  <br>   <br>  <br>  - Starting URL: Enter the URL of the web page that you want to crawl and add as source.<br>  <br>  - Filters: Use the following toggle options to define what you need to extract:<br>    <br>    - Extract only URLs that match specific wildcard syntax: Use URL patterns to focus your crawl. You can add up to 10 patterns.<br>      <br>       <br>      <br>      Examples: <br>      <br>      - *product*– matches and extracts URLs containing "product."<br>      <br>      - *help* – matches and extracts only URLs containing "help."<br>      <br>      - */blog/* - matches and extracts URL with /blog/ in the path.<br>    <br>    - Extract only subdomains of the starting URL: If your target content spans multiple subdomains, you can specify up to 10 subdomains to include (for example, support.example.com).<br>- Under Extract Scope: Define the scope based on which the system extracts the content from the web pages.<br>  <br>   <br>  <br>  - Depth limit<br>    <br>    - 0: Crawls only the starting page or the landing page URL.<br>    <br>    - 1: Crawls the starting page and all pages directly linked from it.<br>    <br>    - 2: Crawls the starting page, directly linked pages, and pages linked from those.<br>  <br>  - Page limit: Enter the number of pages you want the system to crawl. You can crawl up to 250 pages. If you define the depth limit as '0', you can't configure page limit.<br>  <br>   <br>  <br>  For example: If page limit =100 and crawl_depth=1, and if only 50 links are available, the crawler returns 50 pages.<br>  <br>   <br>  <br>  - Content Exclusions: <br>    <br>    - **All**: Exclude headers, footer, navigation elements, and form elements.<br>    <br>    - **Nav**: Exclude navigation elements.<br>    <br>    - **Footer**: Exclude footer elements.<br>    <br>    - **Form**: Exclude form elements.<br>- Sync Run Schedule: This section allows you to configure the frequency of the data sync source. You can also choose to configure how the changes should be applied to agents.<br>  <br>   <br>  <br>  - Sync frequency: The default and currently supported option is Run on demand. This allows you to sync web pages manually for recent changes.<br>  <br>  - Sync content change: Choose to automatically apply changes or hold them for approval.<br>    <br>     <br>    <br>    - Automatically apply changes to agents or skills (default option).<br>    <br>    - Hold changes for admin approval before making them available. |
| 4 | Click Add Source. |

<a id="result_kx4_f3v_jjc"></a>

The web url is added to the Sources page. The status shows as syncing. The system:

- Converts the content extracted from the web pages to a structured markdown format.

- Extracts the main article.

- Filters navigation and promotional content as per the settings.

- Tables and lists maintain their structure.

To make any changes to the web URL source, click the **Edit** icon under **Controls**. To delete the source, click the **Delete** icon.

<a id="postreq_dxj_k3w_v3c"></a>

What to do next

Map the web URL source to the AI agent. See the [Configure knowledge base](https://help.webex.com/en-us/article/ncs9r37/Webex-AI-Agent-Studio-Administration-guide#task-template_9b7eb61b-facf-4467-902b-53276bd3723d) section in the Webex AI Agent Studio Administration Guide.

<a id="trigger-a-manual-sync"></a>

#### Trigger a Manual Sync

<a id="context_gbj_bdx_43c"></a>

After creating a web URL knowledge source, do a manual sync operation to keep your knowledge source information current and updated.

|  |  |
| --- | --- |
| 1 | Navigate to your knowledge base page. |
| 2 | Scroll to the required web URL knowledge source list entry. |
| 3 | Click the Sync now icon under Controls.<br> <br>You can also click the **Edit** icon to open the web URL knowledge source page. Click **Save changes and sync** to sync the content with the latest changes on the website. The status shows as Syncing. |
| 4 | If content approval option is enabled, review the extracted content before it becomes available to your AI agents. |

<a id="postreq_uws_2kx_43c"></a>

What to do next

- Sync only when you expect content changes.

- Monitor sync history to identify optimal frequency.

- Consider the impact on system resources.

- Plan syncs during low-usage periods when possible.

- Number of concurrent syncs allowed: 1 website sync/crawl is allowed at a time in one KB. 3 website sync/crawls are allowed per org.

<a id="approve-content-after-review"></a>

#### Approve content after review

<a id="context_uty_5kx_43c"></a>

If content approval is enabled, review the extracted content before it becomes available to your AI agents.

|  |  |
| --- | --- |
| 1 | When sync status shows Pending approval, click Review content. |
| 2 | Preview the extracted information in structured markdown format. |
| 3 | See a summary of changes:<br> <br>- Added: New content found during this sync.<br>- Modified: Existing content that has changed.<br>- Deleted: Content no longer available on the source site. |

What to do next

After reviewing:

- Click Approve to add the content to your knowledge base immediately.

- Click Decline to discard the content. Rejected content is permanently discarded.

<a id="best-practices-and-limitations"></a>

#### Best practices and limitations

Follow these guidelines to get the most value from web URL knowledge sources while ensuring compliance and optimal performance.

**Strategy**:

- Plan your crawl strategy in advance.

- Start focused, then expand. Begin with narrow crawls to understand extraction results.

- Test URL patterns on small sections first.

- Choose the right starting URL:
  
  - **Best**: Landing pages for specific content areas.
  
  - **Good**: Direct links to content sections.
  
  - **Avoid**: Homepage URLs that lead to mixed content types.

- Use URL patterns strategically. After your first crawl:
  
  - Review extracted content quality.
  
  - Identify unwanted sections that got included.
  
  - Adjust URL patterns or exclusion settings.
  
  - Re-crawl with refined settings, if needed.

**Performance and efficiency**

- Set realistic page limits based on your needs.

- Use appropriate crawl depth for your content goals.

- Focus on high-value content areas first.

- Monitor processing times and adjust accordingly.

**Resource considerations**

- Large crawls consume more processing time.

- Multiple simultaneous crawls may affect performance.

- Storage requirements increase with content volume.

- Network resources are shared across all users.

**Content type restrictions**

- Primarily designed for HTML content.

- Some interactive content may not be captured.

- Some websites are blocked based on their classification.

**Compliance and Ethical Crawling** 

- **Respect website policies**: Ensure that you have permission to crawl and respect rate limiting.

- **Data responsibility**: Only crawl publicly accessible content that you own or have permissions to crawl.

- **Content ownership**: Consider intellectual property implications and maintain attribution where required.

**Getting help**

If you encounter issues:

- Review sync history for error details.

- Check that your target URLs are publicly accessible.

- Verify your URL patterns match intended content.

- Consider adjusting crawl depth or page limits.

- Contact support for persistent technical issues.

<a id="task-template_2840ec24-0d0a-4f9d-a205-f896103bd152"></a>

### Access knowledge base

Before you begin

Create the knowledge base required for the AI agent.

|  |  |
| --- | --- |
| 1 | Log in to the Webex AI Agent Studio platform. |
| 2 | Click the Knowledge icon on the left navigation pane. The knowledge bases appear as cards on the Knowledge page.<br> <br>Each card displays the number of source files associated with the specific knowledge base. |
| 3 | Click on a card to navigate to the specific knowledge base. You can see the following:<br> <br>- Sources: Details of the sources associated with the knowledge base such as:<br>  <br>  - Source name<br>  <br>  - Description<br>  <br>  - Type<br>  <br>  - Created by<br>  <br>  - Last updated by<br>  <br>  - Last updated at<br>  <br>  - Status<br>  <br>  - Controls<br>- Used by: Details of the AI agent using the specific knowledge base.<br>- History: History of activities on the knowledge base.<br> <br>You can also access the knowledge base from the Knowledge tab of the AI agent configuration page. For more information, see [Configure knowledge base](https://help.webex.com/article/ncs9r37#task-template_9b7eb61b-facf-4467-902b-53276bd3723d) section.<br> <br>You can search for the required knowledge base using the following criteria: <br>- Name of the knowledge base.<br>- Type of the knowledge base.<br>- Knowledge bases updated between specified dates.<br>- Knowledge bases created between specified dates.<br> <br>Click Reset all to reset the search criteria. |

<a id="content"></a>

<a id="concept-template_7f4b97c9-5d5e-49b5-a651-5293923e98f9"></a>

Autonomous AI agents operate independently without direct human intervention. Autonomous agents can access and use a knowledge repository to provide informative and accurate answers to user queries. These agents use advanced algorithms and machine learning techniques to analyze data, learn from their environment, and adapt their actions to achieve specific goals.

You can use the autonomous AI agents in various scenarios, including: 

- Provide customer support—Answer FAQs, troubleshoot issues, and guide customers through processes.

- Offer technical assistance—Provide expert advice on specific topics or domains.

- Natural Language Processing (NLP)—Understand and respond to human language in a natural and conversational manner.

- Decision making—Make informed choices based on available information and predefined rules.

- Automation—Automate repetitive or time-consuming tasks.

Guardrails configured in the autonomous AI agents ensure that the AI agent doesn't respond with unethical and harmful content.

<a id="task-template_cd5ff649-b94c-4546-82e9-6dac68310ab9"></a>

### Create an autonomous AI agent

<a id="prereq_kvr_kr1_f2c"></a>

Before you begin

Ensure to create the knowledge base for the autonomous AI agent. For more information, see [Create knowledge source for AI agent](https://help.webex.com/article/ncs9r37#create-knowledge-source-for-ai-agent).

|  |  |
| --- | --- |
| 1 | Log in to the Webex AI Agent Studio platform. |
| 2 | On the **Dashboard**, click +Create agent. |
| 3 | On the Create an AI agent screen, choose Start from scratch and click Next.<br> <br>You can also choose a predefined template to create your AI agent quickly. You can filter the AI agent type as `Autonomous`. In this case, the fields on the **Profile** page autopopulate. For more information on the templates, see [Use AI agent templates](https://help.webex.com/en-us/article/n8mo4c/). |
| 4 | Choose Autonomous agent type. |
| 5 | Specify the following required details:<br> <br>- Agent name—Enter the name of the AI agent. The agent name can have a maximum length of 256 characters.<br>- System ID—A system-generated unique identifier. This field is editable.<br>- AI engine—Choose one of the following AI engines from the drop-down list to meet your contact center needs:<br>  <br>   <br>  <br>  - Webex AI Pro 1.0 (to be deprecated soon)/ Webex AI Pro 2.0: This default option supports AI agents in multi-language contact centers, delivering human-like conversations.<br>  <br>  - Webex AI Pro-US. 1.0 (to be deprecated soon)/Webex AI Pro-US. 2.0: Delivers natural, human-like conversations in English, tailored for US regional accents and regulatory requirements.<br>    <br>    Webex AI Pro-US 1.0/Webex AI Pro-US. 2.0 is available for US customers only. Regional media from remote locations is currently not supported with this engine.<br>  <br>  - Webex AI Pro-Europe 1.0 (to be deprecated soon)/Webex AI Pro-Europe 2.0: Delivers a localized experience tailored to regional accents, offering improved user experience and compliance with European regulations.<br>    <br>    Webex AI Pro-Europe 1.0/Webex AI Pro-Europe 2.0 is available for EU customers only. Regional media from remote locations is currently not supported with this engine.<br>  <br>   <br>  <br>  Webex AI Pro 1.0, Webex AI Pro-US. 1.0, and Webex AI Pro-Europe 1.0 will be deprecated in the near future.<br>  <br>   <br>  <br>  Your choice of AI engine determines the conversation settings—such as language, voice, DTMF, delays & interruptions and vocabulary—available for configuring your AI agent. Since each engine offers unique capabilities, the configuration options displayed in the **Conversations** tab will update dynamically based on your selection. For details about AI engine's capabilities, refer to the [Understand AI engines for AI agents](https://help.webex.com/article/ne6s80cb) article. |
| 6 | Click Create. You've now successfully created the autonomous AI agent which is now available on the Dashboard.<br> <br>- You can create up to 100 AI agents, which include both scripted and autonomous types.<br>- Don’t create a single autonomous AI agent with a complex scope. Instead, create multiple AI agents with limited scopes. Use the transfer action option to transfer the call from one AI agent to another. See the  section for more information.<br> <br>On the AI agent header, you can perform the following tasks:<br>- Preview<br>- Copy Access Token<br>- Delete<br>- Export<br>For more information, see [Tasks on AI agent card](https://help.webex.com/article/ncs9r37#section_us5_zdw_ycc).<br> <br>You can also import prebuilt AI agents. For more information, see [Import AI agent](https://help.webex.com/article/ncs9r37#section_grn_byz_zcc). |

What to do next

Configure the autonomous AI agent.

<a id="concept-template_44e053dc-5482-48e5-8b91-7f8aa7774fcd"></a>

### Configure autonomous AI agent

The following sections guide you on how to configure autonomous AI agent for your specific needs:

- [Update autonomous AI agent profile](https://help.webex.com/article/ncs9r37#task-template_5416be2f-b95e-4b80-bebc-3fa8201414bf)

- [Add actions to autonomous AI agent](https://help.webex.com/article/ncs9r37#concept-template_5ea99e1f-a679-4cf9-8e33-7a4f83d9f66a)

  - [Configure slot filling](https://help.webex.com/article/ncs9r37#concept-template_0ec5103d-ff6f-426f-a28c-bb335bc7b1bb)
  
  - [Configure fulfillment](https://help.webex.com/article/ncs9r37#task-template_74dc7494-8351-48cc-9e97-5ad6d0d52df6)

- [Configure knowledge base](https://help.webex.com/article/ncs9r37#task-template_9b7eb61b-facf-4467-902b-53276bd3723d)

- [Configure conversation settings](https://help.webex.com/article/ncs9r37#configure_conversation_settings)

<a id="task-template_5416be2f-b95e-4b80-bebc-3fa8201414bf"></a>

#### Update autonomous AI agent profile

Use the Profile tab to manage customer-facing identity settings.

Before you begin

Create an autonomous AI agent.

|  |  |
| --- | --- |
| 1 | On the Dashboard, click the AI agent that you've created. |
| 2 | Navigate to the Configurations > Profile tab and configure the following details:<br> <br>- Agent name—Edit the name of the AI agent, if needed.<br>- System ID—Edit the system id of the AI agent, if needed.<br>- URL for agent profile image—The default URL from where the system fetches the AI agent's logo or image. Change this if needed.<br>- Time zone—Displays the time zone configured at the organization level, by default. If needed, choose a different time zone for your individual AI agents from the drop-down list.<br>  <br>   <br>  <br>  The system preserves agent-level configurations when organization-level settings change.<br>- AI engine—Choose one of the following options from the drop-down list to update the AI engine:<br>  <br>   <br>  <br>  - Webex AI Pro 1.0 (to be deprecated soon)/ Webex AI Pro 2.0: Supports AI agents in multi-language contact centers, delivering human-like conversations.<br>  <br>  - Webex AI Pro-US. 1.0 (to be deprecated soon)/Webex AI Pro-US. 2.0: Delivers natural, human-like conversations in English, tailored for US regional accents and regulatory requirements. <br>    <br>    Webex AI Pro-US 1.0//Webex AI Pro-US. 2.0 is available for US customers only.<br>  <br>  - Webex AI Pro-Europe 1.0 (to be deprecated soon)/Webex AI Pro-Europe 2.0: Delivers a localized experience tailored to regional accents, offering improved user experience and compliance with European regulations.<br>    <br>    Webex AI Pro-Europe 1.0/Webex AI Pro-Europe 2.0 is available for EU customers only.<br>  <br>   <br>  <br>  Your choice of AI engine determines the conversation settings—such as language, voice, DTMF, delays & interruptions and vocabulary—available for configuring your AI agent. Since each engine offers unique capabilities, the configuration options displayed in the Conversations tab will update dynamically based on your selection. For details about AI engine's capabilities, refer to the [Understand AI engines for AI agents](https://help.webex.com/article/ne6s80cb) article.<br>- AI transparency—Enable or disable the transparency note that tells customers they are interacting with an AI agent. For new AI agents, the AI transparency toggle is enabled by default. If you turn it off, you must acknowledge the warning and provide a reason.<br>  <br>   <br>  <br>  - **In European regions**: This feature is enabled by default. A transparency message plays or appears (depending on the channel) for all agent types. If administrators decide to disable this feature, they must acknowledge the risks and add audit comments before opting out.<br>    <br>    Customers with EU-facing deployments should review the default transparency message and confirm that the final wording meets their own branding, legal, and compliance requirements before August 2nd 2026.<br>  <br>  - **In all other regions**: Administrators can choose whether to enable the feature and configure the message if needed. Cisco recommends enabling AI transparency as a best practice to help ensure end users are informed when interacting with AI.<br>    <br>    You can also configure AI transparency message for existing AI agents in your organization. This is recommended but optional.<br>  <br>   <br>  <br>  For voice conversations, a transparency note plays before the welcome message and callers cannot interrupt it. For digital conversations, the transparency note is added to the first AI-generated response in the session.<br>- Welcome message—The default welcome message that the AI agent uses to start the interaction. Update this, as required.<br>  <br>   <br>  <br>  Specify the welcome message in the desired language for the AI agent. This message won't be automatically translated and will appear or play as configured, regardless of the language configured for the AI agent. |
| 3 | Click Save changes. |
| 4 | Click Publish to make the AI agent live. For more information, see the [Publish your autonomous AI agent](https://help.webex.com/article/ncs9r37#task-template_bed3102a-f6bb-4ded-99d9-8ffb87f3dd9a) section. |

What to do next

Define and optimize instructions for your Webex AI agent.

<a id="concept-template_b690286b-fda6-4794-8975-de53d27c6111"></a>

#### AI-optimized instructions for autonomous agents

Webex AI Agent Studio provides AI-powered assistance to generate, optimize, and refine instructions for autonomous AI agents. Start from a simple description or example, improve existing instructions using prompt-engineering best practices, review the changes, and edit the result before saving. With this feature, you can create clear, well-structured instructions that maximize your AI agent's performance.

<a id="section_what_is_optimization"></a>

##### What is instruction optimization

Instruction optimization is an AI-powered feature that analyzes your draft instructions and generates an improved version following best practices for LLM prompt engineering. The feature uses a specialized AI service to restructure your content into a format that Large Language Models understand most effectively.

The optimization process:

- Analyzes your original instructions to understand intent and context.

- Applies proven LLM prompting patterns and structures.

- Generates instructions with clear sections for Role/Identity, Reasoning Order, Output Format, and Edge Cases, tailored to the selected AI engine.

- Provides a View changes option so you can compare the original and AI-generated instructions side by side and review the highlighted changes.

<a id="section_when_to_use"></a>

##### When to use optimization

Use the instruction optimization feature when:

- **Creating a new agent**: Start with a draft of your requirements and let the optimization feature structure them properly.

- **Improving existing agents**: If your agent's responses are inconsistent or unclear, optimize the instructions to improve clarity.

- **Adapting to a new AI engine**: When switching between AI engines (e.g., from Webex AI Pro 1.0 to Webex AI Pro-US 1.0), re-optimize instructions to align with the new model's capabilities.

Review the optimized version alongside your original to ensure that the instructions are accurate.

<a id="section_limitations"></a>

##### Limitations and considerations

Be aware of the following limitations when using instruction optimization:

- **Stateless operation**:Each optimization request is independent. To refine the result, edit the instructions or add follow-up guidance, then run the optimization again.

- **Design-time only**: Optimization is available only when configuring an agent, not for runtime adjustments.

- **Manual review required**: Always review optimized instructions to ensure they include your specific business context, terminology, and requirements.

- **Network dependency**: Requires an active connection to the optimization service; offline editing is not optimized.

<a id="task-template_2285157c-d0fa-41d9-98b4-9082d7a33c9e"></a>

##### Define and optimize instructions

Use instruction optimization to improve draft instructions before you save or publish the AI agent.

Before you begin

Create an autonomous AI agent.

<a id="steps_s5h_b5z_1kc"></a>

|  |  |
| --- | --- |
| 1 | On the Dashboard click the autonomous AI agent that you have created. |
| 2 | Navigate to Configuration > Instructions tab. |
| 3 | Enter draft instructions for your AI agent with a short description of the Agent's goal and expected behavior. |
| 4 | Alternatively, navigate to the **Examples** tab, choose an example, and click **Insert example**.<br> <br>Click Best practices & Tips to see the Do's and Don'ts while drafting instructions. |
| 5 | Click Optimize instruction after drafting the instructions. Wait while the system generates the updated instructions. |
| 6 | Review the optimized instructions and the list of changes. Do one of the following:<br> <br>- Click Accept to use the optimized instructions that are streamed back.<br>- Click Discard to keep your existing instructions.<br> <br>Optimization feature handles non-sensical instructions and also refines abusive, offensive or overly strong language. |
| 7 | After reviewing optimized instructions, you can provide feedback. Under **Is this helpful?**, select thumbs up or thumbs down to rate the AI-generated instructions. |
| 8 | Click Save changes. |

What to do next

Configure actions for your autonomous AI Agent.

<a id="concept-template_5ea99e1f-a679-4cf9-8e33-7a4f83d9f66a"></a>

#### Add actions to autonomous AI agent

Autonomous AI agents are designed to comprehend user intents and act accordingly. For example, consider a restaurant with the need to automate online food order intake. To accomplish the task, create an autonomous AI agent that performs the following actions: 

- Get the required information from the customer.

- Transfer the information to the required flow.

- Deliver the customer requirement.

The autonomous AI agent works on the following three building blocks:

- Action—A task that an AI agent performs by understanding user intents and completes by connecting to external systems.

- Entity or slot—Represents a step in fulfilling the user's intent. Slot filling involves asking specific questions to the customer to fulfill the customer's intent based on utterances. It's the trigger for an AI agent to start performing an action.

- Fulfillment—Determines how the AI agent completes the action by connecting with external systems.

<a id="task-template_031f8a5e-98ec-4521-ad2f-6c271e5a969b"></a>

<a id="context_apg_n2f_53c"></a>

|  |  |
| --- | --- |
| 1 | On the Dashboard, click the AI agent that you've created. |
| 2 | Navigate to Configurations > Actions tab.<br> <br>The Actions page displays the **Agent handover** action. The Agent handover action is enabled by default allowing the AI agent to escalate the conversation to a human agent. Use the toggle option to disable it. |
| 3 | Click +Add Actions to add a new action for an AI agent.<br> <br>- Choose Browse actions > Select available for MCP client configuration.<br>- Choose Add new > Fulfillment to create fulfillment action.<br>- Choose Add new > Transfer to create a custom transfer action.<br> <br>You can configure a maximum of 10 actions for an AI agent.<br> <br>See the following sections for detailed configuration steps. |

<a id="task-template_74dc7494-8351-48cc-9e97-5ad6d0d52df6"></a>

#### Configure fulfillment

<a id="context_ez5_tbn_g2c"></a>

You can configure fulfillment flows for AI agent actions on the Webex Connect Flow builder. For more information, see [Configure Fulfillment Flows for AI Agent Actions](https://help.webexconnect.io/docs/configure-fulfilment-flows-for-ai-agent-actions).

- As part of PCI compliance, autonomous AI agent currently doesn't support fulfillment that involves debit card or credit cards. All user verification or payment that involve a debit card or credit card must be done through third-party integration.

|  |  |
| --- | --- |
| 1 | On the Add a new action page, specify the following details:<br> <br>- Action name—Enter the name of the action. For example, `Book tickets`. The maximum length of the Action name field is 64 characters.<br>- Action description—Provide a brief description about the expected action. Ensure that the action description is clear and accurate. The maximum length of Action description is 1024 characters. |
| 2 | Configure slots. See the [Configure slot filling](https://help.webex.com/article/ncs9r37#concept-template_0ec5103d-ff6f-426f-a28c-bb335bc7b1bb) for more information. |
| 3 | Configure fulfillment. You can choose one of the following options.<br> <br>- If you choose Use Webex Connect Flow Builder Fulfillment, perform the following configuration:<br>  <br>   <br>  <br>  - Select service—Choose the required service that is configured in the Webex Connect client workspace.<br>    <br>    The Webex AI Agent Studio can only access service and flows configured within the client-level workspace.<br>  <br>  - Select a flow—Choose the required flow that is configured in the Webex Connect client workspace.<br>- If you choose, Manage in the source flow (voice only), you must configure custom events. See the [Configure custom data and custom events for AI agents](https://help.webex.com/en-us/article/n5uo60x/Configure-custom-data-and-custom-events-for-AI-agents) for detailed information. |
| 4 | Click Add to complete the configuration. |

<a id="postreq_i3y_q2r_bdc"></a>

What to do next

Configure the knowledge base.

<a id="concept-template_0ec5103d-ff6f-426f-a28c-bb335bc7b1bb"></a>

##### Configure slot filling

Slot filling involves adding the required input entities for the AI engine. In the Slot filling section of the Actions page, add the input entities:

- You can add the entities one by one in table format. For more information, see [Add input entities in table format](https://help.webex.com/article/ncs9r37#task-template_9848e5ed-72de-4e31-a88d-e7a0b141399a).

- You can also use the JSON file and define the entities. See [A Tour of JSON Schema](https://tour.json-schema.org/) for details.

<a id="task-template_9848e5ed-72de-4e31-a88d-e7a0b141399a"></a>

###### Add input entities in table format

|  |  |
| --- | --- |
| 1 | To add an input entity, click **+New input entity**. |
| 2 | On the Add a new input entity page, specify the following details:<br> <br>- Entity name—Enter the name of the input entity. The maximum length of the Entity name can be 256 characters.<br>- Entity type—Choose the data type of the entity.<br>- Entity description—Provide a brief description about the entity. Ensure that the entity description is clear and accurate. The maximum length of the Entity description can be 512 characters.<br>- Entity examples—Enter an example for the entity. Click +Add to add more examples.<br>- Check the Required check box to make this entity mandatory. |
| 3 | Click Add to add the input entity. You can add as many input entities as you need. |
| 4 | Click Add to add the action to the AI agent. |
| 5 | Click Publish to make the AI Agent live. For more information, see the [Publish your autonomous AI agent](https://help.webex.com/article/ncs9r37#task-template_bed3102a-f6bb-4ded-99d9-8ffb87f3dd9a).<br> <br>After adding the action, use the **Controls** option to edit or delete the entities. |

<a id="concept-template_7d93102d-6315-44a3-a257-9c211827de36"></a>

###### Add entities using a JSON editor

- To add an input entity in JSON, click Use JSON instead.

- Enter the input parameter schema in JSON format.

- Click Add.

For more information, see [A Tour of JSON Schema.](https://tour.json-schema.org/)

<a id="section_c22_vkp_bdc"></a>

**Input parameter structure**

The input parameters must adhere to the following structure:

- **type**—Data type of the parameters object. This is always 'object' to denote that the parameters are structured as an object.

  **properties**—An object where each key represents a parameter and its associated metadata.

  **required**—An array of strings listing the names of parameters that are mandatory.

<a id="section_xfv_qht_bdc"></a>

**properties Object**

Each key in the **properties object** represents an input entity/parameter and contains another object with metadata about that parameter. The metadata should always include the following keywords:

- **type**—Data type of the parameter. The allowed types are:

  - **string**—Textual data.
  
  - **integer**—Numeric data without decimals.
  
  - **number**—Numeric data that can include decimals.
  
  - **boolean**—True/false values.
  
  - **array**—A list of items, all of which are typically of the same type.
  
  - **object**—A complex data structure with nested properties.

- **description**—A brief explanation of what the entity represents. This helps the AI engine understand the purpose and usage of the parameter. A description that's concise and consistent with the agent's instructions and action description is good for better accuracy.

- Validation is enforced by the platform for ‘type’ only. ‘Description’ isn't enforced for all entities but it's highly recommended that it’s added. Other useful keywords for entity metadata are:
  
  - **enum**—The enum field lists the possible values for a parameter. This is useful for parameters that should only accept a limited set of values. Developers can define custom lists of values that a parameter should accept to use this.
  
  - **pattern**—Use the pattern field with string types to specify a regular expression that the string must match. This is useful for validating specific formats, such as phone numbers, postal codes, or custom identifiers.
  
  - **examples**—The examples field provides one or more examples of valid values for the parameter. This helps the AI engine understand the kind of data it needs and can be especially useful for interpretation and validation purposes.

There are other keywords that can make the entity definition more accurate and robust. For more information, see [A Tour of JSON Schema](https://tour.json-schema.org/).

<a id="section_rjw_fnp_bdc"></a>

**Example**

The following example includes various types of entities and keywords:

```text
The following example includes various types of entities and keywords:

{
    "type": "object",
    "properties": {
        "username": {
            "type": "string",
            "description": "The unique username for the account.",
            "minLength": 3,
            "maxLength": 20
        },
        "password": {
            "type": "string",
            "description": "The password for the account.",
            "minLength": 8,
            "format": "password"
        },
        "email": {
            "type": "string",
            "description": "The email address for the account.",
            "pattern": "\\w+([-+.']\\w+)*@\\w+([-.]\\w+)*\\.\\w+([-.]\\w+)*"
        },
        "birthdate": {
            "type": "string",
            "description": "The birthdate of the user.",
            "examples": ["mm/dd/YYYY"]
        },
        "preferences": {
            "type": "object",
            "description": "User preferences settings.",
            "properties": {
                "newsletter": {
                    "type": "boolean",
                    "description": "Whether the user wants to receive newsletters.",
                    "default": true
                },
                "notifications": {
                    "type": "string",
                    "description": "Preferred notification method.",
                    "enum": ["email", "sms", "push"]
                }
            }
        },
        "roles": {
            "type": "array",
            "description": "List of roles assigned to the user.",
            "items": {
                "type": "string",
                "enum": ["user", "admin", "moderator"]
            }
        }
    },
    "required": ["username", "password", "email"]
}
```

This example includes the following entities:

- **username**—A string type with minimum and maximum length constraint.

- **password**—A string type with a minimum length and a specific format (password indicates that secure handling is required).

- **email**—A string type with a regex pattern to ensure it’s a valid email address.

- **birthdate**—A string type with examples to prescribe the format of the date.

- **preferences**—An object type with nested properties (newsletter and notifications), including a boolean with a default value and a string with specific allowed values (enum).

- **roles**—An array type where each item is a string limited to specific values (enum).
  
  The username, password, and email are mandatory as defined by the ‘required’ array.

In this example, the entities have descriptive names, clear descriptions, and follow a consistent structure and naming convention. Follow these best practices to create well-defined entities that are easy for the AI engine to interpret and enforce.

This schema will result in JSON format being sent to connect AI Agent start node that looks like the following:

```text
{
    "username":"username-example",
    "password":"password-example",
    "email":"fake@example.com",
    "preferences": {
        "newsletter":true,
        "notifications":"email, sms"
    },
    "roles":"user"
    
}
```

Webex Connect might not receive the preferences and roles input in certain situations because they were not designated as required in the schema.

<a id="concept-template_9483e1f4-c3e2-4080-b9d3-5359b553a785"></a>

#### Configure MCP client action

The Model Context Protocol (MCP) client capability enables the autonomous AI agents to connect directly to third-party tools and services without requiring custom-built API integrations. This streamlines how agents retrieve data and perform actions during live customer conversations.

By setting up an MCP client, your AI agents can:

- Automatically invoke third-party tools during live conversations.

- Retrieve real-time data from external systems.

- Perform actions without human intervention.

<a id="task-template_c15af56d-160d-4a6b-bd14-1560595b73e3"></a>

Before you begin

Before you configure MCP action in the Webex AI Agent Studio, you must:

- Have the MCP server URL, authentication type, and credentials for the third-party tools you want to connect.

- Register MCP apps on the Webex Developer Portal. See the [Onboard your Agent App](https://developer.webex.com/mcp/docs/onboard-your-agent) section in the developer portal for more information. The Webex AI Agent studio supports only the following authentication types: :
  
  - OAuth2 client credentials
  
  - API key
  
  - Custom Header based Auth

- Authorize the tool in the Control Hub for your organization. See the [Provision on Control Hub](https://developer.webex.com/mcp/docs/provisioning-on-control-hub) section in the developer portal for more information.

**Note:** MCP actions are read-only once created. If you need to change action settings, you must create a new action.

|  |  |
| --- | --- |
| 1 | Log in to the Webex AI Agent Studio platform. |
| 2 | Choose the AI agent for which you want to configure the MCP action. You can also create a new autonomous AI agent. See [Create an autonomous AI agent](https://help.webex.com/en-us/article/preview/ncs9r37/Webex-AI-Agent-Studio-Administration-guide#task-template_cd5ff649-b94c-4546-82e9-6dac68310ab9) section for more information. |
| 3 | Navigate to the Actions tab. Click +Add actions. |
| 4 | In the Add actions pop-up, under Browse actions choose Select available<br> <br>This displays all the available MCP tools with the provider name and MCP label. |
| 5 | Choose the MCP tool you want to add. You can add multiple MCP tools at any time. Click Add.<br> <br>Your agent can support a maximum number of actions as defined by your organization's configuration. |

What to do next

Once an MCP tool is added, the system automatically populates the following details from the MCP server definition:

- **Action name (MCP tool name)**

- **Description**

- **Input entities** (required fields and data types)

If you need to modify any of these details, you must update the MCP server definition at the registration or provisioning stage. Changes get synchronized automatically to the AI Agent Studio via notifications.

**Verify MCP tool status**

After adding an MCP action, verify its status in the action list:

- **Tool name, description, and server details**

- **Input parameters** sent to the tool

- **Output** returned by the tool

- **Execution state** (Success or Failure)

- **Latency** (in milliseconds)

- **Server name and ID**

- **Transaction ID**

**Limitations**

Be aware of the following limitations:

- Group-level access control is not supported. MCP tool access is managed at the organization level only.

- MCP actions are read-only once created in AI Agent Studio. To update an action, create a new one.

- Maximum number of actions per agent is defined by your organization's configuration. Contact your administrator for details.

<a id="task-template_91018ba5-7914-4ad9-938f-f8837f776f8c"></a>

#### Configure custom transfer action

The custom transfer action feature enables you to transfer calls from one AI agent to another AI agent, to a human agent, or to any another desired destination (voicemail box, hunt group, or any other number) to ensure seamless customer experience. Depending on the need, you can configure the transfer as an announced transfer or a silent transfer. By using a transfer action, you exit out of the escalated path of the Virtual Agent V2 Activity in Flow Builder with metadata that allows you to orchestrate the next path in the conversation. See the [Multi-agent orchestration](https://help.webex.com/en-us/article/5a07xcb/Multi-agent-orchestration) article for more details on flow configuration.

Before you begin

Create the required autonomous AI agents to use when transferring calls. You can now configure each transfer action independently.

|  |  |
| --- | --- |
| 1 | On the Dashboard, click the AI agent that you've created. |
| 2 | Navigate to Configurations > Actions tab. |
| 3 | Click the Create new drop-down list. |
| 4 | On the Create a transfer action page, specify the following details:<br> <br>- In the General information section, specify the following details:<br>  <br>   <br>  <br>  - Action name—Enter the name of the action. For example, Leave_Voicemail.<br>  <br>  - Transfer condition—Describe the condition for transfer. For example, the user wants to leave a voicemail.<br>  <br>  - Transfer visibility—Toggle option to announce transfers.<br>    <br>    - Turn-on the toggle: the AI Agent informs the customer about the transfer before executing it.<br>    <br>    - Turn off the toggle: the AI Agent performs a silent transfer and handles the action using neutral languages.<br>- (optional) Click +New input entity. In the Add a new input entity page, enter the following details:<br>  <br>   <br>  <br>  - Entity name—Enter the name of the input entity. The maximum length of the Entity name can be 256 characters.<br>  <br>  - Entity type—Choose the data type of the entity.<br>  <br>  - Entity description—Provide a brief description about the entity. Ensure that the entity description is clear and accurate. The maximum length of the Entity description can be 512 characters.<br>  <br>  - Entity examples—Enter an example for the entity. Click +Add to add more examples.<br>- Click Add. |

What to do next

Configure the Virtual Agent V2 activity. See the [Use AI agents for customer interactions](https://help.webex.com/en-us/article/s0qro1/Use-AI-agents-for-customer-interactions) for more details.

<a id="task-template_9b7eb61b-facf-4467-902b-53276bd3723d"></a>

#### Configure knowledge base

Before you begin

Create an autonomous AI agent.

|  |  |
| --- | --- |
| 1 | On the Dashboard page, click the AI agent that you've created. |
| 2 | Navigate to the Configurations > Knowledge  tab. |
| 3 | Choose the required knowledge base from the drop-down list.<br> <br>We strongly recommend you to choose a knowledge base that uses the same language as your AI agent for optimal performance.<br> <br>- To navigate to the chosen Knowledge base, choose Manage Knowledge base from the drop-down list.<br>- To disconnect the knowledge base from the AI agent, choose None from the drop-down list.<br>- To create a new knowledge base, choose +Add New from the drop-down list. For more information, see [Create knowledge base for AI agent](https://help.webex.com/article/ncs9r37#task-template_81b96f90-1e6b-4e42-9cc1-c0d2c70f2f7c).<br> <br>You can map a knowledge base to multiple AI agents. |
| 4 | Click Save changes. |
| 5 | Click Publish to make the AI agent live. For more information, see [Publish your autonomous AI agent](https://help.webex.com/article/ncs9r37#task-template_bed3102a-f6bb-4ded-99d9-8ffb87f3dd9a). |

<a id="configure_conversation_settings"></a>

#### **Configure conversation settings**

This section outlines how to configure the AI agent’s language and voice, choose a response style, add custom words for recognition, and manage how the AI agent handles pauses or interruptions during conversations.

Before you begin

- Ensure you are logged into the Webex AI Agent Studio.

- Ensure you’ve created the autonomous AI agent.

|  |  |
| --- | --- |
| 1 | On the **Dashboard** page, click the AI agent that you've created. |
| 2 | On the AI agent configuration page, navigate to the **Configuration**> **Conversation** tab. |
| 3 | Configure the **Language and response style**settings:<br> <br>- **Language:**Based on the chosen AI engine for your AI agent (while creating the agent or updating the AI agent profile), configure the required language option:<br>  <br>   <br>  <br>  - For the Webex AI Pro 1.0 engine, the default language is set to `English`. Choose the desired language from the drop-down list. To view the list of supported languages, see the [Supported languages and voices](https://help.webex.com/en-us/article/pdef2d/Supported-languages-for-Scripted-AI-Agents) article.<br>  <br>  - For the Webex AI Pro-US 1.0 engine, English is the only supported language by default, with `en-US` set as the default locale. Webex AI Pro-US 1.0 is available for US customers only.<br>  <br>  - For the Webex AI Pro-Europe 1.0 engine, English is the only supported language by default, with `en-GB` set as the default locale. Webex AI Pro-Europe 1.0 is available for Europe customers only.<br>- **Response style:**—Choose how you want your AI agent to respond to customers:<br>  <br>   <br>  <br>  - **Active** **- quick acknowledgments before a substantive response**—Provides quick acknowledgments before giving a full response. This means the agent will first say something like "I understand your response" or "Got it," which helps reassure the customer that their input was received before moving on to a detailed answer. You can further configure style, frequency, and length of the responses:<br>    <br>    - Style—Choose the response style for the conversation: Brief, Empathetic, Conversational, or Formal. For example, conversations in a healthcare setting should use an empathetic tone.<br>    <br>    - Frequency—Choose an appropriate response frequency: Always or When appropriate. Too many responses can sometimes be distracting or annoying.<br>    <br>    - Length—Choose the preferred response length:<br>      <br>      - Very short: Up to two words.<br>      <br>      - Short: Up to four words.<br>      <br>      - Medium: Up to six words.<br>      <br>      - Long: Up to eight words.<br>  <br>  - **Direct - slight delay, only returns the substantive response**—The agent waits for a moment and then replies with only the substantive response, without any initial acknowledgment.<br>  <br>  - Check the **Include disfluencies** check box if you want to add fillers like "um" or "like" to make the agent sound more human and relatable. |
| 4 | Configure the **Voice channel**settings:<br> <br>- **Voice**—Choose the desired voice for your AI agent from the **Select voice** drop-down, based on the chosen AI engine and configured language. To view the list of supported voices, see the [Supported languages and voices](https://help.webex.com/en-us/article/pdef2d/Supported-languages-for-Scripted-AI-Agents) article.<br>  <br>   <br>  <br>  - For the Webex AI Pro 1.0 engine, the default voice for English is `en-US-Jennifer`. To use a different language or voice, select the preferred language in the previous step; the available voices for that language will then appear in the drop-down.<br>  <br>  - For the Webex AI Pro-US 1.0 engine, the default voice for English is set to `en-US-Jess`. Currently, you can only switch to other English voices.<br>  <br>  - For the Webex AI Pro-Europe 1.0 engine, the default voice for English is set to `en-GB-Grace`. Currently, you can switch to `en-IE` voices only.<br>- **Speaking rate**—Enter the numeric value to increase or decrease the rate/speed of speech output. Valid values range from 0.7 to 1.2, with the default set to 1.0 for normal speed.<br>  <br>   <br>  <br>  - This setting overrides the speaking rate configured in the Flow Designer.<br>  <br>  - Extreme values close to the minimum or maximum speaking rate may impact the quality of the generated speech. |
| 5 | Configure **Custom Vocabulary**. Enter words or phrases separated by commas (up to 100 words or phrases). Adding custom vocabulary helps the AI agent better recognize and respond to specific terms, names, or industry-specific language relevant to your use case. |
| 6 | Configure the **Delays and interruptions**settings:<br> <br>- Toggle the **Allow customer to interrupt**option to enable or disable customers speaking over the agent. Enabling this option lets callers interrupt the agent without waiting for a pause.<br>- Toggle the **Use Webex AI Voice Detection** option to enable or disable a smoother barge-in experience for the customer. Enabling this option allows your AI agents to detect when a customer starts speaking much sooner. The AI agent stops speaking and starts listening with significantly reduced delay. This option is applicable for English and other supported languages.<br>- Adjust the **End of speech sensitivity**slider to set how quickly the agent responds after the caller stops talking. Valid values range from 500 ms (Aggressive) to 2000 ms (Relaxed) with a default value of 500 ms (Aggressive).<br>- Enter the **Fulfilment timeout**(in seconds) to set a time limit for task execution and to forcibly stop the task. Valid values range from 10 to 30 seconds with a default value of 30.<br>- Enter the **Caller turn timeout**(in milliseconds) to specify how long the system waits before checking if the customer has finished speaking. Valid values range from 750 and 3000 milliseconds with a default value of 1500.<br>- Enter the **No-input timeout**(in seconds) to set the maximum time to wait for customer input before the system assumes no response. Valid values range from 10 to 30 with a default value of 10. |
| 7 | Configure the**DTMF** settings:<br> <br>- Enter the timeout between two digits (in seconds). This sets how long the AI agent waits for the next DTMF input from the customer before proceeding with the conversation flow. The default value is 5 seconds. The value can range from 2 to 10 seconds.<br>- Enter the termination character that the customer can use to indicate the end of DTMF input. The termination character can be either **#**or *****.<br>- Enter the **Max length**(in characters) to set the maximum allowed length for DTMF input from customers. The default is 16 characters. The value can range from 8 to 32 characters. |
| 8 | Click **Save changes**.<br> <br>You can preview the conversation experience before you publish the changes, and the same conversation settings will apply to the voice preview experience. For more information, see [Preview voice conversation](https://help.webex.com/article/ncs9r37#task-template_9b45b012-ad0c-4ec7-88e5-75bb5f695d9a). |
| 9 | Click **Publish** to make the AI agent live. For more information, see [Publish your autonomous AI agent](https://help.webex.com/article/ncs9r37#task-template_bed3102a-f6bb-4ded-99d9-8ffb87f3dd9a). |

<a id="concept-template_b729b9a3-2be8-4818-ac2d-9b3f326d7676"></a>

### Preview your autonomous AI agent

You can preview the autonomous AI agents at the time of creating the AI agent, while editing, and after deploying the agent.

You can open the preview from:

- **AI agent dashboard**—On hovering over an AI agent card, the Preview option for that AI agent become visible. Click to open the preview of the AI agent.

- **AI agent header**— Click on the AI agent card to open the AI agent. The Preview option is always visible in the header section.

- **Minimized widget**—After you launch the preview and minimize it, a chat head widget appears at the bottom right of the page. You can use this option to easily reopen the preview mode.

<a id="section_u5c_25w_1dc"></a>

#### Platform preview widget

The preview widget appears on the bottom-right section of the screen. You can provide utterances (or a sequence of utterances) to check the AI agent's responses and ensure it’s functioning correctly.

Also, you can minimize the preview widget, provide consumer information, and initiate multiple rooms to test the AI agent.

<a id="concept-template_ebc2af13-75b1-4ef6-8f9d-d8710285f634"></a>

#### Preview chat conversation

<a id="section_rlz_ldy_dfc"></a>

The chat preview feature lets you interact with the AI agent as an end user and observe how it responds to different queries through text.

If AI transparency is enabled, preview includes the disclosure experience so you can verify the first customer-facing message before you publish the agent.

|  |  |
| --- | --- |
| 1 | On the AI agent configuration page, click Preview in the header. The AI agent preview widget appears.<br> <br>- If you’ve chosen Webex AI Pro 1.0, you can preview voice conversations in the configured languages.<br>- If you’ve chosen Webex AI Pro-US 1.0 or Webex AI Pro-Europe 1.0, you can preview voice conversations only in English. |
| 2 | Click Start a Chat. The AI agent starts the interaction with its welcome message. If AI transparency is enabled, the preview shows the transparency note with that first AI-generated message. |
| 3 | Type your query in the text box and press Enter. |
| 4 | You can then see and assess the response from the AI agent.<br> <br>To start a new chat conversation or session, click Preview in the header. |

<a id="task-template_9b45b012-ad0c-4ec7-88e5-75bb5f695d9a"></a>

#### Preview voice conversation

The voice preview feature lets you interact with the AI agent as an end user and observe how it responds to different queries through voice.

- You need browser permissions to preview voice conversations. When prompted by your browser, make sure to click 'Allow' to enable the required access. We recommend using the following browsers:
  
  - Safari on macOS
  
  - Chrome on Windows

- Use a headset for the best experience. When a caller interrupts the AI agent (via barge-in), the AI agent detects the speech, stops the prompt that it is playing, and processes the caller's input accordingly—this works optimally only when you are using a headset.

- When not using a headset, avoid setting the volume to 100%.

If AI transparency is enabled, preview includes the disclosure before the welcome message so you can verify the voice experience before you publish the agent.

|  |  |
| --- | --- |
| 1 | On the AI agent configuration page, click Preview in the header. The AI agent preview widget appears.<br> <br>- If you’ve chosen Webex AI Pro 1.0 engine, you can preview voice conversations in the configured languages.<br>- If you’ve chosen Webex AI Pro-US 1.0 engine or Webex AI Pro-Europe 1.0, you can preview voice conversations in English language only. |
| 2 | Click Start a call. If AI transparency is enabled, the call begins with the transparency note before the welcome message. Callers cannot interrupt the transparency note. You can also see the live transcript of the conversation in the widget. |
| 3 | Voice your query. As you speak, you can see the live transcript of the conversation.<br> <br>To mute your voice while interacting, click Mute. |
| 4 | For your query, you can then hear and assess the response from the AI agent. |
| 5 | To end the call, click End call. |

<a id="task-template_bed3102a-f6bb-4ded-99d9-8ffb87f3dd9a"></a>

### Publish your autonomous AI agent

Before you begin

Create the autonomous AI agent.

|  |  |
| --- | --- |
| 1 | On the AI agent configuration page, click Publish. |
| 2 | On the Publish changes screen, enter the Version name and click Publish.<br> <br>You can view the version details on the History page. For more information, see the [History](https://help.webex.com/article/ncs9r37#section_vby_ttw_1dc) section. |

<a id="concept-template_e0106832-a025-4a69-ac77-e520c4fb9b9e"></a>

### View autonomous AI agent sessions and history

You can view the details of sessions established with the customers and the history of the configuration changes performed on the AI agent.

<a id="section_qbv_qtw_1dc"></a>

#### Sessions

The Sessions page provides a comprehensive record of all interactions between AI agents and users. To access Sessions:

- On the Dashboard, click the autonomous AI agent for which you want to view the session details.

- From the left navigation pane, click **Sessions**.

The Sessions page appears. Each session is displayed as a record that contains all the messages of the session. This information is useful to audit, analyze, and improve the AI agent.

The sessions table shows a list of all the sessions/rooms created for that AI agent. The table gets paginated if there are more rows than can be accommodated in one screen. Any of the fields in the table can be sorted or filtered using the Refine Results section on the left-hand side. The fields represent the following information about any particular session:

- **Session ID**—The unique room id or session id for a conversation.

- **Consumer Id**—The id of the consumer who interacted with the AI agent.

- **Channels**—Channel where the interaction took place.

- **Updated At**—Time of the room closure.

- **Room Metadata**—Contains additional information about the room.

- Check the required check boxes:

  - Hide test sessions—To hide the test sessions and display only the list of live sessions.
  
  - Agent handover happened—To filter the sessions that are handed over to an agent. If agent handover happens, it displays the Headphone icon indicating the handover of the chat to a human agent.
  
  - Error occurred—To filter the sessions in which the error occurred.
  
  - Downvoted—To filter the downvoted sessions.

<a id="section_cwz_lk3_f2c"></a>

#### View session details

To view the session details:

- Click on an individual row in the sessions table for a detailed view of that session. If the session is locked, you need to have permission to decrypt the session.

- Click the Decrypt content to view the session data.
  
  The Decrypt content button appears only if you've decrypt access within the AI agent studio application.

- The system displays the following session details: 
  
  - Shows a transcript of all session interactions in chronological order, providing context for the conversation. Use the search bar to quickly find a specific conversation transcript. This allows you to navigate lengthy interactions easily without having to manually scroll through the entire text.
    
    AI Agent transcripts are stored for 90 days before being automatically purged.
  
  - Shows the corresponding responses generated by the AI agent.
    
    - The AI agent's **barge-in detection** feature identifies instances where a user interrupts or speaks during an ongoing agent utterance. For example, while the AI agent is responding with, "I have checked your account and your balance is...", and the user interrupts with "Okay.", the AI agent detects this user input. Consequently, it immediately stops its current utterance, preventing the full completion of its intended message.
    
    - The AI agent response appears with the message bubble, "User interruption detected" in the session transcript, notifying AI agent developers about the specific agent prompt that was interrupted and exact point of interruption.
    
    - The **Response interrupted** section in the right panel provides a detailed breakdown of the barge-in event. For example, it displays the complete, intended AI agent response (for example, "I have checked your account and your balance is five thousand dollars."). It also identifies the "Unplayed content" (for example, "five thousand dollars"), explicitly indicating the portion of the AI agent's response that was suppressed or truncated due to the user's real-time interruption.

      Currently, "Unplayed content" is available only for fulfillment responses. It will be extended to general prompts soon.
    
    - **Agent closed the session**: The **Agent closed the session** event indicates that the AI agent ended the current interaction. It is an informational status and does not, by itself, indicate an error.

      This event can occur in the following scenarios:
      
      - If a customer indicated that no further assistance is required by saying “goodbye” or “no, thanks.”
      
      - The AI agent completed the customer’s request and determined that the conversation is finished.
      
      - During a voice interaction, no customer input is detected after three consecutive prompts.

      The customer must start a new interaction if further assistance is needed.

      If a session closes unexpectedly:
      
      - Review the preceding conversation to determine if the customer indicated that the interaction was complete.
      
      - For voice interactions, check if the customer was silent or if their speech was not detected.
      
      - If the conversation ended before the request was completed, record the session ID, approximate time, and the last messages exchanged. Contact your administrator or Cisco Support.

      The **Agent closed the session** event should be interpreted separately from agent handover, which indicates that the interaction was transferred to another agent.
  
  - Shows the recording playback modal (along with the session transcript) for conversations between the AI agent and the customer. Recordings are available only for voice sessions, not chat sessions. You can play the recording from the beginning or jump to a specific point. 
    
    The recording playback modal provides a suite of audio controls:
    
    - **Play/Pause**: Click  to start listening to the interaction session and click  to pause the recording playback.
    
    - **Playback speed**: Click 1X to adjust the audio playback speed, ranging from 0.5X to 2X.
    
    - **Sound control**: Click  to mute or unmute the sound of the audio during playback. You can also use the volume slider to adjust the playback volume.

    - When conversations contain PCI data, the system enforces enhanced security measures. Depending on the scenario:

      - If PCI data is detected, the playback modal for the recording is disabled in the session view, preventing access to the audio.
    
    - When a call is escalated from an AI agent to a human agent, and the human agent then consults back to the same or another AI agent, the recording of the consulted leg is currently not supported.
  
  - For the corresponding response, the right panel displays the **Actions performed** section with the following details:
    
    - Agent transfer action
    
    - Slot filling and fulfillment related to all actions

    The General information section provides detailed information about each of the actions.

    Use the **Expand all** button to expand the transaction. The right panel also displays details about the knowledge utilization with details about document names and files uploaded.

    For voice call sessions, the fulfillment output in session details displays only transaction metadata, such as Transaction ID and Size. However, chat preview sessions display the complete fulfillment payload.

<a id="section_vby_ttw_1dc"></a>

#### History

The History page allows you to view the details of the configuration changes performed on the AI agent. To view the history of a specific agent:

- On the Dashboard, click the autonomous AI agent for which you want to view the history.

- From the left navigation pane, click History.

The History page appears with the following tabs:

- Version history—Click the Version History tab to view the various versions of the autonomous AI agent.

- Change logs—Click the Change Logs tab to view the changes made to the AI agents.

<a id="section_nmr_ktw_1dc"></a>

#### Version history

Whenever you publish the autonomous AI agent, a version of the autonomous AI agent is saved and is available in the Version history tab. You can view the various versions of the AI agent from the Version history tab.

- Version description—A brief description about the version of the AI agent.

- AI engine—The AI engine used for that version of the AI agent.

- Updated at—Date and time when the version was created.

- Actions—Allows you to perform the following actions on the AI agent:

  - Load as draft—All changes on the AI agent is lost. You must perform the configuration again.
  
  - Export—Use to export the AI agent.

<a id="section_yhv_gtw_1dc"></a>

#### Change logs

The Change logs tab tracks the changes made to the autonomous AI agent. The Change logs tab displays the following details:

Users with Admin or AI agent developer roles can only access the Change logs tab. Users with custom roles that have the ‘Get Audit log’ permission can also view the audit logs.

- Updated at—The date and time of the change.

- Updated by—The name of the user who incorporated the change.

- Change Location—The specific section of the AI agent where the change was made.

- Description—Additional information about the change.

You can search for a specific audit log using the Updated by, Change Location, and Description search options. You can sort the logs based on the Updated at and Updated by fields.

<a id="concept-template_3e7d5e05-f8d3-4d40-bd41-a79b131b35c6"></a>

### View Autonomous AI agent performance using analytics

The AI agent analytics section provides a graphical representation of the key metrics to evaluate the AI agent performance and effectiveness. To generate the analytics of the Autonomous AI agent:

- Choose the AI agent from the Dashboard.

- On the left navigation pane, click **Analytics**. An overview of the AI agent performance appears in both tabular format and graphical representation.

The first section displays the following statistics about sessions and messages for the AI agent.

- Total sessions and sessions handled by the AI agent without human intervention.
 
- Total agent handovers, which is a count of number of sessions handed over to human agents.
 
- Daily average sessions.
 
- Total messages (human and AI agent messages) and how many of those messages came from users.
 
- Daily average messages.

The second section displays the statistics about the users. It provides a count of total users and information about average sessions per user and daily average users.

The third section displays the AI agent responses and agent handovers.

<a id="content"></a>

<a id="concept-template_4777d368-bcf4-4e97-9b5d-9eb0db6b6393"></a>

Scripted AI agents enhance the no-code agent-building capabilities of the Webex AI Agent Studio platform. They enable multiturn conversations, gathering relevant data from customers to perform specific tasks. This includes:

- Running simple commands—Follow instructions to complete predefined actions.
 
- Processing data—Manipulate and transform data according to specified rules.
 
- Interacting with other systems—Communicate with and control other solutions.

Scripted AI agents are knowledge-driven agents whose knowledge base consists of a corpus of questions and answers. Scripted AI agent can provide answers based on a user-created training corpus, which is a collection of examples and answers. This capability is useful in scenarios where:

- Specific knowledge is required—The agent needs to answer questions within a predefined domain.
 
- Consistency is important—The agent must provide consistent responses to similar queries.
 
- Limited flexibility is needed—The agent's responses are constrained by the information in the training corpus.

<a id="task-template_72a02c77-a182-4301-b588-235a042809a2"></a>

### Create a scripted AI agent

|  |  |
| --- | --- |
| 1 | Log in to the Webex AI Agent Studio platform. |
| 2 | On the dashboard, click + Create agent. |
| 3 | On the Create an AI Agent screen, choose Start from scratch and click Next.<br> <br>You can also choose a predefined template to create your AI agent quickly. You can filter the AI agent type to `Scripted`. In this case, the fields on the Profile page autopopulate. For more information on the templates, see [Use AI agent templates](https://help.webex.com/en-us/article/n8mo4c/). |
| 4 | Choose Scripted agent type. |
| 5 | Specify the following details:<br> <br>- Agent name—Enter the name of the AI agent.<br>- System ID—A system-generated unique identifier. This field is editable.<br>- AI engine—Choose an AI engine from the drop-down list. The available options are:<br>  <br>   <br>  <br>  - Webex AI Agent Pro 2.0 (with Swiftmatch)—this is the default option.<br>  <br>  - Webex AI Agent Pro 1.0 (with Swiftmatch)<br>  <br>   <br>  <br>  For details about each AI engine's capabilities, refer to the [Understand AI engines for AI agents](https://help.webex.com/article/ne6s80cb) article. |
| 6 | Click Create. You have now successfully created the scripted AI agent which is now available on the Dashboard.<br> <br>You can create up to 100 AI agents, which includes both scripted and autonomous types.<br> <br>On the AI Agent header, you can perform the following tasks:<br>- Preview<br>- Copy Access Token<br>- Delete<br>- Export<br>For more information, see [Tasks on AI agent card](https://help.webex.com/article/ncs9r37#section_us5_zdw_ycc).<br> <br>Also, you can import the AI agents. For more information, see [Import AI agent](https://help.webex.com/article/ncs9r37#section_grn_byz_zcc). |

What to do next

[Configure your scripted AI agent](https://help.webex.com/article/ncs9r37#concept-template_48f88bed-db0d-4b55-8fcf-a0435deec60a).

<a id="concept-template_48f88bed-db0d-4b55-8fcf-a0435deec60a"></a>

### Configure scripted AI agent

The following sections guide you on how to configure scripted AI agent for your specific needs:

- [Update scripted AI agent profile](https://help.webex.com/article/ncs9r37#task-template_c7edf167-b532-4222-b464-d54ad1d8b893)

- [Configure scripts](https://help.webex.com/article/ncs9r37#concept-template_48a58175-b53a-49e7-afd8-70d950c50bc1)

  - [Create an intent](https://help.webex.com/article/ncs9r37#task-template_6361ba29-ee9e-4b62-b9b5-b80cfe6652e7)
  
  - [Create an entity](https://help.webex.com/article/ncs9r37#task-template_5e5dea5a-2b74-4883-a52f-8b70e07671b7)
  
  - [Create a response](https://help.webex.com/article/ncs9r37#task-template_336f85da-d3db-4427-b942-d5821752e630)

- [Configure agent handover](https://help.webex.com/article/ncs9r37#task-template_d3113eca-9043-44af-a1ba-493fc6f90af8)

- [Configure language and voice](https://help.webex.com/article/ncs9r37#task-template_f628b019-be9c-483e-92ea-b870a6b51a50)

<a id="task-template_c7edf167-b532-4222-b464-d54ad1d8b893"></a>

#### Update scripted AI agent profile

<a id="context_ckk_t2s_zcc"></a>

Use the Profile tab to manage the customer-facing disclosure that tells customers when they are interacting with an AI agent.

<a id="prereq_bkk_t2s_zcc"></a>

Before you begin

Create a scripted AI agent.

<a id="steps_dkk_t2s_zcc"></a>

|  |  |
| --- | --- |
| 1 | On the Dashboard, click the AI agent that you've created. |
| 2 | Navigate to the Configurations >  Profile tab and configure the following details:<br> <br>- Agent name—Edit the name of the AI agent, if needed.<br>- System ID—Edit the system id of the AI agent, if needed.<br>- URL for agent profile image—The default URL from where the system fetches the AI agent's logo or image. Change this if needed.<br>- Time zone—Choose your time zone from the drop-down list.<br>- Allow feedback—Enable this toggle to let an AI agent ask for feedback in the message.<br>- AI engine—Displays the chosen AI engine. You can update the AI engine by clicking the icon next to the drop-down list. For more information, see [Update AI engine settings](https://help.webex.com/article/ncs9r37#task-template_6df54695-7d89-4046-b0c1-3648dfec3067).<br>- Description—Enter the details about the AI agent.<br>- Custom error message—Enter a custom error message for server or proxy errors.<br>- AI transparency—Enable or disable the transparency note that tells customers they are interacting with an AI agent. Click Edit transparency disclosure to edit the default transparency message.<br>  <br>   <br>  <br>  - The default transparency note is used when a language-specific message is unavailable.<br>  <br>  - For digital conversations, the transparency note is added to the first AI-generated response in the session.<br>  <br>  - For voice conversations, the transparency note plays before the AI interaction continues and callers cannot interrupt it.<br>  <br>  - New AI agents have AI transparency enabled by default. If you turn it off, acknowledge the warning and provide a reason. |
| 3 | Click Save changes. |
| 4 | Click Publish to make the AI agent live. |

<a id="task-template_6df54695-7d89-4046-b0c1-3648dfec3067"></a>

##### **Update AI engine settings**

Scripted AI agents use AI engines (powered by machine learning) to understand and respond to customer queries. Here's a quick overview of the AI engines used: 

- **Webex AI Pro 2.0 (with Swiftmatch)**—An advanced generative AI-powered NLU engine that delivers high-precision intent recognition. It features adaptive learning for better generalization, reducing the need for extensive manual training examples.

- **Webex AI Pro 1.0 (with Swiftmatch)**—A fast and lightweight training engine that supports multiple languages.

To change the AI engine for the AI agent:

<table class="stepTable" id="" border="0"><tbody>
            <tr class="li step" id=""><td align="center" valign="middle" class="ordered-number">1</td><td align="left" valign="top" border="0">
              <p class="ph cmd" id="">On the <span class="ph uicontrol">Dashboard</span>, click the AI agent that you&#x27;ve created.</p>
            </td></tr>
            <tr class="li step" id=""><td align="center" valign="middle" class="ordered-number">2</td><td align="left" valign="top" border="0">
              <p class="ph cmd" id="">Navigate to <span class="menucascade"><span class="ph uicontrol">Configurations</span> &gt; <span class="ph uicontrol">Profile</span></span> tab.</p>
            </td></tr>
            <tr class="li step" id=""><td align="center" valign="middle" class="ordered-number">3</td><td align="left" valign="top" border="0">
              <p class="ph cmd" id="">Click the icon next to the AI engine.</p>
            </td></tr>
            <tr class="li step" id=""><td align="center" valign="middle" class="ordered-number">4</td><td align="left" valign="top" border="0">
              <p class="ph cmd" id="">In the <span class="ph uicontrol">Manage AI Engine</span> page, configure the following
          fields:</p>
              <ol type="a" class="ol substeps"><li class="li substep substepexpand">
                  <p class="ph cmd" id="">
                    <span class="ph uicontrol">Training Engine</span>—Choose the required AI engine from the
              drop-down list. </p>
                  <div class="itemgroup info">
              <div class="olh_note"><div class="note__content"><div class="olh_note" role="note"><div class="note-container"><span class="svg-container"></span>
                <p class="p">Training an AI agent using Webex AI Pro 2.0 (with Swiftmatch) model may take
                  slightly longer than Webex AI Pro 1.0 (with Swiftmatch) model.</p>
              </div></div></div></div>
            </div>
                </li><li class="li substep substepexpand">
                  <p class="ph cmd" id="">
                    <span class="ph uicontrol">Inference</span>—Specify the following information:</p>
                  <div class="itemgroup info">
              <ul class="ul"><li class="li">
                  <p class="p"><span class="ph uicontrol">Score below which fallback is shown</span>—The minimum
                    confidence needed to display a response, below which a fallback response
                    appears. Note that switching your AI engine will change the default value of
                    this setting. </p>
                  <table width="100%" border="1"><caption><span class="table--title-label table title">Table 1. </span><span class="tabletitle">Fallback score values for AI engines</span></caption><thead><tr><th id="" font-weight="bold" align="">AI Engine</th><th id="" font-weight="bold" align="">Range of Values</th><th id="" font-weight="bold" align="">Default Value</th><th id="" font-weight="bold" align="">Input method</th></tr></thead><tbody><tr><td headers="" align=""><strong class="ph b">Webex AI Pro 2.0 (with Swiftmatch)</strong></td><td headers="" align="">-0.1, -0.05, 0.0, 0.05, 0.1, 0.15, 0.2 </td><td headers="" align="">0.05</td><td headers="" align="">Choose a predefined value from the drop-down list. </td></tr><tr><td headers="" align=""><strong class="ph b">Webex AI Pro 1.0 (with Swiftmatch)</strong></td><td headers="" align="">0 to 1</td><td headers="" align="">0.3</td><td headers="" align="">Enter a valid value in the text box.</td></tr></tbody></table>
                </li><li class="li">
                  <p class="p"><span class="ph uicontrol">Difference in score for partial match</span>—The minimum gap
                    between confidence levels of responses to clearly display the best match below
                    which a partial match template is shown. Note that switching your AI engine will
                    change the default value of this setting. For both engines, the score is 0
                    -1.</p>
                  <table width="100%" border="1"><caption><span class="table--title-label table title">Table 2. </span><span class="tabletitle">Partial match score values for AI engines</span></caption><thead><tr><th id="" font-weight="bold" align="">AI Engine</th><th id="" font-weight="bold" align="">Range of Values</th><th id="" font-weight="bold" align="">Default Value</th><th id="" font-weight="bold" align="">Input method</th></tr></thead><tbody><tr><td headers="" align=""><strong class="ph b">Webex AI Pro 2.0 (with Swiftmatch)</strong></td><td headers="" align="">0—1</td><td headers="" align="">0.02</td><td headers="" align="">Enter a valid value in the text box.</td></tr><tr><td headers="" align=""><strong class="ph b">Webex AI Pro 1.0 (with Swiftmatch)</strong></td><td headers="" align="">0—1</td><td headers="" align="">0.05</td><td headers="" align="">Enter a valid value in the text box.</td></tr></tbody></table>
                  <div class="olh_note"><div class="note__content"><div class="olh_note" role="note"><div class="note-container"><span class="svg-container"></span>
                    <p class="p">In most cases, the default threshold value is sufficient. For use cases that
                      require customization, validate alternative fallback threshold values using
                      the testing functionality and choose the range that performs best based on the
                      samples added.</p>
                  </div></div></div></div>
                  <p class="p"><strong class="ph b">Webex AI Pro 2.0 (with Swiftmatch)</strong> uses two scores: a Similarity score
                    and a Partial Match score to determine intent matches. An intent is considered a
                    match if its score is above 0.05. <ul class="ul"><li class="li">
                        <p class="p"><strong class="ph b">Partial Match</strong>: If two or more intents have scores above 0.05, and
                          the difference between their scores is less than or equal to 0.02, the AI
                          agent triggers a partial match and asks the user to clarify between the
                          options.</p>
                      </li><li class="li">
                        <p class="p"><strong class="ph b">Confident Match</strong>: If the difference between the top two intent
                          scores is greater than 0.02, the system identifies the highest-scoring
                          intent as the potential match.</p>
                      </li></ul></p>
                </li></ul>
            </div>
                </li></ol>
              <div class="itemgroup info">
          <ul class="ul"><li class="li">
              <p class="p"><span class="ph uicontrol">Advanced Settings</span>—Specify the following information:</p>
              <ul class="ul"><li class="li">
                  <p class="p"><span class="ph uicontrol">Expand contractions</span>—Check this option to convert
                    contractions in training data and consumer queries into their full forms for
                    better accuracy. This option is available for Webex AI Pro 1.0 (with
                    Swiftmatch).</p>
                </li><li class="li">
                  <p class="p"><span class="ph uicontrol">Spellcheck in inference</span>—Check this option to identify
                    and fix the spelling mistakes before processing the text. This option is
                    available for all three AI engines.</p>
                </li><li class="li">
                  <p class="p"><span class="ph uicontrol">Prioritize slot filling</span>—Check this option to prioritize
                    slot filling over intent detection. This option is available for Webex AI Pro
                    1.0 (with Swiftmatch).</p>
                </li><li class="li">
                  <p class="p"><span class="ph uicontrol">Results stored per message</span>—Enter the number of
                    transactions (for which the AI agent has calculated confidence scores) to list
                    under Transaction information in the Sessions. This option is available for all
                    three AI engines. </p>
                </li><li class="li">
                  <p class="p"><span class="ph uicontrol">Multi-lingual model</span>—Choose the model from the drop-down
                    list to enable the multilingual inference. Configure more than one language for
                    an AI agent to enable this option and this option is available only for Webex AI
                    Pro 1.0 (with Swiftmatch).</p>
                </li><li class="li">
                  <p class="p"><span class="ph uicontrol">Vector model</span>—Choose the vector model from the drop-down
                    list to improve the accuracy of the AI agent. This feature is only available for
                    Webex AI Pro 1.0 (with Swiftmatch).</p>
                </li><li class="li">
                  <p class="p"><span class="ph uicontrol">Remove stopwords</span>—Check this option to remove the
                    stopwords during training and inference. This feature is only available for
                    Webex AI Pro 1.0 (with Swiftmatch). </p>
                </li><li class="li">
                  <p class="p"><span class="ph uicontrol">Remove special characters</span>—Check this option to remove
                    special characters from customer queries for better responses. This option is
                    available only for Webex AI Pro 1.0 (with Swiftmatch).</p>
                </li><li class="li">
                  <p class="p"><span class="ph uicontrol">Replace entities in inference</span>—Check this option to
                    replace entity values in training data and inference with entity IDs. This
                    option is available only for Webex AI Pro 1.0 (with Swiftmatch). </p>
                </li><li class="li">
                  <p class="p"><span class="ph uicontrol">Wordform expansion</span>—Check this option to expand training
                    data with wordforms (such as plurals, verbs, and so on), along with the synonyms
                    present in the data. This option is available only for Webex AI Pro 1.0 (with
                    Swiftmatch). </p>
                </li></ul>
            </li></ul>
        </div>
            </td></tr>
            <tr class="li step" id=""><td align="center" valign="middle" class="ordered-number">5</td><td align="left" valign="top" border="0">
              <p class="ph cmd" id="">Click <span class="ph uicontrol">Update</span> to change the AI engine settings for the AI
          agent.</p>
            </td></tr>
            <tr class="li step" id=""><td align="center" valign="middle" class="ordered-number">6</td><td align="left" valign="top" border="0">
              <p class="ph cmd" id="">Click <span class="ph uicontrol">Save changes</span> to update the AI engine settings.</p>
            </td></tr>
          </tbody></table>

<a id="concept-template_48a58175-b53a-49e7-afd8-70d950c50bc1"></a>

#### Configure scripts

Scripts are the building blocks that power your AI agent's understanding and responses. This section describes three key components: 

- **Intents** capture the various goals or actions users want to accomplish when interacting with your AI agent. Mapping user intents enables the AI agent to recognize and respond appropriately to user requests. To create an intent, see [Create an intent](https://help.webex.com/article/ncs9r37#task-template_6361ba29-ee9e-4b62-b9b5-b80cfe6652e7).

- **Entities** are the specific pieces of information your AI agent needs to extract from user inputs. These include dates, product names, or custom values unique to the customer use case. Entities are important variables that your AI agent must understand to fulfill the user requests effectively. To create an entity, see [Create an entity](https://help.webex.com/article/ncs9r37#task-template_5e5dea5a-2b74-4883-a52f-8b70e07671b7).

- **Responses** are your AI agent's carefully crafted replies to user requests. They dictate how your AI agent communicates with the users after understanding their intent and gathering the necessary entities. To create a response, see [Create a response](https://help.webex.com/article/ncs9r37#task-template_336f85da-d3db-4427-b942-d5821752e630).

Together, these components work together to create fluid and purposeful conversations between your agent and its users. For more information, see [Understand intents, entities, and responses in AI Agent Studio](https://help.webex.com/en-us/article/sz02k8/Understand-intents,-entities,-and-responses-in-AI-Agent-Studio).

<a id="task-template_6361ba29-ee9e-4b62-b9b5-b80cfe6652e7"></a>

##### **Create an intent**

|  |  |
| --- | --- |
| 1 | On the **Dashboard**, click the AI agent that you've created. |
| 2 | Navigate to Configurations > Scripts > Intents. |
| 3 | Click +Create intent. |
| 4 | On the Add a new intent screen, specify the following details:<br> <br>- **Intent name**—Enter a name for the intent.<br>- **Intent description**—Enter a clear and concise description for the intent. To optimize AI agent performance, provide a descriptive phrase rather than just one or two words. This field is mandatory and applicable only to the **Webex AI Pro 2.0 (Swiftmatch)** engine. If you switch from **Webex AI Pro 1.0 (Swiftmatch)** engine to **Webex AI Pro 2.0 (Swiftmatch)** engine, you must provide a description to resolve any validation error.<br>  <br>   <br>  <br>  If harmful content is detected in the intent description, a generic warning will appear, and you can't save the changes until the content is removed or corrected.<br>- Settings—Toggle on and off the following settings for the intent:<br>  <br>   <br>  <br>  - Reset slots after completion—Toggle on to reset the slot values collected in the conversation once the intent is complete. If this toggle is in disabled status, the slot retains the old values and displays the same response.<br>  <br>  - End conversation—Toggle on to close the session after this intent. Webex Connect and voice flows can use this to close a conversation with customers.<br>- Context—Provide the entry and exit contexts for the intent. For more information, see [Contexts](https://help.webex.com/article/sz02k8#concept-template_b150cc96-f8db-484d-8cd5-e7cbbef3bb24).<br>  <br>   <br>  <br>  - Entry context—Enter the required input in the text box and press the Enter or Return key to add the entry context. You can configure a maximum of 5 entry contexts for a particular intent. <br>    <br>    Entry contexts control whether an intent can be matched with the customer query based on the active context of the session.<br>  <br>  - Exit context—Enter the required input in the text box and press the Enter or Return key to add the exit context. You can configure a maximum of 15 exit contexts for a particular intent. <br>    <br>    Exit contexts control the active contexts for a session.<br>- Intent & utterances—Add an utterance or a phrase to determine the intent and click +Add.<br>  <br>   <br>  <br>  For voice-channel DTMF choices that trigger scripted intents, add the keypad digit as an utterance for the matching intent. For example, if the prompt says “Press 1 for billing, press 2 for support,” add 1 as an utterance to the Billing intent and 2 as an utterance to the Support intent.<br>  <br>   <br>  <br>  **Webex AI Pro 2.0 (Swiftmatch)** engine requires at least`10 utterances` per intent. This number is calculated across all configured languages within the intent. When switching from **Webex AI Pro 1.0 (Swiftmatch)** engine to **Webex AI Pro 2.0 (Swiftmatch)** engine, you must meet this 10-utterance minimum to resolve validation error.<br>  <br>   <br>  <br>  If any harmful content is detected in the utterances, a generic warning will appear, and you can't save the changes until the content is removed or corrected.<br>  <br>   <br>  <br>  - **Generate variants**—For the system to generate utterances automatically based on the intent, click Generate variants. <br>    <br>    - In the Generate variants dialog box, provide a description of your intent to generate relevant training data or utterances.<br>    <br>    - Enter the number of variants to be generated and choose how creative you want the underlying LLM to be while generating these variants.<br>    <br>    - Click Generate.<br>  <br>  - **Add entities as slots**—If any entities are present in the added utterances, they are auto annotated in the utterances and appear in the Slots section. You can select the part of the utterance as a slot for that intent and choose an already created entity or create a new entity.<br>  <br>   <br>  <br>  The intent requires at least 3 utterances and 2 slot annotations for training with the current AI engine.<br>  <br>   <br>  <br>  Each slot displays the following:<br>- Slots (optional)—Link the entities for the slot filling. This ensures that the AI agent gathers all the required information.<br>  <br>   <br>  <br>  - Click +Link to link an entity to the intent. If there’s no entity in the list, the +Link option doesn’t appear. To create an entity, see the [Create an entity](https://help.webex.com/article/ncs9r37#task-template_5e5dea5a-2b74-4883-a52f-8b70e07671b7) section. The following slot details appear and you can configure the retries and response for the required slot:<br>    <br>    - The linked entity name.<br>    <br>    - Required—Check the check box to determine whether it’s required for intent completion.<br>    <br>    - Retries—Enter the number of retries the AI agent attempts to get this slot value from the customer.<br>    <br>    - Response—Choose the response for the slot from the drop-down list. To create a new custom response, click +Create new.<br>  <br>  - Configure the following Settings:<br>    <br>    - Toggle the Update slot values on to update the slot value during the conversation with the customer.<br>      <br>      The AI agent considers the last value filled in the slot to process the data. If you enable this feature, the system updates values for filled slots whenever customers provide new information for the same slot type.<br>    <br>    - Toggle the Provide suggestions for slots on to provide suggestions for slot filling and alternate slot values in the final response, based on customer input.<br>- Response—In the Response section, choose the response that you want to return to customers on completion of the intent. Once chosen, click **View the content of selected response** to view the response content. To add a new custom response, click +Create new to create a new response. For more information, see [Create a response](https://help.webex.com/article/ncs9r37#task-template_336f85da-d3db-4427-b942-d5821752e630). |
| 5 | Click Add to create an intent. |
| 6 | Click Publish to make the AI agent live. |

<a id="task-template_5e5dea5a-2b74-4883-a52f-8b70e07671b7"></a>

##### **Create an entity**

|  |  |
| --- | --- |
| 1 | On the **Dashboard**, click the AI agent that you've created. |
| 2 | Navigate to Configurations > Scripts > Entities. |
| 3 | Click+Create entity. |
| 4 | On the Create entity window, specify the following fields:<br> <br>- **Entity name**—Enter the entity name.<br>- **Entity type**—Choose an entity type from the drop-down list. Based on the chosen entity type, enter a value in the additional field, if it appears.<br>  <br>   <br>  <br>  - If the AI agent has difficulty identifying a person's name with the `Person names` entity type, try using the `Free form` entity type for improved recognition.<br>  <br>  - If the AI Agent doesn’t recognize inputs as expected when using `Regex` or `Alphanumeric` entity value with spaces in the character class (for example, `^[a-zA-Z 0-9]+$`), try using the `Free Form` entity type for broader matching. If you prefer to use `Regex` or `Alphanumeric` entity values with spaces, you can uncheck the "Replace entities in inference" option in the advanced engine settings. |
| 5 | Click Save changes.<br> <br>You can use Edit and Delete options in the Actions column to perform related actions. You can edit only the entity name and not the entity type. |

<a id="task-template_336f85da-d3db-4427-b942-d5821752e630"></a>

##### **Create a response**

|  |  |
| --- | --- |
| 1 | On the **Dashboard**, click the AI agent that you've created. |
| 2 | Navigate to Configurations > Scripts > Responses.<br> <br>The system provides default conditional responses for Web channel which you can use for customer interactions. If AI transparency is enabled, the default AI transparency response appears in the list. You can use the Edit icon in each response to modify the response settings. You can't delete the default responses and Web channel. |
| 3 | To create a custom response, click +Add response.<br> <br>Add a new response screen appears. |
| 4 | On the Add a new response screen, enter the new Response name. |
| 5 | For the configured language, you can optionally add a conditional response by clicking Add condition.<br> <br>- Enter the condition name and click Create.<br>- Click the condition and go to the Rules section, provide the IF and OR variable conditions, as needed.<br>  <br>   <br>  <br>  - In the **Left variable**field, choose the response variable from the drop-down list. For more information about response variables, see the [List of common response variables](https://help.webex.com/en-us/article/sz02k8/Understand-intents,-entities,-and-responses-in-AI-Agent-Studio#concept-template_352cad79-2ed2-433b-a37d-658b8e003604) table. This table contains the list of variables that you can use in this field to define rules. These variables can also be used to customize AI agent responses.<br>  <br>  - Choose the appropriate operator to execute the rule.<br>  <br>  - Choose the data type from the drop-down list. Data types are populated based on the chosen operator.<br>  <br>  - In the **Right variable**field, specify the response variable. The type of variable value with which the syntax in the left variable must match. This field is displayed only when you set the Operator to any of these values—Equals to, Not Equals to, In, Greater than, Less than. You can also use the list of variables to define rules in the right variable of the conditional response type if you set the `Data type` to `Variable`.<br>- Click **Actions** to create a response for the defined rule. In the Actions section, you can configure the response to be displayed for the customer query once the rule is fulfilled.<br>  <br>  - To add a response for Web (default) channel:<br>    <br>    - Choose the response type from the right pane. The supported response types are Text, Carousel, Quick Reply, Image, Video, Audio, and File.<br>    <br>    - For the chosen response type, configure the required settings. For information on how to configure various responses for Web (default), see the [Configure response types](https://help.webex.com/article/ncs9r37#concept-template_86a220a2-df7a-4973-be7b-fa58dba3dce7) section.<br>  <br>  <br>  <br>  - To add a response for the other channels:<br>    <br>    - Click + next to Web (default).<br>    <br>    - Choose the desired channel from the drop-down list. The supported channels are Messenger, SMS, WhatsApp, Apple Messages for Business, RCS, and Voice.<br>    <br>    - Choose the response type for the chosen channel from the right pane. For supported response types for various channels, see the [Supported response types for channels](https://help.webex.com/article/sz02k8/Understand-intents,-entities,-and-responses-in-AI-Agent-Studio#section_xrr_w2k_g2c) section.<br>    <br>    - Configure the required settings for the chosen response type. For information on how to configure various responses, see the [Configure response types](https://help.webex.com/article/ncs9r37#concept-template_86a220a2-df7a-4973-be7b-fa58dba3dce7) section. |
| 6 | Click Create to create a response. |

<a id="concept-template_86a220a2-df7a-4973-be7b-fa58dba3dce7"></a>

###### **Configure response types**

In Response Designer, you can configure channel-specific responses for the intents. For more information on how to create a response, see the [Create a response](https://help.webex.com/article/ncs9r37#task-template_336f85da-d3db-4427-b942-d5821752e630) section.

Refer to the following section for details:

- [Configure text response type](https://help.webex.com/article/ncs9r37#text-response-type-configuration)

- [Configure carousel response type](https://help.webex.com/article/ncs9r37#carousel-response-type-configuration)

- [Configure quick reply response type](https://help.webex.com/article/ncs9r37#quick-reply-response-type-configuration)

- [Configure image response type](https://help.webex.com/article/ncs9r37#image-response-type-configuration)

- [Configure video response type](https://help.webex.com/article/ncs9r37#video-response-type-configuration)

- [Configure audio response type](https://help.webex.com/article/ncs9r37#audio-response-type-configuration)

- [Configure file response type](https://help.webex.com/article/ncs9r37#file-response-type-configuration)

- [Configure reply button response type](https://help.webex.com/article/ncs9r37#reply-button-response-type-configuration)

- [Configure list messages response type](https://help.webex.com/article/ncs9r37#list-messages-response-type-configuration)

- [Configure numbered list response type](https://help.webex.com/article/ncs9r37#numbered-list-response-type-configuration)

- [Configure list picker response type](https://help.webex.com/article/ncs9r37#list-picker-response-type-configuration)

- [Configure time picker response type](https://help.webex.com/article/ncs9r37#time-picker-response-type-configuration)

- [Configure media response](https://help.webex.com/article/ncs9r37#media-response-type-configuration)

- [Configure rich link response type](https://help.webex.com/article/ncs9r37#rich-link-response-type-configuration)

- [Configure form response type](https://help.webex.com/article/ncs9r37#form-response-type-configuration)

- [Configure custom events response types](https://help.webex.com/article/ncs9r37#custom-events-response-type-configuration)

<a id="text-response-type-configuration"></a>

###### **Configure text response type**

You can configure text messages as responses for all channels. To add a text response type for the chosen channel (default or custom), follow these steps:

|  |  |
| --- | --- |
| 1 | For the chosen channel, select Text response type. |
| 2 | Enter the text message in the **Variant** textbox.<br> <br>You can customize agent responses using variables received from the channel or collected from customers during the conversation. You can also enter `${` to choose the required variable in the text area. |
| 3 | To add multiple variants, click **Add Variant** and enter the text message. |
| 4 | Click **Create** to create the response. |

<a id="carousel-response-type-configuration"></a>

###### **Configure carousel response type**

You can configure carousel responses for Web (default) and Messenger channels. Each carousel response can contain an image, a description, and up to three buttons.Follow these steps:

|  |  |
| --- | --- |
| 1 | For the chosen channel, click Carousel in the right pane. The rich carousel card appears. |
| 2 | Click Configure to view or edit the image URL. By default, the system displays the image URL. |
| 3 | Enter the Title and Description (optional) for the card. |
| 4 | To send a configured payload to the AI agent and invoke the corresponding response for the intent, click **+ Add quick reply**.<br> <br>- Choose the **Text** button type and enter the text and payload/identifier. Click **Done**.<br>- For URL redirection, choose the **URL** button type (applicable only for Web channel), enter the text and URL, and click **Done**.<br>  <br>   <br>  <br>  Click Renew Now to change the text and URL redirection. |
| 5 | Click **Create** to create the response. |

<a id="quick-reply-response-type-configuration"></a>

###### **Configure quick reply response type**

You can configure quick reply responses for Web (default), SMS, Messenger, Apple Messages for Business, and RCS channels. Follow these steps:

|  |  |
| --- | --- |
| 1 | For the chosen channel, click Quick Reply on the right pane. |
| 2 | Enter the quick reply message for the intent. |
| 3 | To send a configured payload to the AI agent, click **+ Add quick reply**. Choose the **Text** button type and enter the text and payload/identifier. Click **Done** to add a text quick reply.<br> <br>For URL redirection, choose the **URL** button type (only applicable for Web chat), enter the text and URL, and click **Done**. |
| 4 | Click **Create** to create the response.<br> <br>A partial match happens when there's uncertainty about incoming user queries. AI agent responds with intents that are close to the user query as options. Partial match responses are displayed for the Web. |

<a id="image-response-type-configuration"></a>

###### **Configure image response type**

You can configure image responses for Web (default), Messenger, and WhatsApp channels. Follow these steps:

|  |  |
| --- | --- |
| 1 | For the chosen channel, click Image on the right pane. The image card appears with the default configurations. |
| 2 | Update the image URL. |
| 3 | Choose the image type (jpeg or png). |
| 4 | Click **Create** to create the response. |

<a id="video-response-type-configuration"></a>

###### **Configure video response type**

You can configure video responses for Web (default), Messenger, and WhatsApp channels. Follow these steps:

|  |  |
| --- | --- |
| 1 | For the chosen channel, click Video on the right pane. The video card appears with the default configuration. |
| 2 | Update the video URL. |
| 3 | Choose the required video type (mp4). |
| 4 | Click **Create** to create the response. |

<a id="audio-response-type-configuration"></a>

###### **Configure audio response type**

You can configure audio responses for Web (default) and WhatsApp. Follow these steps:

|  |  |
| --- | --- |
| 1 | For the chosen channel, click Audio in the right pane. The audio card appears with the default configuration. |
| 2 | Update the audio URL. |
| 3 | Choose the audio type (mp3 or aac). |
| 4 | Click **Create** to create the response. |

<a id="file-response-type-configuration"></a>

###### **Configure file response type**

You can configure the file as a response for Web (default) and WhatsApp channels. Follow these steps:

|  |  |
| --- | --- |
| 1 | For the chosen channel, click File on the right pane. The File card appears. |
| 2 | Enter the file URL. |
| 3 | Choose the file type. Supported file types are .html, .pdf, plaintext, .jpeg, .png, .mp4, .mp3, and .aac. |
| 4 | Click **Create** to create the response. |

<a id="reply-button-response-type-configuration"></a>

###### **Configure reply button response type**

You can configure reply button responses for the WhatsApp channel. Follow these steps:

|  |  |
| --- | --- |
| 1 | Click Reply Button in the right pane. |
| 2 | Configure the header details (Optional).<br> <br>- Choose the type of header—Text (can be 20 characters long), Video, Image, Document.<br>- Enter the value depending on the header type selected. |
| 3 | Enter the body text. This field can contain up to 1024 characters. |
| 4 | Enter the footer text (optional). This field can contain up to 60 characters. |
| 5 | To add a new reply button, click **Add button**, enter the text and payload, and click **Done**<br> <br>You can configure up to three reply buttons (with a 20-character limit). |
| 6 | Click **Create** to create the response. |

<a id="list-messages-response-type-configuration"></a>

###### **Configure list messages response type**

You can configure the list messages as responses for the WhatsApp channel. Follow these steps:

|  |  |
| --- | --- |
| 1 | Click List Messages in the right pane. |
| 2 | Navigate to the **Configuration** tab and configure the following settings:<br> <br>- (Optional) Configure the header details (can be 20 characters long).<br>- Enter the body text (can be 1024 characters long).<br>- (Optional) Enter the footer text (can be 60 characters long).<br>- Enter the List title. |
| 3 | Navigate to the **List Sections** tab and configure the following settings:<br> <br>- (Optional) Enter the section name (can be 24 characters long).<br>- Enter the row title (can be 24 characters long).<br>- Enter the row ID, which is a unique identifier for each row that will help you identify the users’ choice.<br>- Enter the row description (can be 20 characters long).<br>- To add a new section, click **Add section**. |
| 4 | Click **Create** to create the response. |

<a id="numbered-list-response-type-configuration"></a>

###### **Configure numbered list response type**

You can configure the numbered list as a response for the WhatsApp channel. Follow these steps:

|  |  |
| --- | --- |
| 1 | Click Numbered List in the right pane. |
| 2 | Edit the default text provided. |
| 3 | Click **+Add list item**. |
| 4 | Under the **Text** button type, configure the following:<br> <br>- Enter the text and payload/identifier to send the payload to the AI agent when the user clicks the button.<br>- Click **Done**. |
| 5 | Click **Create** to create the response. |

<a id="list-picker-response-type-configuration"></a>

###### **Configure list picker response type**

You can configure list picker responses for the Apple Business Messages channel. Follow these steps:

|  |  |
| --- | --- |
| 1 | Click List Picker in the right pane. |
| 2 | Navigate to the **Configuration** tab and configure the following settings:<br> <br>- Enter the list picker title.<br>- (Optional) Enter the preview image URL and choose the image style (Icon, Small, Large).<br>- Enter the description for the list picker.<br>- Enter the title and description for the reply message based on the selected list picker option. |
| 3 | Navigate to the **List sections** tab and configure the following settings:<br> <br>- Enter the title for items in the list.<br>- Enter the title for items in the list.<br>- In the **List Item** field, configure the following settings:<br>  <br>   <br>  <br>  - Enter the image URL for the list item.<br>   <br>  - Enter a title.<br>   <br>  - Enter the identifier for an item. When a user selects an item, the identifier is sent to the AI agent, which displays the next steps.<br>   <br>  - Enter the description for the list item.<br>   <br>  - To add another item, click the **+** icon.<br>   <br>  - To delete an item, click the **Delete** icon. |
| 4 | To add a new list section, click **Add List section**. |
| 5 | Click **Create** to create the response. |

<a id="time-picker-response-type-configuration"></a>

###### **Configure time picker response type**

You can configure time picker responses for the Apple Business Messages channel. Follow these steps:

|  |  |
| --- | --- |
| 1 | Click Timer Picker in the right pane.<br> <br>Navigate to the **Configuration** tab and configure the following:<br> <br>- Enter a title for the time picker.<br>- (Optional) Enter the preview image URL and choose the image style (Icon, Small, Large).<br>- Enter the description.<br>- Enter the title and description for the reply message based on the selected time picker option. |
| 2 | Navigate to the **Event details** tab and configure:<br> <br>- Enter the event title.<br>- Enter the timezone for the event.<br>- Configure slots:<br>  <br>   <br>  <br>  - Enter the date and time for slot1.<br>   <br>  - Enter the duration for slot1.<br>   <br>  - Enter the identifier for the slot. When a user selects a slot, the identifier is sent to the AI agent, which displays the next step.<br>   <br>  - To add a new slot, click **Add slot**. |
| 3 | Click **Create** to create the response. |

<a id="media-response-type-configuration"></a>

###### **Configure media response**

You can configure media responses for the Apple Business Messages channel. Follow these steps:

|  |  |
| --- | --- |
| 1 | Click Media in the right pane. |
| 2 | Enter the text. |
| 3 | Choose the media type and enter the URL. |
| 4 | To add more attachments, click **Add attachments**. |
| 5 | Click **Create** to create the response. |

<a id="rich-link-response-type-configuration"></a>

###### **Configure rich link response type**

You can configure rich link responses for the Apple Business Messages channel. Follow these steps:

|  |  |
| --- | --- |
| 1 | Click **Rich Link** in the right pane. |
| 2 | Enter the image URL and choose the image type (jpeg or png). |
| 3 | Enter the website URL for redirection. |
| 4 | Enter the URL title for the video or image. |
| 5 | Enter the video URL supporting MIME protocol and choose the type (video/mp4). |
| 6 | Click **Create** to create the response. |

<a id="form-response-type-configuration"></a>

###### **Configure form response type**

You can configure form responses for the Apple Business Messages channel. Follow these steps:

|  |  |
| --- | --- |
| 1 | Click Form in the right pane. |
| 2 | Enter the form in JSON format. Each JSON contains information about the pages that go as a part of the form with customizations. The pages can be of different types:<br> <br>- **Splash**: An introduction page with a title, description, action button, and image.<br> <br>- **Select**: A page for either a single "True/False" selection or multiple selections, supporting image assets.<br> <br>- **Picker**: A page for a single selection from multiple options.<br> <br>- **Date Picker**: Provides Apple's standard Date Picker with customizable date format and limits.<br> <br>- **Input**: A page featuring various input fields to collect information.<br> <br>The structured content metadata allows the user to specify the form's pages and visual layout. This template comprises two sections:<br> <br>- **BusinessFormEvent**: Configures page identifiers, summary, pages, and images.<br> <br>- **BusinessChatMessage**: Configures received and reply message information.<br> <br>Click **Download sample JSON** to download the sample JSON file and understand the form structure.<br> <br>Refer to [Apple's official documentation](https://register.apple.com/resources/messages/msp-rest-api/type-interactive#form-message)for more information. |

<a id="custom-events-response-type-configuration"></a>

###### **Configure custom events response types**

You can configure custom events as responses for the voice channel. Follow these steps:

|  |  |
| --- | --- |
| 1 | Click **Custom Events**in the right pane. |
| 2 | Enter the incoming event name that the AI agent receives. |
| 3 | In the **Voice settings**, configure the following settings to be added to each agent response:<br> <br>- **Timeout (s)**: Specify the duration, in seconds, that the agent waits for a user response. If there's no response, you can set it to either prompt the user again or end the conversation. The default timeout is 5 seconds.<br>- **Timeout response**: Specify the response message to be sent to the user if a timeout occurs.<br>- **Allow barge-in**: Check this option to let the user interrupt the agent's response with new input. If unchecked, the user must wait until the agent has finished its response before responding.<br>- **DTMF input**: Check this option to let users enter specific details through their keypad. This is helpful for gathering information expressed as long numbers. Enabling DTMF input allows you to configure the following settings:<br>  <br>   <br>  <br>  - **Input mode**: Choose the required input mode to let the user respond with DTMF only or using both – DTMF and voice.<br>   <br>  - **Timeout between digits (s):** Set the maximum idle time allowed between entering each digit. If the user exceeds this time, the digits entered so far are sent to the flow as their input.<br>   <br>  - **Termination character**: Specify the termination character, like # or *, to mark the end of user input. When the user presses this key, the preceding keypad input is sent to the flow as user input.<br>   <br>  - **Max length**: Specify the maximum length of characters allowed for user input. |
| 4 | Click **Create** to create the response.<br> <br>For configuring custom events for scripted AI agent, see the [Configure custom events](https://help.webex.com/article/n5uo60x) article. |

<a id="task-template_d3113eca-9043-44af-a1ba-493fc6f90af8"></a>

#### Configure agent handover

<a id="context_ckk_t2s_zcc"></a>

<a id="prereq_bkk_t2s_zcc"></a>

Before you begin

Create the scripted AI agent.

<a id="steps_dkk_t2s_zcc"></a>

|  |  |
| --- | --- |
| 1 | On the Dashboard, click the scripted AI agent that you've created. |
| 2 | Navigate to Configuration >  Handover and toggle on or off the required settings:<br> <br>- Handover on partial match—A number of consecutive partial matches in a session can initiate a handover. This number is configurable.<br>- Handover on fallback—A number of consecutive fallback messages in a session can initiate an agent handover. This number is configurable in the provided text box.<br>- Handover after repeated agent responses—Consecutive repeated messages in a session can initiate agent handover. The number of repetitions needed for this trigger is configurable.<br>- Handover when slot filling retry limit reached—When the retry attempts for the slot filling is reached to the maximum limit, it initiates an agent handover. |
| 3 | Click Save changes. |

<a id="postreq_vzn_jjg_1dc"></a>

What to do next

Navigate to the [preview your Scripted AI Agent](https://help.webex.com/article/ncs9r37#concept-template_7950670d-af45-4860-90b9-db9ea8dccef3).

<a id="task-template_f628b019-be9c-483e-92ea-b870a6b51a50"></a>

#### Configure language and voice

<a id="context_fjd_zjm_g2c"></a>

You can configure multiple languages and language-specific voices for the scripted AI agent to handle customer interactions.

<a id="prereq_tvg_3hc_1dc"></a>

Before you begin

Create the Scripted AI Agent.

<a id="steps_fyp_g31_xcc"></a>

|  |  |
| --- | --- |
| 1 | On the AI agent configuration page, navigate to the Configuration > Language tab.<br> <br>The default language and voice are set to English. For other supported languages and voices, see the [Supported languages and voices](https://help.webex.com/en-us/article/pdef2d/Supported-languages-for-Scripted-AI-Agents) article. |
| 2 | To add more languages to the AI agent, click +Add language. |
| 3 | Choose the desired language and locale from the drop-down list and click Add. |
| 4 | Click Add languages. The newly added language appears in the Language  tab with the Enabled toggle set to 'on' by default.<br> <br>Adding more than one language enables the Polymatch multilingual model in the AI Engine Advanced settings. |
| 5 | Choose the appropriate voice from the Voice Name drop-down list. The available voices automatically appear based on the chosen language. |
| 6 | To set the desired language and voice as defaults for the AI agent, click Set as default under Controls column.<br> <br>You can’t remove the default language and voice, but you can change them as needed. Changing the default language might impact responses, intents, curation, testing, and preview experiences. |

<a id="concept-template_882552ff-3375-4221-93fe-e9bbd916bc02"></a>

#### Configure fulfillment

You can configure the fulfillment for the scripted AI agents to interact with external systems and retrieve, update, or store data through APIs. For more information, see the [Configure fulfillment for scripted AI agents](https://help.webex.com/article/mzpuseb) article.

<a id="concept-template_7950670d-af45-4860-90b9-db9ea8dccef3"></a>

### Preview your scripted AI agent

Webex AI Agent Studio allows you to preview your AI agents during and after development. This feature lets you test how your AI agent works and check if it provides the expected responses to different input queries. You can preview your scripted AI agent in the following ways:

You can open the preview from: 

- **AI agent dashboard**—When you hover over an AI agent card, the Preview option appears for that AI agent. Click it to open the preview.

- **AI agent header**—Click the AI agent card to open the agent. The Preview option is always visible in the header section.

- **Minimized widget**—After you launch the preview and minimize it, a chat head widget appears at the bottom right of the page. You can use this widget to easily reopen the preview mode.

<a id="section_u3r_33x_wcc"></a>

#### Platform preview widget

The preview widget appears at the bottom right of the screen. You can enter utterances (or a sequence of utterances) to see how the AI agent responds, helping you confirm it works as expected. The AI agent preview supports multiple languages and can automatically detect the language of your input. You can also manually select the language in the preview by clicking the language selector and choosing from the available options.

You can maximize the preview widget for a better view. You can also provide consumer information and start multiple rooms to thoroughly test the AI agent.

<a id="task-template_1bacff9f-0e09-41f5-8b78-3b87bdd7e170"></a>

#### Preview chat conversation

The chat preview feature lets you interact with the AI agent as an end user and observe how it responds to different queries through text.

If AI transparency is enabled, preview includes the disclosure experience so you can verify the first AI-generated reply before you publish the agent.

|  |  |
| --- | --- |
| 1 | On the AI agent configuration page, click Preview in the header. The AI agent preview widget appears. |
| 2 | Click Start a Chat. If AI transparency is enabled, the preview prepends the transparency note to the first AI-generated response in the session.<br> <br>- By default, you can preview chat conversations in the English language (en-US).<br>- (Available in Beta) You can preview chat conversations in the other languages you've configured. To configure more languages, refer to the [Configure Language and Voice](https://help.webex.com/en-us/article/ncs9r37/Webex-AI-Agent-Studio-Administration-guide#task-template_f628b019-be9c-483e-92ea-b870a6b51a50) section. |
| 3 | Type your query in the text box and press Enter. |
| 4 | You can then see and assess the response from AI agent.<br> <br>To start a new chat conversation or session, click Preview in the header. Restart the session to verify the transparency note again. |

<a id="task-template_0d438e02-c62e-44c2-a8cb-a10f584092e1"></a>

#### Preview voice conversation

<a id="context_j13_cvq_dgc"></a>

The voice preview feature lets you interact with the AI agent as an end user and observe how it responds to different queries through voice.

- You need browser permissions to preview voice conversations. When prompted by your browser, make sure to click 'Allow' to enable the required access. We recommend using the following browsers:
  
  - Safari on macOS
  
  - Chrome on Windows

- Use a headset for the best experience. When a caller interrupts the AI agent (via barge-in), the AI agent detects the speech, stops the prompt that it is playing, and processes the caller's input accordingly—this works optimally only when you are using a headset.

- When not using a headset, avoid setting the volume to 100%.

If AI transparency is enabled, preview includes the disclosure before the AI interaction continues so you can verify the voice experience before you publish the agent.

<a id="steps_k13_cvq_dgc"></a>

|  |  |
| --- | --- |
| 1 | On the AI agent configuration page, click Preview in the header. The AI agent preview widget appears. |
| 2 | Voice your query. As you speak, you can see the live transcript of the conversation.<br> <br>To mute your voice while interacting, click Mute. |
| 3 | For your query, you can then hear and assess the response from the AI agent. |
| 4 | To end the call, click End call. |

<a id="task-template_839bb67a-b321-4045-a556-f8799d6a0ac9"></a>

### Publish your scripted AI agent

After configuring and previewing your AI agent, you can publish the agent to make it live.

Before you begin

Create the scripted AI agent.

|  |  |
| --- | --- |
| 1 | On the AI agent configuration page, click **Publish**. |
| 2 | Enter the version name and click **Publish**.<br> <br>You can view the version details on the **History** page. For more information, see the History section. |

<a id="concept-template_a91f6514-6e3a-4084-a36b-f583530f30c3"></a>

### Common management sections for Scripted AI Agent

The following sections appear on the left panel of the AI Agent configuration page:

<a id="concept-template_a2c9cfa0-3c80-42fb-8dca-ae3a25dd78c9"></a>

#### Test scripted agent

As AI agents evolve and become more complex, changes to their logic or Natural Language Understanding (NLU) can sometimes have unintended consequences. To ensure optimal performance and identify potential issues, the AI agent platform offers a convenient one-click AI agent testing framework. You can:

- Easily create and run a comprehensive set of test cases.
 
- Define test messages and expected responses for various scenarios.
 
- Simulate complex interactions by creating test cases with multiple messages.

<a id="section_nyz_m5w_1dc"></a>

##### Define tests

You can define tests using the following steps:

- Log in to the Webex AI Agent Studio platform.

- On the **Dashboard**, click the scripted AI agent that you've created.

- Click Testing in the left pane. By default, the Testcases tab appears.

- Select a test case and click Execute selected tests.

Each row in the table represents a test case having the following parameters:

Table 3. Test cases
| Parameter | Description |
| --- | --- |
| Message | A sample message that represents the types of queries and statements you can expect users to send to your AI agent. |
| Expected language | The language in which the you interact with the AI agent. |
| Expected intent | Specify the intent to be displayed in response to a particular user message. To assist you in finding the most relevant intent, this column features a Smart auto-complete function. As you enter, the system suggests matching intents based on the text entered so far. |
| Reset previous context | Click the check box to isolate test cases and run them independently of any existing AI agent context. When enabled, each test case is simulated in a new session, preventing interference from previous interactions, or stored data. |
| Include partial matches | Enable this toggle to consider test cases successful even if the expected intents only partially match the actual response. |
| Import from CSV | Import test cases from a comma-separated file (CSV) file. In this case, all existing test cases are overwritten. |
| Export to CSV | Export test cases to a comma-separated file (CSV) file. |
| Test callbacks | Enable this toggle to simulate incoming callbacks and test the flow behavior without requiring actual incoming calls. |
| Callback in flow | Click the check box in this column to indicate that an intent must trigger a callback. |
| Expected callback template | Specify the template key to activate when the callback occurs. |
| Callback timeout (s) | The maximum amount of time (in seconds) the AI agent waits for a callback response before considering the callback as timed out. The system allows a maximum of 20-second timeout. |

<a id="section_jnr_q5w_1dc"></a>

##### Execute tests

On the Execution tab, click Execute selected tests to initiate a sequential execution of all selected test cases. 

You can also execute test cases from the **Test cases** tab.

.

As each test case completes, the system displays its result next to the corresponding entry. To terminate a running test case, click Abort Run at the top-right corner of the screen.

To view test cases with specific outcomes, click the desired result (for example, `Passed`, `Passed with partial match`, `Failed`, `Pending`) in the summary ribbon. This filters the test case list to display only those matching the selected result.

The `session ID` associated with each test case is displayed in the results. This allows you to quickly cross-reference test cases and view transaction details. To perform this, choose the `Transaction Details` option in the Actions column.

<a id="section_c43_s5w_1dc"></a>

##### Execution history

On the History tab, access all executed test cases. 

- Click the Download icon from the Actions column to export the executed test data as a CSV file for offline analysis or reporting.

- Review the specific engine and algorithm settings used for each test case execution. This information helps developers optimize the AI agent's performance.

- To view the advanced algorithm configuration settings used for a particular training engine, click the Info icon next to the training engine name. This provides insights into the parameters and settings that influenced the AI agent's behavior during testing.

<a id="concept-template_edb280bf-311f-4a59-981b-27e4d0190228"></a>

#### View agent sessions

The Sessions section provides a comprehensive record of all interactions between AI agents and customers. Each session includes a detailed history of messages exchanged. You can export session data as a CSV file for offline analysis and auditing. Use this data to analyze user interactions, identify areas for improvement, and refine AI agent responses.

It can handle large data sets by displaying results on pages. You can use the Refine Results section to filter and sort sessions based on various criteria. Each row in the table displays essential session details, including:

- **Channels**—The channel where the interaction occurred (for example, chat, voice).

- **Session ID**—A unique identifier for the session.

- **Consumer ID**—The unique identifier of the user.

- **Messages**—The number of messages exchanged during the session.

- **Updated at**—The last updated system time.

- **Metadata**—Additional information about the session.
  
  - **Hide test sessions**—Check this check box to hide the test sessions and display only the list of live sessions.
  
  - **Agent handover happened**—Check this check box to filter sessions that we hand over to an agent. If agent handover happens, it displays the headphone icon indicating the handover of the chat to a human agent.
  
  - **Error occurred**—Check this check box to filter the sessions in which an error occurred.
  
  - **Downvoted**—Check this check box to filter the downvoted sessions.

Click on a row to access the detailed view of a specific session. Use check boxes to filter sessions based on agent handover, errors, and downvotes. Decrypting sessions requires user-level permission and advanced data protection settings. Click Decrypt content to view the session details.

<a id="section_w2r_bvw_1dc"></a>

##### View session details in the scripted AI agent

Click the session in each row to view the individual session details.

The Transaction Info tab provides a detailed breakdown of a specific interaction, categorizing information into four sections:

The **Messages** section:

- Shows a transcript of all session interactions in chronological order, providing context for the conversation.
  
  AI Agent transcripts are stored for 90 days before being automatically purged.

- Shows the corresponding responses generated by the AI Agent.

- Shows the recording playback modal (along with the session transcript) for conversations between the AI agent and the customer. Recordings are available only for voice sessions, not chat sessions. You can play the recording from the beginning or jump to a specific point. 
  
  The recording playback modal provides a suite of audio controls:
  
  - **Play/Pause**: Click  to start listening to the interaction session and click  to pause the recording playback.
  
  - **Playback speed**: Click 1X to adjust the audio playback speed, ranging from 0.5X to 2X.
  
  - **Sound control**: Click  to mute or unmute the sound of the audio during playback. You can also use the volume slider to adjust the playback volume.

  - When conversations contain PCI data, the system enforces enhanced security measures. Depending on the scenario:

    - If PCI data is detected, the playback modal for the recording is disabled in the session view, preventing access to the audio.
    
    - When using secure entities, recording is automatically muted during the portions where PCI data is present, ensuring sensitive information is not audible.
  
  - When a call is escalated from an AI agent to a human agent, and the human agent then consults back to the same or another AI agent, the recording of the consulted leg is currently not supported.

The Intents Identified section:

- Displays the intents identified for the customer's query.

- Indicates the confidence level associated with each identified intent.

- Lists the slots that are associated with the identified intent. Click the slot to view additional information about its value and how the system extracts it from the user's query.

Entities Identified section lists the entities that the system extracts from the customer's message and associates it with the active consumer intent. These entities represent the key pieces of information that the AI Agent identified within the user's query.

The **Algorithm Results** section provides insights into the underlying processes that led to the AI Agent's response. Here's a breakdown of the information displayed:

- **List of Intents**—Shows the identified intents and their corresponding similarity scores.

- **Entity List**—Displays the entities that were extracted from the user's message.

The **Other Info** displays:

- **Processed Query**—Indicates the preprocessed version of the customer's input after the AI Agent's natural language understanding (NLU) pipeline processes it.

- **Language detection provider**—The provider who offers technology that can automatically identify the language of a given text.

- **Language detected**—The language detected by technology.

- **Agent Handover**—Indicates whether an agent handover occurred during the session. Check the Agent Handover by Rules check box if an agent handover was triggered by specific rules.

- **Template Key**—Indicates the template key associated with the intent that triggered the AI agent's response.

- **Response Type**—Indicates the type of response generated by the AI agent.

- **Response Condition**—Indicates the specific condition or rule that triggered the AI agent's response.

- **NLU AI Engine**—Identifies the NLU AI engine used to process the customer's query.

- **Vector model**—A way of representing text as numerical vectors.

- **Min threshold Scores**—Displays the minimum threshold score.

- **Partial match score difference**—The partial match score difference configured in the **Handover and Inference** settings. The system determines whether a query is out of scope or requires agent intervention based on these values.

- **Debug Logs**—Provides a list of debug logs associated with the specific transaction ID. Advanced logs are typically retained for 180 days.

You can also download and view the transaction info in the JSON format using the download option.

<a id="concept-template_6f7b8836-c807-4c55-9c37-2f2a67cf429e"></a>

#### View version history and change logs

Whenever you add or update intents or entities, the system retrains your scripted AI agent to keep it up to date. After each training session, test your AI agent thoroughly to ensure accuracy and effectiveness. Each time you publish a scripted AI agent, a version is saved and accessible in the **Version History** tab, where you can view all versions of the scripted AI agent.

The **History** page allows you to access the following updates made to your agents:

- Track when you published the version history and the changes made in the form of a note left by developers when publishing.
 
- View the AI engine used for each published version, along with its settings. You can also see the time elapsed to get each version ready to publish.
 
- Monitor changes to settings, intents, entities, responses, and curation in the **Change logs** tab.
 
- Publish, Preview, or Load an older version as draft if needed.
 
- **View Training History**—Track when you trained a corpus and the changes made.
 
- **Compare Training Engines**—Review the training engines used for different iterations and their corresponding training durations.
 
- **Track changes**—Monitor changes to settings, intents, responses, and curation.
 
- **Revert to previous versions**—Easily revert to an older training set if needed.

<a id="section_ik3_fvw_1dc"></a>

##### Change Logs

The Change Logs section provides a detailed record of modifications made to your scripted AI agent. To access change logs:

- Navigate to the **Dashboard** and click the AI agent that you've created.

- Click the Version History tab to view the AI agent's history.

- Click the Change Logs tab to see a detailed log of changes:
  
  - **Updated at**—The date and time the system made the change.
  
  - **Updated by**—The user who made the change.
  
  - **Change Location**—The section of the AI agent where the modification occurred (for example, Corpus, Intent, and Response).
  
  - **Description**—Additional details about the change.

- Use the `Updated by` and `Change Location` search options to find specific change log entries.

- The Version History tab displays a maximum of 10 corpora for each AI agent.

<a id="concept-template_926ff668-f78c-491f-bda5-0268609bab8c"></a>

#### Curate scripted AI agent

The system adds messages to the Curation console based on the following criteria:

- Fallback Messages—When the AI agent fails to understand your message and triggers the fallback intent.
 
- **Downvoted Messages**—Messages that users have downvoted during AI agent previews.
 
- **Agent Handover**—Messages that result in a human agent handover due to configured rules.
 
- **From Session**—Messages flagged by users as not receiving the desired response from session or room data.
 
- **Low Confidence**—Messages with a confidence score falling within the specified low-confidence threshold.
 
- **Partial Match**—Messages where the AI agent couldn't figure out the right intent or response.

<a id="section_uzj_s5w_1dc"></a>

##### Resolve issues

The Issues tab allows you to review and address messages flagged for curation. You can do the following:

- Choose to resolve or ignore issues based on their severity and relevance.

- Examine the original user utterance, the AI Agent's response, and any attached media.

You can view the full content of encrypted sessions by using the Decrypt Content option, if you’ve decrypt access enabled.

If the **Advanced Data Protection** is enabled in the backend, the system grants the decrypted access at the user level.

To resolve an issue, you can:

- **Link to an existing intent**—To connect an issue to an existing intent, select the Link option and search for the desired intent.

- **Add to a new intent**—Use the Add to a New Intent option to create a new intent directly from the Curation Console.

- **Ignore issues**—Resolve or ignore issues to remove them from the Curation Console.

- You can't link to default intents (welcome message, fallback message, partial match).

- For a scripted AI agent, select the appropriate intent from the drop-down list and tag any relevant entities.

- After making changes, the system retrains your AI agent to ensure that it reflects the new knowledge in its responses.

- Resolve or ignore multiple issues simultaneously for efficient management.

The Resolved tab displays all issues addressed by the system. You can view a summary of each resolved issue, including whether we linked it to an existing intent, created a new intent, or ignored it. If you see responses that you don't like that the system didn't catch, you can manually add specific examples to the Curation Console.

To add issues from sessions:

- **Identify the Utterance**—Locate the utterance that triggered the incorrect response.

- **Check Curation Status**—If the issue isn't already in the Curation Console, the system displays the `Curation Status` toggle.

- **Toggle the Flag**—Enable the `Curation Status` toggle to add the utterance to the Curation Console for review and resolution.

If the issue is already in the Curation Console, the toggle's appearance changes to show its status.

<a id="concept-template_cb93923b-e1b2-4803-a125-4b336d4580fd"></a>

### View your scripted AI agent performance using Analytics

The **Analytics** section provides a graphical representation of key metrics to evaluate the AI agent performance and effectiveness. The key metrics are divided into four sections represented as tabs, namely Overview, Responses, Training, and Curation.

On the Analytics page, you can select the AI agent you want to see the analytics for. You can customize the analytics view by choosing the channel, date range, and data granularity. By default, the system displays analytics data for the last month for all channels, with each day as a data point.

<a id="section_uvx_lzp_wcc"></a>

#### Overview

The overview contains key metrics and graphs that provide a snapshot of overall AI agent usage and performance to the developers.

- From the **Dashboard**, choose the AI agent that you've created.

- On the left navigation pane, click **Analytics**. An overview of the AI agent performance appears in both tabular format and graphical representation.

**Sessions and messages**

The first section in the overview displays the following statistics about sessions and messages for the AI agent:

- The count of the total sessions and the sessions that the AI agent handles without human intervention.

- Total agent handovers, which is a count of the number of sessions handed over to human agents.

- Daily average sessions

- Total messages (human and AI agent messages) and how many of those messages came from users.

- Daily average messages

The system follows this with a graphical representation of sessions (stacked column representing sessions handled by the AI agent and sessions handed over) and the total responses sent out by the AI agent.

**Users**

The second section in the overview contains stats about users for the AI agent. It provides a count of total users and information about average sessions per user and daily average users. This is followed by a graph displaying new and returning users for each unit depending on the selected granularity.

**Performance**

The third section provides statistics about the AI agent’s responses to users. Here one can see the total responses sent out by the AI agent and the split up between responses where the AI agent:

- Identified the user’s intent.

- Responded with a fallback message.

- Responded with a partial match message.

- Informed the user of an agent handover.

The same is aggregated in a pie chart and an area graph provides information based on selected granularity.

<a id="section_csm_vw5_1dc"></a>

#### Training

The training section represents of the ‘health’ of an AI agent corpus. It’s recommended that developers configure 20+ training utterances for each intent in their AI Agents. This section displays all intents as rectangles, with color and size indicating the amount of training data. The closer an intent is to white color, the more training data it needs for your AI Agent’s accuracy to improve.

<a id="section_vch_vzp_wcc"></a>

#### Responses

This section gives a detailed view of what the customers are asking about and how often they are asking it. It graphically shows the most popular intents for AI agents for answering questions and response templates for AI Agents for performing actions.

This section provides a detailed view of customer inquiries and their frequency. It visually displays the most popular intents and response types that AI agents use to solve customer queries.

<a id="section_j5x_11q_wcc"></a>

#### Curation

This section visually summarizes the number of curation issues that arise each day and the number that AI agents resolve.

<a id="content"></a>

<a id="concept-template_5c92bed9-7ad7-4117-a0ef-06ac55bf181e"></a>

This section outlines how to integrate AI agents with both voice and digital channels to manage customer conversations.

<a id="generic-template_43f4e186-63f4-4ed0-b4cd-aa2b6aea7485"></a>

### Use AI agents for voice and digital interactions

After you've created and configured your autonomous or scripted AI agents in the Webex AI Agent Studio platform, the next step is to integrate them with the voice and digital channels. This integration allows the AI agents to handle both voice-based and digital conversations with your customers, providing a seamless and interactive user experience.

For more information, see [Use AI agents for voice and digital interactions](https://help.webex.com/article/s0qro1) article.

<a id="content"></a>

<a id="generic-template_fd16b670-22d3-4677-b46f-23d5baa1464f"></a>

You can use global variables to generate custom reports and analyze calls routed to the AI agent.

Currently, out-of-the-box reports for the AI agent are not available in Analyzer.

<a id="task-template_eef8283c-fed9-4307-b1f7-b6d3aabd7a50"></a>

### Create a global variable

|  |  |
| --- | --- |
| 1 | Sign in to [Control Hub](https://admin.webex.com/login). |
| 2 | From the Contact Center navigation pane, choose Flows > Global Variables. |
| 3 | Click Create a new global variable and provide the name and description for the variable. Create a variable with the name CustomAIAgentInteractionOutcome. Choose String as the variable type. |
| 4 | Toggle Make Reportable on to display the variable in Analyzer for reporting purposes. |
| 5 | Click Save. |

<a id="task-template_18604dde-7538-40df-8cc7-0dddb72522d9"></a>

### Add the global variable to the flow

The following instructions are also available within the linked sample flow import.

|  |  |
| --- | --- |
| 1 | Sign in to your customer organization using [Control Hub](https://admin.webex.com/login). |
| 2 | Navigate to Contact Center > Customer Experience > Flows. The Flows page appears. |
| 3 | Click the Go to Flow Designer icon beside the flow. The Flow Designer window appears. |
| 4 | In the Global Flow Properties pane, scroll down to Variable Definition > Predefined Variables section. |
| 5 | In the Global Variables section, click Add Global Variables. Add the global variable CustomAIAgentInteractionOutcome to your flow. |
| 6 | Use the Set Variable  activity to assign the value **ABANDONED** to the variable CustomAIAgentInteractionOutcome. |
| 7 | Configure your Virtual Agent V2 activity in the flow. |
| 8 | Connect the Handled outcome of the Virtual Agent V2 Activity and use the Set Variable  activity to assign the value **HANDLED**to the variable CustomAIAgentInteractionOutcome. |
| 9 | Connect the Escalated outcome of the Virtual Agent V2  activity and use the Set Variable  activity to assign the value **ESCALATED** to the variable CustomAIAgentInteractionOutcome. |
| 10 | Connect the errored path of the Virtual Agent V2  activity and use the Set Variable  activity to assign the value **ERRORED** to the variable CustomAIAgentInteractionOutcome. |
| 11 | Complete the rest of the flows based on your business logic and publish them. Any calls going through this flow will have the value of the variable CustomAIAgentInteractionOutcome set to **Abandoned**, **Handled**, **Escalated** or **Errored**, depending on the path the call takes. |

<a id="concept-template_23fb6bf7-93d0-4982-a3c4-ee4d5d225b01"></a>

### Create custom visualizations

You can create custom reports for AI agent call records and AI agent outcome distribution in Analyzer.

<a id="task-template_d96eff43-5b5b-495c-82ee-870e19b2292b"></a>

#### Create AI Agent Call Records visualization

<a id="steps_qvd_yvk_g2c"></a>

|  |  |
| --- | --- |
| 1 | Download the **AI Agent Call Records.json** file from [AI Agent Call Records](https://github.com/WebexSamples/webex-contact-center-api-samples/blob/main/Custom%20Reports%20for%20AI%20Agents%20/AI%20Agent%20Call%20Records.json). |
| 2 | Log in to Analyzer. |
| 3 | On the Home page, click the Visualization icon in Analyzer. |
| 4 | Click Import. |
| 5 | Click Browse to select the file (.json format) to be imported. |
| 6 | Click Import to import the **AI Agent Call Records.json** file. |
| 7 | Click Edit to modify the imported Visualization. |
| 8 | Click on Edit Filters for CustomAIAgentInteractionOutcome. |
| 9 | Click the is in radio button and add the values ABANDONED, ESCALATED, ERRORED, HANDLED. |
| 10 | Save and initiate a few test calls. |
| 11 | Run the visualization to view the results. |

<a id="task-template_c0ce4cb2-9244-422c-92a0-06e2919095fc"></a>

#### Create AI Agent Outcome Distribution visualization

|  |  |
| --- | --- |
| 1 | Download the **AI Agent Outcome Distribution.json** file from [AI Agent Outcome Distribution](https://github.com/WebexSamples/webex-contact-center-api-samples/blob/main/Custom%20Reports%20for%20AI%20Agents%20/AI%20Agent%20Outcome%20Distribution.json). |
| 2 | Log in to Analyzer. |
| 3 | On the home page, click the Visualization icon in Analyzer. |
| 4 | Click Import. |
| 5 | Click Browse  to choose the file (in JSON format) to be imported. |
| 6 | Click Import to import the **AI Agent Outcome Distribution.json** file. |
| 7 | Click Edit  to modify the imported Visualization. |
| 8 | Click on Edit Filters for CustomAIAgentInteractionOutcome. |
| 9 | Click the is in radio button and add the values ABANDONED, ESCALATED, ERRORED, HANDLED. |
| 10 | Save and initiate a few test calls. |
| 11 | Run the visualization to view the results. |

<a id="content"></a>

<a id="concept-template_e2b4da7c-fb4c-4354-bf5e-92da5a0748e0"></a>

### Understand AI transparency for AI agents

Many regions require organizations to notify users when providing AI services, for example, [The EU Artificial Intelligence Act](https://artificialintelligenceact.eu/) in Europe. AI transparency lets you tell customers when they are interacting with an AI agent before the conversation continues. This disclosure applies for both scripted and autonomous AI agents, works across supported voice and digital channels, and can be previewed with the existing welcome experience in the AI Agent Studio user interface.

#### How AI transparency works

Use the AI transparency settings in the agent profile to control the customer-facing disclosure message.

- Autonomous AI agents use the transparency note like a welcome message setting. For more information, see [Update autonomous AI agent profile](https://help.webex.com/en-us/article/preview/ncs9r37/Webex-AI-Agent-Studio-Administration-guide#task-template_5416be2f-b95e-4b80-bebc-3fa8201414bf).

- Scripted AI agents let you configure language-specific transparency notes and fall back to the default note when a language-specific message is unavailable. For more information, see [Update scripted AI agent profile](https://help.webex.com/en-us/article/preview/ncs9r37/Webex-AI-Agent-Studio-Administration-guide#task-template_c7edf167-b532-4222-b464-d54ad1d8b893).

- **In European regions**: This feature is enabled by default. A transparency message will play or appear (depending on the channel) for all agent types. To disable this feature, you must acknowledge the risks and add audit comments before opting out.

- **In all other regions**: You can choose whether to enable the feature and configure the message as needed. Cisco recommends enabling AI transparency as a best practice to help ensure end users are informed when interacting with AI agents.

#### Channel behavior

- For voice interactions, the transparency note plays before the welcome message and callers cannot interrupt it.

- For digital interactions, the transparency note is added to the first AI-generated response in the session.

#### What to review before you publish

- Review the default transparency message ensuring that the wording clearly identifies AI interaction.

- Limit it to 200 characters.

- Make sure the message matches your organization's legal and brand guidance.

- Preview the disclosure in each supported channel and language.

- If you turn off AI transparency, acknowledge the warning and provide a reason.

- Make sure to have AI disclosure language, such as "I am an AI assistant", "I am an AI agent" as a prefix for your branding changes.

<a id="reference-template_974fb480-6259-4175-abe7-a660e2cc9868"></a>

### **AI development, data privacy, security, and safety**

**AI Product Development** 

For every AI-powered feature, we undergo an AI Impact Assessment against our [Responsible AI principles](https://www.cisco.com/c/dam/en_us/about/doing_business/trust-center/docs/cisco-responsible-artificial-intelligence-principles.pdf?CCID=cc000742&DTID=odicdc000016), and adhere to the [Responsible AI Framework](https://www.cisco.com/c/dam/en_us/about/doing_business/trust-center/docs/cisco-responsible-artificial-intelligence-framework.pdf), in addition to existing Security, Privacy, and Human Rights by Design processes.

 **Privacy and Security** 

We don’t retain customer input data after the inference process, and the third-party model provider, Microsoft, doesn’t access, monitor, or store Cisco customer data. For more detail on feature-specific data retention policies, see [Webex AI Agent AI transparency technical note](https://trustportal.cisco.com/c/r/ctp/trust-portal.html?search_keyword=webex%20ai%20agent#/19445370048945010) in the Cisco Trust Portal.

 **Data Sources for Training and Evaluation** 

Our third-party model provider, Microsoft doesn't use customer content to improve Azure OpenAI models and doesn’t store or retain Cisco customer data in Azure infrastructure.

 **Safety and Ethical Considerations** 

All generative AI features are prone to errors, so we prioritize content safety for AI features by opting in to [Content filtering](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/content-filter?tabs=warning%2Cpython-new), provided by Azure OpenAI.

 **Model Evaluation and Performance** 

We prioritize the performance and accuracy of AI Assistant by involving humans in the review, testing, and quality assurance of the underlying model.
