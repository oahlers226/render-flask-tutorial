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
def db_test():
    conn = None
    try:
        conn = psycopg2.connect(DATABASE_URL)
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS Basketball(
                    First varchar(255),
                    Last varchar(255),
                    City varchar(255),
                    Name varchar(255),
                    Number int"""
        ))
        return "Basketball Table Created"
    except Exception as e:
        return f"Database connection failed: {e}"
    finally:
        if conn is not None:
            conn.close()
