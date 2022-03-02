Total_products=eval(input("Enter the number of products: "))
dict={}
for i in range(Total_products):
  name=input("Enter the name of the product: ")
  price=eval(input("Enter the price of the product: "))
  dict[name]=price             

# while true is used for repetition as in the question
while True:
  namecheck=input("Enter the product name for the price: ")
  if namecheck in dict:
    print("The price of ",namecheck," is",dict[name])
  else:
    print("The entered product is not in the entered dictionary. ")