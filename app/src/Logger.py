import logging
from utils import get_datetime


class Logger:
    """
    A class to represent a log service.

    Attributes
    ----------
    logger: logging
        logger from python's logging lib

    Methods
    -------
    log_formatter(): dict
        formats and writes the step log based on levels of severity and time of input in log_file.
    info(): void
        logs messages in an info level.
    warn(): void
        logs messages in a warning level.
    error(): void
        logs messages in an error level.
    """
    def __init__(self):
        # Sets logger and handler for class
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        logging.basicConfig(format='%(message)s')

    def log_formatter(self, level, message, stack_trace=None):
        """
        Formats and writes the step log based on levels of severity and time of input in log_file.

        Parameters
        ----------
            level : str
                level of a log input (INFO, WARN or ERROR).
            message: str
                the message to be inserted in a log input.
            stack_trace: str
                a traceback of the exception raised at ERROR level.
        Returns
        -------
            formatted_log: str
                formatted log of a log input.
        """
        if level == "ERROR":
            formatted_log = f"{get_datetime()} - [{level}]: {message}. Traceback: {stack_trace}"
        else:
            formatted_log = f"{get_datetime()} - [{level}]: {message}"

        # self.log_file.write(f"{formatted_log}\n")
        return formatted_log

    def info(self, message):
        """
        Insert log input of INFO level of severity.

        Parameters
        ----------
            message: str
                the message to be inserted in a log input.

        Returns
        -------
            None.
        """
        self.logger.info(self.log_formatter(level='INFO', message=message))

    def warn(self, message):
        """
        Insert log input of WARN level of severity.

        Parameters
        ----------
            message: str
                the message to be inserted in a log input.

        Returns
        -------
            None.
        """
        self.logger.warning(self.log_formatter(level='WARN', message=message))

    def error(self, message, stack_trace=None):
        """
        Insert log input of ERROR level of severity.

        Parameters
        ----------
            message: str
                the message to be inserted in a log input.
            stack_trace: str
                a traceback of the exception raised at this level.

        Returns
        -------
            None.
        """
        self.logger.error(self.log_formatter(level='ERROR', message=message, stack_trace=stack_trace))
