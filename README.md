# 💰 Budget Buddy - Personal Finance Tracker

A comprehensive web-based personal finance management application built with Flask, designed to help users track expenses, manage budgets, and analyze spending patterns.

## 📋 Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Screenshots](#screenshots)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

### 1. Dashboard
- Real-time overview of financial status
- Summary cards showing total income, expenses, and balance
- Recent transactions list with filtering options
- Clean and intuitive user interface

### 2. Transaction Management
- Add income and expense transactions
- Categorize transactions (Food, Transportation, Shopping, etc.)
- Add descriptions and dates for better tracking
- Edit and delete transactions
- Support for multiple transaction types

### 3. Budget Management
- Set monthly budgets for different categories
- Visual progress bars showing budget utilization
- Color-coded alerts (green, yellow, red) based on spending
- Track remaining budget in real-time
- Budget vs actual spending comparison

### 4. Reports & Analytics
- Category-wise expense breakdown
- Interactive pie charts for expense distribution
- Monthly trend analysis with line charts
- Last 6 months income vs expense comparison
- Detailed tabular reports with percentages

### 5. Data Visualization
- Beautiful charts using Chart.js
- Responsive design for all devices
- Color-coded visual indicators
- Interactive hover effects

## 🛠️ Technologies Used

### Backend
- **Python 3.x** - Core programming language
- **Flask** - Web framework
- **SQLite** - Database for data persistence
- **Werkzeug** - WSGI utility library

### Frontend
- **HTML5** - Structure
- **CSS3** - Styling with modern features
- **JavaScript** - Interactivity
- **Chart.js** - Data visualization
- **Font Awesome** - Icons

### Database Schema
```sql
-- Expenses Table
CREATE TABLE expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL NOT NULL,
    category TEXT NOT NULL,
    description TEXT,
    date TEXT NOT NULL,
    type TEXT NOT NULL
);

-- Budgets Table
CREATE TABLE budgets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT NOT NULL UNIQUE,
    amount REAL NOT NULL,
    month TEXT NOT NULL
);
```

## 📦 Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)
- Git

### Step-by-Step Installation

1. **Clone the repository**
```bash
git clone https://github.com/shubhamjadhav0715/budget-buddy.git
cd budget-buddy
```

2. **Create a virtual environment** (recommended)
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
python app.py
```

5. **Access the application**
Open your web browser and navigate to:
```
http://127.0.0.1:5000
```

## 🚀 Usage

### Adding a Transaction
1. Click on "Add Transaction" in the navigation menu
2. Select transaction type (Income or Expense)
3. Enter the amount
4. Choose a category
5. Add a description (optional)
6. Select the date
7. Click "Add Transaction"

### Setting a Budget
1. Navigate to "Budgets" page
2. Select a category
3. Enter the budget amount
4. Choose the month
5. Click "Set Budget"

### Viewing Reports
1. Go to "Reports" page
2. View category-wise expense breakdown
3. Analyze monthly trends
4. Check pie charts and line graphs

## 📁 Project Structure

```
budget-buddy/
│
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── budget_buddy.db            # SQLite database (auto-created)
│
├── templates/                 # HTML templates
│   ├── base.html             # Base template
│   ├── index.html            # Dashboard
│   ├── add_transaction.html  # Add transaction form
│   ├── budgets.html          # Budget management
│   └── reports.html          # Reports and analytics
│
└── static/                    # Static files
    ├── css/
    │   └── style.css         # Main stylesheet
    └── js/
        └── script.js         # JavaScript functions
```

## 📸 Screenshots

### Dashboard
The main dashboard provides a quick overview of your financial status with summary cards and recent transactions.

### Budget Management
Set and track budgets for different categories with visual progress indicators.

### Reports & Analytics
Comprehensive reports with interactive charts showing spending patterns and trends.

## 🔮 Future Enhancements

- [ ] User authentication and multi-user support
- [ ] Export data to CSV/PDF
- [ ] Recurring transactions
- [ ] Bill reminders and notifications
- [ ] Mobile app version
- [ ] Integration with bank APIs
- [ ] Advanced filtering and search
- [ ] Custom categories
- [ ] Multi-currency support
- [ ] Data backup and restore

## 🎓 Educational Purpose

This project was developed as part of MCA (Master of Computer Applications) curriculum to demonstrate:
- Full-stack web development skills
- Database design and management
- RESTful API concepts
- Data visualization techniques
- User interface design
- Software engineering best practices

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**[Shubham Jadhav]**
- GitHub: [@shubhamjadhav0715](https://github.com/shubhamjadhav0715)
- Project: [Budget Buddy](https://github.com/shubhamjadhav0715/budget-buddy)

## 🙏 Acknowledgments

- Flask documentation and community
- Chart.js for beautiful visualizations
- Font Awesome for icons
- All open-source contributors

---

**Note:** This is an educational project. For production use, please implement proper security measures, user authentication, and data encryption.

## 📞 Support

If you have any questions or need help, please open an issue in the GitHub repository.

**Happy Budgeting! 💰**
