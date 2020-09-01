from datahandlers.input.i_input import IInput
from datahandlers.input.similarity_input import SimilarityInput

from utils.logger import Logger
logger = Logger.get_logger(__file__)


class CMDReader(IInput):
    """Read from Command-line input arguments"""

    def __init__(self, first_image, second_image):
        self.__first_image = first_image
        self.__second_image = second_image
        self.__count = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def __iter__(self):
        return self

    def __next__(self) -> SimilarityInput:
        while self.__count >= 1:
            raise StopIteration
        self.__count += 1
        return SimilarityInput(self.__first_image, self.__second_image)

