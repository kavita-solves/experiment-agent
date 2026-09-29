import os
os.environ.setdefault("OPENAI_API_KEY", "test-key")  # tools/__init__ builds a model at import

from tools.sample_size import (
    calculate_sample_size_proportion as prop,
    calculate_sample_size_continuous as cont,
)

BASE = {"baseline_rate": 0.10, "mde": 0.02, "daily_traffic": 1000}

def test_equal_split_matches_textbook():
    r = prop.invoke({**BASE, "split": 0.5})
    assert abs(r["total_sample"] - 7678) <= 2
    assert abs(r["sample_treatment"] - 3839) <= 1

def test_uneven_split_matches_textbook():
    r = prop.invoke({**BASE, "split": 0.8})
    assert abs(r["total_sample"] - 11421) <= 3

def test_uneven_split_needs_more_traffic_than_even():
    even = prop.invoke({**BASE, "split": 0.5})["total_sample"]
    uneven = prop.invoke({**BASE, "split": 0.8})["total_sample"]
    assert uneven > even

def test_missing_split_asks_instead_of_guessing():
    assert "error" in prop.invoke(BASE)

def test_invalid_split_rejected():
    assert "error" in prop.invoke({**BASE, "split": 1.5})

def test_continuous_mde_is_not_a_percent_string():
    r = cont.invoke({"mean": 50, "std_dev": 20, "mde_abs": 2, "daily_traffic": 1000})
    assert r["mde_absolute"] == 2