# _*_ coding : utf-8 _*-
#作者wxs
# @Time: 2021/1/18 19:51
#@Email:525418383@qq.com
#@File:baseobject.py
'''封装http请求'''
from base_page.common import comm
from base_page.logger import logger
import requests,json


class baseObject(comm):
    INDEX=0
    def __init__(self):
        self.initialize()
    def initialize(self):
        da = self.read_yaml() #获取url
        self.url=da['api_url']['test_api']
        self.headers = {}
    def data_convert(self,data,files):
        if isinstance(data,dict):
            data = json.dumps(data)
            if files:
                data = json.loads(data)
            return data

    def file_convert(self,files):
        files = files[1:len(files)-1]
        # print("属性：",eval(files),type(files))
        return eval(files)
    def headers_init(self,headers,files):
        self.headers = {'Content-Type': 'application/json'}
        for key,value in headers.items():
            self.headers[key]=value
        if files:
            self.headers={}
            for key, value in headers.items():
                self.headers[key] = value
    def name_convert(self,name):
        if "${{" in name and "}}" in name:
            value = name.split("{{")[1].split("}}")[0]
            value = self.read_extract(value)
            name=name.split('$')[0] + value
            self.url = self.url+name
        else:
            self.url = self.url+name
    def post(self,data,files):
        res = requests.request('post',url=self.url,data=data,headers=self.headers,files=files)
        return res.json()
    def get(self,data,files):
        res = requests.request('get',url=self.url,data=data,headers=self.headers,files=files)
        return res.json()
    #传值
    def sendinfo(self,data,res):
        if 'extract' in data and data['extract']: #如果存在提取变量的字段
            for key, value in data['extract'].items():
                extract = {}
                extract[key] = res[value]
                self.write_yaml(extract) #存到yaml文件中
    #断言
    def validate(self,yuqi,shiji):
        num = baseObject.INDEX
        for key,value in yuqi.items():
            if key in shiji:
                if value != shiji[key]:
                    print("用例{3}判断为：{2}!\n返回值：{0}!= 预期结果：{1}".format(shiji[key], value, False,num))
                    assert shiji[key] == value, "实际与预期不符"
            else:
                if isinstance(shiji,list):
                    for data in shiji:
                        logger.info("这是接口返回值：{0}".format(data))
                        yuqi_new = {}
                        yuqi_new[key] = value
                        self.validate(yuqi=yuqi_new, shiji=data)
                elif isinstance(shiji,dict):
                    for _key,_value in shiji.items():
                        if isinstance(_value,dict) and (key in _value):
                            print("这是实际;", _value)
                            yuqi_new = {}
                            yuqi_new[key]=value
                            self.validate(yuqi=yuqi_new,shiji=_value)
    def base_info(self,mother,name,data=None,headers=None,files=None):
        if files:
            files = self.file_convert(files)
        if data:
            data = self.data_convert(data,files)
        if headers:
            self.headers_init(headers,files)
        if name:
            self.name_convert(name)
        res=''
        mother = mother.upper()
        if mother=='POST':
            res = self.post(data,files)
        elif mother=='GET':
            res = self.get(data,files)
        baseObject.INDEX += 1
        logger.info("-->>>开始测试用例{0}，这是接口url：{1}".format(baseObject.INDEX, self.url))
        logger.info("这是接口入参：{0}".format(data))
        logger.info("这是请求头：{1}，这是接口返回值：{0}".format(res, headers))
        self.initialize()
        return res
