# _*_ coding : utf-8 _*-
# 作者:wxs
# @Time: 2021\1\20 0020 8:50
#@Email:525418383@qq.com
#@File:logger.py
import logging,os
path = os.path.abspath('./caseinfo_page')

# log日志打印
logger = logging.getLogger('test')
logger.setLevel(logging.DEBUG)  # 输出所有大于DEBUG级别的log
# 设置日志输出格式
fmt = logging.Formatter('[%(filename)-6s]: [%(levelname)-6s] [%(asctime)s]: %(message)s')
# 日志文件的地址
log_name = path+'/testlogs.log'
# 创建一个FileHandler， 向文件logname输出日志信息
fh = logging.FileHandler(log_name, 'a', encoding='utf-8')
# 设置日志等级
fh.setLevel(logging.DEBUG)
# 设置handler的格式对象
fh.setFormatter(fmt)
fh.close()
# 将handler增加到logger中
logger.addHandler(fh)
# 创建一个StreamHandler,用于输出到控制台
stream_hdl = logging.StreamHandler()
stream_hdl.setFormatter(fmt)  # 等级
stream_hdl.setLevel(logging.DEBUG)  # 格式
logger.addHandler(stream_hdl)