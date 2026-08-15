from .schemas import DetalleCreate
from .services import DetalleService


class DetalleController:


    def __init__(self):

        self.service = DetalleService()



    def save_product(
        self,
        regristo_id,
        recipiente,
        cantidad,
        observacion
    ):


        data = DetalleCreate(

            regristo_id=regristo_id,

            recipiente=recipiente,

            cantidad=cantidad,

            observacion=observacion,

        )


        return self.service.create(data)



    def products(self):

        return self.service.get_all()