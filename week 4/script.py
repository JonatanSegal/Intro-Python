# List comprehensions

l = []
for i in range(10):
    l.append(i)


lRange = [i for i in range(10)]

lenList = [len(i) for i in ['Hello','text','Ola']]

capitalList = [chr(i) for i in range(65,91)]
#print(capitalList)

excludeList = [chr(i) for i in range(65,91) if i not in [70,75,80,85]]
#print(excludeList)

fToOList = [chr(i) for i in range(65,91) if i not in range(70,78,2)]
#print(fToOList)

color = ['Black','White']
size = ['s','m','l','xl']

shop = [(i,j) for i in color for j in size]
print(shop)

soled_out = [('Black', 'm'), ('White', 's')]
shop = [(i,j) for i in color for j in size if (i,j) not in soled_out]
print(shop)
