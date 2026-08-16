from nicegui import ui

from core.database import engine
from models.base import Base

# Importar modelos para que SQLAlchemy los registre
from models.cliente import Cliente
from models.recipiente import Recipiente
from models.registro import Registro
from models.detalle_registro import DetalleRegistro

from modules.cliente.views import cliente_view
from modules.recipiente.views import recipiente_view
from modules.registro.views import registro_view


# Crear las tablas
Base.metadata.create_all(bind=engine)


@ui.page("/")
def index():

    cliente_view()

@ui.page("/recipientes")
def recipiente():

    recipiente_view()

@ui.page("/registros")
def registro():

    registro_view()

ui.run()
