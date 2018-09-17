question_1 = [9,9,9]
print(question_1)

def carryInt(addOne):
    i = int("".join(map(str,addOne)))
    i += 1
    l = list(map(int,list(str(i))))
    return l
print(carryInt(question_1))