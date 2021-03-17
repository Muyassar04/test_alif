def function(first_number, second_number, trans):
    if trans == '+':
        return first_number + second_number
    elif trans == '-':
        return first_number - second_number
    elif trans == '*':
        return first_number * second_number
    else:
        if second_number == 0:
            return 'Деление на 0!!!'
        else:
            return first_number / second_number


file_name = input('Укажите имя файла: ')
operation = input('Укажите какую действие выполнять? (+, -, *, /): ')

data_list = []
with open("test.txt") as test_file:
    for line in test_file:
        data_list.append([int(x) for x in line.split()])

test_file.close()

negative = open('negative.txt', 'w')
positive = open('positive.txt', 'w')

for i_data in range(len(data_list)):
    s = function(data_list[i_data][0], data_list[i_data][1], operation)
    if s == 'Деление на 0!!!':
        print('Шаг', i_data, s, str(data_list[i_data][0]) + '/' + str(data_list[i_data][1]))
    elif s >= 0:
        positive.write(str(s) + '\n')
    else:
        negative.write(str(s) + '\n')

negative.close()
positive.close()

print('Задания выполнено успешно!')
