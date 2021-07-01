from request_put import *
from request_get import *
from request_post import *
from request_delete import *

var_for_put = "https://petstore.swagger.io/v2/pet"
var_for_get = "https://petstore.swagger.io/v2/pet/findByStatus"
var_for_post = "https://petstore.swagger.io/v2/pet"
var_for_delete = "https://petstore.swagger.io/v2/pet/"

if __name__ == '__main__':
    test_func_put_success_200(var_for_put)
    # test_func_put_failure_404(var_for_put)
    test_func_put_failure_415(var_for_put)

    test_func_get_success_200(var_for_get)
    test_func_get_failure_400(var_for_get)

    test_func_post_success_200(var_for_post)
    test_func_post_failure_415(var_for_post)

    test_func_delete_success_200(var_for_delete)
    test_func_delete_failure_404(var_for_delete)
