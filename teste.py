dic ={"a": 2, "b": 3, "c":2.4}

dic.update({"d": 6})

for elem in dic:
    print(elem + ": " + str(dic.get(elem)))