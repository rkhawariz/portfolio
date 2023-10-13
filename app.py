# import library yang dibutuhkan
from os.path import join, dirname
from dotenv import load_dotenv

from flask import Flask, render_template

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


app = Flask(__name__)

# pada route ('/') atau home akan menampilkan file index.html yang terdapat pada folder templates
@app.route('/')
def home():
   return render_template('index.html')


if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)
