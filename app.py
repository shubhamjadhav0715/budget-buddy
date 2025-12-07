from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from datetime import datetime
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_here_change_in_production'

# Database setup
DATABASE = 'budget_buddy.db'

def get_db_connection():
    """Create a database connection"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize the database with required tables"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create expenses table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            description TEXT,
            date TEXT NOT NULL,
            type TEXT NOT NULL
        )
    ''')
    
    # Create budgets table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS budgets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT NOT NULL UNIQUE,
            amount REAL NOT NULL,
            month TEXT NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()

# Initialize database when app starts
init_db()

@app.route('/')
def index():
    """Home page - Dashboard"""
    conn = get_db_connection()
    
    # Get current month expenses
    current_month = datetime.now().strftime('%Y-%m')
    expenses = conn.execute(
        'SELECT * FROM expenses WHERE date LIKE ? ORDER BY date DESC',
        (f'{current_month}%',)
    ).fetchall()
    
    # Calculate total income and expenses
    total_income = sum([exp['amount'] for exp in expenses if exp['type'] == 'income'])
    total_expense = sum([exp['amount'] for exp in expenses if exp['type'] == 'expense'])
    balance = total_income - total_expense
    
    # Get budgets
    budgets = conn.execute('SELECT * FROM budgets WHERE month = ?', (current_month,)).fetchall()
    
    conn.close()
    
    return render_template('index.html', 
                         expenses=expenses, 
                         total_income=total_income,
                         total_expense=total_expense,
                         balance=balance,
                         budgets=budgets)

@app.route('/add_transaction', methods=['GET', 'POST'])
def add_transaction():
    """Add new income or expense"""
    if request.method == 'POST':
        amount = float(request.form['amount'])
        category = request.form['category']
        description = request.form['description']
        date = request.form['date']
        trans_type = request.form['type']
        
        conn = get_db_connection()
        conn.execute(
            'INSERT INTO expenses (amount, category, description, date, type) VALUES (?, ?, ?, ?, ?)',
            (amount, category, description, date, trans_type)
        )
        conn.commit()
        conn.close()
        
        flash('Transaction added successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('add_transaction.html')

@app.route('/budgets', methods=['GET', 'POST'])
def budgets():
    """Manage budgets"""
    if request.method == 'POST':
        category = request.form['category']
        amount = float(request.form['amount'])
        month = request.form['month']
        
        conn = get_db_connection()
        try:
            conn.execute(
                'INSERT INTO budgets (category, amount, month) VALUES (?, ?, ?)',
                (category, amount, month)
            )
            conn.commit()
            flash('Budget set successfully!', 'success')
        except sqlite3.IntegrityError:
            # Update existing budget
            conn.execute(
                'UPDATE budgets SET amount = ? WHERE category = ? AND month = ?',
                (amount, category, month)
            )
            conn.commit()
            flash('Budget updated successfully!', 'success')
        conn.close()
        
        return redirect(url_for('budgets'))
    
    conn = get_db_connection()
    current_month = datetime.now().strftime('%Y-%m')
    budgets_list = conn.execute('SELECT * FROM budgets WHERE month = ?', (current_month,)).fetchall()
    
    # Calculate spending for each budget category
    budget_data = []
    for budget in budgets_list:
        spent = conn.execute(
            'SELECT SUM(amount) as total FROM expenses WHERE category = ? AND type = ? AND date LIKE ?',
            (budget['category'], 'expense', f"{current_month}%")
        ).fetchone()
        
        spent_amount = spent['total'] if spent['total'] else 0
        remaining = budget['amount'] - spent_amount
        percentage = (spent_amount / budget['amount'] * 100) if budget['amount'] > 0 else 0
        
        budget_data.append({
            'category': budget['category'],
            'budget': budget['amount'],
            'spent': spent_amount,
            'remaining': remaining,
            'percentage': percentage
        })
    
    conn.close()
    
    return render_template('budgets.html', budgets=budget_data)

@app.route('/reports')
def reports():
    """View reports and analytics"""
    conn = get_db_connection()
    current_month = datetime.now().strftime('%Y-%m')
    
    # Get category-wise expenses
    category_expenses = conn.execute('''
        SELECT category, SUM(amount) as total 
        FROM expenses 
        WHERE type = 'expense' AND date LIKE ?
        GROUP BY category
    ''', (f'{current_month}%',)).fetchall()
    
    # Get monthly trend (last 6 months)
    monthly_data = conn.execute('''
        SELECT strftime('%Y-%m', date) as month, 
               SUM(CASE WHEN type = 'income' THEN amount ELSE 0 END) as income,
               SUM(CASE WHEN type = 'expense' THEN amount ELSE 0 END) as expense
        FROM expenses
        GROUP BY month
        ORDER BY month DESC
        LIMIT 6
    ''').fetchall()
    
    conn.close()
    
    return render_template('reports.html', 
                         category_expenses=category_expenses,
                         monthly_data=monthly_data)

@app.route('/delete_transaction/<int:id>')
def delete_transaction(id):
    """Delete a transaction"""
    conn = get_db_connection()
    conn.execute('DELETE FROM expenses WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    
    flash('Transaction deleted successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/api/chart_data')
def chart_data():
    """API endpoint for chart data"""
    conn = get_db_connection()
    current_month = datetime.now().strftime('%Y-%m')
    
    # Category-wise expenses
    category_data = conn.execute('''
        SELECT category, SUM(amount) as total 
        FROM expenses 
        WHERE type = 'expense' AND date LIKE ?
        GROUP BY category
    ''', (f'{current_month}%',)).fetchall()
    
    categories = [row['category'] for row in category_data]
    amounts = [row['total'] for row in category_data]
    
    conn.close()
    
    return jsonify({
        'categories': categories,
        'amounts': amounts
    })

if __name__ == '__main__':
    app.run(debug=True)
