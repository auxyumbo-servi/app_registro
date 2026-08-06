from core.database import SessionLocal

from models.registro import Registro


class RegistroService:


    def create(self, data):

        db = SessionLocal()


        registro = Registro(
            fecha=data.fecha,
            nombre=data.nombre_id,
            aforo=data.aforo
        )


        db.add(registro)

        db.commit()

        db.refresh(registro)


        db.close()


        return registro



    def get_all(self):

        db = SessionLocal()

        registros = db.query(Registro).all()

        db.close()


        return registros