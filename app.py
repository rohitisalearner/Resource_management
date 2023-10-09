from flask import Flask
import os
from flask_restful import Api
from tables import db
from myResource import imageCrud,assetCrud,categoryCrud,getToken,fetchCategoryDetail,fetchImageDetail,fetchAssetDetail,usersCrud,fetchUsersDetail, assignedCrud
import json
file_path = os.path.join(os.path.dirname(__file__), 'config.json')
f = open(file_path)
ConfigData = json.load(f)

import json

app = Flask(__name__)
api = Api(app)


# app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:rohit123@localhost/Resource_Assets'
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://'+ConfigData['Techpath']['Database']['User']+':'+ConfigData['Techpath']['Database']['Password']+'@'+ConfigData['Techpath']['Database']['Host']+'/'+ConfigData['Techpath']['Database']['Database']
app.config['SQLALCHEMY_POOL_RECYCLE'] = 3600
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

api.add_resource(getToken,'/generate')
api.add_resource(categoryCrud,'/categoryCrud')
api.add_resource(assetCrud, '/assetCrud')
api.add_resource(imageCrud,'/imageCrud')
api.add_resource(usersCrud, '/usersCrud')
api.add_resource(assignedCrud, '/assignedCrud')
api.add_resource(fetchCategoryDetail, '/fetchCategoryDetail')
api.add_resource(fetchAssetDetail, '/fetchAssetDetail')
api.add_resource(fetchImageDetail, '/fetchImageDetail')
api.add_resource(fetchUsersDetail, '/fetchUsersDetail')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True,port=5000, host="0.0.0.0")