from flask import Flask, request
from flask import render_template
import hashlib
import requests
import os
import json

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
	is_data_null = str(json.dumps(falseortrue_result, indent=2))
	if is_data_null == "null":
		return str(json.dumps(falseortrue['message'], indent=2)), 201

	return str(json.dumps(falseortrue_result, indent=2)), 201

@app.route("/test-button", methods=['POST'])
def test_button():
	button = {
			"version": "v2",
			"content": {
			"type": "instagram",
			"messages": [
			  {
			    "type": "text",
			    "text": "Pilih Diamonds 😄",
			    "buttons": [
			      {
				"type": "node",
				"caption": "17 💎 [Rp.17.000]",
				"target": "mantap_jiwa"
			      },
			      {
				"type": "node",
				"caption": "18 💎 [Rp.20.000]",
				"target": "mantap_jiwa"
			      },
			      {
				"type": "node",
				"caption": "19 💎 [Rp.25.000]",
				"target": "mantap_jiwa"
			      },
			      {
				"type": "node",
				"caption": "20 💎 [Rp.30.000]",
				"target": "mantap_jiwa"
			      }

			    ]
			  }
			],
			"actions": [],
			"quick_replies": []
			}
		}

	return str(json.dumps(button, indent=2))
