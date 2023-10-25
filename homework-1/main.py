"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv
from pathlib import Path


CUSTOMERS_PATH = Path(Path.cwd(), 'north_data', 'customers_data.csv')
EMPLOYEES_PATH = Path(Path.cwd(), 'north_data', 'employees_data.csv')
ORDERS_PATH = Path(Path.cwd(), 'north_data', 'orders_data.csv')


params = psycopg2.connect(
    host="localhost",
    database="north",
    user="postgres",
    password="dbreyz12")


with params as conn:
    with conn.cursor() as cur:
        # Подтягиваем данные в таблицу customers
        try:
            with open(CUSTOMERS_PATH, encoding='utf-8') as csvfile:
                data = csv.DictReader(csvfile)
                for row in data:
                    customer_id = row['customer_id']
                    company_name = row['company_name']
                    contact_name = row['contact_name']
                    cur.execute('INSERT into customers VALUES (%s, %s, %s)', (customer_id, company_name, contact_name))
        except psycopg2.errors.UniqueViolation:
            print('psycopg2.errors.UniqueViolation')
        except FileNotFoundError:
            print('FileNotFoundError')
        conn.commit()
        # Подтягиваем данные в таблицу employees
        try:
            with open(EMPLOYEES_PATH, encoding='utf-8') as csvfile:
                data = csv.DictReader(csvfile)
                for row in data:
                    employee_id = row['employee_id']
                    first_name = row['first_name']
                    last_name = row['last_name']
                    title = row['title']
                    birth_date = row['birth_date']
                    notes = row['notes']
                    cur.execute('INSERT into employees VALUES(%s, %s, %s, %s, %s, %s)',
                                (employee_id, first_name, last_name, title, birth_date,notes))
        except psycopg2.errors.UniqueViolation:
            print('psycopg2.errors.UniqueViolation')
        except FileNotFoundError:
            print('FileNotFoundError')
        conn.commit()
        # Подтягиваем данные в таблицу ordera
        try:
            with open(ORDERS_PATH, encoding='utf-8') as csvfile:
                data = csv.DictReader(csvfile)
                for row in data:
                    order_id = row['order_id']
                    customer_id = row['customer_id']
                    employee_id = row['employee_id']
                    order_date = row['order_date']
                    ship_city = row['ship_city']
                    cur.execute('INSERT into orders VALUES(%s, %s, %s, %s, %s)', (order_id, customer_id, employee_id,
                                                                                  order_date, ship_city))
        except psycopg2.errors.UniqueViolation:
            print('psycopg2.errors.UniqueViolation')
        except FileNotFoundError:
            print('FileNotFoundError')
        conn.commit()
conn.close()
