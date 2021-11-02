# def fancy_hello_world():
#     fancy_string = """
#  ──▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───
#  ──█▒▒░░░░░░░░░▒▒█───
#  ───█░░█░░░░░█░░█────
#  ▄▄──█░░░▀█▀░░░█──▄▄─
# █░░█─▀▄░░░░░░░▄▀─█░░█
#
#     """
#     return fancy_string
# print(fancy_hello_world())



# def absolute_value(x):
#     if x < 0:
#         return -x
#     elif x > 0:
#         return x
#     else:
#         return x
#
# print(absolute_value())


# def compare(x,y):
#     if x > y:
#         return 1
#     elif x == y:
#         return 0
#     elif x < y:
#         return -1
# print(compare(12,23))



# Dictionary
# eng2uz = {'one': 'bir', 'two': 'ikki', 'three': 'uch'}
# print(eng2uz.get('ff' , 'not found'))









# Task7
# mark1 = int(input("enter first mark > "))
# mark2 = int(input('enter second mark >   '))
# mark3 = int(input('enter third mark > '))
#
# def calculate () :
#     result = (mark1 + mark2 + mark3)/3
#     return result
#
# print(calculate())


# mark1 = int(input("enter first mark > "))
# mark2 = int(input('enter second mark >   '))
# mark3 = int(input('enter third mark > '))
# myFinalMarks = {'CSF': mark1, 'FunPro': mark2, 'WT': mark3}
# def calculate () :
#
#
#     result = (mark1 + mark2 + mark3)/3
#     return result
#
# print(calculate())




def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

h = histogram('dictionary')
print(h.get('s', 0))