from flask import Flask, request
from flask import render_template
import hashlib
import requests
import os

url_vip = os.getenv("URL_VIP")

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/profile", methods=['POST'])
def profile():
	
	url = url_vip
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1)'}

	key_and_id_vip = request.get_json('key_vip')

	id_vip = key_and_id_vip['id_vip']
	key_vip = key_and_id_vip['key_vip']
	
	sign_vip = id_vip+key_vip
	sign_vip = hashlib.md5(sign_vip.encode('utf-8')).hexdigest()

	payload = { "key":key_vip, 
		   		"sign": sign_vip
		   	  }
	r = requests.post(url,headers=headers, data=payload)
	falseortrue = r.json()
	falseortrue_result = falseortrue['data']
	return falseortrue['data'], 201
