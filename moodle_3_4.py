def single_root_words(root_word, *other_words): #1.	Объявляем функцию с параметрами
    same_words =[] # 2.	Создаем внутри функции пустой список
    required_word = list(other_words) # ограничиваемся длиной списка

    for i in range(len(required_word)): # 3.	При помощи цикла for перебераем  подходящие слова
         if root_word.lower() in required_word[i].lower() or required_word[i].lower() in root_word.lower():
             # условие, при котором добавляются слова в результирующий список same_words.
            same_words.append(required_word[i]) # добавляем список подходящими словами

    return (same_words)
# Вызоваем функцию
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)

