from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db


# Models go here!
metadata = MetaData(
    naming_convention={
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    }
)

db = SQLAlchemy(metadata=metadata)


class User(db.Model):
    __tablename__ = "users_table"

    # serialize_rules = ("-order_list.product_object",)

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password_digest = db.Column(db.String)

    order_list = db.relationship("Order", back_populates="users", cascade="all, delete-orphan")

    def __repr__(self):
        return f'<User id="{self.id}" username="{self.username}">'

    def to_dict(self):
        return {"id": self.id, "username": self.username}


class Order(db.Model, SerializerMixin):
    __tablename__ = "order_table"

    serialize_rules = ("-order_products", "-users")

    id = db.Column(db.Integer, primary_key=True)
    total_price = db.Column(db.Float)
    closed = db.Column(db.Boolean, default = False)
    user_id = db.Column(db.Integer, db.ForeignKey("users_table.id"))

    users = db.relationship("User", back_populates="order_list")
    
    order_products = db.relationship("OrderProduct", back_populates="order_object")
    products = association_proxy("order_products","product_object")
    

    # def to_dict(self):
    #     return {"id": self.id,"total_price": self.total_price}
    
    def total_price(self):                                          
        sum_price = sum([x.price for x in self.products])            
        return (sum_price)                                            
        
class OrderProduct(db.Model, SerializerMixin):
    __tablename__ = "orderproduct_table"

    # serialize_rules = ("-order_object.order_products", "-product_object.order_products")

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("order_table.id"))
    product_id = db.Column(db.Integer, db.ForeignKey("product_table.id"))

    order_object = db.relationship("Order", back_populates = "order_products")
    product_object = db.relationship("Product", back_populates = "order_products")




class Product(db.Model, SerializerMixin):
    __tablename__ = "product_table"

    # serialize_rules = ("-order_products.product_object",)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Float)
    image_url = db.Column(db.String, nullable = False)

    order_products = db.relationship("OrderProduct", back_populates="product_object")
    orders = association_proxy("order_products", "order_object")


    def to_dict(self):
        return {"id": self.id, "name": self.name, "price": self.price, "image_url": self.image_url}