from flask import Flask, render_template, request,abort
from solution import Solution

sol = Solution()
app = Flask(__name__)

@app.get('/')
def index():
    return render_template('index.html')

@app.post('/result')
def palindromic_substrings_count():
    try:
        string = request.form['input_text']
        data = sol.countSubstrings(string)
        return {"count": data}
    except TypeError:
        abort(400)
    except AssertionError:
        abort(400)
    except KeyError:
        abort(400)


if __name__ == '__main__':
		app.run(debug=True)