import pytest
from app import app, entries


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_add_entry_with_happiness(client):
    # Log in first
    client.post(
        "/login", data={"password": "einSehrGeheimesPasswort"}
    )  # Make sure PASSWORD is imported or defined

    # Check initial length of entries
    initial_len = len(entries)

    # Perform the POST request to add an entry
    client.post("/add_entry", data={"content": "Test content", "happiness": "🙂"})

    # Assertions
    assert len(entries) == initial_len + 1
    assert entries[-1].content == "Test content"
    assert entries[-1].happiness == "🙂"
