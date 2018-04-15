# -*- coding:utf-8 -*-
import poplib

from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr


def getemaillen(host, username, password):
    # 创建一个pop3对象，这个时候实际上已经连接上服务器了
    pp = poplib.POP3(host)
    # 设置调试模式，可以看到与服务器的交互信息
    pp.set_debuglevel(1)
    # 向服务器发送用户名
    pp.user(username)
    # 向服务器发送密码
    pp.pass_(password)
    # 获取服务器上信件信息，返回是一个列表，第一项是一共有多上封邮件，第二项是共有多少字节
    ret = pp.stat()
    maxnum = ret[0]
    pp.quit()
    return maxnum


def fpemail(host, username, password, startnum, maxnum):
    # 创建一个pop3对象，这个时候实际上已经连接上服务器了
    pp = poplib.POP3(host)
    # 设置调试模式，可以看到与服务器的交互信息
    pp.set_debuglevel(1)
    # 向服务器发送用户名
    pp.user(username)
    # 向服务器发送密码
    pp.pass_(password)
    # 获取服务器上信件信息，返回是一个列表，第一项是一共有多上封邮件，第二项是共有多少字节
    ret = pp.stat()
    print (ret)
    #resp_one,mails,octets_one = pp.list()
    #查看返回列表
    #print(mails)
    #获取最新的一封邮件，索引号为1开始
    print('startnum:%s' % startnum)
    msglist = []
    for i in range(maxnum+1):
        if i >= startnum:
            print('read email num:%s'%i)
            try:
                resp_two, lines, octets_two = pp.retr(i)
            except:
                pass

            #lines存储邮件原始文本每行并进行解析
            msg_content = b'\r\n'.join(lines).decode('utf-8', 'ignore')
            #print(msg_content)
            msg = Parser().parsestr(msg_content)
            msglist.append(msg)
        else:
            pass
    pp.quit()
    return msglist


def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset,'ignore')
    return value


def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset


# indent用于缩进显示:
def print_info(msg, indent=0, msgs=[]):
    """
    print email info
    """
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header=='Subject':
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            print('%s%s: %s' % ('  ' * indent, header, value))

    if (msg.is_multipart()):
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            #print('%spart %s' % ('  ' * indent, n))
            #print('%s--------------------' % ('  ' * indent))

            return msgs + print_info(part, indent + 1)

    else:
        content_type = msg.get_content_type()
        if content_type=='text/plain' or content_type=='text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset, 'ignore')
                msgs.append(content)
            #print('%sText: %s' % ('  ' * indent, content + '...'))
        else:
            print('%sAttachment: %s' % ('  ' * indent, content_type))

    return msgs





# pop3服务器地址
host = "pop.exmail.qq.com"
# 用户名
username = "yongqiang.chen@yooli.com"
# 密码
password = "UnLt9eYVCcNgMUmb"

maxnum = getemaillen(host, username, password)
#print('max email number:%s'%maxnum)

msglists = fpemail(host, username, password, 957, maxnum)
msg_content_lists = []
msgs = []
for msg in msglists:
    msg_content = print_info(msg=msg,msgs=msgs)
    for i in msg_content:
        pass#print('---------------------------%s'%i)
    msg_content_lists.append(msg_content)


import bs4 as bs

jsoncontent = {}

for msg_content in msg_content_lists:
    i = 1
    #print(msg_content)
    for msgs in msg_content:

        readSoup = bs.BeautifulSoup(msgs.encode().decode(),'lxml')
        lists = readSoup.find_all("div",class_="body-text")
        if len(lists) > 2:
            for list in lists[2]:
                if len(list) > 0:
                    listcontent = list[34:].rstrip()
                    dictcontent = {i:listcontent}
                    jsoncontent.update(dictcontent)
                    #print(jsoncontent)
                    i = i + 1
                    #print('list_len:%s'%len(list))

import json

import codecs
fp = codecs.open('data.json', 'a', 'utf-8')
fp.write(json.dumps(jsoncontent,ensure_ascii=False))
fp.close()