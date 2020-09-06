# coding=utf8

from flask import Flask
app = Flask(__name__)

@app.route('/pi')
def pi():
    pi = 0
    accuracy = 10000000

    for i in range(0, accuracy):
        pi += ((4.0 * (-1)**i) / (2*i + 1))

    return str(pi)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)