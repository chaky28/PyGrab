import psycopg2


def create_postgres_conn(db_params):
    host = db_params.get("host")
    if not host:
        raise Exception("No host for DB supplied.")

    username = db_params.get("username")
    if not username:
        raise Exception("No username for DB supplied.")

    password = db_params.get("password")
    if not password:
        raise Exception("No password for DB supplied.")

    port = db_params.get("port")
    if not port:
        port = "5432"

    conn = psycopg2.connect(host=host, user=username, password=password, port=port)
    if not conn:
        raise Exception("Unable to connect to DB.")

    return conn
