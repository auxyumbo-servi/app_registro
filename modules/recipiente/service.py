from models.recipiente import Recipiente
from modules.recipiente.repository import RecipienteRepository


class RecipienteService:

    repository = RecipienteRepository()

    @staticmethod
    def crear_recipiente(nombre, equivalencia):
        
        if not nombre:
            raise ValueError ('Nombre Obligatorio')

        recipiente = Recipiente(
            nombre=nombre,
            equivalencia=equivalencia
        )
        return RecipienteService.repository.crear_recipiente(recipiente)

    @staticmethod
    def obtener_recipientes():
        return RecipienteService.repository.obtener_recipientes()

    @staticmethod
    def obtener_opciones():
        recipientes = RecipienteService.repository.obtener_recipientes()

        return {
            n.id: n.nombre
            for n in recipientes
        }

    @staticmethod
    def obtener_recipiente(recipiente_id):
        return RecipienteService.repository.obtener_recipiente(recipiente_id)

