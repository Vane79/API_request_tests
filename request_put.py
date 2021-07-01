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


# pet2 = {
#     "id": 5000000000000000000,
#     # "category": {
#     #     "id": 200,
#     #     "name": "Cats"
#     # },
#     "name": "Charles",
#     "photoUrls": [
#         "some.url"
#     ],
#     "tags": [
#         {
#             "id": 200,
#             "name": "Charles"
#         }
#     ],
#     "status": "sold"
# }


def test_func_put_success_200():
    response = requests.put("https://petstore.swagger.io/v2/pet", json=pet)
    assert response.status_code == 200
    print("exit code 200 on POST")


# def test_func_put_failure_404():
#     response = requests.put("https://petstore.swagger.io/v2/pet", json=pet2)
#     # assert response.status_code == 404
#     print(response.status_code)
#     print("exit code 404 on POST")

# def test_func_put_failure_405():
#     response = requests.put("https://petstore.swagger.io/v2/pet", json=)
#     # assert response.status_code == 415  # unsupported media type
#     # print("exit code 415 on POST")
#     print(response.status_code)

# def test_func_put_failure_415():
#     response = requests.put("https://petstore.swagger.io/v2/pet", json=None)
#     assert response.status_code == 415  # unsupported media type
#     print("exit code 415 on POST")


if __name__ == '__main__':
    test_func_put_success_200()
    # test_func_put_failure_404()
    # test_func_put_failure_405()
