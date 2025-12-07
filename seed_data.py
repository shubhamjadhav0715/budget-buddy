"""
Budget Buddy - Data Seeder
This script populates the database with sample data for testing and demonstration
Run this before your presentation to have realistic data in the app
"""

import sqlite3
from datetime import datetime, timedelta
import random

# Database file
DATABASE = 'budget_buddy.db'

def clear_database():
    """Clear all existing data from the database"""
    print("🗑️  Clearing existing data...")
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM expenses')
    cursor.execute('DELETE FROM budgets')
    
    conn.commit()
    conn.close()
    print("✅ Database cleared!")

def seed_transactions():
    """Add sample transactions to the database"""
    print("\n💰 Adding sample transactions...")
    
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # Get current date
    today = datetime.now()
    current_month = today.strftime('%Y-%m')
    
    # Sample income transactions
    income_data = [
        (50000, 'Salary', 'Monthly salary', f'{current_month}-01', 'income'),
        (5000, 'Freelance', 'Website project', f'{current_month}-10', 'income'),
        (2000, 'Investment', 'Dividend income', f'{current_month}-15', 'income'),
        (1000, 'Gift', 'Birthday gift', f'{current_month}-20', 'income'),
    ]
    
    # Sample expense transactions
    expense_data = [
        # Food & Dining
        (1200, 'Food', 'Grocery shopping - Big Bazaar', f'{current_month}-02', 'expense'),
        (450, 'Food', 'Restaurant dinner', f'{current_month}-05', 'expense'),
        (800, 'Food', 'Weekly groceries', f'{current_month}-09', 'expense'),
        (350, 'Food', 'Lunch with friends', f'{current_month}-12', 'expense'),
        (600, 'Food', 'Monthly provisions', f'{current_month}-18', 'expense'),
        (250, 'Food', 'Coffee and snacks', f'{current_month}-22', 'expense'),
        
        # Transportation
        (2000, 'Transportation', 'Petrol for car', f'{current_month}-03', 'expense'),
        (500, 'Transportation', 'Auto rickshaw rides', f'{current_month}-08', 'expense'),
        (1500, 'Transportation', 'Bike service', f'{current_month}-14', 'expense'),
        (300, 'Transportation', 'Parking fees', f'{current_month}-19', 'expense'),
        
        # Shopping
        (2500, 'Shopping', 'New clothes', f'{current_month}-06', 'expense'),
        (1200, 'Shopping', 'Electronics - headphones', f'{current_month}-11', 'expense'),
        (800, 'Shopping', 'Books and stationery', f'{current_month}-16', 'expense'),
        (1500, 'Shopping', 'Shoes', f'{current_month}-21', 'expense'),
        
        # Entertainment
        (600, 'Entertainment', 'Movie tickets', f'{current_month}-04', 'expense'),
        (1200, 'Entertainment', 'Concert tickets', f'{current_month}-13', 'expense'),
        (400, 'Entertainment', 'Netflix subscription', f'{current_month}-01', 'expense'),
        (800, 'Entertainment', 'Gaming subscription', f'{current_month}-17', 'expense'),
        
        # Bills & Utilities
        (1500, 'Bills', 'Electricity bill', f'{current_month}-05', 'expense'),
        (800, 'Bills', 'Internet bill', f'{current_month}-07', 'expense'),
        (1200, 'Bills', 'Mobile recharge', f'{current_month}-10', 'expense'),
        (2000, 'Bills', 'Water bill', f'{current_month}-15', 'expense'),
        
        # Healthcare
        (1500, 'Healthcare', 'Doctor consultation', f'{current_month}-08', 'expense'),
        (800, 'Healthcare', 'Medicines', f'{current_month}-12', 'expense'),
        (500, 'Healthcare', 'Gym membership', f'{current_month}-01', 'expense'),
        
        # Education
        (3000, 'Education', 'Online course fee', f'{current_month}-03', 'expense'),
        (1500, 'Education', 'Books and materials', f'{current_month}-09', 'expense'),
        (2000, 'Education', 'Certification exam', f'{current_month}-18', 'expense'),
        
        # Other
        (1000, 'Other', 'Miscellaneous expenses', f'{current_month}-11', 'expense'),
        (500, 'Other', 'Gifts for family', f'{current_month}-20', 'expense'),
    ]
    
    # Insert income transactions
    for transaction in income_data:
        cursor.execute(
            'INSERT INTO expenses (amount, category, description, date, type) VALUES (?, ?, ?, ?, ?)',
            transaction
        )
    
    # Insert expense transactions
    for transaction in expense_data:
        cursor.execute(
            'INSERT INTO expenses (amount, category, description, date, type) VALUES (?, ?, ?, ?, ?)',
            transaction
        )
    
    conn.commit()
    
    # Count transactions
    total_income = cursor.execute('SELECT COUNT(*) FROM expenses WHERE type = "income"').fetchone()[0]
    total_expense = cursor.execute('SELECT COUNT(*) FROM expenses WHERE type = "expense"').fetchone()[0]
    
    conn.close()
    
    print(f"✅ Added {total_income} income transactions")
    print(f"✅ Added {total_expense} expense transactions")

