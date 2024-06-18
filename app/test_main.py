from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

valid_csv_file = "data.csv"
invalid_csv_column = "extraColumn.csv"
invalid_csv_cell = "emptyStr.csv"
data_folder = "./app/data/"

def test_ping_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"ping":"pong"}

def test_file_upload():
    response = client.post(
        "/csv/",
        files = {"file": (valid_csv_file, open(data_folder + valid_csv_file, "rb"), "text/csv")}
        )
    assert response.status_code == 200
    assert response.json() == {
        "file": valid_csv_file,
        "equals": None,
        "rows": [
            {
            "Response": "Love it",
            "Value": "1"
            },
            {
            "Response": "I hate it",
            "Value": "2"
            },
            {
            "Response": "It's okay",
            "Value": "1"
            },
            {
            "Response": "Don't care",
            "Value": "3"
            },
            {
            "Response": "Why yellow?",
            "Value": "2"
            },
            {
            "Response": "Does it matter that much?",
            "Value": "1"
            },
            {
            "Response": "I don't know",
            "Value": "1"
            },
            {
            "Response": "I don't care",
            "Value": "1"
            },
            {
            "Response": "idk",
            "Value": "3"
            },
            {
            "Response": "Like the packaging",
            "Value": "3"
            },
            {
            "Response": "I personally wouldn't be interested in this product.",
            "Value": "2"
            }
        ]
        }

def test_file_query():
    response = client.post(
        "/csv/",
        files = {"file": (valid_csv_file, open(data_folder + valid_csv_file, "rb"), "text/csv")},
        params = {"equals": 1}
        )
    assert response.status_code == 200
    assert response.json() == {
        "file": valid_csv_file,
        "equals": 1,
        "rows": [
            {
            "Response": "Love it",
            "Value": "1"
            },
            {
            "Response": "It's okay",
            "Value": "1"
            },
            {
            "Response": "Does it matter that much?",
            "Value": "1"
            },
            {
            "Response": "I don't know",
            "Value": "1"
            },
            {
            "Response": "I don't care",
            "Value": "1"
            }
        ]
        }

def test_invfile_column():
    response = client.post(
        "/csv/",
        files = {"file": (invalid_csv_column, open(data_folder + invalid_csv_column, "rb"), "text/csv")}
        )
    assert response.status_code == 400
    assert response.json() == {"detail": "CSV file must only contain columns 'Response' and 'Value'"}

def test_invfile_nan():
    response = client.post(
        "/csv/",
        files = {"file": (invalid_csv_cell, open(data_folder + invalid_csv_cell, "rb"), "text/csv")}
        )
    assert response.status_code == 400
    assert response.json() == {"detail": "'Response' column must not contain empty strings."}

def test_embed_valid():
    response = client.get(
        "/embedding/",
        params = {"text": "It's great"}
        )
    assert response.status_code == 200

def test_embed_valid():
    response = client.get(
        "/embedding/",
        params = {"text": "no"}
        )
    assert response.status_code == 422