from .models import Category,Product

def get_categories():
    return Category.query.all()

def get_products(kw=None, category_id=None):
    product = Product.query

