def splitevenodd(A):
    evenlist=[]
    oddlist=[]
    for i in A:
        if(i%2==0):
            evenlist.append(i)
        else:
            oddlist.append(i)
    print("Even List: ",evenlist)
    print("Odd List: ",oddlist)
A=list()
n=int(input("Enter the size of the first list:: "))
print("Enter elements of first list: ")
for i in range(int (n)):
    k=int(input(" "))
    A.append(k)
splitevenodd(A)