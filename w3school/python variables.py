x = "I'm"
y = 20
print(x)
print(y) #creating variables

z = 8
z = "haha zamenaa"
print(z) #it's not neccessary to add variable types, variable's type can change 

#если хочется, можно добавить type с помощью casting
u = str(8)
q = int(4)
p = float(3)
print (u)
print(q)
print(p)

#get the type using TYPE() function
l = 5
n = "Blabla"
print(type(l))
print(type(n))


##double quotes are the same as single quotes
o = "Almaty"
print(o)
o = 'Almaty'
print(o) 

#variables names are case-sensitive, this will create two different variables
w = "Salem"
W = 11
print(w)
print(W) 

#VARIABLE NAMES
hisname = "Kairat" 
his_name = "Kairat"
_his_name = "Kairat"
hisName = "Kairat"
HISNAME = "Kairat"
hisname2 = "Kairat"
#переменная должна начинаться с буквы или _ ; не может начинатьсяс цифры; cостоит только из букв цифр и _; 
# они case-sensitive (hello, Hello, HELLO - разные variables)
#НЕЛЬЗЯ: 777vip = "Camry"; 777-vip = "Camry"; 777 vip = "Camry"

#ASSIGN MULTIPLE VALUES
t, r, g = "Labubu", "Labu Labu", "Labubuu"
print(t)
print(r)
print(g)

#или можно дать одно значение одной переменной
s = h =  c = "Hello"
print(s)
print(h)
print(c)

numbers = ["raz", "dva", "tri"]
z, c, h = numbers
print(z)
print(c)
print(h)

#output multiple variables
x = "Python"
y = "och"
z = "prikolni"
print (x,y,z) #or print(x+y+z)

x = 5
y = "Good"
print (x, y  ) #nelzya print(x+y) tut

i = "super" #i -> global variable, it can be used anywhere
def myfunc() :
    print ("Pogoda prosto" + " " + i)
myfunc()





