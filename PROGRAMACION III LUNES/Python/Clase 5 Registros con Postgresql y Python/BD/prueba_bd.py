import psycopg2  # Para conectarnos a PostgreSQL

# Inicializamos la variable conexion como None
conexion = None

try:
    conexion = psycopg2.connect(
        host="127.0.0.1",
        database="test_bd",
        user="postgres",
        password="admin",
        port="5432"
    )

    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "SELECT * FROM persona WHERE id_persona = %s " # Placeholder
            id_persona = input("Digite un número para el id_perosna: ")
            cursor.execute(sentencia, (id_persona,))  # Ejecutamos la sentencia
            registros = cursor.fetchone()  # Recuperamos todos los registros

            # Imprimimos los registros
            print("Registros en la tabla persona:")
            for registro in registros:
                print(registro)

except psycopg2.Error as e:
    print(f"Error al conectar a PostgreSQL: {e}")

finally:
    if conexion is not None:  # Verificamos si la conexión existe
        conexion.close()  # Cerramos la conexión si existe
        print("Conexión cerrada")
