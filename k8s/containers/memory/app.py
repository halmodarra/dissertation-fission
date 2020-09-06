# coding=utf8

from flask import Flask
app = Flask(__name__)

@app.route('/memory')
def memory():
    A = [[1,2,3,4,5,6],[1,2,3,4,5,6],[4,5,6,7,8,9],[4,5,6,7,8,9],[10,11,12,13,14,15],[13,14,15,16,17,18]]
    B = [[13,14,15,16,17,18],[10,11,12,13,14,15],[4,5,6,7,8,9],[4,5,6,7,8,9],[1,2,3,4,5,6],[1,2,3,4,5,6]]
    result = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
    # iterating by row of A
    for i in range(len(A)):

        # iterating by coloum by B
        for j in range(len(B[0])):

            # iterating by rows of B
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return('done')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)