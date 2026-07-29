from dotenv import load_dotenv
load_dotenv()
from langchain.tools import tool
from langchain.chat_models import init_chat_model
from pydantic import BaseModel
from typing import List

class PrimaryMetric(BaseModel):
    metric: str
    reason: str
    what_it_measures: str

class Guardrail(BaseModel):
    metric: str
    reason: str
    failure_mode: str

class GuardrailPlan(BaseModel):
    experiment_surface: str
    likely_failure_modes: List[str]
    guardrails: List[Guardrail]

model = init_chat_model(model="gpt-4o")

@tool
def recommend_primary_metric(
    experiment_description: str,
    channel: str
) -> dict:
    """Recommend primary metric based on what is actually being tested.
    Never use a fixed channel-to-metric mapping.
    Always reason from what the experiment is trying to measure.
    Only suggest standard, measurable, commonly tracked metrics.
    Do NOT invent metrics."""

    prompt = f"""
    Analyze this experiment: {experiment_description}
    Channel: {channel}

    Recommend the single best primary metric to measure success.

    Rules:
    - Reason from what the experiment is actually trying to change
    - Do NOT choose metric based on channel alone
    - Consider the GOAL of the experiment:
        Examples (not rules):

            - Re-engagement campaigns:
                Primary metric should measure whether inactive users returned.
                Examples: Reactivation Rate, App Opens

            - Acquisition campaigns:
                Install Rate, Sign-up Rate

            - Checkout redesign:
                Checkout Conversion Rate

            - Pricing experiments:
                Purchase Conversion Rate

            - Feature launches:
                Feature Adoption Rate

            - Content engagement:
                Session Duration or Time on Page only when the goal is to deepen
                engagement after users have already entered the experience.
    - Session Duration is only appropriate when the goal is to DEEPEN 
    existing engagement, NOT to re-engage inactive users
    - Only suggest standard metrics: CVR, CTR, Open Rate, AOV, 
    Feature Adoption Rate, Session Duration, DAU, App Opens, 
    Retention Rate etc.
    - Do NOT invent new metrics
    - Explain why this metric best measures the goal
    - Explain what it actually measures in business terms
    """
    structured_model = model.with_structured_output(PrimaryMetric)
    result = structured_model.invoke(prompt)
    return result.dict()


@tool
def recommend_guardrails(
    experiment_description: str,
    primary_metric: str
) -> dict:
    """Recommend guardrail metrics based on experiment context and failure modes.
    Never use a fixed channel-to-guardrail mapping.
    Always reason from what could go wrong.
    Only suggest standard, measurable metrics.
    Do NOT invent metrics."""

    prompt = f"""
    Analyze this experiment:
    {experiment_description}
    Primary metric: {primary_metric}

    Identify:
    1. Experiment surface — what part of user journey is changing
    2. Likely failure modes — what could go wrong
    3. 2-3 guardrail metrics — each must detect a specific failure mode

    Rules:
    - Do NOT choose metrics based on channel alone
    - Each guardrail must map to a specific failure mode
    - Only suggest standard measurable metrics
    - Do NOT invent new metrics — use established ones like CVR, AOV, 
      bounce rate, cart abandonment rate, unsubscribe rate, opt-out rate, 
      session duration etc.
    - If unsure, suggest most conservative widely accepted metric
    """
    structured_model = model.with_structured_output(GuardrailPlan)
    result = structured_model.invoke(prompt)
    return result.dict()