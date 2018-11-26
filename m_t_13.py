s = input("input: ")
n = len(s)
count = 0

for i in range(0, n) :
    if s[i] == 'b' and s[i+1] == 'o' and s[i+2] == 'b' :
        count += 1


print("Number of times bob occurs is: %d" %count)