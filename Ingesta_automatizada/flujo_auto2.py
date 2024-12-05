import time
import pyodbc
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import pandas as pd
import os

# Definir la clase que manejará los eventos de archivo
class FileHandler(FileSystemEventHandler):
    def __init__(self, db_connection, folder_to_watch):
        self.db_connection = db_connection
        self.folder_to_watch = folder_to_watch

    def on_created(self, event):
        # Verificar si el evento corresponde a un archivo (y no a una carpeta)
        if event.is_directory:
            return

        # Obtener el nombre del archivo y la ruta completa
        file_path = event.src_path
        print(f"Nuevo archivo detectado: {file_path}")

        # Solo procesar los archivos de tipo CSV (puedes modificar este filtro si usas otro formato)
        if file_path.endswith(".csv"):
            self.process_file(file_path)

    def process_file(self, file_path):
        # Leer el archivo CSV usando pandas
        df = pd.read_csv(file_path)

        # Obtener el nombre del archivo sin la extensión para determinar la tabla
        file_name = os.path.basename(file_path)
        table_name = file_name.split('.')[0].lower()  # Asumimos que el nombre del archivo es el de la tabla

        # Determinar qué tabla usar según el nombre del archivo
        if table_name == 'aircrafts':
            self.insert_into_aircrafts(df)
        elif table_name == 'airports':
            self.insert_into_airports(df)
        elif table_name == 'flights':
            self.insert_into_flights(df)
        elif table_name == 'boarding_passes':
            self.insert_into_boarding_passes(df)
        elif table_name == 'booking':
            self.insert_into_booking(df)
        elif table_name == 'seats':
            self.insert_into_seats(df)
        elif table_name == 'tickets':
            self.insert_into_tickets(df)
        elif table_name == 'ticket_flights':
            self.insert_into_ticket_flights(df)
        else:
            print(f"No se ha definido una tabla para el archivo: {file_name}")
            return

        # Eliminar el archivo después de procesarlo
        time.sleep(1)
        os.remove(file_path)
        print(f"Archivo procesado y eliminado: {file_path}")

    def insert_into_aircrafts(self, df):
        cursor = self.db_connection.cursor()
        for _, row in df.iterrows():
            cursor.execute("""
                INSERT INTO dbo.aircrafts_data (aircraft_code, model, range)
                VALUES (?, ?, ?)
            """, (row['aircraft_code'], row['model'], row['range']))
        self.db_connection.commit()

    def insert_into_airports(self, df):
        cursor = self.db_connection.cursor()
        for _, row in df.iterrows():
            cursor.execute("""
                INSERT INTO dbo.airports_data (airport_code, airport_name, city,coordinates,timezone)
                VALUES (?, ?,?,?,?)
            """, (row['airport_code'], row['airport_name'], row['city'],row['coordinates'],row['timezone']))
        self.db_connection.commit()

    def insert_into_flights(self, df):
        cursor = self.db_connection.cursor()
        for _, row in df.iterrows():
            cursor.execute("""
                INSERT INTO dbo.flights (flight_id, flight_no,scheduled_departure,scheduled_arrival, departure_airport,arrival_airport,status,aircraft_code,actual_departure,actual_arrival)
                VALUES (?, ?, ?, ?,?, ?, ?, ?,?, ?)
            """, (row['flight_id'], row['flight_no'], row['scheduled_departure'], row['scheduled_arrival'],row['departure_airport'],row['arrival_airport'],row['status'],row['aircraft_code'],row['actual_departure'],row['actual_arrival']))
        self.db_connection.commit()

    def insert_into_boarding_passes(self, df):
        cursor = self.db_connection.cursor()
        for _, row in df.iterrows():
            cursor.execute("""
                INSERT INTO dbo.boarding_passes (ticket_no,flight_id,boarding_no,seat_no)
                VALUES (?, ?, ?, ?)
            """, (row['ticket_no'], row['flight_id'], row['boarding_no'], row['seat_no']))
        self.db_connection.commit()

    def insert_into_booking(self, df):
        cursor = self.db_connection.cursor()
        for _, row in df.iterrows():
            cursor.execute("""
                INSERT INTO dbo.bookings (book_ref,book_date,total_amount)
                VALUES (?, ?, ?)
            """, (row['book_ref'], row['book_date'], row['total_amount']))
        self.db_connection.commit()

    def insert_into_seats(self, df):
        cursor = self.db_connection.cursor()
        for _, row in df.iterrows():
            cursor.execute("""
                INSERT INTO dbo.seats (aircraft_code,seat_no,fare_conditions)
                VALUES (?, ?, ?)
            """, (row['aircraft_code'], row['seat_no'], row['fare_conditions']))
        self.db_connection.commit()

    def insert_into_tickets(self, df):
        cursor = self.db_connection.cursor()
        for _, row in df.iterrows():
            cursor.execute("""
                INSERT INTO dbo.tickets (ticket_no,book_ref,passenger_id)
                VALUES (?, ?, ?)
            """, (row['ticket_no'], row['book_ref'], row['passenger_id']))
        self.db_connection.commit()

    def insert_into_ticket_flights(self, df):
        cursor = self.db_connection.cursor()
        for _, row in df.iterrows():
            cursor.execute("""
                INSERT INTO dbo.ticket_flights (ticket_no,flight_id,fare_conditions,amount)
                VALUES (?, ?, ?,?)
            """, (row['ticket_no'], row['flight_id'], row['fare_conditions'],row['amount']))
        self.db_connection.commit()


# Función principal para iniciar la observación
def start_watching(directory_to_watch, db_connection_string):
    # Conectar a la base de datos SQL Server usando pyodbc
    conn = pyodbc.connect(db_connection_string)
    print(f"Conectado a la base de datos SQL Server")

    # Crear el handler y observer
    event_handler = FileHandler(db_connection=conn, folder_to_watch=directory_to_watch)
    observer = Observer()
    observer.schedule(event_handler, directory_to_watch, recursive=False)
    
    # Iniciar la observación
    observer.start()
    print(f"Observando la carpeta: {directory_to_watch}")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    folder_to_watch = "C:\\Users\\Invite\\Documents\\datos_agregar_test\\"  # Cambia la ruta a la carpeta que quieres monitorear
    # Cadena de conexión a SQL Server (ajústala a tu entorno)
    db_connection_string = (
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server=DESKTOP-5J022F4;"
        "Database=test;"
        "Trusted_Connection=yes;"
    )
    start_watching(folder_to_watch, db_connection_string)