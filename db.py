from mongoengine import *
from pprint import pprint
from bson.json_util import dumps
connect('tumblelog')

class User(Document):
    
    username=StringField(required=True)
    pasword = StringField(required=True)
    first_name = StringField(max_length=50)
    hash = StringField(required=True, max_length=500)

class Products(Document):
    productId=StringField(required=True)
    category=StringField(required=True)
    productName=StringField(required=True)
    productModel=StringField(required=True)
    price=IntField(required=True)
    availableQuantity=IntField(required=True)


class userCart(Document):
    itemID=IntField(required=True)
    username=StringField(required=True)
    productId=StringField(required=True)
    productName=StringField(required=True)
    quantity=IntField(required=True)


def userInsert(username,pasword,first_name,hash):
    user=User(
        
        username = username,
        pasword = pasword,
        first_name = first_name,
        
        hash=(hash)       
    )
    user.save() 


def itemInsert(productId,category,productName,productModel,availableQuantity,price):
    item=Products(
        productId=productId,
        category = category,
        productName = productName,
        productModel = productModel,
        availableQuantity=availableQuantity,
        price=price    
    )
    item.save() 

def cartInsert(count,username,productId,productName,quantity):
    item=userCart(
        itemID=count,
        username=username,
        productId = productId,
        productName = productName,
        quantity = quantity
    )
    item.save() 
#userInsert('jadedBlues','Acnolgia3245','Shree','23jj')

def viewAll():
    posts = Products.objects
    val={}
    for x in posts:
        val['productId']=x.productId
        val['productName']=x.productName
        val['category']=x.category
        val['productName']=x.productName
        val['productModel']=x.productModel
        val['price']=x.price
        val['availableQuantity']=x.availableQuantity
        
    return val

def cartAll(username):
    posts = userCart.objects(username = username)
    val={}
    for x in posts:
        val['itemID']=x.itemID
        val['username']=x.username
        val['productId']=x.productId
        val['productName']=x.productName
        val['quantity']=x.quantity

        
    return val

#itemInsert("2","cars",'asdfa','spiapfd','5',32)
#print(viewAll())
#User.objects.delete()
#

# x=[i['itemID'] for i in userCart.objects(username).order_by('itemID')][0]
# print(x)

item = userCart.objects.get(Q(username = 'jadedBlues') & Q(itemID= 1))
item.quantity=5
item.save()
print(item.to_json())