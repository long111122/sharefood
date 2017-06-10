from flask import *
from mlab import *
from mongoengine import *
from models.account import Account
from flask_restful import Api
from resources.account_resources import *

mlab_connect()
app = Flask(__name__)
api = Api(app)

api.add_resource(ListAccount, "/login")

if __name__ == '__main__':
    app.run()
