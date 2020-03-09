from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from db import Products, viewAll, cartInsert,User,userCart, cartAll
from mongoengine.queryset.visitor import Q

app = Flask(__name__)
api = Api(app)

todos = {}

class TodoSimple(Resource):
    def post(self, userid,productid,quantity):
        # Retrieve list of users and products by username and product_id
        users = User.objects
        products = Products.objects

        for user in users:
            if userid == user['username']:
                break
            else:
                return jsonify('error': "user not located")

        for product in products:
            if productid==product['productId']:
                productName = product['productName']
                quant = product['availableQuantity']
                if quantity>quant:
                    return jsonify{"error":"the quantity of the product is not sufficient to add to cart"}
                break
        
        count = userCart.objects(username='jadedBlues').order_by('-itemID') 
        count = int(count[0]['itemID'])+1
            
        
        cartInsert(count,userid,productid,productName,quantity)
        
        
        return jsonify(userCart.objects(username=userid).to_json())

class EditSimple(Resource):
    def put(self, userid,itemID,quantity):
        # Retrieve list of users and products by username and product_id
        users = User.objects
        products = Products.objects

        for user in users:
            if userid == user['username']:
                break
            
            else:
                return jsonify('error': "user not located")
        for product in products:
            if productid==product['productId']:
                productName = product['productName']
                quant = product['availableQuantity']
                if quantity>quant:
                    return jsonify{"error":"the quantity of the product is not sufficient to add to cart"}
                break
            
        item = userCart.objects.get(Q(username = userid) & Q(itemID= itemID))
        item.quantity=quantity
        item.save()

        return jsonify(userCart.objects(username=userid).to_json())

class DeleteSimple(Resource):
    def delete(self, userid,itemID):
        # Retrieve list of users and products by username and product_id
        users = User.objects
        products = Products.objects

        for user in users:
            if userid == user['username']:
                break
            
            else:
                return jsonify('error': "user not located")
        
        item = userCart.objects.get(Q(username = userid) & Q(itemID= itemID))
        item.delete()

        return jsonify(userCart.objects(username=userid).to_json())

class CartView(Resource):
    def get(self):
        return jsonify(userCart.objects().to_json())    

class ProductView(Resource):
    def get(self):
        return jsonify(Products.objects().to_json())

api.add_resource(TodoSimple, '/addCart/<string:userid>/<string:productid>/<string:quantity>')
api.add_resource(EditSimple, '/editCart/<string:userid>/<string:itemID>/<string:quantity>')
api.add_resource(DeleteSimple, '/editCart/<string:userid>/<string:itemID>')
api.add_resource(ProductView, '/products')
api.add_resource(CartView, '/viewCart')

if __name__ == '__main__':
    app.run(debug=True)