from flask import Flask, request
import json
import os
import calc

app = Flask(__name__)

@app.route("/add/<value>+<value2>")
def addflask(value,value2):
    sum=calc.add(int(value), int(value2))
    with open("/home/output/test.txt", "a") as f:
        f.write("suma lui {} + {} = {}".format(value,value2,sum))
    #print(os.listdir("/home"))
    return sum

@app.route("/subtract/<value>-<value2>")
def subtractflask(value,value2):
    dif=calc.subtract(int(value), int(value2))
    with open("/home/output/test.txt", "a") as f:
        f.write("suma lui {} - {} = {}".format(value,value2,dif))
    #print(os.listdir("/home"))
    return dif

@app.route("/multiply/<value>*<value2>")
def multiplyflask(value,value2):
    prod=calc.multiply(int(value), int(value2))
    with open("/home/output/test.txt", "a") as f:
        f.write("suma lui {} * {} = {}".format(value,value2,prod))
    #print(os.listdir("/home"))
    return prod

@app.route("/divide/<value>/<value2>")
def divideflask(value,value2):
    div=calc.divide(int(value), int(value2))
    with open("/home/output/test.txt", "a") as f:
        f.write("suma lui {} / {} = {}".format(value,value2,div))
    #print(os.listdir("/home"))
    return div

@app.route('/')
def hello_world():
    return 'Hello world'


@app.route('/hello_iedi')
def hello_iedi():
    return 'Hello iedi'


@app.route("/double/<value>")
def double_num(value):
    with open("/home/output/test.txt", "a") as f:
        f.write("{} ".format(value))
    print(os.listdir("/home"))
    return str(2 * int(value))


@app.route("/get_dict")
def get_dict():
    my_dict = {"a": 1, "b": 2}
    return json.dumps(my_dict)


@app.route("/post_stuff", methods=["GET", "POST"])
def save_new_soldier_info():
    if request.method == "POST":
        info = request.json
        print(info)
        return "stuff has been received"
    else:
        return "This route is for submitting data, please send a POST request with a json"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)