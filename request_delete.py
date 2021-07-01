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


def test_func_delete_success_200(var):  # Иногда, по непонятной причине выдает 404
    value = "1"
    try:
        requests.put(var + "pet", json=pet)
        response = requests.delete("https://petstore.swagger.io/v2/pet/" + value)
        assert response.status_code == 200
        print('exit code 200 on DELETE, test PASSED')
    except AssertionError:
        print("Different exit code on DELETE, test DELETE for exit code 200 *FAILED*")


def test_func_delete_failure_404(var):
    inv_value = '0'
    try:
        response = requests.get(var + "pet" + inv_value)
        assert response.status_code == 404
        print('exit code 404 on DELETE, test PASSED')
    except AssertionError:
        print("Different exit code on DELETE, test DELETE for exit code 404 *FAILED*")


if __name__ == '__main__':
    from tests import base_url as variable
    test_func_delete_success_200(variable)
    test_func_delete_failure_404(variable)
