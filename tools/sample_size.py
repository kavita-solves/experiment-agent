import math
from scipy import stats
from langchain.tools import tool


@tool
def calculate_sample_size_proportion(
    baseline_rate: float,
    mde: float,
    daily_traffic: int,
    split: float = -1 , # -1 = not provided
    power: float = 0.80,
    significance: float = 0.05
) -> dict:
    """Calculate sample size for proportion metrics like
    conversion rate, open rate, click rate.
    
    IMPORTANT: split parameter is required — no default value.
    split = fraction of users seeing NEW experience (treatment).
    Example: 50/50 split → split=0.5, 80/20 split → split=0.8
    
    Always ask PM for split before calling this tool.
    Never assume split=0.5 without confirming with PM.
    """
    if split == -1:
        return {
            "error": "Split not provided. Please ask PM: What percentage of users should see the new experience? Options: 10%, 20%, 50%, 80%"
        }

    z_alpha = stats.norm.ppf(1 - significance / 2)
    z_beta = stats.norm.ppf(power)

    p1 = baseline_rate
    p2 = baseline_rate + mde

    n = (
        (z_alpha + z_beta) ** 2 *
        (p1 * (1 - p1) / split + p2 * (1 - p2) / (1 - split))
    ) / (mde ** 2)

    minimum_duration = 7 # minimum 7 days - seasonality cover karne ke liye
    calc_duration = math.ceil(math.ceil(n * 2) / daily_traffic) # calculated duration based on the inputs
    duration = max(calc_duration, minimum_duration)

    return {
        "sample_per_variant": math.ceil(n),
        "total_sample": math.ceil(n) * 2,
        "baseline_rate": f"{p1 * 100:.2f}%",
        "target_rate": f"{p2 * 100:.2f}%",
        "duration_days": duration,
        "duration_note": "Minimum 7 days recommended to account for weekly seasonality effects.",
        "statistical_power": f"{power*100:.0f}%",
        "significance_level": f"{(1-significance)*100:.0f}%",
        "mde": f"{mde*100:.2f}%"
    }


@tool
def calculate_sample_size_continuous(
    mean: float,
    std_dev: float,
    mde_abs: float,
    daily_traffic: int,
    power: float = 0.80,
    significance: float = 0.05
) -> dict:
    """Calculate sample size for continuous metrics like
    revenue per user, session duration, order value."""

    z_alpha = stats.norm.ppf(1 - significance / 2)
    z_beta = stats.norm.ppf(power)

    n = (
        2 * (std_dev ** 2) * (z_alpha + z_beta) ** 2
    ) / (mde_abs ** 2)

    minimum_duration = 7 # minimum 7 days - seasonality cover karne ke liye
    calc_duration = math.ceil(math.ceil(n * 2) / daily_traffic) # calculated duration based on the inputs
    duration = max(calc_duration, minimum_duration)

    return {
        "sample_per_variant": math.ceil(n),
        "total_sample": math.ceil(n) * 2,
        "baseline_mean": mean,
        "target_mean": mean + mde_abs,
        "std_dev_used": std_dev,
        "duration_days": duration,
        "duration_note": "Minimum 7 days recommended to account for weekly seasonality effects.",
        "statistical_power": f"{power*100:.0f}%",
        "significance_level": f"{(1-significance)*100:.0f}%",
        "mde": f"{mde*100:.2f}%"
    }