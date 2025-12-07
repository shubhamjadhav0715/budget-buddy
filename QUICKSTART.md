# 🚀 BUDGET BUDDY - QUICK START GUIDE

Get Budget Buddy up and running in 5 minutes!

---

## ⚡ FASTEST WAY TO START

### Windows Users:
```bash
# 1. Download the project
git clone https://github.com/shubhamjadhav0715/budget-buddy.git
cd budget-buddy

# 2. Double-click run.bat
# That's it! The app will start automatically.
```

### Mac/Linux Users:
```bash
# 1. Download the project
git clone https://github.com/shubhamjadhav0715/budget-buddy.git
cd budget-buddy

# 2. Make script executable and run
chmod +x run.sh
./run.sh
```

### Access the App:
Open your browser and go to: **http://127.0.0.1:5000**

---

## 🌱 ADD SAMPLE DATA (RECOMMENDED!)

**Before your presentation or demo, populate the database with realistic sample data:**

```bash
# After installing dependencies, run:
python seed_data.py
```

**What it does:**
- ✅ Adds 30+ realistic transactions (income & expenses)
- ✅ Sets up 8 budget categories
- ✅ Creates 5 months of historical data for trends
- ✅ Makes your demo look professional!

**Sample data includes:**
- 💰 Income: Salary, Freelance, Investments
- 💸 Expenses: Food, Transport, Shopping, Bills, etc.
- 📊 Budgets: All major categories
- 📈 Historical trends: Last 6 months

**Output:**
```
📊 DATABASE SUMMARY
Total Transactions: 150+
Total Income: ₹58,000
Total Expenses: ₹35,000
Balance: ₹23,000
```

---

## 📋 MANUAL INSTALLATION

If the scripts don't work, follow these steps:

### Step 1: Install Python
- Download Python 3.7+ from https://www.python.org/
- During installation, check "Add Python to PATH"

### Step 2: Download Project
```bash
git clone https://github.com/shubhamjadhav0715/budget-buddy.git
cd budget-buddy
```

### Step 3: Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 5: Add Sample Data (Optional but Recommended)
```bash
python seed_data.py
# Type 'yes' when prompted
```

### Step 6: Run Application
```bash
python app.py
```

### Step 7: Open Browser
Navigate to: **http://127.0.0.1:5000**

---

## 🎯 FIRST TIME USAGE

### Option 1: Use Sample Data (Recommended)
```bash
python seed_data.py
```
Then start the app and explore with realistic data!

### Option 2: Add Data Manually

#### 1. Explore Dashboard
- You'll see the main dashboard with summary cards
- Initially, all values will be zero

#### 2. Add Your First Transaction
- Click "Add Transaction" in the menu
- Select type: Income or Expense
- Enter amount (e.g., 5000)
- Choose category (e.g., Salary)
- Add description (optional)
- Select date
- Click "Add Transaction"

#### 3. Set a Budget
- Click "Budgets" in the menu
- Choose a category (e.g., Food)
- Enter budget amount (e.g., 3000)
- Select current month
- Click "Set Budget"

#### 4. View Reports
- Click "Reports" in the menu
- See your spending visualized in charts
- Analyze category-wise breakdown

---

## 💡 SAMPLE DATA FOR MANUAL TESTING

Want to add data manually? Use these examples:

### Income:
1. Amount: 50000, Category: Salary, Date: 1st of current month
2. Amount: 5000, Category: Freelance, Date: 15th of current month

### Expenses:
1. Amount: 3000, Category: Food, Description: Groceries
2. Amount: 2000, Category: Transportation, Description: Fuel
3. Amount: 1500, Category: Entertainment, Description: Movie & Dinner
4. Amount: 5000, Category: Bills, Description: Electricity & Internet
5. Amount: 2500, Category: Shopping, Description: Clothes

### Budgets:
1. Food: 5000
2. Transportation: 3000
3. Entertainment: 2000
4. Bills: 6000
5. Shopping: 4000

---

## 🔧 TROUBLESHOOTING

### Problem: "Python not found"
**Solution:** Install Python from https://www.python.org/ and add to PATH

### Problem: "pip not found"
**Solution:** 
```bash
python -m ensurepip --upgrade
```

### Problem: "Module not found"
**Solution:**
```bash
pip install -r requirements.txt
```

