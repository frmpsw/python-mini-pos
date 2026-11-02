products = [
    {"name": "Coffee", "price": 70, "stock": 10},
    {"name": "Tea", "price": 55, "stock": 8},
    {"name": "Cake", "price": 120, "stock": 5}
]

def get_product(products,name):
    for product in products:
        if product["name"]==name:
          return product

def calculate_subtotal(product,quantity):
       total=product["price"]*quantity
       return total

def checkstock(product,quantity):
    if product["stock"]>=quantity:
        return True
    else:
        return False

def sell(product,quantity):
    if checkstock(product,quantity):
        product["stock"] -=quantity
        return product["stock"]
    
    else:
        return ("Not enough stock")

def process_sale(product,quantity):
    if checkstock(product,quantity):
        subtotal=calculate_subtotal(product,quantity)
        return subtotal
    else:
        return ("Not enough stock")

cart=[]

while True:
     namee=input("ชื่อสินค้า (กรอก exit เพื่อจบ) :")
     if namee == "exit":
       break
     product = get_product(products,namee)
     if product is None:
         print("ไม่พบสินค้านี้")
         continue

     try:
        quantity = int(input("จำนวน: "))
     except ValueError:
       print("กรุณากรอกจำนวนเป็นตัวเลขจำนวนเต็ม")
       continue
     
     #quantity = int(input("จำนวน: "))
     if quantity<=0:
         print("กรุณากรอกจำนวนสินค้ามากกว่า 0")
         continue
     
     already_in_cart = 0

     for item in cart:
       if item["name"] == product["name"]:
        already_in_cart += item["quantity"]

     if already_in_cart + quantity > product["stock"]:
      print("สินค้ามีไม่พอ")
      continue
      
     result = process_sale(product, quantity)
     if result==("Not enough stock"):
         print("สินค้ามีไม่พอ")
         continue
     

     cart.append({
        "name":product["name"],
        "quantity":quantity,
        "total":result
     })


     print("ยอดชำระ", result)
     print("จำนวนที่ยังเพิ่มลงตะกร้าได้:", product["stock"] - already_in_cart - quantity)
     print(cart)


if not cart:   
   print("ไม่มีสินค้าในตะกร้า ยกเลิกการชำระเงิน")
   exit()

totalprice=0

for item in cart:
     #print("name",thing["name"],"จำนวน",thing["quantity"],"ราคา",thing["total"])
     print(f'{item["name"]} x {item["quantity"]} = {item["total"]} บาท')
     totalprice+=item["total"]
print("ยอดรวมทั้งหมด:",totalprice)


while True:
      try: 
        money=int(input("เงินที่ลูกค้าจ่าย :"))
      except ValueError:
        print("กรุณากรอกจำนวนตัวเลข")
        continue
      
      if money<0:
       print("กรุณากรอกจำนวนตัวเลขบวก")
       continue
      elif money < totalprice:
       print("เงินขาดอีกจำนวน:",totalprice-money,"บาท")
       continue
      break
  
change = money - totalprice

for i in cart:                  
    product = get_product(products, i["name"])
    sell(product, i["quantity"])

print("เงินทอน:", change)



