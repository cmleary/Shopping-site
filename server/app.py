#!/usr/bin/env python3
from flask import Flask, request, make_response, jsonify,session
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

CORS(app)
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


# SESSION LOGIN/LOGOUT#


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


# EXAMPLE OTHER RESOURCES WITH AUTH #


# @app.get("/films")
# def get_cartoons():
#     if db.session.get(User, session.get("user_id")):
#         return [
#             {"id": 1, "name": "Fateful Findings"},
#             {"id": 2, "name": "Twisted Pair"},
#             {"id": 3, "name": "Double Down"},
#         ], 200
#     else:
#         return {"error": "not authorized"}, 401




@app.get("/users")
def get_users():
    users = User.query.all()
    data = [user.to_dict(rules=("-orders",)) for user in users]
    return make_response(jsonify(data), 200)


@app.get("/users/<int:id>")
def get_user_by_id(id):
    user = User.query.filter(User.id == id).first()
    if not user:
        make_response(jsonify({"error": "no id matches that"}), 404)
    user_dict = user.to_dict()
    return make_response(jsonify(user_dict), 200)


@app.get("/orders")
def get_order():
    order = Order.query.filter(Order.id == session.get("user_id")).first()
    if db.session.get(User, session.get("user_id")):
        return {"total": order.total_price()}, 200
    else:
        return {"error": "not authorized"}, 401


@app.get("/products/<int:id>")
def get_products(id):
    product = db.session.get(Product, id)
    product_dict = product.to_dict(rules=("-orders",))
    return make_response(jsonify(product_dict), 200)

@app.patch("/products/<int:id>")
def patch_products(id):
    data = request.get_json()
    product = Product.query.filter(Product.id == id).first()
    if not product:
        make_response(jsonify({"error": "no such product"}), 404)
    try:
        for key in data:
            setattr(product, key, data[key])
        db.session.add(product)
        db.session.commit()
        return make_response(jsonify(product.to_dict()), 201)
    except:
        return make_response(jsonify({"error": "could not update product"}), 405)


@app.post("/carts")
def post_cart():
    data = request.json
    try:
        cart = Cart(
            product_id=data.get("product_id"),
            user_id=data.get("user_id"),
            day=data.get("day"),
        )
        db.session.add(cart)
        db.session.commit()
        return make_response(
            jsonify(cart.to_dict(rules=("-product_id", "-user_id"))), 201
        )
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 405)



if __name__ == '__main__':
    app.run(port=5555, debug=True)

