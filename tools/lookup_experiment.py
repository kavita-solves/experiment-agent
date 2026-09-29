from langchain.tools import tool
from tools import detect_channel

PAST_EXPERIMENTS = [
    # --- Email ---
    {
        "id": "EXP-101",
        "channel": "Email",
        "primary_metric": "Open Rate",
        "change": "New subject line with personalization",
        "result": "+3.2pp Open Rate",
        "source": "SAMPLE DATA"
    },
    {
        "id": "EXP-102",
        "channel": "Email",
        "primary_metric": "CTR",
        "change": "New hero image in newsletter",
        "result": "+0.4pp CTR",
        "source": "SAMPLE DATA"
    },
    {
        "id": "EXP-111",
        "channel": "Email",
        "primary_metric": "Conversion Rate",
        "change": "Abandoned cart email sequence triggered within 2 hours",
        "result": "+2.4pp Conversion Rate",
        "source": "SAMPLE DATA"
    },

    # --- Push ---
    {
        "id": "EXP-103",
        "channel": "Push",
        "primary_metric": "App Opens",
        "change": "Re-engagement push for inactive users",
        "result": "+1.8pp App Opens",
        "source": "SAMPLE DATA"
    },
    {
        "id": "EXP-104",
        "channel": "Push",
        "primary_metric": "Reactivation Rate",
        "change": "Time-of-day send optimization",
        "result": "+0.9pp Reactivation Rate",
        "source": "SAMPLE DATA"
    },

    # --- SMS ---
    {
        "id": "EXP-105",
        "channel": "SMS",
        "primary_metric": "Click Rate",
        "change": "Shortened SMS copy with urgency framing",
        "result": "+1.1pp Click Rate",
        "source": "SAMPLE DATA"
    },
    {
        "id": "EXP-112",
        "channel": "SMS",
        "primary_metric": "Opt-out Rate",
        "change": "Reduced send frequency from 3x to 1x per week",
        "result": "-1.5pp Opt-out Rate",
        "source": "SAMPLE DATA"
    },

    # --- In-app ---
    {
        "id": "EXP-106",
        "channel": "In-app",
        "primary_metric": "Checkout Conversion Rate",
        "change": "Redesigned checkout button placement",
        "result": "+2.1pp Checkout CVR",
        "source": "SAMPLE DATA"
    },
    {
        "id": "EXP-107",
        "channel": "In-app",
        "primary_metric": "Feature Adoption Rate",
        "change": "New onboarding tooltip for a core feature",
        "result": "+4.5pp Feature Adoption",
        "source": "SAMPLE DATA"
    },
    {
        "id": "EXP-113",
        "channel": "In-app",
        "primary_metric": "Day-7 Retention",
        "change": "Gamified progress bar during initial app setup",
        "result": "+3.1pp Day-7 Retention",
        "source": "SAMPLE DATA"
    },

    # --- Web ---
    {
        "id": "EXP-108",
        "channel": "Web",
        "primary_metric": "Sign-up Rate",
        "change": "Simplified landing page form (5 fields to 2)",
        "result": "+1.6pp Sign-up Rate",
        "source": "SAMPLE DATA"
    },
    {
        "id": "EXP-109",
        "channel": "Web",
        "primary_metric": "Purchase Conversion Rate",
        "change": "Price-anchoring test on pricing page",
        "result": "+0.7pp Purchase CVR",
        "source": "SAMPLE DATA"
    },
    {
        "id": "EXP-114",
        "channel": "Web",
        "primary_metric": "Bounce Rate",
        "change": "Added customer trust badges above the fold",
        "result": "-3.8pp Bounce Rate",
        "source": "SAMPLE DATA"
    },

    # --- Paid ---
    {
        "id": "EXP-110",
        "channel": "Paid",
        "primary_metric": "Install Rate",
        "change": "New ad creative for acquisition campaign",
        "result": "-0.2pp Install Rate (not significant)",
        "source": "SAMPLE DATA"
    },
    {
        "id": "EXP-115",
        "channel": "Paid",
        "primary_metric": "CPA",
        "change": "Dynamic search ads targeted at high-intent keywords",
        "result": "-12.0% CPA",
        "source": "SAMPLE DATA"
    }
]

@tool
def lookup_past_experiments( description: str, experiment_type: str, metric: str = None) ->list:
    """
    Search historical experiment records using experiment_type and description to infer channel,
    and optional primary metric to ground design recommendations on real past evidence.
    """

    channel = detect_channel.invoke({"description": description, "experiment_type" :experiment_type} )
    if channel == "Unclear": 
        return [{"message": "Channel is unclear from description. Please ask user whether this experiment is for Web, In-app, Email, Push, SMS, or Paid."}]
    results = []
    metric_clean = metric.lower().strip() if metric else None

    for exp in PAST_EXPERIMENTS:
        if exp["channel"].lower()== channel.lower():
            if metric_clean and metric_clean not in exp["primary_metric"].lower():
                continue
            results.append(exp)
    if not results:
        return [{"message":f"No past experiment found for channel '{channel}'"}]

    return results