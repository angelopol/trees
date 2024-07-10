import csv
from arboles import AVLTree
from proyecto import Proyecto

class Empresa:
    def __init__(self, id, nombre, descripcion, fecha_creacion, direccion, telefono, correo, gerente, equipo_contacto):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_creacion = fecha_creacion
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.gerente = gerente
        self.equipo_contacto = equipo_contacto
        self.proyectos = AVLTree()

    def __str__(self):
        return f"{self.id}, {self.nombre}, {self.descripcion}, {self.fecha_creacion}, {self.direccion}, {self.telefono}, {self.correo}, {self.gerente}, {self.equipo_contacto}, {self.proyectos}"

class GestionEmpresas:
    def __init__(self, archivo_csv):
        self.archivo_csv = archivo_csv
        self.empresas = self.cargar_empresas()

    def cargar_empresas(self):
        empresas = []
        try:
            with open(self.archivo_csv, mode='r', newline='') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    empresa = Empresa(*row[:9])
                    proyectos = row[9].split(';') if row[9] else []
                    for proyecto_str in proyectos:
                        datos_proyecto = proyecto_str.split(',')
                        if len(datos_proyecto) == 9:
                            proyecto = Proyecto(*datos_proyecto)
                            empresa.proyectos.insertar(proyecto)
                    empresas.append(empresa)
        except FileNotFoundError:
            pass
        return empresas

    def guardar_empresas(self):
        with open(self.archivo_csv, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['id', 'nombre', 'descripcion', 'fecha_creacion', 'direccion', 'telefono', 'correo', 'gerente', 'equipo_contacto', 'proyectos'])
            for empresa in self.empresas:
                proyectos = ';'.join([f"{p.id},{p.nombre},{p.descripcion},{p.fecha_inicio},{p.fecha_vencimiento},{p.estado_actual},{p.empresa},{p.gerente},{p.equipo}" for p in empresa.proyectos.recorrido_in_orden(empresa.proyectos.raiz)])
                writer.writerow([empresa.id, empresa.nombre, empresa.descripcion, empresa.fecha_creacion, empresa.direccion, empresa.telefono, empresa.correo, empresa.gerente, empresa.equipo_contacto, proyectos])

    def crear_empresa(self, empresa):
        self.empresas.append(empresa)
        self.guardar_empresas()

    def modificar_empresa(self, id, nuevos_datos):
        for empresa in self.empresas:
            if empresa.id == id:
                empresa.nombre = nuevos_datos.get('nombre', empresa.nombre)
                empresa.descripcion = nuevos_datos.get('descripcion', empresa.descripcion)
                empresa.fecha_creacion = nuevos_datos.get('fecha_creacion', empresa.fecha_creacion)
                empresa.direccion = nuevos_datos.get('direccion', empresa.direccion)
                empresa.telefono = nuevos_datos.get('telefono', empresa.telefono)
                empresa.correo = nuevos_datos.get('correo', empresa.correo)
                empresa.gerente = nuevos_datos.get('gerente', empresa.gerente)
                empresa.equipo_contacto = nuevos_datos.get('equipo_contacto', empresa.equipo_contacto)
                self.guardar_empresas()
                return empresa
        return None

    def consultar_empresa(self, id):
        for empresa in self.empresas:
            if empresa.id == id:
                return empresa
        return None

    def eliminar_empresa(self, id):
        self.empresas = [empresa for empresa in self.empresas if empresa.id != id]
        self.guardar_empresas()
