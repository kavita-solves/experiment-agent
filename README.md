# 🧪 AI Experiment Design Copilot

> Helping teams design better experiments before implementation.

AI Experiment Design Copilot is an AI-powered assistant that helps Product Managers, Marketers, and Analysts design better experiments through a guided conversation.

Instead of filling in a static template, the agent asks follow-up questions, challenges ambiguous assumptions, performs statistical calculations, and produces a structured experiment brief in business language.

---

## Why I Built This

After spending 10+ years designing experiments across growth and marketing teams, I noticed the same pattern.

Coming up with an experiment idea is easy. Designing a rigorous experiment is much harder.

Before an experiment launches, teams often ask:

- Is this hypothesis measurable?
- Should this be an A/B test or a holdout?
- How much traffic do I need?
- How long should the experiment run?
- What should I measure?
- What happens if we hold users out?

These discussions almost always end up involving a data scientist or experimentation expert.

This project explores whether an AI assistant can guide those conversations while applying experimentation best practices.

---

## Who is this for?

This project is intended for:

• Product Managers validating experiment ideas before implementation.

• Growth Marketers planning campaign experiments.

• Data Scientists and Analysts looking for a structured starting point for experiment design.

• Teams aiming to standardize experimentation best practices.

---
## Demo

![Experiment Designer Demo](Experiment_agent_demo.gif)

---

## What the Agent Does
        Idea

        ↓

        Conversation

        ↓

        Clarifying Questions

        ↓

        Experiment Design

        ↓

        Statistics

        ↓

        Experiment Brief

The agent guides users through the complete experiment design process.

### 1. Understand the Business Problem

- Identifies the business objective
- Clarifies the experiment idea
- Determines the experiment type

---

### 2. Refine the Hypothesis

Generates:

- Problem Statement
- Null Hypothesis
- Alternative Hypothesis

while asking follow-up questions whenever assumptions are unclear.

---

### 3. Design the Experiment

Creates recommendations for:

- Treatment & Control groups
- Randomization strategy
- Eligibility criteria
- Primary metrics
- Guardrail metrics

---

### 4. Validate Statistical Feasibility

Calculates:

- Sample Size
- Minimum Detectable Effect (MDE)
- Statistical Power
- Confidence Level
- Estimated Experiment Duration

using deterministic Python calculations.

---

### 5. Review Business Considerations

For holdout experiments, the agent highlights key trade-offs such as:

- Users intentionally excluded from treatment
- Potential short-term business impact
- Assumptions to validate before launch

---

# Example Output

The final output includes:

- Business Problem
- Experiment Objective
- Null & Alternative Hypothesis
- Experiment Design
- Treatment & Control Setup
- Success Metrics
- Guardrail Metrics
- Sample Size
- Experiment Duration
- Opportunity Cost
- Recommendations & Design Risks

---

# Architecture

```
                User
                  │
                  ▼
            Streamlit UI
                  │
                  ▼
          LangChain Agent
                  │
      ┌───────────┼────────────┐
      ▼           ▼            ▼

 Experiment   Metric      Statistics
 Detection   Selection    Calculator

      ▼
 Structured Experiment Brief
```

---

# Current Capabilities

Design

✅ A/B Tests
✅ Holdout Tests
✅ Hypothesis Generation

Analysis

✅ Primary Metric Recommendation
✅ Guardrail Recommendation
✅ Sample Size
✅ Duration Estimation

Output

✅ Experiment Brief
✅ Business Recommendations

---

# Design Decisions

### Conversational instead of Forms

Rather than asking users to complete a long questionnaire, the agent dynamically asks only the questions required for the current experiment.

---

### Deterministic Statistics

Statistical calculations are performed in Python rather than by the LLM to ensure reproducible and mathematically correct outputs.

The LLM is responsible for reasoning.

Python is responsible for computation.

---

### Business-first Outputs

The goal isn't to teach statistics.

The goal is to help Product Managers and Marketers make better experimentation decisions.

Outputs are therefore written in business language instead of statistical jargon wherever possible.

---

# Tech Stack

- **LangChain** – Agent orchestration
- **OpenAI GPT-4o** – Experiment reasoning & conversation
- **Streamlit** – User Interface
- **Python** – Statistical calculations
- **SciPy** – Power analysis & sample size
- **Pandas** – Data processing
- **Pydantic** – Structured tool outputs

---

# Repository Highlights

```
experiment-agent/

├── app.py
│   ├── Main Streamlit interface
├── agent.py
│   ├── Conversation orchestration
├── tools/
│   ├── Statistical calculations & experiment logic
│
├── README.md
│   ├── Architecture and design
```

---

# Getting Started

```bash
git clone https://github.com/kavita-solves/experiment-agent.git

cd experiment-agent

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

cp .env.example .env

# Add your OpenAI API Key

streamlit run app.py
```

---

# Current Limitations

- Configured for a single business context
- User-level randomization only
- Opportunity cost currently supports marketing use cases
- Does not yet support Geo Experiments
- No experiment memory between sessions

---

# Roadmap

## Phase 2 — Smarter Experiment Planning

- Support Geo Experiments
- Company-specific experimentation guidelines
- Experiment history and search
- PDF export for sharing experiment briefs
- Multi-session conversation memory

## Phase 3 — Learning from Past Experiments

- Search similar historical experiments
- AI recommendations based on previous experiment outcomes
- Knowledge base of experimentation best practices
- Automatic experiment design review
- Company-specific experimentation playbooks

## Phase 4 — Advanced Experimentation

- Bayesian experiment design
- Sequential testing support
- Experiment results analyzer
- Power recalculation during an active experiment
- CUPED and variance reduction recommendations

---

# Lessons Learned

The hardest part wasn't building the agent.

It was deciding what should be deterministic and what should remain conversational.

Some tasks—such as hypothesis generation and follow-up questioning—benefit from an LLM.

Others—such as sample size calculation and statistical power—should remain deterministic.

Designing that boundary between LLM reasoning and deterministic computation turned out to be the most interesting part of the project.

---

# Built By

**Kavita Malhotra**

Staff Data Scientist with 10+ years of experience in experimentation,
growth measurement, and causal inference.

- 💼 LinkedIn: https://linkedin.com/in/kavita-malhotra-in
- 💻 GitHub: https://github.com/kavita-solves