# import library yang dibutuhkan
import os
from os.path import join, dirname
from dotenv import load_dotenv

from flask import Flask, render_template, request, jsonify
import certifi
ca = certifi.where()
from pymongo import MongoClient


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MONGODB_URI = os.environ.get("MONGODB_URI")
DB_NAME =  os.environ.get("DB_NAME")

client = MongoClient(MONGODB_URI, tlsCAFile=ca)

db = client[DB_NAME]

app = Flask(__name__)

# pada route ('/') atau home akan menampilkan file index.html yang terdapat pada folder templates
@app.route('/')
def home():
   return render_template('index.html')

@app.route("/contact", methods=["POST"])
def contact():
    # membuat variable untuk menampung input user yang sudah disimpan pada data bucket_give di sisi client
    name_receive = request.form['name_give']
    email_receive = request.form['email_give']
    subject_receive = request.form['subject_give']
    message_receive = request.form['message_give']
    # menyusun data dalam bentuk dictionary python dengan key value pair untuk diinput ke dalam database
    doc = {
        'name': name_receive,
        'email': email_receive,
        'subject': subject_receive,
        'message': message_receive
    }
    # menginput variable doc yang berisi data ke dalam database collection bucket
    db.portfolio.insert_one(doc)
    return jsonify({'msg': 'pesan terkirim!'})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)
