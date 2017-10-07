import logging.config

import PythonCRUD.crud.deleterecords
import PythonCRUD.crud.utils.databaseutils
import PythonCRUD.crud.utils.query


class DeleteRecordsImpl(PythonCRUD.crud.deleterecords.DeleteRecords):
    """
    This class implements the two interfaces
    Scope of this class is delete the records in to database table
    """

    def __init__(self):
        DeleteRecordsImpl.log = logging.getLogger("DeleteRecordsImpl")
        self.conn_utils = PythonCRUD.crud.utils.databaseutils.DatabaseUtils()
        self.conn = self.conn_utils.get_data_source_connection()
        pass

    def delete_records(self, cause):
        """
        This method will delete the record
        :param cause: condition have to delete
        :return: None
        """
        try:
            query = PythonCRUD.crud.utils.query.DELETE_QUERY
            cursor = self.conn.cursor()
            cursor.execute(query, cause)
            self.conn.commit()
            DeleteRecordsImpl.log.info("Deleted successfully...")
        except Exception as ex:
            DeleteRecordsImpl.log.exception("Exception occurred while delete record(s) : %s", ex)
        finally:
            self.finalized()

    def finalized(self):
        """
        This is close the resources         
        :return:
        """
        self.conn_utils.close_database_connection(self.conn)
