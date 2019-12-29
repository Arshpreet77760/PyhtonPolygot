from flask import Flask, request, jsonify
import math

app = Flask(__name__)


def is_prime(num):
    if num in [0, 1]:
        return False
    for i in range(2, math.floor(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def is_double_prime(num):
    # Checking the number itself
    if not is_prime(num):
        return False
    # Checking the left truncated number
    var = num
    while var != 0:
        if not is_prime(var):
            return False
        var = var / 10
    # Checking the right truncated number
    temp = 10
    while num / temp == 0:
        if not is_prime(num % temp):
            return False
        temp = temp * 10
    return True


@app.route('/check-double-prime/<string:num>', methods=['GET'])
def double_side_prime(num):
    try:
        num = int(num)
        response = is_double_prime(num)
    except ValueError:
        response = "Not a valid integer"
    except BaseException as e:
        response = "Error : " + str(e)
    return jsonify({"input": num, "response": response})


if __name__ == "__main__":
    app.run()
