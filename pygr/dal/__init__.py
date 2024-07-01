from pygr.common import POSTGRES_CONN_TYPE
from .postgres import create_postgres_conn


class DataBase:
    def __init__(self, db_params):
        self.conn = self.init_conn(db_params)
        self.initialize_db(db_params)

    def initialize_db(self, db_params):
        self._do_initialize_db(db_params)

    def init_conn(self, db_params):
        return self._do_initialize_conn(db_params)

    # ------------------------ Child class methods ------------------------

    def _do_initialize_db(self, db_params):
        raise Exception("Not implemented.")

    def _do_initialize_conn(self, db_params):
        raise Exception("Not implemented.")


class GrabbedDataDB(DataBase):
    def __init__(self, db_params):
        super().__init__(db_params)

    def _do_initialize_conn(self, db_params):
        try:
            conn_type = db_params.get("type")
            if not conn_type:
                raise Exception("No GrabberDataDB type found.")

            if conn_type == POSTGRES_CONN_TYPE:
                return create_postgres_conn(db_params)
        except Exception as e:
            raise e

    def _do_initialize_db(self, db_params):
        conn_type = db_params.get("type")
        


