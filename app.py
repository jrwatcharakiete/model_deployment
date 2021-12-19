from flask import Flask, render_template, request

import bankauthmodel

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def predict():
    pred = [-1]
    if request.method == 'POST':
        variance = request.form['variance']
        skewness = request.form['skewness']
        curtosis = request.form['curtosis']
        entropy = request.form['entropy']

        if not variance:
            variance = 0
        if not skewness:
            skewness = 0
        if not curtosis:
            curtosis = 0
        if not entropy:
            entropy = 0

        pred = bankauthmodel.predi([variance, skewness, curtosis, entropy])
        print(pred)

    return render_template('index.html', prediction=pred)

# @app.route('/sub', methods=['POST'])
# def submit():
#     if request.method == 'POST':
#         name = request.form['username']
#     return render_template('sub.html', n = name)

if __name__ == '__main__':
    app.run(debug=True)
