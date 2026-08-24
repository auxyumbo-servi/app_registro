from core.database import SessionLocal

from models.tarifa import Tarifa


class ProductService:


    def create(self, data):

        db = SessionLocal()


        tarifa = Tarifa(
            name=data.name,
            quantity=data.quantity,
            price=data.price,
            expiration_date=data.expiration_date,
            category=data.category
        )


        db.add(Tarifa)

        db.commit()

        db.refresh(tarifa)


        db.close()


        return tarifa



    def get_all(self):

        db = SessionLocal()

        tarifas = db.query(Tarifa).all()

        db.close()


        return tarifas