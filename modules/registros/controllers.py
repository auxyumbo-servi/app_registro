from .schemas import RegistroCreate
from .services import RegistroService


class RegistroController:


    def __init__(self):

        self.service = RegistroService()



    def save_product(
        self,
        fecha,
        nombre,
        aforo
):


        data = RegistroCreate(

            fecha=fecha,

            nombre=nombre,

            aforo=aforo,

        )


        return self.service.create(data)



    def products(self):

        return self.service.get_all()