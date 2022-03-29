# _*_ coding : utf-8 _*-
# 作者:wxs
# @Time: 2021\1\19 0019 9:08
#@Email:525418383@qq.com
#@File:run.py
import pytest
pytest.main(['-s','./testcase_page','-vv','--alluredir','./report/xml'])

#报告生成：allure generate --clean ./report/xml -o ./report/html