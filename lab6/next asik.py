#1
import os
p = input("Path: ")

print("Dirs:")
for x in os.listdir(p):
    if os.path.isdir(os.path.join(p, x)):
        print(x)

print("\nFiles:")
for x in os.listdir(p):
    if os.path.isfile(os.path.join(p, x)):
        print(x)

print("\nAll:")
for x in os.listdir(p):
    print(x)

#2
import os
a = input("Path: ")
print(os.path.exists(a))
print(os.access(a, os.R_OK))
print(os.access(a, os.W_OK))
print(os.access(a, os.X_OK))


#3
import os
p = input("Path: ")
if os.path.exists(p):
    print("ok")
    print(os.path.dirname(p))
    print(os.path.basename(p))
else:
    print("no")


#4
f = input("File: ")
n = 0
for _ in open(f, "r"):
    n += 1
print(n)


#5
a = ["a", "b", "c"]
f = open("out.txt", "w")
for x in a:
    f.write(x + "\n")
f.close()

#6
for i in range(65, 91):
    open(chr(i)+".txt", "w").close()

#7
s = input("Src: ")
d = input("Dst: ")
open(d, "w").write(open(s).read())

#8
import os
p = input("File: ")
if os.path.exists(p) and os.access(p, os.W_OK):
    os.remove(p)
    print("del")
else:
    print("no")



