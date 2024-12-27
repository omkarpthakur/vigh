from flask import Flask, render_template

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    courses = [
        {"name": "Personal Finance Basics",
         "description": "Learn how to manage your finances, budget, and save effectively."},
        {"name": "Investing for Beginners",
         "description": "Understand the basics of investing and build your wealth over time."},
        {"name": "Retirement Planning",
         "description": "Plan and secure your financial future with smart retirement strategies."},
        {"name": "Debt Management", "description": "Discover techniques to manage and eliminate debt effectively."},
        {"name": "Real Estate Investing",
         "description": "Learn how to invest in real estate for financial growth and stability."},
        {"name": "Tax Optimization Strategies",
         "description": "Understand how to minimize taxes and maximize returns legally."},
        {"name": "Building Credit", "description": "Learn how to build, maintain, and improve your credit score."},
        {"name": "Financial Independence",
         "description": "Achieve financial freedom with proven strategies and smart planning."},
        {"name": "Stock Market Essentials",
         "description": "Master the fundamentals of the stock market and start trading confidently."},
        {"name": "Insurance Planning",
         "description": "Learn how to choose the right insurance to protect yourself and your assets."},
        {"name": "  ",
         "description": "   "}
    ]

    return render_template('home.html', courses=courses)

# Tools for Optimization route
@app.route('/tools')
def tools():
    tools_list = [
        "Personal Finance Optimizer",
        "Stock Market Analyzer",
        "Investment Portfolio Tracker",
        "Expense Tracker",
        "Risk Assessment Tool",
        "Tax Calculator",
        "Financial Goal Planner",
        "Budgeting Tool",
        "Dividend Tracker",
        "Cryptocurrency Tracker",
        "Retirement Savings Calculator",
        "Loan Repayment Calculator",
        "Forex Market Analyzer",
        "Savings Planner",
        "Mutual Fund Performance Tracker",
        "  "
    ]

    return render_template('tools.html', tools=tools_list)

# News route
@app.route('/news')
def news():
    news_items = [
        {"title": "Stock Market Today", "content": "Highlights from today's stock market performance."},
        {"title": "Cryptocurrency Trends", "content": "The latest developments in cryptocurrency markets."},
        {"title": "Personal Finance Tips", "content": "Effective strategies for saving and budgeting."},
        {"title": "Federal Reserve Update", "content": "Key announcements from the Federal Reserve meeting."},
        {"title": "Investment Opportunities 2024", "content": "Top sectors to watch for potential growth."},
        {"title": "  "}
    ]

    return render_template('news.html', news=news_items)

# Mentorship route
@app.route('/mentorship')
def mentorship():
    mentors = [
        {"name": "Emma Davis", "expertise": "Personal Finance"},
        {"name": "John Carter", "expertise": "Stock Market Analysis"},
        {"name": "Sophia Brown", "expertise": "Investment Strategies"},
        {"name": "Michael Lee", "expertise": "Cryptocurrency Trading"},
        {"name": "Olivia Wilson", "expertise": "Risk Management"},
        {"name": "  "}
    ]

    return render_template('mentorship.html', mentors=mentors)

# Community Board route
@app.route('/community')
def community():
    posts = [
        {"author": "Emily Clark", "content": "Looking for advice on managing personal finances."},
        {"author": "David Martinez", "content": "Sharing a great resource on stock market basics."},
        {"author": "Sophia Johnson", "content": "What are the best apps for tracking expenses?"},
        {"author": "James Brown", "content": "Tips for investing in mutual funds as a beginner."},
        {"author": "Liam Garcia", "content": "How to diversify a cryptocurrency portfolio effectively?"},
        {"author": "  ", "content": "  "}
    ]

    return render_template('community.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
