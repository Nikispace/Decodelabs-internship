1. Expense Tracker (Python Console App)
   Track your daily expenses with categories, limits, and simple summaries — all from the terminal.

2. What this project does

   2.1 Add expenses with:
       • Main category (e.g., Food & Groceries, Transport & Vehicle)
       • Sub‑category (e.g., Groceries, Fuel / Petrol)
       • Amount, date, and optional description

   2.2 View all past expenses in a clean, readable list.

   2.3 Set budget limits per main category and monitor your spending.

   2.4 See summaries:
       • Weekly summary (last 7 days)
       • Monthly summary (last 30 days)

   2.5 View a dashboard with:
       • Pie‑chart of spending by main category
       • Day / week / month view (your choice)

   2.6 Edit or delete any recorded expense.

3. How to run

   3.1 Make sure Python is installed.

   3.2 Install dependencies (in terminal, not in IDLE)
   ```bash
   pip install matplotlib numpy
   ```
   3.3 Save the script as `expense_tracker.py`.

   3.4 Run:
   ```bash
   python expense_tracker.py
   ```
   3.5 Use the menu:
       1 → Add expense  
       2 → Display expenses  
       3 → Set budget limits  
       4 → Weekly summary  
       5 → Monthly summary  
       6 → Dashboard (pie chart)  
       7 → Delete expense  
       8 → Edit expense  
       9 → Exit  

4. Key design choices

   4.1 Uses a nested category system (main + sub‑category) stored in a dictionary.

   4.2 Stores each expense as a dictionary in a global `expenses` list.

   4.3 Uses `datetime` for date handling and filtering by week/month.

   4.4 Uses `matplotlib` and `numpy` for pie‑charts on the dashboard.

5. Summary

   Run `python expense_tracker.py`, follow the menu, and the app records, summarizes, and visualizes your expenses.
