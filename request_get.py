import requests

value = 'status=available'
# inv_value = ''


def test_func_get_success_200():
    response = requests.get("https://petstore.swagger.io/v2/pet/findByStatus", params=value)
    assert response.status_code == 200
    print('exit code 200 on GET')


# def test_func_get_failure_400():
#     response = requests.get("https://petstore.swagger.io/v2/pet/findByStatus", params=)
#     print(response.status_code)


if __name__ == '__main__':
    test_func_get_success_200()
    # test_func_get_failure_400()
