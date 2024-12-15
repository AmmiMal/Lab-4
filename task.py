items_dict = {'r': [3, 25],
              'p': [2, 15],
              'a': [2, 15],
              'm': [2, 20],
              'k': [1, 15],
              'x': [3, 20],
              't': [1, 25],
              'f': [1, 15],
              'd': [1, 10],
              's': [2, 20],
              'c': [2, 20]
              }


# определяем списки из размеров и очков выживания элементов инвентаря
def get_size_and_points(items_dict):
    size = [items_dict[item][0] for item in items_dict]
    points = [items_dict[item][1] for item in items_dict]
    return size, points


# создание таблицы для мемоизации
def get_memtable(items_dict, A=8):
    size, points = get_size_and_points(items_dict)
    n = len(points)  # находим размеры таблицы

    # создаём таблицу из нулевых значений
    V = [[0 for a in range(A + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        for a in range(A + 1):
            if i == 0 or a == 0:
                V[i][a] = 0
            elif size[i - 1] <= a:
                V[i][a] = max(points[i - 1] + V[i - 1][a - size[i - 1]], V[i - 1][a])
            else:
                V[i][a] = V[i - 1][a]
    return V, size, points


# определение элементов для рюкзака
def get_selected_items_list(items_dict, A=8):
    V, size, points = get_memtable(items_dict, A)
    n = len(points)
    res = V[n][A]
    a = A
    items_list = []

    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == V[i - 1][a]:
            continue
        else:
            items_list.append([size[i - 1], points[i - 1]])
            res -= points[i - 1]
            a -= size[i - 1]
    selected_items = []

    # определяем названия предметов
    was_used = []
    for search in items_list:
        for key, value in items_dict.items():
            if value == search:
                if key in was_used:
                    continue
                else:
                    selected_items.append(key)
                    was_used.append(key)
                    break
    return selected_items, items_list


items_for_bag, items_list = get_selected_items_list(items_dict, 8)

matrix = [[[''], [''], ['']], [[''], [''], ['']], [[''], [''], ['']]]




j=0
n=0
for i in range(3):
    j=0
    if i==0 and j==0:
        matrix[0][0]=["i"]
        j = 1
    while j<3:
        k=items_list[n][0]
        for d in range(k):
            matrix[i][j]=[items_for_bag[n]]
            j+=1
        n+=1
# while len(items_for_bag) > 0:
#     remaining_len = 0
#     for i in range(3):
#         for j in range(3):
#             if matrix[i][j] != 'i':
#                 if remaining_len == 0:
#                     pass
#                 else:
#                     pass

for i in range(3):
    for j in range(3):
        if j != 2:
            print(matrix[i][j], end=', ')
        else:
            print(matrix[i][j], end='\n')

survival_points = 20  # 15 изначальных + 5 за ингалятор
for item in items_dict:
    if item in items_for_bag:
        survival_points += items_dict[item][1]
    else:
        survival_points -= items_dict[item][1]
print(f'Итоговый результат очков выживания у Тома {survival_points}')

print()
items_for_add, items_list = get_selected_items_list(items_dict, 6)
# A=6, т.к. 1 элемент из 7 обязательно ингалятор
print(f'Набор для инвентаря в 7 ячеек, не считая ингалятор: {items_for_add}')
survival_points = 20  # 15 изначальных + 5 за ингалятор
for item in items_dict:
    if item in items_for_add:
        survival_points += items_dict[item][1]
    else:
        survival_points -= items_dict[item][1]

print(f'Итоговый результат очков выживания у Тома {survival_points}, что означает, что при наборе инвентаря'
      f' с максимальным количеством очков выживания Том не выживет, значит, и при меньшем количестве очков тоже.')
