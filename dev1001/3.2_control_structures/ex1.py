item_price=10
customer_has_coupon=False

if customer_has_coupon==True:
    final_price = item_price * 0.9

else:
    final_price = item_price

print (f"price: ${final_price:.2f}")