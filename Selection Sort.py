# Recall the “Building Block” strategy discussed in class. Using this strategy:
# a. Implement “moveMin” algorithm as building block (as a function).
# b. Implement “Selection Sort” algorithm using “moveMin” as the building block.
# c. Test your program on 10 integers taken as input from user.



def Move_Min(List):
    
    for i in range(len(List)-1,0,-1):
        Minimum = 0
        
        for j in range(1 , i+1):
            if List[j] > List[Minimum]:
                Minimum = j
                
        Value = List[i]
        List[i] = List[Minimum]
        List[Minimum] = Value
        print(List)
def Selection_Sort(K):
    #to call Move_Min function as a builidng Block
    return Move_Min(K)

#Driver Code to get input from the user
List1 = []
List_Limit = input("How many numbers you want to store: ")
print("Enter your Numbers for the list Please: ")
for i in range(int(List_Limit)):
    N = int(input(" "))
    List1.append(N)
print("The Original List is: ")
print(List1)
print("The Sorted List is Given Below: ")
Selection_Sort(List1)
print(List1)