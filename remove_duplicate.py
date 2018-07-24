# -*- coding:utf-8 -*-
import sys
def xie_zheng(infile, outfile):
    infopen = open(infile, 'r')
    outopen = open(outfile, 'w')
    lines = infopen.readlines()
    list_l = []
    for line in lines:
        if line not in list_l:
            list_l.append(line)
            outopen.write(line)
    infopen.close()
    outopen.close()


if __name__ == '__main__':
    print(sys.getdefaultencoding())
    reload(sys)
    sys.setdefaultencoding('utf-8')
    print(sys.getdefaultencoding())
    xie_zheng('xie_zheng.txt', 'xie_zheng_1.txt')
