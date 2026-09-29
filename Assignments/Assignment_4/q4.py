item = "jacket"
unitprice = 20.22
quantity = 20
tax= .05
subtotal = unitprice * quantity
taxamount = subtotal * tax
total = subtotal + taxamount
print(f"subtotal: ${subtotal:.2f}")
print(f"taxamount: ${taxamount:.2f}")
print(f"total: ${total:.2f}")
