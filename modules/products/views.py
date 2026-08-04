from nicegui import ui

from datetime import date

from .controllers import ProductController

from .components import product_table



controller = ProductController()



def products_page():


    ui.label(
        "Registro productos"
    ).classes(
        "text-2xl"
    )


    name = ui.input(
        "Nombre"
    )


    quantity = ui.number(
        "Cantidad"
    )


    price = ui.number(
        "Precio"
    )


    expiration = ui.date(
        "Fecha vencimiento"
    )


    category = ui.input(
        "Categoria"
    )


    table = ui.column()



    def load_table():

        table.clear()


        with table:

            product_table(
                controller.products()
            )



    def save():


        controller.save_product(

            name.value,

            int(quantity.value),

            float(price.value),

            expiration.value,

            category.value

        )


        # limpiar campos

        name.value=""

        quantity.value=None

        price.value=None

        expiration.value=None

        category.value=""



        load_table()



    ui.button(
        "Guardar",
        on_click=save
    )


    load_table()