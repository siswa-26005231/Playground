limit = 100
start = 1

temp = []
prime = []

while start <= limit:
    for i in range(start):
        product = start % (i + 1)
        if product == 0:
            temp.append(product)
    if temp[0] == 0 and temp[-1] == 0 and len(temp) == 2:
        prime.append(start)
        temp = []
    else:
        temp = []
    start += 1
print(prime)
