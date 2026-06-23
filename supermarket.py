# ========================================
# SUPERMARKET INVENTORY SYSTEM
# Author: Moh Yaseen Siddiqui
# ========================================

# Inventory: 5 categories, 4 items each
inventory = {
    "Fruits":     {"Apple": 10, "Banana": 12, "Mango": 8,  "Orange": 6},
    "Vegetables": {"Potato": 15, "Tomato": 9, "Onion": 11, "Carrot": 7},
    "Dairy":      {"Milk": 5,   "Cheese": 4, "Butter": 6, "Yogurt": 8},
    "Bakery":     {"Bread": 10, "Bun": 7,    "Cake": 3,   "Cookies": 9},
    "Beverages":  {"Coke": 12,  "Juice": 8,  "Water": 20, "Tea": 6},
}

# Price list for billing
prices = {
    "Apple": 20, "Banana": 10, "Mango": 50, "Orange": 25,
    "Potato": 15, "Tomato": 18, "Onion": 22, "Carrot": 30,
    "Milk": 28, "Cheese": 80, "Butter": 60, "Yogurt": 35,
    "Bread": 40, "Bun": 25, "Cake": 200, "Cookies": 55,
    "Coke": 40, "Juice": 70, "Water": 20, "Tea": 90,
}


# ---------- (a) Display all items by category ----------
def display_inventory():
    print("\n===== SUPERMARKET INVENTORY =====")
    for category, items in inventory.items():
        print(f"\n[{category}]")
        for item, qty in items.items():
            print(f"   - {item}: {qty}")


# ---------- (b) Count total items ----------
def total_count():
    total = sum(qty for items in inventory.values() for qty in items.values())
    print(f"\nTotal items in inventory: {total}")
    return total


# ---------- (d) Low-stock notification ----------
def check_low_stock():
    print("\n--- Low Stock Alerts ---")
    alerts = []
    for category, items in inventory.items():
        for item, qty in items.items():
            if qty < 3:
                msg = f"WARNING: {item} ({category}) low - only {qty} left!"
                print(msg)
                alerts.append(msg)
    if not alerts:
        print("All items sufficiently stocked.")
    return alerts


# Helper: find which category an item belongs to
def find_category(item):
    for cat, items in inventory.items():
        if item in items:
            return cat
    return None


# ---------- (c) Billing page ----------
def billing_page():
    cart = {}
    print("\n===== BILLING PAGE =====")
    while True:
        action = input("\n(a)dd / (r)emove / (c)heckout / (q)uit: ").strip().lower()

        if action == 'a':
            item = input("Item name: ").strip().title()
            try:
                qty = int(input("Quantity: "))
            except ValueError:
                print("Invalid quantity.")
                continue

            cat = find_category(item)
            if not cat:
                print(f"Item '{item}' not found in inventory.")
                continue
            if inventory[cat][item] < qty:
                print(f"Only {inventory[cat][item]} in stock.")
                continue

            inventory[cat][item] -= qty
            cart[item] = cart.get(item, 0) + qty
            print(f"Added {qty} x {item}. Stock remaining: {inventory[cat][item]}")
            check_low_stock()  # Auto-check after each add

        elif action == 'r':
            item = input("Item to remove: ").strip().title()
            if item not in cart:
                print("Item not in cart.")
                continue
            try:
                qty = int(input(f"Remove how many (in cart: {cart[item]}): "))
            except ValueError:
                print("Invalid quantity.")
                continue

            cat = find_category(item)
            qty = min(qty, cart[item])
            cart[item] -= qty
            inventory[cat][item] += qty
            if cart[item] == 0:
                del cart[item]
            print(f"Removed {qty} x {item}. Stock now: {inventory[cat][item]}")

        elif action == 'c':
            if not cart:
                print("Cart is empty.")
                continue
            total = 0
            print("\n----- BILL -----")
            for item, qty in cart.items():
                amt = prices.get(item, 0) * qty
                print(f"{item} x {qty} = Rs.{amt}")
                total += amt
            print(f"-----------------\nTOTAL: Rs.{total}")
            print("Thank you for shopping!")
            cart.clear()
            break

        elif action == 'q':
            print("Exited billing.")
            break

        else:
            print("Invalid option. Choose a/r/c/q.")

# ---------- (e) NEW: Senior Citizen Discount ----------
def apply_discount(amount, is_senior=False):
    """
    Apply a 10% discount for senior citizens.

    Args:
        amount: Total bill amount
        is_senior: True if customer is 60+

    Returns:
        Final amount after discount
    """
    if amount < 0:
        raise ValueError("Amount cannot be negative")

    if is_senior:
        discounted = amount * 0.9  # 10% off
        return round(discounted, 2)
    return amount

# ---------- Main Menu ----------
def main():
    while True:
        print("\n========================================")
        print("  SUPERMARKET INVENTORY SYSTEM MENU")
        print("========================================")
        print("1. Display Inventory")
        print("2. Total Item Count")
        print("3. Billing Page")
        print("4. Check Low Stock")
        print("5. Exit")
        choice = input("Choose option (1-5): ").strip()

        if choice == '1':
            display_inventory()
        elif choice == '2':
            total_count()
        elif choice == '3':
            billing_page()
        elif choice == '4':
            check_low_stock()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()