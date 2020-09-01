import os
import imghdr

from datahandlers.input.similarity_input import SimilarityInput
from utils.logger import Logger

logger = Logger.get_logger(__file__)


class SimilarityOutput(SimilarityInput):

    def __init__(self, first_image_file_path, second_image_file_path, similarity_score, time_taken_in_seconds):
        super().__init__(first_image_file_path, second_image_file_path)
        self.__similarity_score = similarity_score
        self.__time_taken_in_seconds = time_taken_in_seconds


    @property
    def similarity_score(self):
        return self.__similarity_score


    @property
    def time_taken_in_seconds(self):
        return self.__time_taken_in_seconds


    def __str__(self):
        return "{first}, {second}, {score} , {time} secs".format(
            first=self.first_image,
            second=self.second_image,
            score=self.similarity_score,
            time=float("{:.4f}".format(self.time_taken_in_seconds))
        )

    def is_valid(self):
        # upper bound on time also can be applied
        return 0 <= self.score <= 1
