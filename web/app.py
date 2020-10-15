from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from pymongo import MongoClient
from http import HTTPStatus
import helper


app = Flask(__name__)
api = Api(app)
client = MongoClient("mongodb://db:27017")
db = client.ArticlesDB
articles = db["Articles"]


class ArticlesAPI(Resource):
    def post(self):
        data = request.get_json()
        try:
        	helper.validate_data(data)
        except ValueError:
        	return jsonify(
        		{
        			"message": "data you entered is not valid",
        			"code": HTTPStatus.BAD_REQUEST
        		}
        	)
		inner_data = data["data"]
		try:
         	helper.validate_relationships(inner_data["relationships"])
        except (KeyError, ValueError) as ex:
            return jsonify(
				{
					"message": ex.args[0],
					"code": HTTPStatus.BAD_REQUEST
				}
			)
        
api.add_resource(ArticlesAPI, "/articles")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
