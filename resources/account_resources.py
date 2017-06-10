from flask_restful import Resource, reqparse
from models.account import Account

class ListAccount(Resource):
    def get(self):
        return {"hello world" : "fking shit"}