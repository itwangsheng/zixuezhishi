# _*_ coding : utf-8 _*-
#作者wxs
# @Time: 2021/1/18 20:29
#@Email:525418383@qq.com
#@File:common.py
'''封装数据连接方法'''
import yaml,os,pymysql

path = os.path.abspath(r'./caseinfo_page')
class comm():
    #读取url
    def read_yaml(self):
        with open(path+r'/url.yaml','r',encoding='utf-8') as file:
            red = yaml.load(file,Loader=yaml.FullLoader)
            return red
    #连接数据库校验
    def mysql_connert(self,sql):
        sql_connert = pymysql.connect('localhost','root','admin','test1')
        cmd = sql_connert.cursor() #光标
        cmd.execute(sql)
        res = cmd.fetchall()
        return res
    #存储变量
    def write_yaml(self,extract):
        # print(path)
        with open(path+r'/extract.yaml','w') as file:
            yaml.dump(extract,file)
    #读取变量
    def read_extract(self,value):
        with open(path+r'/extract.yaml','r') as file:
            red = yaml.load(file,Loader=yaml.FullLoader)
            red = red[value]
            return red
