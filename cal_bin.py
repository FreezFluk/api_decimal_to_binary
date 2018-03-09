from flask import Flask,request
from flask_restful import Resource ,Api ,reqparse

app= Flask(__name__)
api = Api(app)

@app.after_request
def after_request(response):
	response.headers.add('Access-Control-Allow-Origin','*')
	response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
	response.headers.add('Access-Control-Allow-Methos', 'GET,PUT,POST,DELETE,OPTIONS')
	return response

parser = reqparse.RequestParser()
parser.add_argument('studentid')

def convertDecimalToBinary(id):
   return bin(id)[2:]
class studentidToBinary(Resource):
        def post(self):
                args = parser.parse_args()
                studentid = args['studentid']
                studentid_dec = int(studentid)
                studentid_bin = convertDecimalToBinary(studentid_dec)
                return {"studentid":studentcode_bin}

api.add_resource(studentidToBinary,'/api/studentid-to-binary')


if __name__ == '__main__':
        app.run(host='0.0.0.0',port=5000)
