from loguru import logger

new_list=[]
for i in range(1,11):
    if i%2==0:
        new_list.append(i)
print(new_list)

# LIST_COMPREHENSION
new_list=[i for i in range(1,11) if i%2==0]
print(new_list)


#  New list with even and odd
new_list=["Even" if i%2==0 else "Odd" for i in range(1,11)]
print(new_list)