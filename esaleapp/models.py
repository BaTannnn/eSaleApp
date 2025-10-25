from itertools import product
from tkinter.font import names

from esaleapp import db, app
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship,backref

class BaseModel(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)

class Category(BaseModel):
    name = Column(String(50), nullable=False, unique=True)
    products = relationship('Product', backref='category', lazy=True)

class Product(BaseModel):
    name = Column(String(100), nullable=False)
    description = Column(Text)
    price = Column(Integer)
    image = Column(String(100), default="https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg")
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        categories = ['Điện thoại', 'Máy tính bảng', 'Laptop']
        products = [{
            "name": "iPhone 7 Plus",
            "description": "Apple, 32GB, RAM: 3GB, iOS13",
            "price": 17000000,
            "image":
                "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg",
            "category_id": 1
        }, {
            "name": "iPad Pro 2020",
            "description": "Apple, 128GB, RAM: 6GB",
            "price": 37000000,
            "image":
                "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
            "category_id": 2
        },
            {
                "name": "Galaxy Note 10 Plus",
                "description": "Samsung, 64GB, RAML: 6GB",
                "price": 24000000,
                "image":
                    "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
                "category_id": 1
            }, {
                "name": "iPad Pro 2020",
                "description": "Apple, 128GB, RAM: 6GB",
                "price": 37000000,
                "image":
                    "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
                "category_id": 2
            }, {
                "name": "iPad Pro 2020",
                "description": "Apple, 128GB, RAM: 6GB",
                "price": 37000000,
                "image":
                    "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
                "category_id": 2
            }, {
                "name": "iPad Pro 2020",
                "description": "Apple, 128GB, RAM: 6GB",
                "price": 37000000,
                "image":
                    "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
                "category_id": 2
            }, {
                "name": "iPad Pro 2020",
                "description": "Apple, 128GB, RAM: 6GB",
                "price": 37000000,
                "image":
                    "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
                "category_id": 2
            }]
        # for c in categories:
        #     category = Category(name=c)
        #     db.session.add(category)
        # db.session.commit()
        for p in products:
            product = Product(**p)
            db.session.add(product)
            db.session.commit()
