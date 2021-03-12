from itertools import islice
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Светлана',
    'Владимир', 'Ярослав', 'Ольга'
]
classes = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

joint_l = ((tutors[i], classes[i]) if len(classes) > i else (tutors[i], None) for i in range(len(tutors)))

print(type(joint_l), *joint_l)
print(list(islice(joint_l, 1)))
