# Imports
import mariadb


def connect_db(
        user=None,
        password=None,
        database=None,
        host='localhost',
        port=3306
        ):

    if not user or not password or not database:
        print("Falta algun parametro de conexión")
        quit(1)
    # Connect to MariaDB Platform
    try:
        conn = mariadb.connect(
            user=user,
            password=password,
            host=host,
            port=port,
            database=database
        )
        print("Successfuly database connection!")
        return conn
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        quit(1)


def get_cursor(conn_data):
    # Get Cursor
    cursor = conn_data.cursor()
    return cursor


def query(q_str, *args):
    """
    :param q_str: Query string to specific table
    :param args: Any number of arguments for custom queries
    :return: Array of dict(key: value)
    """
    global cur, db_conn
    try:
        if len(args):
            param = []
            for parametro in args:
                param.append(parametro,)
            cur.execute(q_str, param)
        else:
            cur.execute(q_str)
            db_conn.commit()
        if cur.rowcount > 0:
            resp = []
            rows = cur.fetchall()
            columns = [desc[0] for desc in cur.description]
            for row in rows:
                row = dict(zip(columns, row))
                resp.append(row)
            return resp
    except mariadb.InterfaceError:
        cur.close()
        db_conn.close()
        db_conn = connect_db(user="root", password="121601001", database="adminpatdb", host='127.0.0.1')
        cur = get_cursor(db_conn)


# TODO: definition to load credentials fron .env
db_conn = connect_db(user="root", password="121601001", database="adminpatdb", host='127.0.0.1')
cur = get_cursor(db_conn)
