import requests

value = 'status=available'
inv_value = "status=134"

variable = "https://petstore.swagger.io/v2/pet/findByStatus"


def test_func_get_success_200(var):
    try:
        response = requests.get(var, params=value)
        assert response.status_code == 200
        print('exit code 200 on GET, test PASSED')
    except AssertionError:
        print("Different exit code on GET, test GET for exit code 200 *FAILED*")


def test_func_get_failure_400(var):  # пытаюсь ввести неверный аттрибут для поиска, возвращает 200.
    try:
        response = requests.get(var, params=inv_value)
        assert response.status_code == 400
        print('exit code 400 on GET, test PASSED')
    except AssertionError:
        print("Different exit code on GET, test GET for exit code 400 *FAILED*")


if __name__ == '__main__':
    test_func_get_success_200(variable)
    test_func_get_failure_400(variable)
