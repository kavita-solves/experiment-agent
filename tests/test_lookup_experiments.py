import os
os.environ.setdefault("OPENAI_API_KEY", "test-key")

from tools.lookup_experiment import lookup_past_experiments

def test_clean_match_email_no_metric_filter():
    r = lookup_past_experiments.invoke({
        "description": "new subject line for our newsletter",
        "experiment_type": "Marketing"
    })
    assert len(r) == 3
    assert all(exp["channel"] == "Email" for exp in r)
    ids = [exp["id"] for exp in r]
    assert "EXP-101" in ids and "EXP-102" in ids and "EXP-111" in ids

def test_unclear_channel_asks_instead_of_guessing():
    r = lookup_past_experiments.invoke({
        "description": "improve overall experience",
        "experiment_type": "Marketing"
    })
    assert len(r) == 1
    assert "message" in r[0]
    assert "unclear" in r[0]["message"].lower()

def test_metric_synonym_currently_not_matched():
    """
    Known gap: substring matching doesn't catch 'click-through rate' == 'CTR'.
    Deferred to Week 3-4 (embeddings/semantic retrieval).
    This test documents the gap — flip the assertion once that's built.
    """
    r = lookup_past_experiments.invoke({
        "description": "new subject line for our newsletter",
        "experiment_type": "Marketing",
        "metric": "click-through rate"
    })
    assert len(r) == 1
    assert "message" in r[0]  # currently returns "no experiment found", not EXP-102