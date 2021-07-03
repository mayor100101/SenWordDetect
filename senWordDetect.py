# -*- coding: utf-8 -*-
# author: Dongfang Yishao

import jieba

senWord = open("前端过滤敏感词词库-来自网易.html", "r")
senList = senWord.read().split("|")
label = 0

while True:
  str = input(r"请输入语句：（输入exit退出）")

  if str == "exit":
    break
  else:
    print(r"敏感词：")

  jcut = jieba.lcut(str, cut_all=True)

  for i in range(len(senList)):
    for j in range(len(jcut)):
      if jcut[j] == senList[i]:
        print("\n" + jcut[j])
        label = 1
  
  if label == 0:
    print(r"无")

txtyn = input(r"是否输出txt敏感词文件? Y/N ：")
if (txtyn == "Y") or (txtyn == "y"):
  f = open("senWord.txt", "w")

  for k in range(len(senList)):
    f.write(senList[k]+"\n")
  
  f.close() 


senWord.close()