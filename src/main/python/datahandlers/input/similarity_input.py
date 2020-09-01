import os
import imghdr

from utils.logger import Logger

logger = Logger.get_logger(__file__)


class SimilarityInput:

    def __init__(self, first_image_file_path, second_image_file_path):
        self.__first_image_file_path = first_image_file_path
        self.__second_image_file_path = second_image_file_path


    @property
    def first_image(self):
        return self.__first_image_file_path


    @property
    def second_image(self):
        return self.__second_image_file_path


    @staticmethod
    def __is_image_file(file_path):
        if not file_path:
            return False
        if not os.path.isfile(file_path):
            return False
        file_format = imghdr.what(file_path)
        if not file_format:
            logger.warning("File format is unknown for file: %s", file_path)
            return False
        return True


    def __str__(self):
        return "{first}, {second}".format(first=self.first_image, second=self.second_image)

    def is_valid(self):
        return SimilarityInput.__is_image_file(self.first_image) and SimilarityInput.__is_image_file(self.second_image)