def seed_budgets():
    """Add sample budgets to the database"""
    print("\n📊 Adding sample budgets...")
    
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # Get current month
    current_month = datetime.now().strftime('%Y-%m')
    
    # Sample budgets
    budget_data = [
        ('Food', 5000, current_month),
        ('Transportation', 4000, current_month),
        ('Shopping', 5000, current_month),
        ('Entertainment', 3000, current_month),
        ('Bills', 6000, current_month),
        ('Healthcare', 3000, current_month),
        ('Education', 7000, current_month),
        ('Other', 2000, current_month),
    ]
    
    # Insert budgets
    for budget in budget_data:
        try:
            cursor.execute(
                'INSERT INTO budgets (category, amount, month) VALUES (?, ?, ?)',
                budget
            )
        except sqlite3.IntegrityError:
            # Budget already exists, update it
            cursor.execute(
                'UPDATE budgets SET amount = ? WHERE category = ? AND month = ?',
                (budget[1], budget[0], budget[2])
            )
    
    conn.commit()
    
    # Count budgets
    total_budgets = cursor.execute('SELECT COUNT(*) FROM budgets').fetchone()[0]
    
    conn.close()
    
    print(f"✅ Added {total_budgets} budget categories")

def add_previous_months_data():
    """Add data for previous months to show trends"""
    print("\n📈 Adding historical data for trends...")
    
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # Add data for last 5 months
    for i in range(1, 6):
        month_date = datetime.now() - timedelta(days=30*i)
        month_str = month_date.strftime('%Y-%m')
        
        # Random income for the month
        salary = random.randint(45000, 55000)
        freelance = random.randint(0, 8000)
        
        cursor.execute(
            'INSERT INTO expenses (amount, category, description, date, type) VALUES (?, ?, ?, ?, ?)',
            (salary, 'Salary', f'Monthly salary - {month_str}', f'{month_str}-01', 'income')
        )
        
        if freelance > 0:
            cursor.execute(
                'INSERT INTO expenses (amount, category, description, date, type) VALUES (?, ?, ?, ?, ?)',
                (freelance, 'Freelance', f'Freelance work - {month_str}', f'{month_str}-15', 'income')
            )
        
        # Random expenses for the month
        categories = ['Food', 'Transportation', 'Shopping', 'Entertainment', 'Bills', 'Healthcare', 'Education', 'Other']
        
        for category in categories:
            # Random number of transactions per category
            num_transactions = random.randint(2, 5)
            
            for _ in range(num_transactions):
                amount = random.randint(300, 3000)
                day = random.randint(1, 28)
                
                cursor.execute(
                    'INSERT INTO expenses (amount, category, description, date, type) VALUES (?, ?, ?, ?, ?)',
                    (amount, category, f'{category} expense', f'{month_str}-{day:02d}', 'expense')
                )
    
    conn.commit()
    conn.close()
    
    print(f"✅ Added historical data for last 5 months")

def display_summary():
    """Display summary of seeded data"""
    print("\n" + "="*50)
    print("📊 DATABASE SUMMARY")
    print("="*50)
    
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # Total transactions
    total_transactions = cursor.execute('SELECT COUNT(*) FROM expenses').fetchone()[0]
    total_income = cursor.execute('SELECT SUM(amount) FROM expenses WHERE type = "income"').fetchone()[0]
    total_expense = cursor.execute('SELECT SUM(amount) FROM expenses WHERE type = "expense"').fetchone()[0]
    total_budgets = cursor.execute('SELECT COUNT(*) FROM budgets').fetchone()[0]
    
    # Current month data
    current_month = datetime.now().strftime('%Y-%m')
    current_income = cursor.execute(
        'SELECT SUM(amount) FROM expenses WHERE type = "income" AND date LIKE ?',
        (f'{current_month}%',)
    ).fetchone()[0] or 0
    
    current_expense = cursor.execute(
        'SELECT SUM(amount) FROM expenses WHERE type = "expense" AND date LIKE ?',
        (f'{current_month}%',)
    ).fetchone()[0] or 0
    
    conn.close()
    
    print(f"\n📝 Total Transactions: {total_transactions}")
    print(f"💰 Total Income (All Time): ₹{total_income:,.2f}")
    print(f"💸 Total Expenses (All Time): ₹{total_expense:,.2f}")
    print(f"📊 Total Budgets: {total_budgets}")
    
    print(f"\n📅 Current Month ({current_month}):")
    print(f"   Income: ₹{current_income:,.2f}")
    print(f"   Expenses: ₹{current_expense:,.2f}")
    print(f"   Balance: ₹{current_income - current_expense:,.2f}")
    
    print("\n" + "="*50)
    print("✅ Database seeding completed successfully!")
    print("="*50)
    print("\n🚀 You can now run the app: python app.py")
    print("🌐 Then open: http://127.0.0.1:5000")
    print("\n")

def main():
    """Main function to seed the database"""
    print("\n" + "="*50)
    print("🌱 BUDGET BUDDY - DATA SEEDER")
    print("="*50)
    print("\nThis will populate your database with sample data")
    print("Perfect for testing and presentations!\n")
    
    # Ask for confirmation
    response = input("Do you want to clear existing data and add sample data? (yes/no): ")
    
    if response.lower() in ['yes', 'y']:
        clear_database()
        seed_transactions()
        seed_budgets()
        add_previous_months_data()
        display_summary()
    else:
        print("\n❌ Seeding cancelled. No changes made.")
        print("Run this script again when you're ready!\n")

if __name__ == '__main__':
    main()
