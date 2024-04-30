def coffee_write(brand, price):
    outf = open("coffee_sort.txt", "w")
    for cr in sorted(brands.keys(), reverse=False):
        outf.write(cr + ':' + brands[cr] + ':' + prices[cr])
    outf.close()

inf = open("coffee.txt")
brands ={}
prices = {}

for line in inf:
    (country, brand, price) = line.split(',')
    brands[country] = brand
    prices[country] = price

inf.close()

for countries in brands.keys():
    print(countries + " / " + brands[countries] + " / " + str(prices[countries]))

coffee_write(brands, prices)


