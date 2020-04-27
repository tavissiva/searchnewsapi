from flask import Flask, request, render_template, jsonify
import requests
import os

TEMPLATE_DIR = os.path.abspath('./templates')
STATIC_DIR = os.path.abspath('./static')

# app = Flask(__name__) # to make the app run without any
app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)



bad_html = "<h1 style='margin:20px;'>ERROR!!!<h1> <br><br>"

@app.route("/", methods=["GET", "POST"])
def landingpage():

    if request.method == "POST":
        query = request.form["searchurl"]
        req = requests.get(f"http://newsapiservice.herokuapp.com/api/{query}")
        if req.status_code != 200:
            return f"{bad_html}{req.status_code}"

        message  = req.json()[0]['resource_content']
        message_url  = req.json()[1]['resource_url']
        source_link = req.json()[2]['source_link']
        query_all_link = req.json()[3]['Query_all_link']
        related,related_link = most_related(query_all_link)
        message_content = {}
        flag1=False
        flag2=False

        if message_url is not None:
            # useful_message_url = []
            # for url in message_url:
            #      if ["indiatoday", "timesofindia", "ndtv","hindustantimes"] in message_url:
            #          useful_message_url.append(url)

            for data,url in zip(message,message_url):
                message_content[data] = url 
            flag1 = True

        if message is None and message_url is None:
            flag2 = True
            flag1 = False

        
        response = {
                'query':query,
                'message':message,
                'message_content':message_content,
                'source_link':source_link,
                'related':related,
                'related_link':related_link,
        }

        return render_template("home.html", response=response, flag1=flag1, flag2=flag2)
    #endif
    return render_template("index.html")
    
def most_related(related_link):
    list_content =[]
    content = {}
    count = int(0)
    for link in related_link:
        if count>5:
            break
        data = link.split(".")[1].split(".")[0]
        if "/" in data:
            data = data.split("/")[0]
        if content is None or  not data in content: 
            list_content.append(data)
            content[data] = link
            count+=1

    return list_content,content



if __name__ == "__main__":
    app.run(host="localhost", port="8080",debug=True)