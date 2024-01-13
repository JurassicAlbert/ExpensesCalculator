# ExpensesCalculator

## What I'm Creating?
A project to list expenses and categories of expenses for provided data from a database.

## Why I'm Creating This?
To study the usage of querysets, listviews in Django, and getting accustomed to the framework.

## How I'm Creating This?
By creating and modifying existing functionalities based on the TODO list.

### Technology Stack:
- Django (Python)
- SQLite (Database)

## API Endpoints

### Expenses

#### GET /expenses/expense/list/
- Endpoint to retrieve a list of all expenses.
- Example usage: [http://example.com/expenses/expense/list/](http://example.com/expenses/expense/list/)
- ...

#### POST /expenses/expense/create/
- Endpoint to create a new expense.
- Example usage: [http://example.com/expenses/expense/create/](http://example.com/expenses/expense/create/)
- ...

#### GET /expenses/expense/<int:pk>/edit/
- Endpoint to retrieve details and edit a specific expense by ID.
- Example usage: [http://example.com/expenses/expense/1/edit/](http://example.com/expenses/expense/1/edit/)
- ...

#### POST /expenses/expense/<int:pk>/delete/
- Endpoint to delete a specific expense by ID.
- Example usage: [http://example.com/expenses/expense/1/delete/](http://example.com/expenses/expense/1/delete/)
- ...

### Categories

#### GET /expenses/category/list/
- Endpoint to retrieve a list of all categories.
- Example usage: [http://example.com/expenses/category/list/](http://example.com/expenses/category/list/)
- ...

#### POST /expenses/category/create/
- Endpoint to create a new category.
- Example usage: [http://example.com/expenses/category/create/](http://example.com/expenses/category/create/)
- ...

#### GET /expenses/category/<int:pk>/edit/
- Endpoint to retrieve details and edit a specific category by ID.
- Example usage: [http://example.com/expenses/category/1/edit/](http://example.com/expenses/category/1/edit/)
- ...

#### POST /expenses/category/<int:pk>/delete/
- Endpoint to delete a specific category by ID.
- Example usage: [http://example.com/expenses/category/1/delete/](http://example.com/expenses/category/1/delete/)
- ...

## Dashboard Redirect

### GET /
- Redirects to the expense list as the default dashboard view.
- Example usage: [http://example.com/](http://example.com/)
- ...

## Base Requirements:
- In `expenses.ExpenseList`, allow searching by date (from and/or to).
- In `expenses.ExpenseList`, allow searching by multiple categories.
- In `expenses.ExpenseList`, add sorting by category or date (ascending and descending).
- In `expenses.ExpenseList`, add the total amount spent.
- In `expenses.ExpenseList`, add a table with the total summary per year-month.
- Add an update view for `expenses.Category`.
- Add the number of expenses per category row in the category list.

---

### Project Setup Steps

1. **Install Virtual Environment (Windows Command Prompt)**
    ```bash
    python -m venv venv
    venv/bin/activate
    ```

2. **Set Environment Variables in .env File**
    ```bash
    SECRET_KEY=your_django_secret_key
    DB_NAME=your_database_name
    ```

3. **Install Requirements from requirements.txt**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply Database Migrations (Django Command)**
    ```bash
    python manage.py migrate
    ```

5. **Populate Expenses Database**
    ```bash
    python manage.py loaddata fixtures.json
    ```

**Run Server**
    ```bash
    python manage.py runserver
    ```

**Note:** This project was developed with Django 4.01/Python 3.0.12/OS: Ubuntu 22.04.3LTS
