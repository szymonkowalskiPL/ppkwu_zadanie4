from flask import Flask, request, jsonify
import re
import requests

app = Flask(__name__)

@app.route('/checkstring',  methods=['GET', 'POST'])
def checkString():
    string = request.args.get('string')
    responseType = request.args.get('responseType')
    #print(string, responseType)
    
    #print("send req to API 2")
    link = 'http://127.0.0.1:5000/checkstring?string='+string
    result = requests.post(link)
    data = result.json()
    #print(data)

    returnData=""
    
    if responseType=="txt":
         #print("txt reponse")
         returnData="Lowercase: "+str(data["lower_case"])+"\n"+"Uppercase: "+str(data["upper_case"])+"\n"+"Numbers: "+str(data["numbers"])+"\n"+"Special: "+str(data["special_characters"])
    elif responseType=="json":
        #print("json reponse")
        returnData=data
    elif responseType=="xml":
        #print("xml response")
        returnData = "<string-result id=\"" + string + "\">"
        returnData += "\t<param class=\"upper_case\">" + str(data["upper_case"]) + "</param>"
        returnData += "\t<param class=\"lower_case\">" + str(data["lower_case"]) + "</param>"
        returnData += "\t<param class=\"numbers\">" + str(data["numbers"]) + "</param>"
        returnData += "\t<param class=\"special_chars\">" + str(data["special_characters"]) + "</param>"
        returnData += "</string-result>"
    elif responseType=="csv":
        returnData += str(data["upper_case"])
        returnData += ";"
        returnData += str(data["lower_case"])
        returnData += ";"
        returnData += str(data["numbers"])
        returnData += ";"
        returnData += str(data["special_characters"])


    return returnData

app.run(host="localhost", port=8000, debug=False)
