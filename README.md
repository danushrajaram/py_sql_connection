MySQL Large Data Streaming Project

This project demonstrates how to process a large number of MySQL records in Python without consuming high memory. Instead of loading the entire dataset, rows are fetched in chunks using a generator function.

Database

The project uses the employees sample database, cloned from:

https://github.com/datacharmer/test_db

After cloning, import it into MySQL:
'''
mysql -u root -p < employees.sql
'''

How It Works

A generator function fetches database rows in chunks.

Python processes each row one at a time.

This prevents memory overload even with millions of records.

Run the Script

Install dependencies:
'''
pip install mysql-connector-python
'''

Configure database credentials in db_connect.py.

Run:
'''
python stream.py
'''

You will see progress printed as rows are processed.

If you want me to add badges, screenshots, or full setup instructions — just say the word.