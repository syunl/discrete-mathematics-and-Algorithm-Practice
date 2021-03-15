# 買票系統:判斷歲數和有無其他福利
def ticket_price(age, price, welfare=False):
    if age <= 12:
        return price * 0.5
    elif age <= 18 or welfare:
        return price * 0.75
    elif age >= 19:
        return price


client1 = ticket_price(50, 1000, True)
client2 = ticket_price(3, 300)
client3 = ticket_price(17, 600)
print(client1)
print(client2)
print(client3)
