class Credenciales:
    def __init__(self, usuario, contrasena):
        self.usuario = usuario
        self.contrasena = contrasena

    def autenticar(self):
        return True if (self.usuario == 'Dan' and self.contrasena == '1234') else False

class HacerPedido(Credenciales):
    def __init__(self, usuario, contrasena, tipoBebida, pedidoAcumulado, cafeSabores, tipoLeche, tamano, toppings, cantidadProducto, pedidoFinal):
        super().__init__(usuario, contrasena)
        self._tipoBebida = tipoBebida
        self._pedidoAcumulado = pedidoAcumulado
        self._cafeSabores = cafeSabores
        self._tipoLeche = tipoLeche
        self._tamano = tamano
        self._toppings = toppings
        self._cantidadProducto = cantidadProducto
        self._pedidoFinal = pedidoFinal

    def pedido(self):
        self._cantidadProducto = input('Ingrese la cantidad de productos:\n>> ')
        for i in range(0, int(self._cantidadProducto)):
            print(f'Ingrese la orden para el pedido {i + 1}')
            self._pedidoAcumulado.append(self._tipoBebida[input('Ingrese el tipo de bebida:\n1.Café\n2.Frappé\n>> ')])
            self._pedidoAcumulado.append(self._tamano[input('Ingrese el tamaño de la bebida:\n1.Chico\n2.Mediano\n3.Grande\n>> ')])
            self._pedidoAcumulado = tuple(self._pedidoAcumulado)
            self._pedidoFinal.append(self._pedidoAcumulado)
            self._pedidoAcumulado = list(self._pedidoAcumulado)
            self._pedidoAcumulado.clear()

        return self._pedidoFinal


user = input('Ingrese el usuario: ')
pswd = input('Ingrese la contraseña: ')

empleado1 = Credenciales(user, pswd)
pedido1 = HacerPedido(user, pswd, {'1':'Café', '2':'Frappé'}, [], {'1':'Capuccino', '2':'Moka'}, {'1':'Entera', '2':'Deslactosada', '3':'Almendras', '4':'Coco'}, 
                      {'1':'Chico', '2':'Mediano', '3':'Grande'}, {'1':'Malvaviscos', '2':'Chispas de chocolate', '3':'Ninguno'}, 0, [])

if empleado1.autenticar():
    pedidoFinal = pedido1.pedido()
    for i in pedidoFinal:
        pass
else:
    print('Credenciales no válidas')
    