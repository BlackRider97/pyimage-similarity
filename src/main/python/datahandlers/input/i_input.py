from abc import ABC, abstractmethod

from datahandlers.input.similarity_input import SimilarityInput


class IInput(ABC):
    """Interface to define input streams"""


    @abstractmethod
    def __iter__(self):
        """
        Next iteration element
        :return: Iterator
        """

    @abstractmethod
    def __next__(self) -> SimilarityInput:
        """
        Next iteration element
        :return: next element
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
