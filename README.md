Overview
This task teaches you how to use Python + SQL + SQLite + Pandas + Matplotlib to analyse simple sales data.
You will:
Create a tiny SQLite database
Write SQL queries to calculate:
total quantity sold
total revenue
Load SQL results into pandas
Display the output in the terminal
Create a bar chart showing product revenue
Save everything and upload to GitHub
This task helps you understand the basics of data analysis, including:

Databases
SQL
Python data handling
Data visualization

Files Included
Your project folder should contain:

1. create_database.py
Creates the sales_data.db database and inserts sample data.

2. task7_solution.py
Main script for:
Connecting to SQLite
Running SQL query
Printing summary
Plotting bar chart

3. sales_data.db
The SQLite database (auto-created when you run the script).
4. sales_chart.png
The bar chart saved by the script.

5. README.md
Explains:
Task objective
How to run the files
Tools used
Concepts learned

Topics Covered

This list matches every topic mentioned in the PDF:

1.Connecting Python to SQLite
Using sqlite3.connect().

2.Running SQL queries inside Python
Using cursor.execute() or pandas read_sql_query().

3.Writing SQL with SUM() and GROUP BY
To calculate total quantity and revenue.

4.Importing SQL results into pandas
Using pd.read_sql_query().

5.Printing DataFrame output
Reading table results in terminal.

6.Creating basic bar chart using matplotlib
Visualizing revenue per product.

7.Saving the chart
Using plt.savefig().

8.Learning how SQL + Python work together
Understanding why SQL inside Python is useful.


 Tools Used
 1. Python
The main programming language.

2. SQLite (built into Python)
Lightweight database engine — no installation needed.

3. sqlite3 library
Used to connect Python to the database.

4. pandas
Used to load SQL results into DataFrame.

5. matplotlib
Used to create the bar chart.

6.  .py files
Either can be used to write the scripts (your choice).
