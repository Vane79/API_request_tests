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

value = "1"
inv_value = '0'


def test_func_delete_success_200():  # Иногда, по не понятной причине выдает 404
    try:
        requests.put("https://petstore.swagger.io/v2/pet/", json=pet)
        response = requests.delete("https://petstore.swagger.io/v2/pet/" + value)
        assert response.status_code == 200
        print('exit code 200 on DELETE')
    except ValueError:
        print("Different exit code on DELETE, test DELETE for exit code 200 *FAILED*")


def test_func_delete_failure_404():
    try:
        response = requests.get("https://petstore.swagger.io/v2/pet/" + inv_value)
        assert response.status_code == 404
        print('exit code 404 on DELETE')
    except AssertionError:
        print("Different exit code on DELETE, test DELETE for exit code 404 *FAILED*")


if __name__ == '__main__':
    test_func_delete_success_200()
    test_func_delete_failure_404()
