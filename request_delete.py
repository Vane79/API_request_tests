import requests

value = "1"
inv_value = '0'


def test_func_delete_success_200():
    response = requests.delete("https://petstore.swagger.io/v2/pet/" + value)
    assert response.status_code == 200
    print('exit code 200 on DELETE')


def test_func_delete_failure_404():
    response = requests.get("https://petstore.swagger.io/v2/pet/" + inv_value)
    assert response.status_code == 404
    print('exit code 404 on DELETE')


if __name__ == '__main__':
    test_func_delete_success_200()
    test_func_delete_failure_404()
