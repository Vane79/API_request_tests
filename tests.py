from request_put import *
from request_get import *
from request_post import *
from request_delete import *

if __name__ == '__main__':
    test_func_put_success_200()
    # test_func_put_failure_404()
    test_func_put_failure_415()

    test_func_get_success_200()
    test_func_get_failure_400()

    test_func_post_success_200()
    test_func_post_failure_415()

    test_func_delete_success_200()
    test_func_delete_failure_404()
