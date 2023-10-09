from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_
from tables import Assets, Category, Images, UserLogin,Users, Assigned
from flask import current_app, jsonify,request
import jwt
from datetime import datetime, timedelta
# from config import Config
from functools import wraps

secret_key = 'your-secret-key'

class ResourceFunction:

    def generate_token(self,Username,Password):

        """
        This function will generate token
        """
    
        expiration = datetime.utcnow() + timedelta(minutes=60)
        newtime=str(expiration).split(".")
        print(newtime[1])
        payload = {
            'Username': Username,
            'Password':Password,
            'exp': expiration
        }
        token = jwt.encode(payload,secret_key, algorithm='HS256')

        row = UserLogin(userName=Username,password=Password,token=token,expireTime=expiration)
        current_app.extensions['sqlalchemy'].db.session.add(row)
        current_app.extensions['sqlalchemy'].db.session.commit()
        current_app.extensions['sqlalchemy'].db.session.close()
        data={'expires_in':newtime[1],'token':token}
        print
        return data

    def jwt_required(self,func):

        """
        This function will verify the Token.
        """

        @wraps(func)
        def wrapper(*args, **kwargs):

            token = request.headers.get('Authorization')

            if not token:
                return {'message': 'Token is missing'}, 401
            try:
                payload=jwt.decode(token, secret_key, algorithms=['HS256'])
                username = payload.get('Username')
                password = payload.get('Password')
                print(username,password)
            except jwt.ExpiredSignatureError:
                return {'message':'Token has expired'}
            except jwt.DecodeError:
                return {'message':'Token is invalid'}
            except jwt.InvalidTokenError:
                return {'message':'Invalid token'}
            except Exception as e:
                return {'message': f'Error decoding token: {str(e)}'}, 401

            return func(*args, **kwargs)

        return wrapper


    def insertCategory(self,assetId,categoryName):

        """
        This function will insert data into category table
        """

        row = Category(AssetsId=assetId,categoryName=categoryName)
        current_app.extensions['sqlalchemy'].db.session.add(row)
        current_app.extensions['sqlalchemy'].db.session.commit()
        current_app.extensions['sqlalchemy'].db.session.close()

        return row
    
    def updateCategoryDetail(self, id,assetId,categoryName):

        """
        this function will update data into category table
        """

        print(id)
        row=current_app.extensions['sqlalchemy'].db.session.query(Category).filter_by(id=id).first()
        row.AssetsId=assetId
        row.categoryName=categoryName
        current_app.extensions['sqlalchemy'].db.session.commit()
        return row
    
    def deleteCategoryDetail(self,id):

        """
        this function will delete data into category table
        """

        row=current_app.extensions['sqlalchemy'].db.session.query(Category).filter_by(id=id).first()
        current_app.extensions['sqlalchemy'].db.session.delete(row)
        current_app.extensions['sqlalchemy'].db.session.commit()
        return "row"
    
    def searchCatregory(self):
         
        """
        This function will fetch all the Id's from category Table
        """

        row = current_app.extensions['sqlalchemy'].db.session.query(Category).all()
        return row
    
    def CategoryDetail(self,id):

        """
        This function will fetch all the details from a particular Asset by its id
        """

        row = current_app.extensions['sqlalchemy'].db.session.query(Category).filter_by(id=id).first()
        return row


    def insertAssets(self,name,serialNo,cost,date,userid,model):

        """
        This function will insert data into Assets table
        """

        row = Assets(name=name,serialNo=serialNo,cost=cost,Date=date,userId=userid,model=model)
        current_app.extensions['sqlalchemy'].db.session.add(row)
        current_app.extensions['sqlalchemy'].db.session.commit()
        current_app.extensions['sqlalchemy'].db.session.close()
        return row
    
    def updateAssetDetail(self, id,name,serialNo,cost,date,userid,model):

        """
        this function will update data into Assets table
        """

        row=current_app.extensions['sqlalchemy'].db.session.query(Assets).filter_by(id=id).first()
        row.name=name
        row.serialNo=serialNo
        row.Date=date
        row.cost=cost
        row.userId=userid
        row.model=model
        current_app.extensions['sqlalchemy'].db.session.commit()
        return row
    
    def deleteAssetDetail(self,id):

        """
        This function will delete data from the Assets table
        """

        row=current_app.extensions['sqlalchemy'].db.session.query(Assets).filter_by(id=id).first()
        current_app.extensions['sqlalchemy'].db.session.delete(row)
        current_app.extensions['sqlalchemy'].db.session.commit()
        return "row"
    
    def searchAsset(self):

        """
        This function will fetch all the Id's from Assets Table
        """

        row = current_app.extensions['sqlalchemy'].db.session.query(Assets).all()
        return row
    
    def assetsDetail(self,id):

        """
        This function will fetch all the details from a particular Asset by its id
        """

        row = current_app.extensions['sqlalchemy'].db.session.query(Assets).filter_by(id=id).first()
        return row

    

    def insertImage(self,asset_image_id,category_image_Name):

        """
        this function will insert data into Image table
        """

        row = Images(AssetsImageId=asset_image_id,categoryImageName=category_image_Name)
        current_app.extensions['sqlalchemy'].db.session.add(row)
        current_app.extensions['sqlalchemy'].db.session.commit()
        current_app.extensions['sqlalchemy'].db.session.close()

        return row
    
    def updateImageDetail(self, id,asset_image_id,category_image_Name):

        """
        this function will update data into Image table
        """
        
        row=current_app.extensions['sqlalchemy'].db.session.query(Images).filter_by(id=id).first()
        row.AssetsImageId=asset_image_id
        row.categoryImageName=category_image_Name
        current_app.extensions['sqlalchemy'].db.session.commit()
        return row
    
    def deleteImageDetail(self,id):

        """
        This function will delete data from the Image table
        """

        row=current_app.extensions['sqlalchemy'].db.session.query(Images).filter_by(id=id).first()
        current_app.extensions['sqlalchemy'].db.session.delete(row)
        current_app.extensions['sqlalchemy'].db.session.commit()
        return "row"
    
    def searchImages(self):

        """
        This function will fetch all the Id's from Image Table
        """

        row = current_app.extensions['sqlalchemy'].db.session.query(Images).all()
        return row
    
    def imageDetail(self,id):

        """
        This function will fetch all the details from a particular Image by its id
        """

        row = current_app.extensions['sqlalchemy'].db.session.query(Images).filter_by(id=id).first()
        return row
    
 
    def insertUsers(self,username,email,dob):

        """
        this function will insert data into Users table
        """

        row = Users(userName=username,email=email,dob=dob)
        current_app.extensions['sqlalchemy'].db.session.add(row)
        current_app.extensions['sqlalchemy'].db.session.commit()
        current_app.extensions['sqlalchemy'].db.session.close()

        return row
    
    def updateUsers(self,id,username,email,dob):

        """
        this function will update data into Users table
        """
        
        row=current_app.extensions['sqlalchemy'].db.session.query(Users).filter_by(id=id).first()
        row.userName=username
        row.email=email
        row.dob=dob
        current_app.extensions['sqlalchemy'].db.session.commit()
        return row
    
    def deleteUsers(self,id):

        """
        This function will delete data from the Users table
        """

        row=current_app.extensions['sqlalchemy'].db.session.query(Users).filter_by(id=id).first()
        current_app.extensions['sqlalchemy'].db.session.delete(row)
        current_app.extensions['sqlalchemy'].db.session.commit()
        return "row"
    

    def usersDetail(self, id):

        """
        This function will fetch all the details from a particular Image by its id
        """
          
        row = current_app.extensions['sqlalchemy'].db.session.query(Users).filter_by(id=id).first()
        return row
    


    def searchUsersIds(self):

        """
        This function will fetch all the Id's from Users Table
        """

        row = current_app.extensions['sqlalchemy'].db.session.query(Users).all()
        return row



    def insertAssigned(self,UsersId, assetId, date):

        """
        this function will insert data into Assigned table
        """

        row = Assigned(UsersId=UsersId,assetId=assetId,Date=date)
        current_app.extensions['sqlalchemy'].db.session.add(row)
        current_app.extensions['sqlalchemy'].db.session.commit()
        current_app.extensions['sqlalchemy'].db.session.close()

        return row
    
    def updateAssigned(self, id, UsersId, assetId, date):

        """
        this function will update data into Assigned table
        """
        
        row=current_app.extensions['sqlalchemy'].db.session.query(Assigned).filter_by(id=id).first()
        row.UsersId=UsersId
        row.assetId=assetId
        row.Date=date
        current_app.extensions['sqlalchemy'].db.session.commit()
        return row
        
    def deleteAssignedDetail(self,id):

        """
        This function will delete data from the Assigned table
        """

        row=current_app.extensions['sqlalchemy'].db.session.query(Assigned).filter_by(id=id).first()
        current_app.extensions['sqlalchemy'].db.session.delete(row)
        current_app.extensions['sqlalchemy'].db.session.commit()
        return "row"
    
    def duplicateEntry(self, id):
        print("========",id)
        row=current_app.extensions['sqlalchemy'].db.session.query(Assigned).join(Users and Assets).add_columns(Users.userName,Assets.serialNo,Assigned.Date).all()
        return row
    
    def select(self,assetId,UsersId):
        row = current_app.extensions['sqlalchemy'].db.session.query(Assigned).filter_by(assetId=assetId,UsersId=UsersId).first()

        return row



# [(<Assigned 115>, 'Ahan', 'monitor-023-mgs', datetime.datetime(2023, 9, 22, 17, 5, 44)), (<Assigned 2>, 'Ahan', 'monitor-0232-mgs', datetime.datetime(2023, 9, 21, 13, 57, 48)), (<Assigned 115>, 'arjun', 'monitor-023-mgs', datetime.datetime(2023, 9, 22, 17, 5, 44)), (<Assigned 2>, 'arjun', 'monitor-0232-mgs', datetime.datetime(2023, 9, 21, 13, 57, 48)), (<Assigned 115>, 'rohit', 'monitor-023-mgs', datetime.datetime(2023, 9, 22, 17, 5, 44)), (<Assigned 2>, 'rohit', 'monitor-0232-mgs', datetime.datetime(2023, 9, 21, 13, 57, 48))]