#Input=Robert000Smith000id123
#output={ “first_name”: “Robert”, “last_name”: “Smith”, “id”: “123” }

str1='Robert000Smith000id123'
new_list=str1.split('000')
l2=[]
l3=["first_name","last_name"]
for q in new_list:
    l2.append(q)
l2.pop()

str3=[y for y in new_list[2] if y.isalpha()]
str7=[y for y in new_list[2] if y.isdigit()]
str3=''.join(str3)
str7=''.join(str7)
l2.append(str7)
l3.append(str3)
d1=dict(zip(l3,l2))
print(d1)
print("****++++======================================================================================================================+++++****")
# count of each letter in dictionary for string
str4='robert000smith000id123'
l3=[]
l4=[]
for i in str4:
    l3.append(i)
    l4.append(str4.count(i))

d2=dict(zip(l3,l4))
print(d2)
