# coding=utf-8
# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Press Ctrl+F8 to toggle the breakpoint.

import pandas as pd
import psycopg2
class datos():
    def Almacenar(nombreRecibido,apellidoRecibido,edadRecibido):


        try:
            credenciales = {
                "dbname": "test",
                "user": "postgres",
                "password": "********",
                "host": "localhost",
                "port": 5432
            }
            conexion = psycopg2.connect(**credenciales)

            #creando tabla
            cursor = conexion.cursor()
            consulta = "CREATE TABLE IF NOT EXISTS persona (ID SERIAL PRIMARY KEY, nombre varchar(50),apellido varchar(50), edad int );"
            cursor.execute(consulta)

            #Llenando información
            with conexion.cursor() as cursor:
                consulta = "INSERT INTO persona(nombre, apellido, edad) VALUES (%s, %s, %s);"
                cursor.execute(consulta, (nombreRecibido, apellidoRecibido, edadRecibido))

            conexion.commit()  # Si no haces commit para surgir efecto en la persistencia

        except psycopg2.Error as e:
            print("Ocurrió un error al insertar: ", e)
        finally:
            conexion.close()

        return 200

    def Leer():
        try:
            credenciales = {
                "dbname": "test",
                "user": "postgres",
                "password": "2022.cuenca",
                "host": "localhost",
                "port": 5432
            }
            conexion = psycopg2.connect(**credenciales)

            # Leyendo datos
            with conexion.cursor() as cursor:
                consulta ="SELECT * from PERSONA"
                cursor.execute(consulta)
                datos =  cursor.fetchall()
            return datos
        except psycopg2.Error as e:
            print("Ocurrió un error al leer los datos: ", e)
        finally:
            conexion.close()
        return 200
