from flask import Flask, render_template, request, abort
from solution import Solution

sol = Solution()
app = Flask(__name__)


@app.get('/')
def index():
    return render_template('index.html')


@app.post('/result')
def palindromic_substrings_count_on_json():
    try:
        string = request.form['input_text1']
        data = sol.countSubstrings(string)
        return {"count": data}
    except TypeError:
        abort(400)
    except AssertionError:
        abort(400)
    except KeyError:
        abort(400)


@app.post('/result_page')
def palindromic_substrings_count_on_page():
    try:
        string = request.form['input_text2']
        data = sol.countSubstrings(string)
        return f"<div id='result_container'>Количество палиндромных подстрок = <span id='result'>{data}<span/></div>"
    except TypeError:
        abort(400)
    except AssertionError:
        abort(400)
    except KeyError:
        abort(400)


if __name__ == '__main__':
    app.run(debug=True)
