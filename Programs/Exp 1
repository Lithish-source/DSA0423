prices = [50, 30, 20]
quantities = [2, 3, 1]

discount_rate = 10
tax_rate = 5

subtotal = 0
for i in range(len(prices)):
    subtotal += prices[i] * quantities[i]

discount_amount = (discount_rate / 100) * subtotal
after_discount = subtotal - discount_amount

tax_amount = (tax_rate / 100) * after_discount
total_cost = after_discount + tax_amount

print("Subtotal:", subtotal)
print("Discount Amount:", discount_amount)
print("Tax Amount:", tax_amount)
print("Final Total Cost:", total_cost)
