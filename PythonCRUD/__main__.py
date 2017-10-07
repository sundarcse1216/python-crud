import logging.config
import sys

from crud.insertrecordimpl import InsertRecordsImpl
from crud.retrieverecordsimpl import RetrieveRecordsImpl
from crud.updaterecordsimpl import UpdateRecordsImpl

from PythonCRUD.crud.deleterecordsimpl import DeleteRecordsImpl
from crud.utils.crudutils import CRUTUtils


class CRUDStarter:
    """
    This is the main class of this project
    scope of this project is get the input from user and perform the CRUD operations
    The command line input of this project is minimum one and maximum four is required
    more than four less than one i wont execute
    """
    logger = None
    LOGGER_PATH = "../docs/logging.conf"

    def __init__(self):
        logging.config.fileConfig(CRUDStarter.LOGGER_PATH)
        CRUDStarter.logger = logging.getLogger("CRUDTest")
        CRUDStarter.logger.info("Logger configured successfully...")
        pass

    @staticmethod
    def validate_command_line_input(args):
        """
        This method validate the command line input which given by use
        If command line input is valid, it will invoke the load_operation() method
        :param args: command line input(s)
        :return: None
        """
        valid = False
        if 0 < len(args) <= 4:
            valid = True
            for arg in args:
                if int(arg) > 4:
                    valid = False
                    break
                else:
                    pass
            if valid:
                CRUDStarter.load_operations(args)
                pass
            else:
                CRUDStarter.logger.info("Argument maximum acceptable value is 4")
        else:
            CRUDStarter.logger.info("at least One at most Four argument(s) required")

    @staticmethod
    def load_operations(args):
        """
        This method iterate the input and call tha appropriate operation
        :param args: command line input(s)
        :return: None
        """
        for arg in args:
            if int(arg) == 1:
                insert = InsertRecordsImpl()
                insert.insert_record()
            elif int(arg) == 2:
                get = RetrieveRecordsImpl()
                lists = get.get_all_records()
                CRUTUtils.display_record(lists)
            elif int(arg) == 3:
                try:
                    value = str(raw_input("Enter the Address : "))
                    CRUDStarter.logger.info(value)
                except NameError as ex:
                    CRUDStarter.logger.info("Please enter String only")
                try:
                    cause = input("Enter the ID, you have to update above address : ")
                    update = UpdateRecordsImpl()
                    update.update_records(value, cause)
                except NameError as ex:
                    CRUDStarter.logger.info("Please enter Number only")
            elif int(arg) == 4:
                try:
                    emp_id = input("Enter employee ID you have to delete : ")
                    delete = DeleteRecordsImpl()
                    delete.delete_records(emp_id)
                except NameError as ex:
                    CRUDStarter.logger.info("Please enter Number only")
            else:
                pass


if __name__ == "__main__":
    CRUDStarter()
    CRUDStarter.validate_command_line_input(sys.argv[1:])
