# -*- coding: utf-8 -*-
"""sensitive word detection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ujkU_uBlEkkiqub20Sge0I8j-XZdU_Ji
"""

senWord = open("前端过滤敏感词词库-来自网易.html", "r")
senList = senWord.read().split("|")
label = 0

while True:
  str = input(r"请输入语句：（输入exit退出）")

  if str == "exit":
    break
  else:
    print(r"敏感词：")

  for i in range(len(senList)):
    if str == senList[i]:
      print("\n" + str)
      label = 1
  
  if label == 0:
    print(r"无")

txtyn = input(r"是否输出txt敏感词文件? Y/N ：")
if txtyn == "Y" or "y":
  f = open("senWord.txt", "w")

  for j in range(len(senList)):
    f.write(senList[j]+"\n")
  
  f.close() 


senWord.close()