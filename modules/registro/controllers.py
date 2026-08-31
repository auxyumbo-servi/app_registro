from .schemas import RegistroCreate
from .services import RegistroService


class RegistroController:


    def __init__(self):

        self.service = RegistroService()



    def save_registro(
        self,
        dia,
        cliente,
        cantidad,
        recipiente,
        observacion
    ):


        data = RegistroCreate(

            cliente=cliente,

            cantidad=cantidad,

            recipiente=recipiente,

            dia=dia,

            observacion=observacion
        )


        return self.service.create(data)



    def registros(self):

        return self.service.get_all()