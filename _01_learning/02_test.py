import pytest

def setup_module():            #所有用例开始前和结束前只执行一次
    print("setup_module:每个模块开始前只执行一次")
    print('比如:所有用例开始前只打开一次浏览器')

def teardown_module():
    print('teardown_module:每个模块结束后只执行一次')
    print('比如：所有用例结束后关闭浏览器')

def setup_function():          #每个用例开始和结束调用一次
    print("setup_function:每个用例开始前都会执行")

def teardown_function():
    print("teardown_function:每个用例结束后都会执行")


def test_one():
    print("正在执行----test_one")
    x = "this"
    assert 'h' in x


def test_two():
    print("正在执行----test_two")
    x = "hello"
    assert hasattr(x, 'check')


def test_three():
    print("正在执行----test_three")
    a = "hello"
    b = "hello world"
    assert a in b

if __name__ == "__main__":
    pytest.main("-q","02_test.py")