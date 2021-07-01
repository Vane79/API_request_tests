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


def test_func_put_success_200():
    try:
        response = requests.put("https://petstore.swagger.io/v2/pet", json=pet)
        assert response.status_code == 200
        print("exit code 200 on POST, test PASSED")
    except ValueError:
        print("Different exit code on PUT, test PUT for exit code 200 *FAILED*")


# при попытке с несуществующим id, метод содает новый объект, ошибку 404 выбить не получатся. Это ожидаемое поведение?
# def test_func_put_failure_404():
#     response = requests.put("https://petstore.swagger.io/v2/pet", json=pet2)
#     # assert response.status_code == 404
#     print(response.status_code)
#     print("exit code 404 on POST")


def test_func_put_failure_415():
    response = requests.put("https://petstore.swagger.io/v2/pet", json=None)
    assert response.status_code == 415  # unsupported media type
    print("exit code 415 on POST")


if __name__ == '__main__':
    test_func_put_success_200()
    # test_func_put_failure_404()
    test_func_put_failure_415()

