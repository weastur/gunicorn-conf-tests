import time
from psycopg2.pool import SimpleConnectionPool
from flask import Flask

app = Flask(__name__)
pool = SimpleConnectionPool(
    minconn=2,
    maxconn=2,
    user = "postgres",
    password = "postgres",
    host = "127.0.0.1",
    port = "5432",
    database = "postgres"
)

@app.route('/slow')
def slow():
    time.sleep(5)
    return 'Hello from slow()!'

@app.route('/fast')
def fast():
    return 'Hello from fast()!'
