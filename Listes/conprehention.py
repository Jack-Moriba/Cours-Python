nombres = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
print(nombres)
list_positive = []
for i in nombres:
    if i > 0:
        list_positive.append(i)
        print(list_positive)

# ou encore
nombres = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
print(nombres)
list_negative = [i for i in nombres if i < 0]
print(list_negative)