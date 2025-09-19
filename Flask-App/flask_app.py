from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route("/hello")
def hello():
    """
    A simple hello endpoint.
    ---
    responses:
      200:
        description: Returns a greeting
        examples:
          string: "Hello, Interns!"
    """
    return "Hello, Interns!"

@app.route("/students")
def students():
    """
    Get list of students
    ---
    responses:
      200:
        description: A list of students
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              name:
                type: string
              age:
                type: integer
    """
    return jsonify([
        {"id": 1, "name": "Alice", "age": 22},
        {"id": 2, "name": "Bob", "age": 20},
        {"id": 3, "name": "Charlie", "age": 21}
    ])

if __name__ == "__main__":
    app.run(debug=True)
