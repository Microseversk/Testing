from flask import Flask, render_template, request
from solution import Solution

sol = Solution()
app = Flask(__name__)

@app.get('/')
def index(name = None):
    return render_template('index.html', name=name)

@app.post('/result')
def palindromic_substrings_count():
    string = request.form['input_text']
    return {"count": sol.countSubstrings(string)}


if __name__ == '__main__':
		app.run(debug=True)