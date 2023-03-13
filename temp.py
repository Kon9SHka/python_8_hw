dict = [["God of War (2018)", "2018", "Action/RPG","Пройдена", ""],
        ["Horizon Zero Dawn","2018", "Action/RPG","В процессе", "Сюжет топ"],
        ["FIFA 23","2022", "Sport", "В процессе", "игра говно"]]
print(dict[1][1])
# dict_2 = [("God of War",{"Игра": "God of War (2018)", "Год Выпуска": 2018})]
#         #   ("Horizon Zero Dawn",{"Игра": "Horizon Zero Dawn", "Год Выпуска": 2018})]
# print (dict_2(1))

# поиск

dict_column = ["Название","Год","Жанр","Статус","Комментарий"]
# place = dict_column.index(input(f"Осуществить поиск по {dict_column}: "))
# chek_data = str(input(f"Введите {dict_column[place]}: "))
# for i in range (0,len(dict)):
#     if dict[i][place] == chek_data:
#         print(dict[i])
        
# chek_data = str(input(f"Введите Название игры: "))
# for i in range (0,len(dict)):
#         if dict[i][0] == chek_data:
#             break
# return i



# for i in range(0,len(dict)):
#     array.append(input(f'Введите {dict_column[i]}:'))
    
# print(array)


game_for_change = dict[1]
command = str(input("Что вы хотите изменить? "))
print(command)

if command == "все":
    for i in range (0,len(game_for_change)):
        game_for_change[i]=str(input(f"Введите {dict_column[i]} для изменения: "))
elif command not in dict_column:
    print("Нет такого поля!")
else :
    place = dict_column.index(command)
    game_for_change[place] = str(input(f'Введите изменения по {dict_column[place]} :'))

print(dict[1])