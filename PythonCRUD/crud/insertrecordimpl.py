import logging.config

import PythonCRUD.crud.commons
import PythonCRUD.crud.insertrecords
import PythonCRUD.crud.utils.databaseutils
import PythonCRUD.crud.utils.query


class InsertRecordsImpl(PythonCRUD.crud.insertrecords.InsertRecords, PythonCRUD.crud.commons.Commons):
    """
    This class implements the two interfaces
    Scope of this class is insert the records in to database table
    """

    def __init__(self):
        InsertRecordsImpl.log = logging.getLogger("InsertRecordsImpl")
        # self.query_conf = configparser.ConfigParser()
        self.conn_utils = PythonCRUD.crud.utils.databaseutils.DatabaseUtils()
        self.conn = self.conn_utils.get_data_source_connection()

    def insert_record(self):
        """
        This method insert the value in database
        :return: None
        """
        try:
            query = PythonCRUD.crud.utils.query.INSERT_QUERY
            print(query)
            cursor = self.conn.cursor()
            cursor.execute(query, (int(104), str('sivaraman'), str('s'), int(), str('chn')))
            self.conn.commit()
            InsertRecordsImpl.log.info("insert successfully...")
        except Exception as ex:
            InsertRecordsImpl.log.exception("Exception occurred while insert record : %s", ex)
        finally:
            self.finalized()

    def finalized(self):
        """
        This is metod close the resources
        :return: None
        """
        self.conn_utils.close_database_connection(self.conn)
