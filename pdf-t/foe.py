
vers = [0,1,2,3,4]
dictvers = []
for ver in range(len(vers)):
    dictver = {}
    dictver['a'+str(ver)] = ver
    dictver['b'+str(ver)] = 11
    dictver['c'+str(ver)] = 22
    dictvers.append(dictver)


print dictvers




