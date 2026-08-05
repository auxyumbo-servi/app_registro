from nicegui import ui

from datetime import date

from .controllers import ProductController

from .components import product_table



controller = ProductController()



def products_page():


    expiration = ui.date(
        "Fecha vencimiento"
    )

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

            expiration.value,

            name.value,

            int(quantity.value),

            float(price.value),

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