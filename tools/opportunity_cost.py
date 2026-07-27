from langchain.tools import tool
from langchain.chat_models import init_chat_model
from pydantic import BaseModel

@tool
def calculate_opportunity_cost(
    test_type: str,
    channel_type: str,
    holdout_size: int,
    duration_days: int,
    holdout_split: float,
    open_rate: float,
    ctr: float,
    conversion_rate: float,
    daily_traffic: int,
    aov: float
) ->dict:
    """Calculate opportunity cost for holdout experiments only.
        For A/B tests returns None — no opportunity cost.
        For Control experiments returns None — no opportunity cost.
        For email/push holdouts: uses list size, open rate, CTR, CVR, AOV.
        For web/in-app holdouts: uses daily traffic, holdout split, CVR, AOV, duration."""

    if any (k in test_type.lower() for k in ["a/b test","a/btest","a/b","control"]):
        op_cost = None
    else:
        if any (k in channel_type.lower() for k in ["email","push","sms"]):
            op_cost = holdout_size * open_rate * ctr * conversion_rate * aov
        elif any (k in channel_type.lower() for k in ["in-app","web"]):
            op_cost = holdout_split * daily_traffic * conversion_rate * aov * duration_days
    return {"opportuniyt_cost": op_cost }
