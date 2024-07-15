class NodoAVL:
    def __init__(self, proyecto):
        self.proyecto = proyecto
        self.izquierda = None
        self.derecha = None
        self.altura = 1
#clase
class AVLTree:
    def __init__(self):
        self.raiz = None

    def insertar(self, proyecto):
        if not self.raiz:
            self.raiz = NodoAVL(proyecto)
        else:
            self.raiz = self._insertar(self.raiz, proyecto)

    def _insertar(self, nodo, proyecto):
        if not nodo:
            return NodoAVL(proyecto)
        elif proyecto.id < nodo.proyecto.id:
            nodo.izquierda = self._insertar(nodo.izquierda, proyecto)
        else:
            nodo.derecha = self._insertar(nodo.derecha, proyecto)

        nodo.altura = 1 + max(self._get_altura(nodo.izquierda), self._get_altura(nodo.derecha))

        balance = self._get_balance(nodo)
        if balance > 1:
            if proyecto.id < nodo.izquierda.proyecto.id:
                return self._rotar_derecha(nodo)
            else:
                nodo.izquierda = self._rotar_izquierda(nodo.izquierda)
                return self._rotar_derecha(nodo)
        if balance < -1:
            if proyecto.id > nodo.derecha.proyecto.id:
                return self._rotar_izquierda(nodo)
            else:
                nodo.derecha = self._rotar_derecha(nodo.derecha)
                return self._rotar_izquierda(nodo)
        return nodo

    def eliminar(self, proyecto):
        if not self.raiz:
            return
        else:
            self.raiz = self._eliminar(self.raiz, proyecto)

    def _eliminar(self, nodo, proyecto):
        if not nodo:
            return nodo
        elif proyecto.id < nodo.proyecto.id:
            nodo.izquierda = self._eliminar(nodo.izquierda, proyecto)
        elif proyecto.id > nodo.proyecto.id:
            nodo.derecha = self._eliminar(nodo.derecha, proyecto)
        else:
            if nodo.izquierda is None:
                temp = nodo.derecha
                nodo = None
                return temp
            elif nodo.derecha is None:
                temp = nodo.izquierda
                nodo = None
                return temp
            temp = self._get_min_value_node(nodo.derecha)
            nodo.proyecto = temp.proyecto
            nodo.derecha = self._eliminar(nodo.derecha, temp.proyecto)

        if nodo is None:
            return nodo
        
        nodo.altura = 1 + max(self._get_altura(nodo.izquierda), self._get_altura(nodo.derecha))
        balance = self._get_balance(nodo)
        
        if balance > 1:
            if self._get_balance(nodo.izquierda) >= 0:
                return self._rotar_derecha(nodo)
            else:
                nodo.izquierda = self._rotar_izquierda(nodo.izquierda)
                return self._rotar_derecha(nodo)
        if balance < -1:
            if self._get_balance(nodo.derecha) <= 0:
                return self._rotar_izquierda(nodo)
            else:
                nodo.derecha = self._rotar_derecha(nodo.derecha)
                return self._rotar_izquierda(nodo)
        
        return nodo

    def consultar_proyecto(self, id):
        return self._consultar_proyecto(self.raiz, id)

    def _consultar_proyecto(self, nodo, id):
        if not nodo or nodo.proyecto.id == id:
            return nodo.proyecto if nodo else None
        if id < nodo.proyecto.id:
            return self._consultar_proyecto(nodo.izquierda, id)
        return self._consultar_proyecto(nodo.derecha, id)

    def recorrido_in_orden(self, nodo):
        res = []
        if nodo:
            res = self.recorrido_in_orden(nodo.izquierda)
            res.append(nodo.proyecto)
            res = res + self.recorrido_in_orden(nodo.derecha)
        return res

    def _rotar_derecha(self, z):
        y = z.izquierda
        T3 = y.derecha
        y.derecha = z
        z.izquierda = T3
        z.altura = 1 + max(self._get_altura(z.izquierda), self._get_altura(z.derecha))
        y.altura = 1 + max(self._get_altura(y.izquierda), self._get_altura(y.derecha))
        return y

    def _rotar_izquierda(self, z):
        y = z.derecha
        T2 = y.izquierda
        y.izquierda = z
        z.derecha = T2
        z.altura = 1 + max(self._get_altura(z.izquierda), self._get_altura(z.derecha))
        y.altura = 1 + max(self._get_altura(y.izquierda), self._get_altura(y.derecha))
        return y

    def _get_min_value_node(self, nodo):
        if nodo is None or nodo.izquierda is None:
            return nodo
        return self._get_min_value_node(nodo.izquierda)

    def _get_altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura

    def _get_balance(self, nodo):
        if not nodo:
            return 0
        return self._get_altura(nodo.izquierda) - self._get_altura(nodo.derecha)
