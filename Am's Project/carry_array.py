# def add_one(given_array):
#     carry = 1
#     result = int[given_array.length]
#
#     for i from (given_array.length - 1) down to 0:
#         total = given_array[i] + carry
#         if total == 10:
#             carry = 1
#         else:
#             carry = 0
#             result[i] = total % 10
#         if carry == 1:
#             result = int[given_array.length + 1]
#             result[0] = 1
#         return result

def addOne(givenArray):
    arrayStr = ""
    for i in givenArray:
        arrayStr += str(i)
        arrayInt = int(arrayStr)
    return arrayInt + 1
