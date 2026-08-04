from core.database import SessionLocal

from models.product import Product


class ProductService:


    def create(self, data):

        db = SessionLocal()


        product = Product(
            name=data.name,
            quantity=data.quantity,
            price=data.price,
            expiration_date=data.expiration_date,
            category=data.category
        )


        db.add(product)

        db.commit()

        db.refresh(product)


        db.close()


        return product



    def get_all(self):

        db = SessionLocal()

        products = db.query(Product).all()

        db.close()


        return products