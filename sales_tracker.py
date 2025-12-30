sales = {}

while True:
    print("================================")
    print("   COMPANY DAILY SALES TRACKER  ")
    print("================================")

    print("\n1. Add daily sales")
    print("2. View all sales")
    print("3. Total sales")
    print("4. Average sales")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        date = input("Enter date (YYYY-MM-DD): ")
        amount = int(input("Enter sales amount: "))
        sales[date] = amount
        print("✅ Sales added successfully")

    elif choice == "2":
        if not sales:
            print("No sales data available")
        else:
            print("\n--- All Sales ---")
            for date, amount in sales.items():
                print(date, "→ ₹", amount)

    elif choice == "3":
        if not sales:
            print("No sales data available")
        else:
            total = sum(sales.values())
            print("💰 Total Sales: ₹", total)

    elif choice == "4":
        if not sales:
            print("No sales data available")
        else:
            avg = sum(sales.values()) / len(sales)
            print("📊 Average Sales: ₹", avg)

    elif choice == "5":
        print("Bye 👋 Program closed")
        break

    else:
        print("Invalid choice, try again")

