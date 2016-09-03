from flask import Flask, jsonify,request
from flask_restful import Resource, Api
from pymongo import MongoClient
from bson.json_util import dumps
app = Flask(__name__)
api = Api(app)
c = MongoClient()
db=c.food

m=db.count.insert_one({"count":1})

@app.route('/getorder', methods=['GET'])
def get_orders():
	cursor=db.orders.find()
	#cursor=str(cursor)
	return dumps(cursor)

@app.route('/getorder/<int:orderid>',methods=['GET'])
def get_order(orderid):
	cursor=db.orders.find_one({"order_id":orderid})
	return dumps(cursor)



@app.route('/saveorder',methods=['POST'])
def save_order():
	cursor=db.count.find_one()
	count=cursor['count']
	count=int(count)
	count+=1
	db.orders.insert_one({
	'order_id':count,
	'cust_address':request.json['cust_address'],
	'cust_contact':request.json['cust_contact'],
	'cust_name':request.json['cust_name'],
	'cust_pincode':request.json['cust_pincode'],
	'order_description':request.json['order_description']
	})
	temp=count-1;
	re=db.count.update_one({"count":temp},{"$set":{"count":count}})
	return dumps(db.orders.find_one({"order_id":count}))

@app.route('/saveorder/<int:orderid>',methods = ['POST'])
def update_order(orderid):
	db.orders.update_one({"order_id":orderid},{"$set":{
			'cust_address':request.json['cust_address'],
			'cust_contact':request.json['cust_contact'],
			'cust_name':request.json['cust_name'],
			'cust_pincode':request.json['cust_pincode'],
			'order_description':request.json['order_description']
			}})
	return dumps(db.orders.find_one({"order_id":orderid}))












if __name__ == '__main__':
    app.run(debug=True)