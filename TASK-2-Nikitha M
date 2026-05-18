
from datetime import date, timedelta
import matplotlib.pyplot as plt
import numpy as np
expenses = []
limits = {}  
today = date.today()
today_str = today.strftime("%d/%m/%Y")
day = today.strftime("%A")

def choose_category():
    categories = {
        "Living & Housing": ["Rent / Hostel / PG", "Mortgage / Home Loan", "House Rent", "Home Maintenance",
                             "Home & Supplies", "Utilities", "Water & Electricity", "Gas / LPG",
                             "Internet & Broadband", "Mobile Recharge & Plans", "Insurance (House / Renters)", "Property Tax"],
        "Food & Groceries": ["Groceries", "Vegetables & Fruits", "Milk & Dairy", "Snacks & Beverages",
                             "Food (Eating Out)", "Restaurants & Cafes", "Street Food", "Desserts & Sweets"],
        "Transport & Vehicle": ["Public Transport", "Auto / Cab", "Fuel / Petrol / Diesel",
                                "Vehicle Service & Repairs", "Toll, Parking, Parking Tickets",
                                "Vehicle Insurance", "Vehicle Loan / EMI"],
        "Health & Fitness": ["Medical Consultation", "Medicines", "Medical Tests", "Health Insurance",
                            "Fitness / Gym", "Yoga / Online Classes", "Sports & Equipment",
                            "Dental Care", "Vision / Eye Care"],
        "Personal Care": ["Haircut / Salon", "Skincare & Cosmetics", "Bath & Body Care",
                         "Shaving / Grooming", "Perfume / Deodorant"],
        "Education & Learning": ["Tuition Fees", "School / College Fees", "Books & Notes",
                                "Online Courses", "Educational Apps & Tools", "Software for Learning",
                                "Exam Fees", "Stationery & Supplies"],
        "Entertainment": ["Movies & Cinema", "OTT Subscriptions (Netflix, Prime, etc.)",
                         "Music Streaming", "Gaming & In‑app Purchases", "Concerts / Events",
                         "Hobbies & Creative Supplies", "Magazines / Subscriptions"],
        "Shopping & Lifestyle": ["Clothing & Apparel", "Footwear", "Accessories (bags, wallets, watches)",
                                "Electronics & Gadgets", "Home Decor", "Kitchenware", "Tools & Equipment"],
        "Travel & Outings": ["Domestic Trips", "International Travel", "Flight Tickets", "Train / Bus Tickets",
                            "Hotel / Stay", "Cabs & Local Transport (travel)", "Sightseeing / Tickets",
                            "Food during Travel"],
        "Financial & Debt": ["EMI / Loan Repayment", "Credit Card Payment", "Bank Fees & Charges",
                            "ATM / Transaction Charges", "Insurance (Life / Term / Vehicle)",
                            "Savings / Investment Contribution", "Emergency Fund Deposit"],
        "Gifts & Donations": ["Birthday Gifts", "Festival Gifts", "Charity / Donations",
                             "Wedding / Ceremony Gifts", "Greeting Cards & Wrapping"],
        "Pets & Kids": ["Pet Food", "Pet Grooming", "Pet Vet / Medical", "Pet Toys & Supplies",
                       "Kids Stationery", "Kids Clothing", "Kids Activities / Classes", "Toys & Games"],
        "Subscriptions & Memberships": ["Streaming Services", "Cloud Storage / Backup",
                                        "App Subscriptions", "Club / Community Memberships",
                                        "Co‑working / Library Memberships"],
        "Miscellaneous": ["Unexpected Repairs", "Emergency Cash", "Other"]
    }

    print("Categories:")
    for i, cat in enumerate(categories, 1):
        print(i, cat)

    try:
        ch_main = int(input("Enter category number: "))
        main_cat = list(categories.keys())[ch_main - 1]
    except (ValueError, IndexError):
        print("Invalid choice!")
        return None, None, None

    sub_cats = categories[main_cat]
    print("Sub‑categories:")
    for i, sub in enumerate(sub_cats, 1):
        print("  ", i, sub)

    try:
        ch_sub = int(input("Enter sub‑category number: "))
        selected = sub_cats[ch_sub - 1]
    except (ValueError, IndexError):
        print("Invalid choice!")
        return None, None, None

    try:
        amount = float(input("Enter amount spent: ₹ "))
    except ValueError:
        print("Invalid amount!")
        return None, None, None

    print(f"\nYou spent ₹ {amount} on {selected} ({main_cat}).")
    return main_cat, selected, amount


# --- 1. Add expense (user‑friendly flow)
def add_expense():
    print("\nThat's great, let's kick off!")
    while True:
        print("\nEnter a new expense:")
        main_cat, sub_cat, amount = choose_category()
        if main_cat is None:
            continue

        desc = input("Description (optional): ")

        expense = {
            "Main Category": main_cat,
            "Category": sub_cat,
            "Amount spend": amount,
            "Date": today,
            "Description": desc
        }
        expenses.append(expense)
        print("✅ Expense saved!")

        ans = input("\nWanna add more? (yes/no): ").strip().lower()
        if ans != "yes":
            break
          
def display_expenses():
    if not expenses:
        print("\nNo expenses recorded yet!")
        return

    print("\n━━ All Expenses ━━━")
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. ₹ {exp['Amount spend']:.2f} | {exp['Category']} ({exp['Main Category']}) "
              f"| {exp['Date'].strftime('%d/%m/%Y')}")

def set_limits():
    print("\n━━ Set Budget Limits ━━━")
    for cat in set(exp["Main Category"] for exp in expenses):
        try:
            lim = float(input(f"Limit for '{cat}' (₹): "))
            limits[cat] = lim
        except ValueError:
            print(f"Skipping invalid limit for '{cat}'.")

