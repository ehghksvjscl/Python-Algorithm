snack_price, snack_count, cur_money = map(int,input().split())

snack_sum_price = snack_price * snack_count

def give_me_the_money(sum,cur):  
    if sum > cur:
        return sum - cur
    else:
        return 0

print(give_me_the_money(snack_sum_price,cur_money))