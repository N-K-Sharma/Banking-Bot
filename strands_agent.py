
from strands import Agent, tool
from strands_tools import calculator, current_time

@tool
def calculate_emi(principal: float, rate: float, tenure: int) -> str:
    """Calculate EMI for a loan."""
    monthly_rate = rate / (12 * 100)
    emi = (principal * monthly_rate * (1 + monthly_rate)**tenure) / ((1 + monthly_rate)**tenure - 1)
    return f"Your EMI is ₹{emi:.2f} for {tenure} months."

banking_agent = Agent(
    system_prompt="""You are BankingBot, a helpful assistant for banking queries.
    You can answer FAQs, calculate EMI, and provide financial tips.""",
    tools=[calculator, current_time, calculate_emi]
)

def process_query(query: str) -> str:
    return banking_agent.run(query)
