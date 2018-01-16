#!/usr/bin/python
# -*- coding: utf-8 -*-




test1 = [0, 0, 0, 1, 1, 1]
predict1 = [0, 1, 0, 1, 0, 0]
name =[]
test = []
predict = []

for i in range(len(predict1)):
    if test1[i] != predict1[i]:
        name.append(name1[i])
        test.append(test1[i])
        predict.append(predict1[i])

table = {'name':name,'test':test,'predint':predict}

frame = pand.DataFrame(table)


print frame'''
