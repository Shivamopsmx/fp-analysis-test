import os
import sqlite3
import subprocess

from flask import Flask, request

app = Flask(__name__)

# Hardcoded secret (SAST: secret detection)
API_KEY = "example-hardcoded-api-key-placeholder-abc123"
DB_PASSWORD = "example-hardcoded-db-password-xyz789"


@app.route("/user")
def get_user():
    # SQL injection: user input concatenated into the query
    user_id = request.args.get("id")
    conn = sqlite3.connect("app.db")
    cur = conn.cursor()
    query = "SELECT * FROM users WHERE id = '%s'" % user_id
    cur.execute(query)
    return str(cur.fetchall())


@app.route("/ping")
def ping():
    # Command injection: user input passed to a shell
    host = request.args.get("host")
    return os.popen("ping -c 1 " + host).read()


@app.route("/backup")
def backup():
    # subprocess with shell=True on untrusted input
    name = request.args.get("name")
    subprocess.call("tar czf /tmp/" + name + ".tgz /data", shell=True)
    return "ok"


@app.route("/calc")
def calc():
    # Dangerous eval of user input
    expr = request.args.get("expr", "0")
    return str(eval(expr))


if __name__ == "__main__":
    # Debug mode on in "production"
    app.run(host="0.0.0.0", port=8080, debug=True)
