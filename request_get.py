import requests

value = 'status=available'
inv_value = "status=134"


def test_func_get_success_200():
    try:
        response = requests.get("https://petstore.swagger.io/v2/pet/findByStatus", params=value)
        assert response.status_code == 200
        print('exit code 200 on GET, test PASSED')
    except AssertionError:
        print("Different exit code on GET, test GET for exit code 200 *FAILED*")


def test_func_get_failure_400():
    try:
        response = requests.get("https://petstore.swagger.io/v2/pet/findByStatus", params=inv_value)
        assert response.status_code == 400
        print('exit code 400 on GET, test PASSED')
    except AssertionError:
        print("Different exit code on GET, test GET for exit code 400 *FAILED*")


if __name__ == '__main__':
    test_func_get_success_200()
    test_func_get_failure_400()
