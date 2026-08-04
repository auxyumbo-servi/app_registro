from nicegui import ui


from core.database import create_tables


from modules.products.views import products_page



create_tables()



ui.page("/")(
    products_page
)



ui.run()