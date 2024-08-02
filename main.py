from model import create_crew
from utils import convert_markdown_to_pdf

# Example of how you would pass inputs when kicking off the simulation
inputs = {
    "company_name": "AI Solutions Inc.",
    "vision": "To lead the AI industry by delivering cutting-edge products that revolutionize how businesses operate.",
    "product_name": "AI Assistant Pro",
    "product_features": "Real-time data processing, natural language understanding, and predictive analytics.",
    "target_market": "Small to medium-sized enterprises (SMEs) in the technology sector.",
    "marketing_channels": "Social media, email marketing, and industry events.",
    "sales_targets": "Achieve $10M in revenue within the first year of launch."
}

# Kick off the simulation with the inputs
result = create_crew().kickoff(inputs=inputs)
print(result)

# Convert the Markdown file to PDF
convert_markdown_to_pdf('output/suggestion.md', 'output/suggestion.pdf')