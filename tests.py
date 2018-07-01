import pytest
import process

@pytest.fixture(scope="function", params=[
        (1, 'Один'),
        (2, 'Два'),
        (3, 'Три'),
        (4, 'Четыре')],
        ids = ['First test','Second test','Third test','Fourth test'])

def param_test(request):
    return request.param

def test_our_func(param_test):
    (inp,expected_result) = param_test
    calculated_result = process.getName(inp)
    print("input: {0}, output: {1}, expected: {2}".format(inp, calculated_result, expected_result))
    assert process.getName(inp) == expected_result

if __name__ == '__main__':
    param_test()