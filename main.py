import pymysql
from config import host, user, password, db_name

try:
    connection = pymysql.connect(
        host = host,
        port = 3306,
        user = user,
        password = password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print("Успешно подключен!")
    print("#" * 20)
    try:
        with connection.cursor() as cursor:
            create_table_class = "CREATE TABLE `class` (id_class int AUTO_INCREMENT primary key," \
                                 "name varchar(32));"
            cursor.execute(create_table_class)
            create_table_staff = "CREATE TABLE `staff` (id_staff int AUTO_INCREMENT primary key," \
                                 "phone int, post varchar(32)," \
                                 "surname varchar(32)," \
                                 "name varchar(32));"
            cursor.execute(create_table_staff)
            create_table_rooms = "CREATE TABLE `rooms` (id_rooms int AUTO_INCREMENT primary key," \
                                 "status varchar(32)," \
                                 "class_id int," \
                                 "price int," \
                                 "number_of_places int," \
                                 "FOREIGN KEY (class_id) REFERENCES `class` (id_class));"
            cursor.execute(create_table_rooms)
            create_table_room_service = "CREATE TABLE `room_service` (id_room_service int AUTO_INCREMENT primary key," \
                                        "staff_id int," \
                                        "room_id int," \
                                        "FOREIGN KEY (staff_id) REFERENCES `staff` (id_staff)," \
                                        "FOREIGN KEY (room_id) REFERENCES `rooms` (id_rooms));"
            cursor.execute(create_table_room_service)
            create_table_guests = "CREATE TABLE `guests` (id_guests int AUTO_INCREMENT primary key," \
                                  "passport int unique," \
                                  "check_in date," \
                                  "check_out date," \
                                  "surname varchar(32)," \
                                  "name varchar(32)," \
                                  "room_id int," \
                                  "FOREIGN KEY (room_id) REFERENCES `rooms` (id_rooms));"
            cursor.execute(create_table_guests)
            print("Успешно выполнено!")
    finally:
        connection.close()
except Exception as ex:
    print("В соединении отказано!")
    print(ex)