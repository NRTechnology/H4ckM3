f = open("data.dat", "r")
counter = 0
for str in f:
    if "0001" in str:
        counter+=1
        print(str)

print(counter)