import pytest

#期望结果都是固定的一个
#username "",123,"aaaaaa"
#password "",234,"bbbb"



# @pytest.mark.parametrize("password",["",234,"bbbb"])
# @pytest.mark.parametrize("username",["",123,"aaaaaa"])
#
# def test_eval(username,password):
#     print("\n账号和密码的组合：%s, %s"%(username,password))


@pytest.mark.parametrize("test_input,expected",
                         [
                             ("1+3",4),
                             ("11+3",14)
                         ])
def test_eval(test_input,expected):
    a=test_input
   # print(a)
    print("\n"+a)
    assert eval(a)==expected






def add_eval():
    a="1+3"
    assert eval(a)==4




























