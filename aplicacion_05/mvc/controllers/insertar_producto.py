import web

render = web.template.render('mvc/views/')

lista_de_productos = []

class ListaProductos:
    def GET(self):
        # Aquí obtienes la lista de productos desde donde sea que los estés almacenando
        productos = obtener_lista_de_productos()

        # Luego pasas la lista de productos al renderizar la plantilla
        return render.lista_productos(productos=productos)
