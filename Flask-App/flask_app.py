from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello, Interns!"

@app.route("/students")
def students():
    return jsonify([
        {"id": 1, "name": "Alice", "age": 22},
        {"id": 2, "name": "Bob", "age": 20},
        {"id": 3, "name": "Charlie", "age": 21}
    ])

if __name__ == "__main__":
    app.run(debug=True)
