from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


class Calculator:
    def calculate(self, expression):
        try:
            if len(expression) > 15:
                return "Limit reached"
            return eval(expression)
        except:
            return "Error"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/calculate", methods=["POST"])
def calculate_expression():
    expression = request.get_json().get("expression", "")
    result = Calculator().calculate(expression)
    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
