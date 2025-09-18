#strings
print("Good morning")
print("He is called 'Kairat Nurtas'")
print('He is called "KN"')

#assign string to a variable
u = "AAAAAAA" 
print(u)

a = """Абай Құнанбайұлы 1845 жылы дүниеге келген. Абай Кунанбаев родился в 1845 году.
Abay Kunanbayev was born in 1845.""" #или можно просто ''' с тремя single quotes
print(a)

#достаем через индекс букву
b = "Salem"
print(b[0])

#loop through the letters
for x in "balmuzdaq":
  print(x) 

#string length
a = "Hello, hi!"
print(len(a))

#check string
txt = "London is the capital of the United Kingdom"
print("London" in txt)

#check with if-else
txt = "London is the capital of the United Kingdom"
if "lala" in txt:
  print("Yes")
else:
  print("No.")

#slicing strings
b = "Python, hello!!"
print(b[2:5])

#slice from the start
b = "Python, hiii"
print(b[:6])

#slice to the end
b = "Python, hiii"
print(b[2:])

#negative indexing
b = "Good morning!!!"
print(b[-5:-2])

#Upper case
a = "Hello, World!"
print(a.upper())

#Lower case
a = "Hello, World!"
print(a.lower())

#strip удаляет пробелы до и вначале текста
a = "      Hello, World!      "
print(a.strip())

#меняем места букв с replace
a = "Hello, World!"
print(a.replace("H", "M"))

#split - text between the specified separator becomes the list items
a = "Hello, World!"
print(a.split(",")) 

#CONCATENATION
a = "Hello"
b = "World"
c = a + "," + " " + b
print(c)

#FSTRINGS
age = 20
txt = f"My name is Aruzhan, I am {age}"
print(txt)

txt = f"The price is {743*43} tenge"
print(txt)

#ESCAPE CHARACTERS
txt = 'It\'s alright.'
print(txt)

txt = "Time to study\\ (backslash)."
print(txt) 

txt = "Hello\nWorld!" #new line
print(txt) 

txt = "Hello\nWorld!"
print(txt)  #Carriage Return

txt = "Hello\tWorld!"
print(txt) #TAB

txt = "Hello \bWorld!"
print(txt) 	#Backspace

#Octal value
txt = "\110\145\154\154\157"
print(txt) #A backslash followed by three integers will result in a octal value

#Hex value
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) #A backslash followed by an 'x' and a hex number represents a hex value

#STRING METHODS
txt = "hello, my name's Aruzhan." #capitalize
x = txt.capitalize()
print (x)

txt = "Hello, My Name's Aruzhan." #наоборот
x = txt.casefold()
print(x)

txt = "KBTU" #в центр 
x = txt.center(20)
print(x)

txt = "I love chocolates, they are my favorite" #count
x = txt.count("chocolates")
print(x)




