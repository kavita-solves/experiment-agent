from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code ==200
    assert r.json() == {"status": "ok"}

def test_sample_size_valid_output():
    r = client.post("/tools/samplesize", 
                    json = {"baseline_rate": 0.10, "mde": 0.02, "daily_traffic": 1000, "split": 0.5})
    assert r.status_code == 200
    assert r.json()["total_sample"] == 7678

def test_sample_size_invalid_split():

    r = client.post("/tools/samplesize", 
                    json = {"baseline_rate": 0.10, "mde": 0.02, "daily_traffic": 1000, "split": 1.5})

    assert r.status_code == 400

def test_sample_size_missing_split_rejected_by_pydantic():
    r = client.post("/tools/samplesize", 
                    json = {"baseline_rate": 0.10, "mde": 0.02, "daily_traffic": 1000})
    assert r.status_code == 422

