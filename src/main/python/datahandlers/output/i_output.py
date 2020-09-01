from abc import ABC, abstractmethod

from datahandlers.output.similarity_output import SimilarityOutput


class IOutput(ABC):
    """Interface to define output streams"""


    @abstractmethod
    def write(self, output: SimilarityOutput) -> bool:
        """
        Write given similarity output.
        :return: True if written successfully, False otherwise
        """

    @abstractmethod
    def __enter__(self):
        """
        Enter into context used in with-statements
        :return:
        """

    @abstractmethod
    def __exit__(self, exc_type, exc_value, exc_traceback):
        """
        Leave the context used in with-statements
        :param exc_type: exception type
        :param exc_value: exception value
        :param exc_traceback: stack trace
        :return:
        """
