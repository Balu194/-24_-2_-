# TODO Напишите функцию find_common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

def find_common_participants(group1, group2, delimiter=","):
    set_group1 = set(group1.split(delimiter))
    set_group2 = set(group2.split(delimiter))
    return sorted(set_group1.intersection(set_group2))

participants_first_group = "Иванов,Петров,Сидоров"
participants_second_group = "Петров,Сидоров,Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group)
print(f"Общие участники: {', '.join(common_participants)}")
