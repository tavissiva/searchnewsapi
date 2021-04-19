from flask import Flask, jsonify
from flask_restful import Resource, Api
import json
# import os
# import sys
# BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(BASE_PATH)
from SearchScraping import scrapeMain

app = Flask(__name__)
api = Api(app)

@app.route('/')
def home():
    return "<center><h1> NewsApi <h1></center></br>\
    <center><i><em>Enter the api path to get the response</em></i></center></br></br>\
    <center><i><em>This is an Api services which gives the news, dictionary words,</br>\
    wikipedia information, website link and many other information for keyword search </em></i></center>\
    "


class HelloWorld(Resource):
    def get(self, query):
        query = query.replace("20%","+")
        resource_result, resource_url, result_url_page, result_url_link = scrapeMain.scrapeSearch(query)
        msg = [ {'resource_content': resource_result}, 
                {'resource_url': resource_url},
                {'source_link': result_url_page},
                {'Query_all_link': result_url_link}
        ]
        return jsonify(msg)

#api_key = '7c72wE9kR2s0v15Sn7c4M873v7gR'
api.add_resource(HelloWorld, '/api/<string:query>')
if __name__ == "__main__":
    app.run(debug=True)