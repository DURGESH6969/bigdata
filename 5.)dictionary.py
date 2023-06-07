n=int(input("Enter size of lists: "))
olist=[]
for i in range(0,n):
    e=int(input("ELements: "))
    olist.append(e)
dictionary={}
for i in olist:
    dictionary[i]=olist.count(i)
print("The count of elements in list: ",dictionary)
        