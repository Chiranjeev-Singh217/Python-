print("my frist program")

#for user input

#name=input("enter your name:")
#print(name)

#implement string
name="ramsita"
print(name)

print(name[2])

#string slicing it will not t6ake last element
name="hanuman"
print(name[0:4])

#string function
print(name.count("a"))
print(name.endswith("an"))
print(name.find("u"))
print(name.capitalize())
print(name.replace("a","u"))


#looping in python
#1.for loop :-range contain 3 things (start,stop,step)
for i in  range(1,5,2):
    print(i)
    
# for loop :-when range have(start,stop) it will take by default step =1
for i in  range(1,5):
    print(i) 

# for loop :-when range have(stop) it will take by default step =1 or start =0
for i in  range(5):
    print(i) 
    
#other way to use for loop
print(*range(1,5,1))


#break continue pass

#break
for i in  range(1,5,1):
    if i==3:
        break
    print(i)
else:
    print(0)    

#continue
for i in  range(1,5,1):
    if i==3:
        continue
    print(i)
else:
    print(0)    

