src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
src_unique = set()
src_set = set()
for i in src:
    if i not in src_set:
        src_unique.add(i)
    else:
        src_unique.discard(i)
    src_set.add(i)

print(src_unique)