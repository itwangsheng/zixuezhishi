# _*_ coding : utf-8 _*-
#作者wxs
# @Time: 2021/1/18 21:03
#@Email:525418383@qq.com
#@File:test_case.py
import pytest
from base_page.baseobject import baseObject
class Testcase():
    def setup(self):
        self.base = baseObject()
    def teardown(self):
        print("这是用例结尾")
    #一个用例里面运行多条用例
    def test01(self,datainfo):
        res = self.base.base_info(mother=datainfo['request']['method'],name=datainfo['apiname'],
                                  data=datainfo['request']['data'],files=datainfo['request']['files'])
        self.base.sendinfo(datainfo, res)
        self.base.validate(datainfo['validate'],res)
