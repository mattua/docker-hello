from flask import Flask
from flask_restful import Resource, Api

app=Flask(__name__)
api=Api(app)

class Offices(Resource):

	def get(self):
		return {

			'offices': ['London','Bologna','Glasgow','Mumba']

		}

api.add_resource(Offices,'/')

if __name__ =='__main__':
	app.run(host='0.0.0.0',port=80,debug=True)
			