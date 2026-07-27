from dataclasses import dataclass

@dataclass
class CompanyContext:
    company_name: str = "NovaMart"
    industry: str = "D2C E-commerce"
    primary_metrics: str = "CVR, AOV ,  cart abandonment , repeat purchase"
    avg_daily_traffic: int = 15000
    avg_email_list_size: int = 50000
    avg_email_open_rate: float = 0.22
    avg_email_click_through_rate: float = 0.20
    avg_conversion_rate: float = 0.032
    avg_order_value: float = 85.0
    vision: str = "Become the most customer-centric D2C brand in South Asia"

