from flask import Flask,request,jsonify

app = Flask(__name__)  # intialise base class for flask


@app.route("/", methods=["GET"])  # url  homepage
def home_page():
    return "Home Page"

@app.route("/math", methods=["POST"])
def calculator():
    if (request.method == "POST"):
        operation = request.json['operation']   # we will use square brackets as Dict object is not callable
        num1 = int(request.json["num1"])
        num2 = int(request.json["num2"])

        if operation == 'add':
            r = num1 + num2
            result = "The sum is: "+str(r)


        if operation == 'sub':
            r = num1 - num2
            result = "The subtraction is: "+str(r)


        if operation == 'mul':
            r = num1 * num2
            result = "The multiplication is: "+str(r)


        if operation == 'div':
            r = num1 / num2
            result = "The division is: "+str(r)
        return jsonify(result)


if __name__ == '__main__':
        app.run(debug=True)