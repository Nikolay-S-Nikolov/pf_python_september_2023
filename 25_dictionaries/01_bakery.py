data = input().split()

store = {}
for i in range(0,len(data),2):
    food = data[i]
    quantities = int(data[i+1])
    store[food] = quantities
print(store)
