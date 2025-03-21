numbers = [10, -5, 0, 23, -12, 0, 7]

# 10 is +ve
#-5 is -ve

for i in numbers:
  if i>0:
    print(i,"+ve")
  elif i<0:
    print(i,"-ve")
  else:
    print("number is zero")

   
# 1. Find Unique Elements in a List
list_1 = [1, 2, 3, 2, 4, 1, 5]
unique_list=[]

for i in list_1:
  if i not in unique_list:
    unique_list.append(i)
    #print(unique_list)
print(unique_list)
# [1,2,3,4,5]

# two array add

l=[10,20,30,40]
l2=[20.20,30.20,40.40,60.10]
print(l+l2)

#3. Find Maximum Value in a List
list_1 = [1, 2, 3, 2, 4, 1, 5]
max_value=list_1[0]# 1
for i in list_1:
  if i>max_value:#1>1,2>1,3>2,2>3,4>3,5>4
    max_value=i # 2,3,4,5

print(max_value)

#3. Find Maximum Value in a List

list_1 = [1, 2, 3, 2, 4, 1, 5]
min_value=list_1[0]# 1
for i in list_1:
  if i<min_value:#1>1,2>1,3>2,2>3,4>3,5>4
    min_value=i # 2,3,4,5

print(min_value)

#5. Find Max Key-Value Pair in a Dictionary

dict_1 = {'a': 10, 'b': 20, 'c': 5}
#print(dict_1['a'])
max_key=None
max_value=None
for i in dict_1:# i==a,b,c
  if max_key is None or dict_1[i]>max_value:# None or dict['a']>max_value
    max_key=i# 'a'
    max_value=dict_1[i]# 10
print(max_key,max_value) #'a',10

#2nd cond ,a,or dict['b']>10,20>10


#max_key=b,max_value=20

#3rd cond,b,5>20