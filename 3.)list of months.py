list_of_months=[]
n=int(input("Enter the number of months in the list: "))
for i in range(0,n):
    s=input("Month: ")
    list_of_months.append(s[:3].capitalize())
print("The list of months with 3 characters are: ",list_of_months)    