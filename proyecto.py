class Proyecto:
    def __init__(self, id, nombre, descripcion, fecha_inicio, fecha_vencimiento, estado_actual, empresa, gerente, equipo):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_vencimiento = fecha_vencimiento
        self.estado_actual = estado_actual
        self.empresa = empresa
        self.gerente = gerente
        self.equipo = equipo

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Descripción: {self.descripcion}, Fecha de inicio: {self.fecha_inicio}, Fecha de vencimiento: {self.fecha_vencimiento}, Estado actual: {self.estado_actual}, Empresa: {self.empresa}, Gerente: {self.gerente}, Equipo: {self.equipo}"
