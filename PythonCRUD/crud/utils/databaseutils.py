import logging.config
import configparser
import pymysql


class DatabaseUtils:
    """
    This class will maintain the database connections
    """

    def __init__(self):
        DatabaseUtils.log = logging.getLogger("DatabaseUtils")
        self.load_properties()

    @classmethod
    def load_properties(cls):
        """
        This method load the dbconfig.ini file and load the DB properties
        :return: None
        """
        try:
            config = configparser.ConfigParser()
            config.read('../docs/dbconfig.ini')
            cls.host_name = config['DATABASE']['host']
            cls.port_no = config['DATABASE']['port']
            cls.user_name = config['DATABASE']['user']
            cls.db_name = config['DATABASE']['db']
            cls.password = config['DATABASE']['password']
            DatabaseUtils.log.info("Properties loaded successfully...")
        except KeyError as ex:
            DatabaseUtils.log.exception("Exception occurred : %s", ex)

    @classmethod
    def get_data_source_connection(cls):
        """
        This is create the database connection
        :return: conn - database connection
        """
        conn = None
        try:
            conn = pymysql.connect(host=cls.host_name, database=cls.db_name, user=cls.user_name,
                                   password=cls.password)
        except Exception as ex:
            DatabaseUtils.log.exception("Exception occurred while connect to database : %s", ex)

        return conn

    @classmethod
    def close_database_connection(cls, conn):
        """
        This is close the database connection
        :param conn: connection which we have to close
        :return: None
        """
        try:
            if conn:
                conn.close()
            elif not conn:
                DatabaseUtils.log.info("Connection already closed")
            else:
                DatabaseUtils.log.error(conn)
        except Exception as ex:
            DatabaseUtils.log.exception("Exception occurred while close datasource connection : %s", ex)
