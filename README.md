# Experiment Agent

AI-powered experimentation assistant that helps PMs and Marketers design rigorous A/B tests and holdout experiments — no data science degree needed.

## What It Does

You describe your experiment in plain English. The agent asks the right questions and produces a complete experiment design including:

- Problem Statement
- Null & Alternative Hypothesis
- Power Analysis (sample size, duration, confidence level)
- Experiment Setup (split, eligibility, guardrail metrics)
- Opportunity Cost (for holdout experiments)

## Demo

[Screenshot or GIF here]

## Tech Stack

- **LangChain** — Agent orchestration
- **GPT-4o** — Conversation & hypothesis generation
- **Streamlit** — UI
- **Python** — Sample size calculations (scipy)

## Architecture

User Input (Streamlit)

↓

Agent (GPT-4o + LangChain)

↓

Tools:

├── detect_experiment — Marketing or Product

├── detect_channel — Email, Push, Web, In-app

├── calculate_sample_size — Proportion & Continuous

├── exp_hypothesis — Null & Alternative hypothesis

└── calculate_opportunity_cost — Holdout experiments

↓
Experiment Design Output


## Supported Channels

- Email — Subject line, CTA, Hero image, Send time
- Push Notifications
- Web — Landing pages, Checkout flow
- In-app — Features, UI changes

## Setup

```bash
# Clone repo
git clone https://github.com/kavita-solves/experiment-agent.git
cd experiment-agent

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Add API keys
cp .env.example .env
# Edit .env with your OpenAI key

# Run
streamlit run app.py
```

## Known Limitations

- NovaMart context hardcoded (multi-tenant support coming)
- User level randomization only (Geo experiments coming)
- Marketing channels only for opportunity cost

## Built By

Kavita Malhotra — Staff Data Scientist
[LinkedIn](https://linkedin.com/in/kavita-malhotra-in)
[GitHub](https://github.com/kavita-solves)