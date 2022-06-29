with open("currency.txt") as f:
    lines = f.readlines()
    # print(lines)

currencydict = {}
for line in lines:
    parsed = line.split('\t')
    currencydict[parsed[0]]=parsed[1]

# print(currencydict)

amount = int(input("enter the amount in INR you want to convert\n"))
print("Available option are -")
# print(currencydict.keys())
[print(item) for item in currencydict.keys()]

print("select and enter the cuurency in which you want to convert \n")

currency_name = input()
print(f"{amount} is equal to {amount*float(currencydict[currency_name])} /-{currency_name}")


# Used data is copied from internet