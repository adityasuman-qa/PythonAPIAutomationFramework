# Common Verification
# HTTP Status Code
# Headers
# Data Verification
# JSON Schema

def verify_http_status_code(response_data, expected_data):
    assert response_data.status_code == expected_data, "FailedStatus Code Match"

def verify_response_key(key, expected_data):
    assert key == expected_data

def verify_json_key_for_not_null(key):
    assert key != 0, "Failed -Key is non Empty" + key
    assert key > 0,  "Failed  -key is greater than Zero"


def verify_json_key_for_not_null_token(key):
    assert key != 0, "failed -key is non Empty" + key


def verify_response_delete(response):
    assert "Create" is response
