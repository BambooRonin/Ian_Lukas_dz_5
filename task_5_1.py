def uneven_nums_gen(last_num):
    for num in range(1, int(last_num) + 1, 2):
        yield num


nums = uneven_nums_gen(input('Введите макс. значение генератора: '))
print(*nums)
