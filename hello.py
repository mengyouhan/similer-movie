from flask import Flask, render_template, request, jsonify
from sortl import SortList
app = Flask(__name__)


@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/addnumber')
def add():
    a = request.args.get('a', 0, type=str)
    DA = SortList(a)
    res = DA.start()

    print(jsonify(result=res))
    return jsonify(result=res)

if __name__ == '__main__':
    app.run(debug=True)