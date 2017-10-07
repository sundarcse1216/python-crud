import logging.config

import PythonCRUD.crud.commons
import PythonCRUD.crud.props.retrieveprops
import PythonCRUD.crud.retrieverecords
import PythonCRUD.crud.utils.databaseutils
import PythonCRUD.crud.utils.query


class RetrieveRecordsImpl(PythonCRUD.crud.retrieverecords.RetrieveRecords, PythonCRUD.crud.commons.Commons):
    """
    This class retrieve the record(s) from database table and set those vales to properties
    """

    def __init__(self):
        RetrieveRecordsImpl.log = logging.getLogger("RetrieveRecordsImpl")
        self.db_utils = PythonCRUD.crud.utils.databaseutils.DatabaseUtils()
        self.conn = self.db_utils.get_data_source_connection()

    def get_all_records(self):
        """
        This method will fetch all data from database
        :return: None
        """
        self.props_list = []
        try:
            query = PythonCRUD.crud.utils.query.SELECT_QUERY
            cursor = self.conn.cursor()
            cursor.execute(query)
            result_list = cursor.fetchall()
            self.props_list = self.iterate_result_list(result_list)
        except Exception as ex:
            RetrieveRecordsImpl.log.exception("Exception occurred while retrieve records : %s", ex)

        finally:
            self.finalized()
        return self.props_list

    def finalized(self):
        """
        This is method will close the resources
        :return: None
        """
        self.db_utils.close_database_connection(self.conn)

    @classmethod
    def iterate_result_list(cls, result_list):
        """
        This method iterate the raw result(s) and set into properties
        :param result_list: raw result(s) which come from database
        :return: props_list - Properties list
        """
        cls.props_list = []
        if result_list:
            for results in result_list:
                cls.retrieve_props = PythonCRUD.crud.props.retrieveprops.RedriveProps()
                if results[0]:
                    cls.retrieve_props.id = results[0]
                else:
                    cls.retrieve_props.id = 'N/A'

                if results[1]:
                    cls.retrieve_props.emp_id = results[1]
                else:
                    cls.retrieve_props.emp_id = 'N/A'

                if results[2]:
                    cls.retrieve_props.f_name = results[3]
                else:
                    cls.retrieve_props.f_name = 'N/A'

                if results[3]:
                    cls.retrieve_props.l_name = results[3]
                else:
                    cls.retrieve_props.l_name = 'N/A'

                if results[4]:
                    cls.retrieve_props.salary = results[4]
                else:
                    cls.retrieve_props.salary = 'N/A'

                if results[5]:
                    cls.retrieve_props.address = results[5]
                else:
                    cls.retrieve_props.address = 'N/A'

                cls.props_list.append(cls.retrieve_props)
        return cls.props_list
