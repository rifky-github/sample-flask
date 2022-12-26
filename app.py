from flask import Flask, request
from flask import render_template
import hashlib
import requests
import os
import json

url_vip = os.getenv("URL_VIP")
url_vip_game = os.getenv("URL_VIP_GAME")

app = Flask(__name__)

url = url_vip
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1)'}

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/profile", methods=['POST'])
def profile():
	
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
			  }
			],
			"actions": [],
			"quick_replies": [
			{
			"type": "node",
			"caption": "12 💎 [Rp20,000]",
			"target": "action_milih_diamond"
		    },
			{
			"type": "node",
			"caption": "16 💎 [Rp20,000]",
			"target": "action_milih_diamond"
		    },
		    {
			"type": "node",
			"caption": "18 💎 [Rp20,000]",
			"target": "action_milih_diamond"
		    },
		    {
			"type": "node",
			"caption": "20 💎 [Rp20,000]",
			"target": "action_milih_diamond"
		    },
		    {
			"type": "node",
			"caption": "22 💎 [Rp20,000]",
			"target": "action_milih_diamond"
		    },
		]
		}
	}

	return str(json.dumps(button, indent=2))

@app.route("/cek-idGame-ml", methods=['POST'])
def cek_idGame_ml():

	key_id_idgame_zone_game = request.get_json('key_vip')

	id_vip = key_id_idgame_zone_game['id_vip']
	key_vip = key_id_idgame_zone_game['key_vip']
	user_id_zone = key_id_idgame_zone_game['id_game']
	
	x = user_id_zone.split("(")
	y = x[1].replace(')', '')

	user_id = x[0]
	zone_id= y
	
	sign_vip = id_vip+key_vip
	sign_vip = hashlib.md5(sign_vip.encode('utf-8')).hexdigest()

	payload = { 
			"key":key_vip, 
			"sign": sign_vip,
			"type":"get-nickname",
			"code":"mobile-legends",
			"target":"{user_id}",
			"additional_target":"{zone_id}"
			}.format(user_id = user_id, zone_id = zone_id)
	r = requests.post(url,headers=headers, data=payload)
	falseortrue = r.json()
	
	return str(json.dumps(falseortrue, indent=2))

@app.route("/metode-pembayaran", methods=['POST'])
def metode_pembayaran():
	macam_pembayaran = '''[FYI]
	QRIS : Biaya Admin Rp.'''+'100'+'''
	BCA  : Biaya Admin Rp.'''+'4.000'+'''
	BRI  : Biaya Admin Rp.'''+'4.000'+'''
	Permata Bank : Biaya Admin Rp.'''+'4.000+'''
	button = {
			"version": "v2",
			"content": {
			"type": "instagram",
			"messages": [
			  {
			    "type": "text",
			    "text": {macam_pembayaran},
			  }
			],
			"actions": [],
			"quick_replies": [
			{
			"type": "node",
			"caption": "QRIS",
			"target": "action_metode_pembayaran"
		    },
		    {
			"type": "node",
			"caption": "BCA",
			"target": "action_metode_pembayaran"
		    },
		    {
			"type": "node",
			"caption": "BRI",
			"target": "action_metode_pembayaran"
		    },
		    {
			"type": "node",
			"caption": "Permata Bank",
			"target": "action_metode_pembayaran"
		    }
		]
		}
	}.format(macam_pembayaran = macam_pembayaran)

	return str(json.dumps(button, indent=2))


