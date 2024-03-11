import web

urls = (
    '/',
    'mvc.controllers.index.Index',
    '/ver_producto',
    'mvc.controllers.ver_producto.VerProducto',
    '/insertar_producto',
    'mvc.controllers.insertar_producto.InsertarProducto',
    '/borrar_producto',
    'mvc.controllers.borrar_producto.BorrarProducto',
    '/actualizar_producto',
    'mvc.controllers.actualizar_producto.ActualizarProducto',
)

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
