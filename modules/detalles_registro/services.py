from core.database import SessionLocal

from models.detalle_registro import DetalleRegistro


class DetalleService:


    def create(self, data):

        db = SessionLocal()


        detalle = DetalleRegistro(
            fecha=data.fecha,
            nombre=data.nombre_id,
            quantity=data.quantity,
            price=data.price,
            category=data.category
        )


        db.add(detalle)

        db.commit()

        db.refresh(detalle)


        db.close()


        return detalle



    def get_all(self):

        db = SessionLocal()

        detalles = db.query(DetalleRegistro).all()

        db.close()


        return detalles