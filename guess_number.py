# -*- coding: utf-8 -*-
"""
產生一個隨機整數1~100(不要印出來)
讓使用者重復輸入數字去猜
猜對的話 印出 "終於答對了!"
猜錯的話 要告訴他 比答案大/小

延伸題1 印出猜了幾次
延伸題2 讓使用者決定隨機數範圍
"""

import random

#延伸題2 讓使用者決定隨機數範圍
while True:
    s = int(input('請輸入亂數最小值: '))
    b = int(input('請輸入亂數最大值: '))
    if s > b: #最小值不能大於最大值
        print('最小值大於最大值,輸入錯誤')
    else:
        break

r = random.randint(s, b)
i = 0 #count

print(r) #先知道亂數數字,方便測試

while True:
    n = int(input('請使用者輸入數字: '))
    i += 1 #i = i + 1 快寫法 延伸題1 印出猜了幾次
    if r == n: #題目跟解答一樣時
        print('終於答對了!')
        break
    elif r < n: #答案比題目小
        print('比答案大')
    elif r > n: #答案比題目大
        print('比答案小')
    print('使用者總共猜了: ', i, '次')