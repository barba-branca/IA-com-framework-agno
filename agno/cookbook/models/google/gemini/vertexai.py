from agno.agent import Agent
from agno.models.google import Gemini
import os

# Check if GOOGLE_API_KEY is set
google_api_key = os.environ.get("GOOGLE_API_KEY")
if google_api_key:
    print(f"GOOGLE_API_KEY: {google_api_key[:10]}... (configured)")
else:
    print("⚠️  GOOGLE_API_KEY environment variable is not set!")
    print("Please set it with: export GOOGLE_API_KEY=your_api_key_here")

agent = Agent(
    model=Gemini(id="gemini-2.0-flash"),
    markdown=True
)


# Get the response in a variable
# run: RunResponse = agent.run("Share a 2 sentence horror story")
# print(run.content)

# Print the response in the terminal
agent.print_response("Share a 2 sentence horror story")
