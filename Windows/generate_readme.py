#!/usr/bin/python3
# coding=utf-8
# 生成readme 文件

import os
import time
import codecs

cur_path = os.getcwd() + os.sep
paths = []
index = 1
for file in os.listdir(cur_path):
    if os.path.isdir(file) and not file.startswith("."):
        sort = "%02d" % (index)
        name = file
        paths.append(sort + ". " + "[%s](%s)" % (name, name.replace(" ", "+")))
        index = index + 1
        print (paths[index - 2])
# 更新时间
# change_time = "## " + "更新时间：" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
change_time = "## " + "更新时间：" + time.strftime("%Y-%m-%d", time.localtime())
# README
file = codecs.open("README.md", "w", "utf-8")

file.write(change_time)
file.write('\n')

file.write('\n'.join(paths))
file.close()
