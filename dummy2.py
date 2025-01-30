#input = [[5, 8], [2, 9], [5, 12], [16, 5]]
#output = (5, 3)

input1=[[5, 8], [2, 9], [5, 12], [16, 5]]

numbers=[i for x in input1 for i in x]
occurance= max([numbers.count(o) for o in numbers])
output=[]

for i in numbers:
    if numbers.count(i)==occurance:
        output.extend([i,occurance])
        break
output=tuple(output)
print(output)

lst  = [7382, 346, 67, 91]
# o/p = [2, 1, 4, 1]

l1=list(map(str,lst))
l2=[]
for i in range(len(l1)):
   l2.append(str(sum([int(n) for n in l1[i]])))
op=[]
for op1 in range(len(l2)):
    op.append(sum([int(n) for n in l2[op1]]))


print(l2)
print(op)


# import requests
#
# url="http://www.google.com/"
# payload={
#     "firstname" : "Prateek",
#     "lastname" : "Brown",
#     "totalprice" : 111,
#     "depositpaid" : True,
#     "bookingdates" : {
#         "checkin" : "2018-01-01",
#         "checkout" : "2019-01-01"
#     },
#     "additionalneeds" : "Breakfast"
# }'
# headers={"Content-Type":"application/json"}
# response=requests.post(url=url,json=payload,headers=headers)
# assert response.status_code==201

#decorators

# def my_decorator(func):
#     def wrapper():
#         print("Something is getting executed before function")
#         func()
#         print("Something is getting executed after function")
#     return wrapper
#
# @my_decorator
# def existing_function():
#     print("I am getting executed in between")
#
# existing_function()