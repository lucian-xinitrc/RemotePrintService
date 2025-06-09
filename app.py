import os
import subprocess
from flask import Flask, request, render_template

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/", methods=['GET', 'POST'])
def upload():
	file = request.files['file']
	file.save(os.path.join(UPLOAD_FOLDER, file.filename))
	message = "File Uploaded"
	status = 200

	return render_template('index.html', message=message, status= status, filename=file.filename)

@app.route("/print", methods=['GET', 'POST'])
def print():
	subprocess.run(['lp', "uploads/{request.form['filename']}"], check=True)
	return "Printing"

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)