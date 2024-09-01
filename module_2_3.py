# input data
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5, 0, 109, -10, 4]
i = 0
# сделать так, чтобы все положительные числа вывелись в консоль

# program
while i < len(my_list):
    if  my_list[i] > 0:
        print(my_list[i])
        i = i + 1
    elif my_list[i] == 0:
        i = i + 1
    else:
        break

