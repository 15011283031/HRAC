# -*- coding:utf-8 -*-
import poplib

from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

"""
    用于使用POP3 接收并处理邮件 最终输出文本字符串列表
"""


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
    print(ret)
    resp_one, mails, octets_one = pp.list()
    # 查看返回列表
    # print(mails)
    # 获取最新的一封邮件，索引号为1开始
    print('startnum:%s' % startnum)
    msglist = []
    for i in range(maxnum + 1):
        if i >= startnum:
            print('read email num:%s' % i)
            resp_two, lines, octets_two = pp.retr(i)
            # lines存储邮件原始文本每行并进行解析
            msg_content = b'\r\n'.join(lines).decode('utf-8')
            msg = Parser().parsestr(msg_content)
            msglist.append(msg)
        else:
            pass
    pp.quit()
    return msglist


def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
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
def print_info(msg, indent=0):
    """
    print email info
    """
    content = ''
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header == 'Subject':
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            print('%s%s: %s' % ('  ' * indent, header, value))
    if (msg.is_multipart()):
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('%spart %s' % ('  ' * indent, n))
            print('%s--------------------' % ('  ' * indent))
            print_info(part, indent + 1)
    else:
        content_type = msg.get_content_type()
        if content_type == 'text/plain' or content_type == 'text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            print('%sText: %s' % ('  ' * indent, content + '...'))
        else:
            print('%sAttachment: %s' % ('  ' * indent, content_type))
    return content


# pop3服务器地址
host = "pop.exmail.qq.com"
# 用户名
username = "yongqiang.chen@yooli.com"
# 密码
password = "UnLt9eYVCcNgMUmb"

maxnum = getemaillen(host, username, password)

print('max email number:%s' % maxnum)

for i in range(maxnum):
    print(i)

msglists = fpemail(host, username, password, 995, maxnum)
msg_content_lists = []
for msg in msglists:
    msg_content = print_info(msg)
    msg_content_lists.append(msg_content)

