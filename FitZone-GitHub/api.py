from flask import Flask, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)


@app.route("/")
def main():
    return open("index.html", encoding="utf-8").read()


@app.route("/search")
def search():
    name = request.args.get("name", "")

    conn = sqlite3.connect("data.db")
    c = conn.cursor()

    try:
        statement = "SELECT * FROM data WHERE name LIKE '%" + name + "%'"
        c.execute(statement)
        products = c.fetchall()

        if not products:
            return "No products found"

        result = "<h3>Search results:</h3>"
        for p in products:
            result += f"<p>{p[1]} | {p[2]} | {p[3]} EUR | {p[4]}</p>"

        return result

    except sqlite3.Error as e:
        return str(e)

    finally:
        conn.close()


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