### Problem: "Port 5000 already in use"
**Solution:** Edit app.py, change last line to:
```python
app.run(debug=True, port=5001)
```

### Problem: Database errors
**Solution:** Delete `budget_buddy.db` file and restart the app

### Problem: Charts not showing
**Solution:** Check internet connection (Chart.js loads from CDN)

### Problem: No data showing after seeding
**Solution:** 
```bash
# Delete old database
rm budget_buddy.db  # Mac/Linux
del budget_buddy.db  # Windows

# Run seeder again
python seed_data.py
```

---

## 📱 BROWSER COMPATIBILITY

**Recommended Browsers:**
- ✅ Google Chrome (Latest)
- ✅ Mozilla Firefox (Latest)
- ✅ Microsoft Edge (Latest)
- ✅ Safari (Latest)

**Not Recommended:**
- ❌ Internet Explorer

---

## 🎓 FOR PRESENTATION/DEMO

### Before Your Presentation:

1. **Clean Database & Add Sample Data:**
   ```bash
   # Delete old database
   rm budget_buddy.db  # Mac/Linux
   del budget_buddy.db  # Windows
   
   # Add fresh sample data
   python seed_data.py
   # Type 'yes' when prompted
   
   # Start the app
   python app.py
   ```

2. **Verify Sample Data:**
   - Open http://127.0.0.1:5000
   - Check dashboard shows data
   - Verify charts are visible
   - Test all features

3. **Take Screenshots:**
   - Dashboard with data
   - Budget progress bars
   - Reports with charts
   - Transaction list

4. **Practice Demo Flow:**
   - Dashboard overview (30 sec)
   - Add a live transaction (1 min)
   - Show budget tracking (1 min)
   - Display reports (1 min)
   - Explain technology (2 min)

### During Presentation:

1. Start with Dashboard overview
2. Add a live transaction
3. Show budget tracking
4. Display reports and charts
5. Explain the technology stack

---

## 📚 NEXT STEPS

After getting started:

1. **Read Full Documentation:**
   - Check `DOCUMENTATION.md` for detailed info
   - Review `README.md` for features

2. **Customize:**
   - Add your own categories
   - Modify colors in `style.css`
   - Add new features

3. **Deploy:**
   - Deploy to Heroku
   - Share with friends
   - Add to portfolio

4. **Learn More:**
   - Flask documentation
   - SQLite tutorials
   - Chart.js examples

---

## 🆘 NEED HELP?

**Resources:**
- 📖 README.md - Full documentation
- 📄 DOCUMENTATION.md - Project report
- 📊 PRESENTATION.md - Presentation outline
- 💻 GitHub Issues - Report bugs

**Common Questions:**

**Q: Can I use this for my project?**
A: Yes! It's open source. Just add your name and college details.

**Q: How do I add my details?**
A: Edit `DOCUMENTATION.md` and `PRESENTATION.md` files.

**Q: Can I modify the code?**
A: Absolutely! Feel free to customize and enhance.

**Q: How do I reset the database?**
A: Delete `budget_buddy.db` and run `python seed_data.py` again.

**Q: How do I deploy online?**
A: Check deployment guides for Heroku, PythonAnywhere, or Render.

---

## ✅ CHECKLIST FOR PROJECT SUBMISSION

Before submitting your project:

- [ ] Code is working without errors
- [ ] Sample data is loaded (run seed_data.py)
- [ ] All features are functional
- [ ] Documentation is complete
- [ ] Presentation is ready
- [ ] Screenshots are taken
- [ ] Your name is added to docs
- [ ] College details are updated
- [ ] Guide name is mentioned
- [ ] GitHub repo is public
- [ ] README is updated

---

## 🎉 YOU'RE ALL SET!

Budget Buddy is now running on your system with realistic sample data. Enjoy exploring the features and good luck with your project presentation!

**Happy Coding! 💻**

---

**Quick Links:**
- 🏠 Dashboard: http://127.0.0.1:5000
- ➕ Add Transaction: http://127.0.0.1:5000/add_transaction
- 💰 Budgets: http://127.0.0.1:5000/budgets
- 📊 Reports: http://127.0.0.1:5000/reports

**Quick Commands:**
```bash
# Add sample data
python seed_data.py

# Start the app
python app.py

# Reset database
rm budget_buddy.db && python seed_data.py
```

---
