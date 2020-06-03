import pytest

def test_add_raises():
    str_to_change="字符串不能转数字"
    with pytest.raises(ValueError):  #预期异常
        num = int(str_to_change)

if __name__ == "__main__":
    pytest.main("-s","06_ValueErrpr_test.py")