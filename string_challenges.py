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
    if letters in 'А, О, У, Ы, Э, Е, Ё, И, Ю, Я':
        count += 1
print(count)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'

print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'

for words in sentence.split():
    print(words[0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'

avg = len(sentence.replace(' ', '')) / len(sentence.split())
print(avg)