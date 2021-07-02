import requests

pet = {
    "id": 200,
    "category": {
        "id": 200,
        "name": "Cats"
    },
    "name": "Charles",
    "photoUrls": [
        "some.url"
    ],
    "tags": [
        {
            "id": 200,
            "name": "Charles"
        }
    ],
    "status": "sold"
}


def test_func_post_success_200(base_url):
    response = requests.post(base_url + "pet", json=pet)
    assert response.status_code == 200


def test_func_post_failure_415(base_url):
    response = requests.post(base_url + "pet", json=None)
    assert response.status_code == 415  # unsupported media type
