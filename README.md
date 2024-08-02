Multi-Agent AI System for Company Strategy and Product Development
Welcome to the Multi-Agent AI System! This Python-based application leverages the power of AI to create a comprehensive strategy and development plan for a company’s new product. Below is a detailed guide on what this system does, how to provide the necessary inputs, and how to run the code.

![Untitled](https://github.com/user-attachments/assets/82592bdb-57ba-4cd6-ad2e-d3dbb647d8a9)

Overview
This system utilizes a multi-agent approach to perform the following tasks:

Determine the overall company strategy.
Develop a new AI product with a detailed roadmap.
Plan and execute a marketing campaign.
Create and implement a sales strategy.
The system uses advanced AI tools from CrewAI and LangChain, including the Ollama language model and various data processing tools, to achieve these goals.

Prerequisites
Python Environment: Ensure you have Python installed (version 3.8 or higher recommended).
Libraries: Install the required Python libraries. Run the following command:
bash
Kodu kopyala
pip install python-dotenv crewai crewai-tools langchain-community markdown pdfkit
wkhtmltopdf: Install wkhtmltopdf to convert Markdown files to PDF. Download it from wkhtmltopdf.org and ensure it is installed at C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe. Update the path in the convert_markdown_to_pdf function if necessary.
Configuration
Environment Variables: Create a .env file in the same directory as your script with the following content:

makefile
Kodu kopyala
SERPER_API_KEY=your_serper_api_key
COMPANY_DOCUMENT_PATH=path_to_your_company_document
Replace Placeholders: Edit the inputs dictionary in the script with your specific values:

python
Kodu kopyala
inputs = {
    "company_name": "Your Company Name",
    "vision": "Your vision statement here.",
    "product_name": "Your Product Name",
    "product_features": "Key features of the product.",
    "target_market": "Target market for the product.",
    "marketing_channels": "Marketing channels to be used.",
    "sales_targets": "Sales targets for the product."
}
Running the Code
Script Execution: Run the script by executing:

bash
Kodu kopyala
python your_script_name.py
Output: The script will generate a Markdown file with the sales strategy and convert it to a PDF file saved in the output directory.

Code Details
Main Components
Agent Definitions: Four agents are defined—CEO, CTO, Marketing Manager, and Sales Manager. Each agent is assigned specific tasks and goals.
Tasks: Tasks are defined with descriptions, expected outputs, and associated agents.
Crew Creation: The create_crew function initializes a crew with agents and tasks and executes them sequentially.
Markdown to PDF Conversion: The convert_markdown_to_pdf function converts the resulting Markdown file into a PDF format.
Example Input Configuration
Adjust the following inputs to match your specific scenario:

python
Kodu kopyala
inputs = {
    "company_name": "AI Solutions Inc.",
    "vision": "To lead the AI industry by delivering cutting-edge products that revolutionize how businesses operate.",
    "product_name": "AI Assistant Pro",
    "product_features": "Real-time data processing, natural language understanding, and predictive analytics.",
    "target_market": "Small to medium-sized enterprises (SMEs) in the technology sector.",
    "marketing_channels": "Social media, email marketing, and industry events.",
    "sales_targets": "Achieve $10M in revenue within the first year of launch."
}
Running the Simulation
Initialize Crew: Use the create_crew function to create and start the crew process with your inputs.
View Results: Check the output directory for the generated Markdown and PDF files.
Troubleshooting
wkhtmltopdf Not Found: Ensure wkhtmltopdf is installed correctly and the path is set in the script.
Environment Variables: Verify that your .env file contains the correct API keys and file paths.
Feel free to reach out for any additional questions or support. Enjoy your AI-powered strategy and development planning!






