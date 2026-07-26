from flask import Flask
import psycopg2

app = Flask(__name__)

DATABASE_URL = "postgresql://render_flask_tutorial_db_user:7x58Q5YgWOTMFhPI0GewAICQ04bst1o3@dpg-d9ioasfavr4c73b6ka3g-a/render_flask_tutorial_db"

@app.route('/')
def hello_world():
    return 'Hello World from Owen Ahlers in 3308'


@app.route("/db_test")
def db_test():
    conn = None
    try:
        conn = psycopg2.connect(DATABASE_URL)
        return "Database connection successful"
    except Exception as e:
        return f"Database connection failed: {e}"
    finally:
        if conn is not None:
            conn.close()


@app.route("/db_create")
def db_create():
    conn = None
    try:
        conn = psycopg2.connect(DATABASE_URL)
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS Basketball(
                    First varchar(255),
                    Last varchar(255),
                    City varchar(255),
                    Name varchar(255),
                    Number int);"""
        )
        conn.commit()
        return "Basketball Table Created"
    except Exception as e:
        return f"Database connection failed: {e}"
    finally:
        if conn is not None:
            conn.close()


@app.route('/db_insert')
def db_inserting():
    conn = None
    try:
        conn = psycopg2.connect(DATABASE_URL)
        c = conn.cursor()
        c.execute("""
            INSERT INTO Basketball (First, Last, City, Name, Number)
            Values
            ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
            ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
            ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
            ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
        """)
        conn.commit()
        return "Basketball Table Successfully Populated"
    except Exception as e:
        return f"Database connection failed: {e}"
    finally:
        if conn is not None:
            conn.close()


@app.route('/db_select')
def selecting():
    conn = None
    try:
        conn = psycopg2.connect(DATABASE_URL)
        c = conn.cursor()
        c.execute("SELECT * FROM Basketball;")
        records = c.fetchall()

        html = "<table border='1'>"
        html += "<tr><th>First</th><th>Last</th><th>City</th><th>Name</th><th>Number</th></tr>"
        for row in records:
            html += "<tr>"
            for value in row:
                html += f"<td>{value}</td>"
            html += "</tr>"
        html += "</table>"

        return html
    except Exception as e:
        return f"Database connection failed: {e}"
    finally:
        if conn is not None:
            conn.close()


@app.route('/db_drop')
def dropping():
    conn = None
    try:
        conn = psycopg2.connect(DATABASE_URL)
        c = conn.cursor()
        c.execute('''
            DROP TABLE IF EXISTS Basketball;
        ''')
        conn.commit()
        return "Basketball Table Dropped"
    except Exception as e:
        return f"Database connection failed: {e}"
    finally:
        if conn is not None:
            conn.close()