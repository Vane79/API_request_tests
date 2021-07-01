from request_put import *
from request_get import *
from request_post import *
from request_delete import *

base_url = "https://petstore.swagger.io/v2/"

if __name__ == '__main__':
    test_func_put_success_200(var_for_put)
    test_func_put_failure_404(var_for_put)
    test_func_put_failure_415(var_for_put)

    test_func_get_success_200(base_url)
    test_func_get_failure_400(base_url)

    test_func_post_success_200(base_url)
    test_func_post_failure_415(base_url)

    test_func_delete_success_200(base_url)
    test_func_delete_failure_404(base_url)
