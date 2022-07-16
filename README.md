# IP&whois&finger.py

本源码由python语言编写，

author：Ninggo

主要提供对域名的IP反查，whois查询，CDN查询，端口扫描及子域名判断，通过python自带库及第三方库方法来运行并判断回显。

## 安装要求

1.python3版本以上

2.安装第三方whois库

3.引入内置socket库，os库

## 测试

命令行运行python脚本，并输入域名，直接输入xxx.com，因为在子域名查询参数引入时默认作了拼接www.。

使用方式：python3 IP&whois&finger.py

在提示中输入域名即可自动进行扫描。

在端口扫描中只规定了一些常规端口，各位可以在源码中修改相关配置以便于实现全端口或定制端口扫描，但是要注意过高的扫描频率可能会造成IP封禁。

同时需要注意提前准备子域名查询字典，名字为dict.txt，放置于源码同文件夹下。如果有大佬可以对代码进行优化感激不尽。