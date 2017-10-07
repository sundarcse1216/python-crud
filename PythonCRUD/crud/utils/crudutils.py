import logging.config


class CRUTUtils:
    def __init__(self):
        pass

    @staticmethod
    def display_record(results_props):
        """
        This method will iterate the results and display the results in console
        :param results_props: result properties, which is have to iterate
        :return: None
        """
        logger = logging.getLogger("CRUTUtils")
        if results_props:
            for result_props in results_props:
                logger.info(result_props.id)
                logger.info(result_props.emp_id)
                logger.info(result_props.f_name)
                logger.info(result_props.l_name)
                logger.info(result_props.salary)
                logger.info(result_props.address)
        pass
