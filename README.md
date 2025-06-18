# 📚 Library Management System

A modern, responsive web-based application to manage library operations such as managing books, 
card holders, lending/returning books, viewing lending history, and ordering new books.
Built using **Flask**, **MySQL**, and **Bootstrap 5**.


## 🚀 Features
- 📘 View, add, and delete books
- 🆕 Register and view card holders
- 📕 Lend books to members
- 📗 Mark books as returned
- 📘 Track lending history by card number
- 📦 Order new books for the library
- 🎨 Stylish, responsive dashboard UI
- ❤️ Personalized footer credit


## 🛠️ Tech Stack
- **Backend:** Python (Flask)
- **Database:** MySQL
- **Frontend:** HTML, Bootstrap 5, CSS
- **Icons:** Emojis for a clean and intuitive experience


## 📦 Installation
### 1. Clone the repository
```bash
git clone https://github.com/Gauraang05/library-management-system.git
cd library-management-system
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up MySQL

Create a database and required tables:
```sql
CREATE DATABASE library_management_system;
```
> Use the schema from your `app.py` file to create the tables `books`, `card_holders`, `library_transactions`, and `ordered_books`.

Update the database connection in `app.py`:
```python
mydb = mysql.connector.connect(
    host="localhost",
    user="your_mysql_username",
    password="your_mysql_password",
    database="library_management_system")
```

## ▶️ Running the App
```bash
python app.py
```
Visit `http://127.0.0.1:5000` in your browser.


Have suggestions or want to contribute? Feel free to fork this project or reach out.  
Let's make library management smarter, together.

Thank you for checking out this project.  
If you found it useful, give it a ⭐ on GitHub and share it with others!
