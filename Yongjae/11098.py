n = int(input())
if n <= 100:
    for i in range(n):
        dic_price = {}
        max_vlaue = 0
        players = int(input())
        if 1 <= players <= 100:
            for j in range(players):
                price, name = input().split()
                price = int(price)
                name = name.strip()
                dic_price[price] = name
            max_key = max(dic_price.keys())
            print(dic_price[max_key])