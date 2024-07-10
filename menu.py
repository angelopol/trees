from empresa import GestionEmpresas, Empresa
from proyecto import Proyecto
from datetime import datetime

def mostrar_menu():
    print("Sistema de Gestión de Empresas y Proyectos")
    print("1. Crear empresa")
    print("2. Modificar empresa")
    print("3. Consultar empresa")
    print("4. Eliminar empresa")
    print("5. Listar empresas")
    print("6. Crear proyecto")
    print("7. Modificar proyecto")
    print("8. Consultar proyecto")
    print("9. Eliminar proyecto")
    print("10.Listar proyectos")
    print("0. Salir")

def solicitar_datos_empresa():
    id = input("ID: ")
    nombre = input("Nombre: ")
    descripcion = input("Descripción: ")
    fecha_creacion = input("Fecha de creación (YYYY-MM-DD): ")
    direccion = input("Dirección: ")
    telefono = input("Teléfono: ")
    correo = input("Correo: ")
    gerente = input("Gerente: ")
    equipo_contacto = input("Equipo de contacto: ")
    return Empresa(id, nombre, descripcion, fecha_creacion, direccion, telefono, correo, gerente, equipo_contacto)

def solicitar_datos_proyecto():
    id = input("ID: ")
    nombre = input("Nombre: ")
    descripcion = input("Descripción: ")
    fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ")
    fecha_vencimiento = input("Fecha de vencimiento (YYYY-MM-DD): ")
    estado_actual = input("Estado actual: ")
    empresa = input("Empresa: ")
    gerente = input("Gerente: ")
    equipo = input("Equipo: ")
    return Proyecto(id, nombre, descripcion, fecha_inicio, fecha_vencimiento, estado_actual, empresa, gerente, equipo)

def main():
    gestion_empresas = GestionEmpresas('empresas.csv')

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            empresa = solicitar_datos_empresa()
            gestion_empresas.crear_empresa(empresa)
        elif opcion == '2':
            id = input("Ingrese el ID de la empresa a modificar: ")
            nuevos_datos = {}
            print("Deje en blanco los campos que no desee modificar.")
            nuevos_datos['nombre'] = input("Nuevo nombre: ")
            nuevos_datos['descripcion'] = input("Nueva descripción: ")
            nuevos_datos['fecha_creacion'] = input("Nueva fecha de creación (YYYY-MM-DD): ")
            nuevos_datos['direccion'] = input("Nueva dirección: ")
            nuevos_datos['telefono'] = input("Nuevo teléfono: ")
            nuevos_datos['correo'] = input("Nuevo correo: ")
            nuevos_datos['gerente'] = input("Nuevo gerente: ")
            nuevos_datos['equipo_contacto'] = input("Nuevo equipo de contacto: ")
            empresa = gestion_empresas.modificar_empresa(id, {k: v for k, v in nuevos_datos.items() if v})
            if empresa:
                print("Empresa modificada con éxito.")
            else:
                print("No se encontró la empresa.")
        elif opcion == '3':
            id = input("Ingrese el ID de la empresa a consultar: ")
            empresa = gestion_empresas.consultar_empresa(id)
            if empresa:
                print(empresa)
            else:
                print("No se encontró la empresa.")
        elif opcion == '4':
            id = input("Ingrese el ID de la empresa a eliminar: ")
            gestion_empresas.eliminar_empresa(id)
            print("Empresa eliminada con éxito.")
        elif opcion == '5':
            for empresa in gestion_empresas.empresas:
                print(empresa)
        elif opcion == '6':
            id_empresa = input("Ingrese el ID de la empresa para agregar un proyecto: ")
            empresa = gestion_empresas.consultar_empresa(id_empresa)
            if empresa:
                proyecto = solicitar_datos_proyecto()
                empresa.proyectos.insertar(proyecto)
                gestion_empresas.guardar_empresas()
                print("Proyecto creado con éxito.")
            else:
                print("No se encontró la empresa.")
        elif opcion == '7':
            id_empresa = input("Ingrese el ID de la empresa para modificar un proyecto: ")
            empresa = gestion_empresas.consultar_empresa(id_empresa)
            if empresa:
                id_proyecto = input("Ingrese el ID del proyecto a modificar: ")
                proyecto = empresa.proyectos.consultar_proyecto(id_proyecto)
                if proyecto:
                    nuevos_datos = {}
                    print("Deje en blanco los campos que no desee modificar.")
                    nuevos_datos['nombre'] = input("Nuevo nombre: ")
                    nuevos_datos['descripcion'] = input("Nueva descripción: ")
                    nuevos_datos['fecha_inicio'] = input("Nueva fecha de inicio (YYYY-MM-DD): ")
                    nuevos_datos['fecha_vencimiento'] = input("Nueva fecha de vencimiento (YYYY-MM-DD): ")
                    nuevos_datos['estado_actual'] = input("Nuevo estado actual: ")
                    nuevos_datos['empresa'] = input("Nueva empresa: ")
                    nuevos_datos['gerente'] = input("Nuevo gerente: ")
                    nuevos_datos['equipo'] = input("Nuevo equipo: ")
                    proyecto.nombre = nuevos_datos.get('nombre', proyecto.nombre)
                    proyecto.descripcion = nuevos_datos.get('descripcion', proyecto.descripcion)
                    proyecto.fecha_inicio = nuevos_datos.get('fecha_inicio', proyecto.fecha_inicio)
                    proyecto.fecha_vencimiento = nuevos_datos.get('fecha_vencimiento', proyecto.fecha_vencimiento)
                    proyecto.estado_actual = nuevos_datos.get('estado_actual', proyecto.estado_actual)
                    proyecto.empresa = nuevos_datos.get('empresa', proyecto.empresa)
                    proyecto.gerente = nuevos_datos.get('gerente', proyecto.gerente)
                    proyecto.equipo = nuevos_datos.get('equipo', proyecto.equipo)
                    gestion_empresas.guardar_empresas()
                    print("Proyecto modificado con éxito.")
                else:
                    print("No se encontró el proyecto.")
            else:
                print("No se encontró la empresa.")
        elif opcion == '8':
            id_empresa = input("Ingrese el ID de la empresa para consultar un proyecto: ")
            empresa = gestion_empresas.consultar_empresa(id_empresa)
            if empresa:
                id_proyecto = input("Ingrese el ID del proyecto a consultar: ")
                proyecto = empresa.proyectos.consultar_proyecto(id_proyecto)
                if proyecto:
                    print(proyecto)
                else:
                    print("No se encontró el proyecto.")
            else:
                print("No se encontró la empresa.")
        elif opcion == '9':
            id_empresa = input("Ingrese el ID de la empresa para eliminar un proyecto: ")
            empresa = gestion_empresas.consultar_empresa(id_empresa)
            if empresa:
                id_proyecto = input("Ingrese el ID del proyecto a eliminar: ")
                proyecto = empresa.proyectos.consultar_proyecto(id_proyecto)
                if proyecto:
                    empresa.proyectos.eliminar(proyecto)
                    gestion_empresas.guardar_empresas()
                    print("Proyecto eliminado con éxito.")
                else:
                    print("No se encontró el proyecto.")
            else:
                print("No se encontró la empresa.")
        elif opcion == '10':
            id_empresa = input("Ingrese el ID de la empresa para listar sus proyectos: ")
            empresa = gestion_empresas.consultar_empresa(id_empresa)
            if empresa:
                for proyecto in empresa.proyectos.recorrido_in_orden(empresa.proyectos.raiz):
                    print(proyecto)
            else:
                print("No se encontró la empresa.")
        elif opcion == '0':
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    main()
