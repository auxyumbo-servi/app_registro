from core.database import SessionLocal

from models.registro import Registro


class RegistroService:


    def create(self, data):

        db = SessionLocal()


        registro = Registro(
            cliente=data.cliente,
            cantidad=data.cantidad,
            recipiente=data.recipiente,
            dia=data.dia,
            observacion=data.observacion
        )


        db.add(registro)

        db.commit()

        db.refresh(registro)


        db.close()


        return Registro



    def get_all(self):

        db = SessionLocal()

        registros = db.query(Registro).all()

        db.close()


        return registros