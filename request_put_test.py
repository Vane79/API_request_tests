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
pet2 = {
    "id": -200,
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


def test_func_put_success_200(url):
    response = requests.put(url + "pet", json=pet)
    assert response.status_code == 200


def test_func_put_failure_404(url):
    # при попытке редактирования объекта с несуществующим id, метод создает новый объект,
    # ошибку 404 выбить не получатся. Это ожидаемое поведение?
    response = requests.put(url + "pet", json=pet2)
    assert response.status_code == 404


def test_func_put_failure_415(url):
    response = requests.put(url + "pet", json=None)
    assert response.status_code == 415  # unsupported media type
