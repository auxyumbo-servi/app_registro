from modules.recipiente.service import RecipienteService

class RecipienteController:

    @staticmethod
    def crear_recipiente(nombre, equivalencia):
        return RecipienteService.crear_recipiente(
            nombre,
            equivalencia
        )

    @staticmethod
    def recipientes():
        return RecipienteService.obtener_recipientes()

    @staticmethod
    def opciones_recipientes():
        return RecipienteService.obtener_opciones()

    @staticmethod
    def obtener_recipiente(recipiente_id):
        return RecipienteService.obtener_recipiente(recipiente_id)
