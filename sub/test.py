import pprint
test = [0]*5

Storage = [0, 0, 0, 0, 0] # Node数分

for x in range (len(Storage)):
    Storage[x] = 0.4*(x+1)
    print("S:{}".format(Storage))
    print(type(Storage))
    # test.append(Storage)
    # print("t:{}".format(test))
    # print("t:")
    # pprint.pprint(test)
    test[x] = Storage

pprint.pprint(test)