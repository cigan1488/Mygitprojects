text = "i love python programming in python" # tehtava 1
#Заменяю питон на Питон
replaced_text = text.replace('python', 'Python')
print(replaced_text)

text1 = 'Hello World!' # tehtava 2
# меняю заглавыне буквы и строчные между собой
swapcased_text = text1.swapcase()
print(swapcased_text)

a = "Hello World!" # tehtava 3
# использую index slicing и беру значение элемента по индексу
print(a[6:11])

b = "   Python is awesome!" # Tehtava 4
# использую метод strip и убираю все пробелы
x = b.strip()
print(x)

txt = "Python" # tehtava 5
#использую метод center и переношу значение переменной txt на 20 табов вперед в строке
x = txt.center(20)
print(x)

txt = "python is a great language" # tehtava 6
# изменяю первый элемент каждого слова на верхний зеристор
x = txt.title()
print(x)

txt = "banana sandwich" # tehtava 7
# с помощью метода count определяю колво одинаковых элементов в строке
x = txt.count("a")
print(x)

#используя метод maketrans первым параметром позначаю какие элементы буду убирать,вторым на что 
txt = str.maketrans("eauiuyo", "       ") #tehtava 8
s = "beautiful python"
res = s.translate(txt)
#используя метод translate осуществляю изменения метода maketrans в переменной txt
res = s.translate(txt)
# с помощью join(res.split()) убираю пробелы во всей строке
v = ''.join(res.split())
print(v)

x = "Python Programming" # tehtava 9
# используя слайсы с нег шагом по примеру [start:end:step] переворачиваю все предложение
print(x[-1:-19:-1])

x = "I have a cat and a dog"
x1 = x.replace("cat","animal")
x2 = x.replace("dog","animal")
print(x1,"\n",x2)