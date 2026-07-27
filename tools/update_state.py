from langchain.tools import tool, ToolRuntime
from langgraph.types import Command
from langchain.messages import ToolMessage

@tool
def update_experiment_state(
    test_type: str = "",
    primary_metric: str = "",
    baseline_rate: float = 0.0,
    mde: float = 0.0,
    daily_traffic: int = 0,
    list_size: int = 0,
    duration_days: int = 0,
    split: float = 0.0,
    runtime: ToolRuntime = None
) -> Command:
    """Update experiment state with PM's answers.
    Call this tool whenever PM provides any of these values:
    - primary_metric: confirmed metric (e.g. CTR, Open Rate, CVR)
    - test_type: A/B test or Holdout
    - baseline_rate: current metric rate as decimal (e.g. 3% = 0.03)
    - mde: target improvement as decimal (e.g. 1% = 0.01)
    - list_size: email/push list size
    - daily_traffic: web/in-app daily visitors
    - split: treatment fraction (e.g. 50% = 0.5)
    """
    update = {}

    if primary_metric:
        update["primary_metric"] = primary_metric
    if test_type:
        update["test_type"] = test_type
    if baseline_rate > 0:
        update["baseline_rate"] = baseline_rate
    if mde > 0:
        update["mde"] = mde
    if list_size > 0:
        update["list_size"] = list_size
    if daily_traffic > 0:
        update["daily_traffic"] = daily_traffic
    if split > 0:
        update["split"] = split
    updates["messages"] = [ToolMessage(
        f"State updated : {updates}",
        tool_call_id = runtime.tool_call_id
    )]

    return Command(update=updates)