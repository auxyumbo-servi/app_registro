from .schemas import ProductCreate
from .services import ProductService


class ProductController:


    def __init__(self):

        self.service = ProductService()



    def save_product(
        self,
        name,
        quantity,
        price,
        expiration_date,
        category
    ):


        data = ProductCreate(

            name=name,

            quantity=quantity,

            price=price,

            expiration_date=expiration_date,

            category=category
        )


        return self.service.create(data)



    def products(self):

        return self.service.get_all()