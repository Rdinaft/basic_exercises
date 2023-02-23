# Вывести последнюю букву в слове
word = 'Архангельск'

print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'

print(word.lower().count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'

count = 0
for letters in word.upper():
    if letters in 'АОУЫЭЕЁИЮЯ':
        count += 1
print(count)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'

print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'

for letters in sentence.split():
    print(letters[0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'

avg_word_length = len(sentence.replace(' ', '')) / len(sentence.split())
print(avg_word_length)