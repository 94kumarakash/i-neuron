price=int(input("Enter Price : "))
if price > 500:
    print("I won't be able to buy")
elif price<500:
    print("ok...buy")
elif price==500:
    print("Bargain")
else:
    print("I Don't Know")