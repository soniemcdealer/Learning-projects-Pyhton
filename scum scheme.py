var_1 = int(input("Введите первое число: "))
var_2 = int(input("Введите второе число: "))
var_3 = int(input("Введите третье число: "))
agregator = []
agregator.append(var_1)
agregator.append(var_2)
agregator.append(var_3)
for i in range(0, 3):
    for j in range(0, 3):
        for k in range(0, 3):
            if(i != j & j != k & k != i):
                print(agregator[i], agregator[j], agregator[k])
# Вывод:
Введите первое число: 10
Введите второе число: 20
Введите третье число: 30
10 20 30
10 30 20
20 10 30
20 30 10
30 10 20
30 20 10