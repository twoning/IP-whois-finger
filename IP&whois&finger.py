# -*- coding: UTF-8 -*- #
"""
@filename:IP&whois&finger.py
@author:Ning
@time:2022-07-16
"""

import time

from whois import whois
import socket,os

#域名反查IP
def ip_check(url):
    ip = socket.gethostbyname(url)
    print(f"{url}对应的IP为{ip}")



#whois查询
def whois_check(url):
    try:
       info=whois(url)   #Info返回了所有的whois查询信息，可根据需要选择想要提取的查询方法
       print(info)
    except:
       return None




#CDN查询
#如果nslookup返回结果数目为1则不存在CDN
#利用python执行系统命令 os模块
def cdn_check(url):
    ns = "nslookup " + url
    cdn_data = os.popen(ns).read()
    # print(cdn_data)
    x = cdn_data.count('.')
    if x>10:
        print("CDN存在")
    else:
        print("CDN不存在")
#利用IP地址为x.x.x.x，则有3个点则为一个IP地址


#端口扫描
# 1.原生字写socket协议tcp,udp扫描
# 2.调用第三方模块扫描
# 3.调用系统工具脚本执行
def port_check(url):
    ip = socket.gethostbyname(url)
    ports = {'21', '22', '25','53','110', '135', '80', '8080', '8888', '7000', '7001', '3389', '443', '3306', '1433',
             '1521', '9090', '8089', '4848', '445'}
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    for port in ports:
        data_ip = server.connect_ex((ip, int(port)))
        #connect_ex，有返回值，连接成功时返回 0 ，连接失败时候返回编码，例如：10061
        if data_ip == 0:
            print(ip + ":" + port + '|开放')
        else:
            print(ip + ":" + port + '|关闭')


#子域名查询
# 1.使用字典爆破查询
# 2.使用搜索引擎语法查询
def subdomain_check(url):
    urls = url.replace('www','')
    for zym in open('dict.txt'):
        zym = zym.replace('\n','')
        url = zym+'.url'
        try:
            ip = socket.gethostbyname(url)
            print(url+'----'+ip)
            time.sleep(0.1)
        except Exception as e:
            pass


def main(url):
    ip_check(url)
    whois_check(url)
    cdn_check(url)
    port_check(url)


if __name__ == '__main__':
    url = input("请输入域名：").strip()
    if url != "exit":
        main(url)
    else:
        print("域名有误！")
