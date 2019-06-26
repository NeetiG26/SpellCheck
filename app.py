from flask import Flask, request, render_template
from spell import *

app = Flask(__name__)

@app.route('/spellCorrect')
def get_page():
	return render_template('page.html')

@app.route('/spellCorrect', methods=['POST'])
def spellCorrect():
	word = request.form['word']
	candidate = candidates(word)
	segments = segment(word)
	return render_template('page.html', candidates = candidate, segments=segments )

if __name__ == '__main__':
   app.run(debug = True, host='0.0.0.0', port=8080)