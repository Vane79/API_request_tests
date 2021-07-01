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


def test_func_post_success_200(var):
    try:
        response = requests.post(var+"pet", json=pet)
        assert response.status_code == 200
        print("exit code 200 on POST, test PASSED")
    except AssertionError:
        print("Different exit code on POST, test POST for exit code 200 *FAILED*")


def test_func_post_failure_415(var):
    try:
        response = requests.post(var+"pet", json=None)
        assert response.status_code == 415  # unsupported media type
        print("exit code 415 on POST, test PASSED")
    except AssertionError:
        print("Different exit code on POST, test POST for exit code 415 *FAILED*")


if __name__ == '__main__':
    from tests import base_url as variable
    test_func_post_success_200(variable)
    test_func_post_failure_415(variable)
