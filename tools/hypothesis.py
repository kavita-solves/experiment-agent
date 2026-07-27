from langchain.tools import tool
from langchain.chat_models import init_chat_model
from pydantic import BaseModel

class structured_hypothesis(BaseModel):
    Problem_statement: str
    Null_Hypothesis: str
    Alternate_Hypothesis: str

@tool
def exp_hypothesis(description: str,
  experiment_type: str,
  channel_type: str,
  primary_metric: str) -> dict:
    """Generate null and alternative hypothesis for the experiment."""
    
    model=init_chat_model (
        model = "gpt-5-nano",
        response_format = structured_hypothesis
    )
    prompt = f"""
    Write a clear problem statement, Null hypothesis and alternative hypothesis for:
    Experiment: {description}
    type: {experiment_type}
    channel: {channel_type}
    primary_metric: {primary_metric}
    """
    response=model.invoke(prompt)
    return response.dict()
    
