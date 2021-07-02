import requests

pet = {
    "id": 1,
    "category": {
        "id": 0,
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


def test_func_delete_success_200(base_url):  # Иногда, по непонятной причине выдает 404
    value = "1"
    requests.put(base_url + "pet", json=pet)
    response = requests.delete("https://petstore.swagger.io/v2/pet/" + value)
    assert response.status_code == 200


def test_func_delete_failure_404(base_url):
    inv_value = '0'
    response = requests.get(base_url + "pet" + inv_value)
    assert response.status_code == 404
