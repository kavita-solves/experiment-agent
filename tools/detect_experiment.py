from langchain.tools import tool


@tool
def detect_experiment(description: str) -> str:
    """Detect if experiment is Marketing or Product based on PM's description.
    Marketing: email, push, SMS, paid ads, social
    Product: in-app changes, UI, features, onboarding"""
    description_l = description.lower()

    marketing_key  = [
         "email", "push", "sms", "notification", "paid",
        "ad", "campaign", "subject line", "open rate",
        "click rate", "unsubscribe", "newsletter",
        "hero image", "image", "visual", "banner",
        "creative", "design", "template"
    ]

    product_key = [
        "in-app", "feature", "ui", "button", "onboarding",
        "checkout", "landing page", "flow", "funnel",
        "signup", "registration", "dashboard"
    ]

    marketing_score = sum( 1 for k in marketing_key if k in description_l)
    product_score = sum( 1 for k in product_key if k in description_l)

    if marketing_score > product_score:
        return "Marketing"
    elif marketing_score < product_score:
        return "Product"
    else:
        return "Unclear"
    

@tool
def detect_channel(description:  str, experiment_type: str) -> str:
    """Detect the specific channel for the experiment.
    Marketing channels: Email, Push, SMS, Paid
    Product channels: Web, In-app"""

    

    description_l = description.lower()

    if experiment_type.lower() == "marketing":
        if any(k in description_l for k in ["email", "subject line", "newsletter","hero image"]):
            return "Email"
        elif any(k in description_l for k in ["push", "notification"]):
            return "Push"
        elif "sms" in description_l:
            return "SMS"
        elif any(k in description_l for k in ["paid", "ad", "social media"]):
            return "Paid"
        else:
            return "Unclear"
    else:
        if any(k in description_l for k in ["in-app", "feature", "button", "ui", " in-app checkout"]):
            return "In-app"
        elif any(k in description_l for k in ["web checkout", "landing", "web funnel", "web flow"]):
            return "Web"
        elif any(k in description_l for k in ["checkout", "funnel", "flow"]):
            return "Unclear - Web or In-app"
        else:
            return "Unclear"