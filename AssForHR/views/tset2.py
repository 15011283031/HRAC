# -*- coding:utf-8 -*-
import base64

str = '6Zeo5oi357O757uf5ZGY5bel6LSm5Y+35a+G56CB?='
byt = str.encode('utf-8')

lens = len(byt)
lenx = lens - (lens % 4 if lens % 4 else 4)

result = base64.decodebytes(byt[:lenx])
print('subject:%s' % result.decode('utf-8'))





