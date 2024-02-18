import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Function to connect to the database
def connect_db():
    return sqlite3.connect('expenses.db')

# Route to display the form for adding an expense
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission and add expense to the database
@app.route('/add_expense', methods=['POST'])
def add_expense():
    conn = connect_db()
    c = conn.cursor()
    
    amount = request.form['amount']
    category = request.form['category']
    date = request.form['date']
    description = request.form['description']
    
    c.execute('''INSERT INTO expenses (amount, category, date, description) 
                 VALUES (?, ?, ?, ?)''', (amount, category, date, description))
    
    conn.commit()
    conn.close()
    
    return redirect(url_for('index'))

# Route to display the list of expenses
@app.route('/expenses')
def expenses():
    conn = connect_db()
    c = conn.cursor()
    
    c.execute('''SELECT * FROM expenses ORDER BY date DESC''')
    expenses = c.fetchall()
    
    conn.close()
    
    return render_template('expenses.html', expenses=expenses)

if __name__ == '__main__':
    # Check if the 'expenses' table exists
    conn = connect_db()
    c = conn.cursor()
    c.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='expenses' ''')
    if c.fetchone()[0] == 0:
        # Create the 'expenses' table if it doesn't exist
        c.execute('''CREATE TABLE expenses
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      amount REAL,
                      category TEXT,
                      date DATE,
                      description TEXT)''')
    conn.commit()
    conn.close()

    app.run(debug=True)
