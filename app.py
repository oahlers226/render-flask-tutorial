from flask import Flask
import psycopg2-binary
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
