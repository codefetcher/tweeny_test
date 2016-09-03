from flask import Flask, jsonify,request
import json
from flask_restful import Resource, Api



app = Flask(__name__)
api = Api(app)

orders=[
    {
      "cust_address": u"katraj", 
      "cust_contact": 9923593344, 
      "cust_name": u"mayank", 
      "cust_pincode": 411043, 
      "order_description": u"less spicy", 
      "order_id": 1
    }, 
    {
      "cust_address": u"katraj", 
      "cust_contact": 9923593344, 
      "cust_name": u"gupta", 
      "cust_pincode": 411043, 
      "order_description":u"spicy", 
      "order_id": 2
    }
  ]


@app.route('/getorder', methods=['GET'])
def get_orders():
	return jsonify( {"orders":orders})

@app.route('/getorder/<int:orderid>',methods	=['GET'])
def get_order(orderid):
	
	for order in orders:
		if order['order_id']==orderid:
			curr_order=[order]
	return jsonify({"order":curr_order[0]})



@app.route('/saveorder',methods=['POST'])
def save_order():
	order={
	'order_id':orders[-1]['order_id']+1	,
	'cust_address':request.json['cust_address'],
	'cust_contact':request.json['cust_contact'],
	'cust_name':request.json['cust_name'],
	'cust_pincode':request.json['cust_pincode'],
	'order_description':request.json['order_description']
	}
	orders.append(order)
	return jsonify({"order":order})

@app.route('/saveorder/<int:orderid>',methods = ['POST'])
def update_order(orderid):
	for order in orders:
		if order['order_id']==orderid:
			order[0]['cust_address']=request.json['cust_address']
			order[0]['cust_contact']=request.json['cust_contact']
			order[0]['cust_name']=request.json['cust_name']
			order[0]['cust_pincode']=request.json['cust_pincode']
			order[0]['order_description']=request.json['order_description']
			return jsonify({"orders":order})












if __name__ == '__main__':
    app.run(debug=True)