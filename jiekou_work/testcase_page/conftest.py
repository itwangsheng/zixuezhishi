# _*_ coding : utf-8 _*-
#作者wxs
# @Time: 2021/1/18 21:23
#@Email:525418383@qq.com
#@File:conftest.py
import pytest,yaml,os
path = os.path.abspath(r'./caseinfo_page')
def read_yaml():
    with open(path+r'/caseinfo.yaml','r',encoding='utf-8') as file:
        red = yaml.load(file,Loader=yaml.FullLoader)
        return red
@pytest.fixture(params=read_yaml())
def datainfo(request):
    return request.param
