from flask import Flask,jsonify
from flask.globals import request

app = Flask(__name__)

from products import products

@app.route('/ping')
def ping():
    return jsonify({"message":"pong!"})

@app.route('/products',methods=['GET'])
def getProducts():
    return jsonify(products)

@app.route('/products/<string:product_name>')
def getProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if (len(productFound) > 0):
        return jsonify(productFound[0])
    else: 
        return jsonify({"message":"Product not Found"})

@app.route('/products',methods=['POST'])
def addProduct():
    products.append(request.json)
    return jsonify({"message":"saved","products":products})

@app.route('/product/<string:product_name>',methods=['PUT'])
def updateProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    productFound[0] = request.json
    return jsonify({"message":"saved","product updated":productFound[0]})

@app.route('/product/<string:product_name>',methods=['DELETE'])
def deleteProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    products.remove(productFound[0])
    return jsonify({"message":"deleted","product deleted":products})

if __name__ == '__main__':
    app.run(debug=True,port=4000)