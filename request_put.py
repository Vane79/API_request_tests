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

variable = "https://petstore.swagger.io/v2/pet"


def test_func_put_success_200(var):
    try:
        response = requests.put(var, json=pet)
        assert response.status_code == 200
        print("exit code 200 on POST, test PASSED")
    except ValueError:
        print("Different exit code on PUT, test PUT for exit code 200 *FAILED*")


# при попытке с несуществующим id, метод создает новый объект, ошибку 404 выбить не получатся. Это ожидаемое поведение?
# def test_func_put_failure_404(var):
#     response = requests.put(var, json=pet2)
#     # assert response.status_code == 404
#     print(response.status_code)
#     print("exit code 404 on POST")


def test_func_put_failure_415(var):
    try:
        response = requests.put(var, json=None)
        assert response.status_code == 415  # unsupported media type
        print("exit code 415 on put, test PASSED")
    except ValueError:
        print("Different exit code on PUT, test PUT for exit code 415 *FAILED*")


if __name__ == '__main__':
    test_func_put_success_200(variable)
    # test_func_put_failure_404(variable)
    test_func_put_failure_415(variable)