def weekly_summary():
    now = today
    week_ago = now - timedelta(days=6)

    weekly = [e for e in expenses if week_ago <= e["Date"] <= now]
    if not weekly:
        print("\nNo expenses in the last 7 days.")
        return

    totals = {}
    for e in weekly:
        cat = e["Main Category"]
        totals[cat] = totals.get(cat, 0) + e["Amount spend"]

    print("\n━━ Weekly Summary (last 7 days) ━━━")
    total_week = 0
    for cat, total in totals.items():
        total_week += total
        print(f"  {cat}: ₹ {total:.2f}")

    print(f"\nTotal this week: ₹ {total_week:.2f}")

def monthly_summary():
    now = today
    month_ago = now - timedelta(days=30)

    monthly = [e for e in expenses if month_ago <= e["Date"] <= now]
    if not monthly:
        print("\nNo expenses in the last 30 days.")
        return

    totals = {}
    for e in monthly:
        cat = e["Main Category"]
        totals[cat] = totals.get(cat, 0) + e["Amount spend"]

    print("\n━━ Monthly Summary (last 30 days) ━━━")
    total_month = 0
    for cat, total in totals.items():
        total_month += total
        print(f"  {cat}: ₹ {total:.2f}")

    print(f"\nTotal this month: ₹ {total_month:.2f}")

def show_pie_chart(exp_list, title):
    totals = {}
    for e in exp_list:
        cat = e["Main Category"]
        totals[cat] = totals.get(cat, 0) + e["Amount spend"]

    if not totals:
        print(f"No data for {title.lower()}.")
        return

    cats = list(totals.keys())
    amounts = list(totals.values())
    percents = [100 * a / sum(amounts) for a in amounts]

    cats = np.array(cats)
    percents = np.array(percents)
    plt.figure(figsize=(8, 6))
    wedges, texts, autotexts = plt.pie(
        percents,
        labels=cats,
        autopct=lambda p: f'{p:.1f}%',
        startangle=90
    )
    plt.title(title)
    plt.tight_layout()
    plt.show()

def dashboard():
    if not expenses:
        print("\nNo expenses to show in dashboard yet.")
        return

    print("\n━━ Dashboard ━━━")
    print("1. Today's expenses")
    print("2. This week (7 days)")
    print("3. This month (30 days)")

    try:
        ch = int(input("Choose time range: "))
    except ValueError:
        print("Invalid choice.")
        return

    now = today

    if ch == 1:
        target = [e for e in expenses if e["Date"] == now]
        show_pie_chart(target, f"Expenses Today — {now.strftime('%d/%m/%Y')}")

    elif ch == 2:
        week_ago = now - timedelta(days=6)
        target = [e for e in expenses if week_ago <= e["Date"] <= now]
        show_pie_chart(target, f"Weekly Expenses ({week_ago.strftime('%d/%m/%Y')} – {now.strftime('%d/%m/%Y')})")

    elif ch == 3:
        month_ago = now - timedelta(days=30)
        target = [e for e in expenses if month_ago <= e["Date"] <= now]
        show_pie_chart(target, f"Monthly Expenses ({month_ago.strftime('%d/%m/%Y')} – {now.strftime('%d/%m/%Y')})")
    else:
        print("Invalid choice.")
      
def delete_expense():
    if not expenses:
        print("\nNo expenses to delete.")
        return

    display_expenses()
    try:
        idx = int(input("\nEnter expense number to delete: ")) - 1
        if 0 <= idx < len(expenses):
            del_exp = expenses.pop(idx)
            print(f" Deleted: ₹ {del_exp['Amount spend']:.2f} on {del_exp['Category']}.")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a number.")


# --- 9. Edit an expense
def edit_expense():
    if not expenses:
        print("\nNo expenses to edit.")
        return

    display_expenses()
    try:
        idx = int(input("\nEnter expense number to edit: ")) - 1
        if 0 <= idx < len(expenses):
            exp = expenses[idx]
            print(f"Editing: ₹ {exp['Amount spend']:.2f} on {exp['Category']} "
                  f"({exp['Main Category']}, {exp['Date'].strftime('%d/%m/%Y')})")

            main_cat, sub_cat, amount = choose_category()
            if main_cat is None:
                print("Edit cancelled.")
                return

            new_desc = input("New description (Enter to keep old): ")
            if not new_desc:
                new_desc = exp["Description"]

            expenses[idx] = {
                "Main Category": main_cat,
                "Category": sub_cat,
                "Amount spend": amount,
                "Date": exp["Date"],
                "Description": new_desc
            }
            print(" Expense updated!")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a number.")
def user_flow():
    print(f"\nIt's {day}, {today_str} — Fresh day, new start!")

    while True:
        print("\n━━ Main Menu ━━━")
        print("1. Add expense")
        print("2. Display all expenses")
        print("3. Set budget limits")
        print("4. Weekly summary")
        print("5. Monthly summary")
        print("6. Dashboard (pie chart)")
        print("7. Delete expense")
        print("8. Edit expense")
        print("9. Exit")

        try:
            ch = int(input("Choose an option: "))
        except ValueError:
            print("Please enter a number.")
            continue

        if ch == 1:
            add_expense()
        elif ch == 2:
            display_expenses()
        elif ch == 3:
            set_limits()
        elif ch == 4:
            weekly_summary()
        elif ch == 5:
            monthly_summary()
        elif ch == 6:
            dashboard()
        elif ch == 7:
            delete_expense()
        elif ch == 8:
            edit_expense()
        elif ch == 9:
            print("\n Thank you for using the Expense Tracker. Have a great day! ")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    user_flow()
