from nicegui import ui


def product_table(rows):


    data=[]


    for p in rows:

        data.append({

            "name": p.name,

            "quantity": p.quantity,

            "price": p.price,

            "category": p.category

        })


    ui.table(

        columns=[

            {
                "name":"name",
                "label":"Nombre",
                "field":"name"
            },

            {
                "name":"quantity",
                "label":"Cantidad",
                "field":"quantity"
            },


            {
                "name":"price",
                "label":"Precio",
                "field":"price"
            },


            {
                "name":"category",
                "label":"Categoria",
                "field":"category"
            }

        ],


        rows=data

    )