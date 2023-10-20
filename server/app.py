#!/usr/bin/env python3
from flask import Flask, request, make_response, jsonify, session
from flask_cors import CORS
from flask_migrate import Migrate
# Standard library imports

# Remote library imports
from flask import request
from flask_restful import Resource
from flask_bcrypt import Bcrypt

# Local imports
from config import app, db, api
# Add your model imports
from models import db, User, Order, Product, OrderProduct

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

app.secret_key = b"Y\xf1Xz\x00\xad|eQ\x80t \xca\x1a\x10K"

bcrypt = Bcrypt(app)

CORS(app, resources='*')
migrate = Migrate(app, db)

db.init_app(app)

# Views go here!

@app.route('/')
def index():
    return 'the stuff'

@app.post("/users")
def create_user():
    json = request.json

    password_digest = bcrypt.generate_password_hash(json["password"]).decode("utf-8")

    new_user = User(username=json["username"], password_digest=password_digest)
    db.session.add(new_user)
    db.session.commit()
    session["user_id"] = new_user.id
    return new_user.to_dict(), 201

@app.post("/login")
def login():
    json = request.json
    user = User.query.filter(User.username == json["username"]).first()

    if user and bcrypt.check_password_hash(user.password_digest, json["password"]):
        session["user_id"] = user.id
        return user.to_dict(), 200
    else:
        return {"error": "Invalid username or password"}, 401


@app.get("/check_session")
def check_session():
    user = User.query.filter(User.id == session.get("user_id")).first()
    if user:
        return user.to_dict(), 200
    else:
        return {"message": "No user logged in"}, 401


@app.delete("/logout")
def logout():
    session.pop("user_id")
    return {"message": "Logged out"}, 200


@app.post("/order_products")
def order_products():
    request_data = request.get_json()
    try:
        order_products = OrderProduct(
            order_id=session.get("order_id"),
            prooduct_id =request_data["product_id"],
        )
        db.session.add(book)
        db.session.commit()
        return make_response(jsonify(book.to_dict()), 202)
    except:
        return make_response(jsonify({"error": "ya messed up son"}), 405)


@app.get("/orders")
def get_order():
    order = Order.query.filter(Order.id == session.get("user_id")).first()
    if db.session.get(User, session.get("user_id")):
        return {"total": order.total_price()}, 200
    else:
        return {"error": "not authorized"}, 401


@app.get("/products")
def get_products():
    products = Product.query.all()
    data =  [product.to_dict() for product in products]
    return make_response(jsonify(data), 200)


# @app.post("/order")
# def post_order():
#     data = request.json
#     try:
#         order = Order(
#             product_id=data.get("product_id"),
#             user_id=data.get("user_id"),
#             total_price=data.get("total_price"),
#         )
#         db.session.add(order)
#         db.session.commit()
#         return make_response(
#             jsonify(order.to_dict(rules=("-product_id", "-user_id"))), 201
#         )
#     except Exception as e:
#         return make_response(jsonify({"error": str(e)}), 405)



if __name__ == '__main__':
    app.run(port=5555, debug=True)

