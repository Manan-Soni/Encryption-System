#Da Vinci's Cryptex
n = int(input("No of rings : "))
crack = input("crack word : ")
letter = (input("Hint word : "))
letter_i = int(input("Hint word position : "))

l = []                      #Creating a list of rings
for i in range(n):
    print("Ring",i+1,":")
    x = input()
    l.append(x)

l1 = []                     #Indexes of first letter of crack in rings
for i in range(len(crack)):
    for j in range(len(l[0])):
        if l[i][j] == crack[i]:
            l1.append(j)
            break

l2 = []                     #Doubling ringes so we can cut out the desired part
for i in l:                 #from the middle
    i += i
    l2.append(i)


le = int(len(l2[0])/2)
lr = []
for i in range(5):          #creating a list of rings in the correct order
    t = l1[i]
    u = l2[i]
    lr.append(u[t:(le+t)])

lr
for i in range(len(lr)):    #Finding the index of hint word
    if i == letter_i:
        for j in range(len(lr[i])):
            if lr[i][j] == letter:
                li = j

for i in lr:                #Printing the secret Code
    print(i[li])