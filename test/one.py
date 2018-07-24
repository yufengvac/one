# -*- coding: utf-8 -*-
file = open("test.txt", "r")
count = 0
for line in file.readlines():
    count = count + 1
    print(count)
    print(line)
