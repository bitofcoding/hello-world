t = int(input())

for z in range(t):
    data = input()
    prime = 0
    for i in range(len(data)):
        for j in range(len(data)):
            value = 0
            count = 0
            a = []
            sub_string = data[i: j]
            for k in range(len(sub_string)):
                a.append(sub_string[k])
            for l in a:
                if int(l) == 1:
                    value += 2**int(l)
                else:
                    value += 0
            for m in range(1, value+1):
                if value % m == 0:
                    count += 1
            if count == 2:
                prime += 1
    if prime > 0:
        print("Yes")
    else:
        print("No")
        print("I DONT CARE MAN")
