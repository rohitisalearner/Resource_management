from flask_restful import Api, Resource, reqparse,request
from flask import current_app, jsonify
from CrudFun import ResourceFunction
from datetime import date, datetime

obj=ResourceFunction()

class getToken(Resource):
    def get(self):

        data=request.get_json('auth')
        Username=data['auth']['Username']
        Password=data['auth']['Password']
        token=obj.generate_token(Username,Password)

        return token

class assetCrud(Resource):
    @obj.jwt_required
    def get(self):
        Id=[]
        data={"assetsIds":Id}
        rows=obj.searchAsset()
        for row in rows:
            Id.append(row.id)
        return data
    
    def post(self):
        data=request.get_json("assetDetail")
        name=data["assetDetail"]["name"]
        serialNo=data["assetDetail"]["serialNo"]
        cost=data["assetDetail"]["cost"]
        date = datetime.now()
        print(date,"==========")
        userid=data["assetDetail"]["userid"]
        model=data["assetDetail"]["model"]
        obj.insertAssets(name,serialNo,cost,date,userid,model)
        return "inserted"
    
    def put(self):
        data=request.get_json("updateAssetDetail")
        Id=data["updateAssetDetail"]["Id"]
        name=data["updateAssetDetail"]["name"]
        serialNo=data["updateAssetDetail"]["serialNo"]
        cost=data["updateAssetDetail"]["cost"]
        date = datetime.now()
        print(date,"==========")
        userid=data["updateAssetDetail"]["userid"]
        model=data["updateAssetDetail"]["model"]
        jsonData=obj.updateAssetDetail(Id,name,serialNo,cost,date,userid,model)
        return "updated"
    
    def delete(self):
        data=request.get_json("Id")
        id=data["Id"]
        print(id)
        obj.deleteAssetDetail(id)
        return "deleted"
    
class categoryCrud(Resource):
    @obj.jwt_required
    def get(self):
        Id=[]
        data={"categoryIds":Id}
        rows=obj.searchCatregory()
        for row in rows:
            Id.append(row.id)
        return data
    
    def post(self):
        data=request.get_json("categoryDetail")
        assetId=data["categoryDetail"]["assetId"]
        categoryName=data["categoryDetail"]["categoryName"]
        obj.insertCategory(assetId,categoryName)
        return "inserted"
    
    def put(self):
        data=request.get_json("updateCategoryDetail")
        Id=data["updateCategoryDetail"]["Id"]
        assetId=data["updateCategoryDetail"]["assetId"]
        categoryName=data["updateCategoryDetail"]["categoryName"]
        jsonData=obj.updateCategoryDetail(Id,assetId,categoryName)
        return "updated"
    
    def delete(self):
        data=request.get_json("Id")
        id=data["Id"]
        print(id)
        obj.deleteCategoryDetail(id)
        return "deleted"

class imageCrud(Resource):
    @obj.jwt_required
    def get(self):
        Id=[]
        data={"imageIds":Id}
        rows=obj.searchImages()
        for row in rows:
            Id.append(row.id)
        return data
    
    def post(self):
        data=request.get_json("imageDetail")
        assetId=data["imageDetail"]["assetImgId"]
        categoryName=data["imageDetail"]["categoryImgName"]
        obj.insertImage(assetId,categoryName)
        return "inserted"
    
    def put(self):
        data=request.get_json("updateImageDetail")
        Id=data["updateImageDetail"]["Id"]
        assetId=data["updateImageDetail"]["assetImgId"]
        categoryName=data["updateImageDetail"]["categoryImgName"]
        jsonData=obj.updateImageDetail(Id,assetId,categoryName)
        return "updated"
    
    def delete(self):
        data=request.get_json("Id")
        id=data["Id"]
        print(id)
        obj.deleteImageDetail(id)
        return "deleted"
    
class usersCrud(Resource):

    def get(self):
        Id=[]
        data={"UsersIds":Id}
        rows=obj.searchUsersIds()
        for row in rows:
            Id.append(row.id)
        return data

    def post(self):
        data=request.get_json("usersDetail")
        username=data["usersDetail"]["username"]
        email=data["usersDetail"]["email"]
        dob=data["usersDetail"]["dob"]
        obj.insertUsers(username,email,dob)
        return "inserted"

    def put(self):
        data=request.get_json("usersDetail")
        id=data["usersDetail"]["id"]
        username=data["usersDetail"]["username"]
        email=data["usersDetail"]["email"]
        dob=data["usersDetail"]["dob"]
        obj.updateUsers(id,username,email,dob)
        return "updated"
    
    def delete(self):
        data=request.get_json("Id")
        id=data["Id"]
        print(id)
        obj.deleteUsers(id)
        return "deleted"

class fetchCategoryDetail(Resource):
    @obj.jwt_required
    def get(self):
        data=request.get_json("Id")
        id=data["Id"]
        row=obj.CategoryDetail(id)
        data={"Id":row.id,"assetId":row.AssetsId,"categoryName":row.categoryName}
        return data

class fetchAssetDetail(Resource):
    @obj.jwt_required
    def get(self):
        data=request.get_json("Id")
        id=data["Id"]
        row=obj.assetsDetail(id)
        newDate = str(row.Date)
        print(type(newDate))
        data={"id":row.id,"name":row.name,"serialNo":row.serialNo,"date":newDate,"cost":row.cost,"userId":row.userId,"model":row.model}
        print(data)
        return data

class fetchImageDetail(Resource):
    @obj.jwt_required
    def get(self):
        data=request.get_json("Id")
        id=data["Id"]
        row=obj.imageDetail(id)
        data={"Id":row.id,"ImageId":row.AssetsImageId,"categoryImageName":row.categoryImageName}
        return data

class fetchUsersDetail(Resource):
    def get(self):
        data = request.get_json("Id")
        id = data["Id"]
        row=obj.usersDetail(id)
        data={"Id":row.id,"username":row.userName,"email":row.email,"dob":row.dob}
        print(data)
        return data

class assignedCrud(Resource):

    def post(self):
        data=request.get_json("assignedDetail")
        userId=data["assignedDetail"]["UserId"]
        assetId=data["assignedDetail"]["assetId"]
        date = datetime.now()
        rows=obj.select(assetId,userId)
        print(rows,"------------")
        if rows!=None:
            id=rows.id
            data=obj.duplicateEntry(id)
            print(data)
            result="Already assigned"
            return result
        else:
            obj.insertAssigned(userId, assetId, date)
            return "inserted"

    def put(self):
        data=request.get_json("updateAssignedDetail")
        id=data["updateAssignedDetail"]["Id"]
        userId=data["updateAssignedDetail"]["UserId"]
        assetId=data["updateAssignedDetail"]["assetId"]
        date = datetime.now()
        # print(userId, assetId, date)
        obj.updateAssigned(id,userId, assetId, date)
        return "updated"
    
    def delete(self):
        data=request.get_json("Id")
        id=data["Id"]
        print(id)
        obj.deleteAssignedDetail(id)
        return "deleted"
