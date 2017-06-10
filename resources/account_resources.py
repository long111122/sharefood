from flask_restful import Resource, reqparse
from models.account import Account

class ListAccount(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(username="username", type=str, location=json)
        parser.add_argument(password="password", type=str, location=json)
        body = parser.parse_args()
        username = body["username"]
        password = body["password"]
        account = Account(username=username, password=password)
        account.save()

        return {"username":username, "password":password}