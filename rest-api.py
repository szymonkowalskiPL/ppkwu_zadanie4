from flask import Flask, request, jsonify
import re
import requests

app = Flask(__name__)

@app.route('/checkstring',  methods=['GET', 'POST'])
def checkString():
    string = request.args.get('string')
    returnType = request.args.get('returnType')
    downloadType = request.args.get('downloadType')
    print(string, returnType, downloadType)

    
   
    link = 'http://127.0.0.1:8000/checkstring?string='+string+'&responseType='+returnType
    result = requests.post(link)
    data = result.text
    
    
    returnData=""
    
    if returnType=="txt":
         #print("txt reponse")
         returnData="Lowercase: "+str(data["lower_case"])+"\n"+"Uppercase: "+str(data["upper_case"])+"\n"+"Numbers: "+str(data["numbers"])+"\n"+"Special: "+str(data["special_characters"])
    elif returnType=="json":
        #print("json reponse")
        returnData=data
    elif returnType=="xml":
        #print("xml response")
        returnData = "<string-result id=\"" + string + "\">"
        returnData += "\t<param class=\"upper_case\">" + str(data["upper_case"]) + "</param>"
        returnData += "\t<param class=\"lower_case\">" + str(data["lower_case"]) + "</param>"
        returnData += "\t<param class=\"numbers\">" + str(data["numbers"]) + "</param>"
        returnData += "\t<param class=\"special_chars\">" + str(data["special_characters"]) + "</param>"
        returnData += "</string-result>"
    elif returnType=="csv":
        returnData += str(data["upper_case"])
        returnData += ";"
        returnData += str(data["lower_case"])
        returnData += ";"
        returnData += str(data["numbers"])
        returnData += ";"
        returnData += str(data["special_characters"])


    return returnData

app.run(host="localhost", port=8001, debug=False)
