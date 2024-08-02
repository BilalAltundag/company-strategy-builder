import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool, FileReadTool
from langchain_community.llms import Ollama

# Load environment variables from .env file
load_dotenv()

# Set the API key for SerperDevTool using an environment variable
os.environ["SERPER_API_KEY"] = os.getenv('SERPER_API_KEY')

# Retrieve the path from environment variables
company_document_path = os.getenv('COMPANY_DOCUMENT_PATH')

# Initialize the tools
search_tool = SerperDevTool()
file_read_tool = FileReadTool(file_path=company_document_path)

# Initialize the language model
llm = Ollama(model="llama3.1", num_gpu=16)

# Define the agents with their respective roles and goals
ceo = Agent(
    role='CEO',
    goal='Determine the overall strategy for {company_name}. Just read the company document.',
    verbose=True,
    memory=True,
    backstory=(
        "As the visionary leader of {company_name}, your job is to make"
        " strategic decisions for the future of the company. Leading the way in"
        " innovative technologies and ensuring company growth are your top responsibilities."
    ),
    tools=[file_read_tool],
    llm=llm,
    allow_delegation=False,
    max_iter=3
)

cto = Agent(
    role='CTO',
    goal='Lead the development of the new AI product, {product_name}.',
    verbose=True,
    memory=True,
    backstory=(
        "As the technology leader at {company_name}, your job is to develop the new AI product."
        " Your technical expertise and innovative thinking will ensure the development of top-notch products."
    ),
    tools=[search_tool],
    llm=llm,
    allow_delegation=False,
    max_iter=3
)

marketing_manager = Agent(
    role='Marketing Manager',
    goal='Plan and execute the marketing campaign for {product_name}.',
    verbose=True,
    memory=True,
    backstory=(
        "As the marketing expert, your job is to launch {company_name}'s new product to the market."
        " With strategic thinking and creative campaigns, you will ensure the product is successfully introduced."
    ),
    llm=llm,
    allow_delegation=False,
    max_iter=3
)

sales_manager = Agent(
    role='Sales Manager',
    goal='Develop and implement the sales strategy for {product_name}.',
    verbose=True,
    memory=True,
    backstory=(
        "As the sales leader, your job is to bring {company_name}'s new AI product to customers."
        " Through effective sales strategies, you will ensure the product is well-positioned in the market."
    ),
    llm=llm,
    allow_delegation=False,
    max_iter=3
)

# Define the tasks with placeholders for dynamic content
strategy_task = Task(
    description=(
        "Determine the overall strategy for {company_name}. Focus on innovation and market leadership."
        " Your final answer MUST include a clear vision for the next 5 years: {vision}."
    ),
    expected_output='A comprehensive strategy document outlining the vision for the next 5 years.',
    agent=ceo
)

product_development_task = Task(
    description=(
        "Develop the new AI product, {product_name}, focusing on cutting-edge technology and user experience."
        " Include features such as {product_features}. Your final answer MUST include a detailed product development roadmap."
    ),
    expected_output='A complete product development roadmap with milestones and timelines.',
    agent=cto
)

marketing_campaign_task = Task(
    description=(
        "Plan and execute the marketing campaign for {product_name}."
        " Target market: {target_market}. Marketing channels: {marketing_channels}."
        " Your final answer MUST include a detailed marketing strategy and campaign plan."
    ),
    expected_output='A marketing campaign plan that outlines key strategies, target audience, and channels.',
    agent=marketing_manager
)

sales_strategy_task = Task(
    description=(
        "Develop and implement the sales strategy for {product_name}."
        " Your sales targets: {sales_targets}."
        " Your final answer MUST include a sales plan with targets and tactics."
    ),
    expected_output='A sales strategy document with detailed targets and tactics for market penetration.',
    agent=sales_manager,
    output_file='output/suggestion.md'
)

def create_crew():
    """ Create a crew model with agents and tasks executed sequentially.

    Returns:
        Crew: A Crew object with agents and tasks.
    """
    crew = Crew(
        agents=[ceo, cto, marketing_manager, sales_manager],
        tasks=[strategy_task, product_development_task, marketing_campaign_task, sales_strategy_task],
        process=Process.sequential  # Tasks will be executed sequentially
    )
    
    return crew
