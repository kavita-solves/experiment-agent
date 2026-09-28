# Experiment Agent — TODO List

## Phase 2 — August Mid
- [ ] Product metrics — DAU, MAU, time spent, feature adoption
- [ ] Continuous metric in business language — 
      "average order value" instead of "mean/std/variance"
- [ ] Ask PM — "What is your current average order value?" 
      instead of "What is the mean?"
- [ ] add the continous metrics and mean, variance in the agent state
- [ ] Continuous metrics mein uneven split support
## Phase 2 — Agentic Guardrail System
- [ ] recommend_guardrails tool — LLM proposes, Python validates
- [ ] ExperimentContext structured output — surface, user_action, failure_modes
- [ ] Validation layer — reject duplicates, ensure failure mode mapping
- [ ] Remove all hardcoded channel-to-metric mappings
- [ ] Move from hardcoded answers to hardcoded decision principles

## Phase 2.1 — Agent Intelligence (inspired by LinkedIn feedback)

### Ending with Contested Choices (not a finished plan)
- Output ke end mein add karo:
  * Assumptions the agent had to invent
  * 2-3 alternative framings it considered and rejected — with reasons
- Review conversation should open at disagreements, not at a finished artifact

### Let it Refuse
- Jab business question underspecified ho — agent should stop and ask
- Never fill in missing information silently
- Default failure mode of every assistant: filling gaps — avoid this

### Fluency ≠ Rigor Warning
- A well-formed weak experiment is harder to challenge than a vague one
- Agent should surface weak assumptions explicitly even when design looks polished

## Phase 3 — August End
- [ ] Geo experiment support
- [ ] Platform experiments — Meta, Google own A/B testing
      (educate PM that these platforms handle it themselves)
- [ ] Control experiment opportunity cost formula

## Future
- [ ] Multi-tenant — company specific context
- [ ] Web holdout opportunity cost
- [ ] Customer segments in context
- [ ] Email type wise conversion rates