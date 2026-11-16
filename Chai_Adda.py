CHAI ADDDA - CAFE MANAGEMENT SYSTEM

def menu():
    print("\n========== CHAI ADDDA ==========")
    print("           MENU CARD")
    print("================================")
    print("1. Cutting Chai       - Rs.12")
    print("2. Masala Chai        - Rs.20")
    print("3. Ginger Chai        - Rs.20")
    print("4. Elaichi Chai       - Rs.25")
    print("5. Kulhad Chai        - Rs.30")
    print("6. Irani Chai         - Rs.30")
    print("7. Bun Maska          - Rs.35")
    print("8. Samosa             - Rs.15")
    print("9. Veg Sandwich       - Rs.50")
    print("10. Maggi             - Rs.40")
    print("0. Finish Order")
    print("================================")


def main():
    items = [
        "Cutting Chai", "Masala Chai", "Ginger Chai",
        "Elaichi Chai", "Kulhad Chai", "Irani Chai",
        "Bun Maska", "Samosa", "Veg Sandwich", "Maggi"
    ]

    prices = [12, 20, 20, 25, 30, 30, 35, 15, 50, 40]

    cart = []
    total = 0

    print("WELCOME TO CHAI ADDDA!")

    name = input("Enter Customer Name: ")
    mobile = input("Enter Mobile Number: ")

    print("\n1. Dine In")
    print("2. Take Away")

    choice = input("Select Order Type: ")

    if choice == "1":
        order_type = "Dine In"
    else:
        order_type = "Take Away"

    while True:
        menu()

        try:
            item_no = int(input("Enter Item Number: "))

            if item_no == 0:
                break

            if item_no < 1 or item_no > 10:
                print("Invalid Item Number!")
                continue

            qty = int(input("Enter Quantity: "))

            if qty <= 0:
                print("Quantity must be positive!")
                continue

            index = item_no - 1
            amount = prices[index] * qty

            cart.append((items[index], qty, amount))
            total = total + amount

            print(items[index], "added successfully!")

        except ValueError:
            print("Please enter a valid number!")

    if total == 0:
        print("No items ordered!")
        return

    print("\nSelect Payment Method")
    print("1. Cash")
    print("2. UPI")

    payment = input("Enter Choice: ")

    if payment == "1":
        payment_method = "Cash"
    elif payment == "2":
        payment_method = "UPI"
    else:
        payment_method = "Not Selected"

    print("\n========== FINAL RECEIPT ==========")
    print("CHAI ADDDA - CAFE")
    print("-----------------------------------")
    print("Customer:", name)
    print("Mobile:", mobile)
    print("Order Type:", order_type)
    print("-----------------------------------")

    for item, qty, amount in cart:
        print(item, "x", qty, "=", "Rs.", amount)

    print("-----------------------------------")
    print("TOTAL BILL: Rs.", total)
    print("Payment:", payment_method)
    print("-----------------------------------")
    print("THANK YOU FOR VISITING!")
    print("VISIT AGAIN!")
    print("===================================")


main()