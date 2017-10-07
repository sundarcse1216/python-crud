import logging.config

import PythonCRUD.crud.commons
import PythonCRUD.crud.updaterecords
import PythonCRUD.crud.utils.databaseutils
import PythonCRUD.crud.utils.query


class UpdateRecordsImpl(PythonCRUD.crud.updaterecords.UpdateRecords, PythonCRUD.crud.commons.Commons):
    """
    This class implements two interfaces
    Scope of this class is update the record(s) in database
    """

    def __init__(self):
        UpdateRecordsImpl.log = logging.getLogger("UpdateRecordsImpl")
        self.conn_util = PythonCRUD.crud.utils.databaseutils.DatabaseUtils()
        self.conn = self.conn_util.get_data_source_connection()
        pass

    def update_records(self, value, cause):
        """
        This method update the record in database
        :param value: value have to update
        :param cause: this is condition
        :return: None
        """
        try:
            query = PythonCRUD.crud.utils.query.UPDATE_QUERY
            cursor = self.conn.cursor()
            cursor.execute(query, (str(value), int(cause)))
            self.conn.commit()
            UpdateRecordsImpl.log.info("Update successfully...")
        except Exception as ex:
            UpdateRecordsImpl.log.exception("Exception occurred while update record(s) : %s", ex)
        finally:
            self.finalized()

    def finalized(self):
        """
        this is close the resources
        :return: None 
        """
        self.conn_util.close_database_connection(self.conn)
