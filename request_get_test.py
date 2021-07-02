import requests


def test_func_get_success_200(base_url):
    value = 'status=available'
    response = requests.get(base_url + "pet/findByStatus", params=value)
    assert response.status_code == 200


def test_func_get_failure_400(base_url):  # пытаюсь ввести неверный аттрибут для поиска, возвращает 200.
    inv_value = "status=134"
    response = requests.get(base_url + "pet/findByStatus", params=inv_value)
    assert response.status_code == 400
