import time

from algorithms.i_image_algorithm import IImageAlgorithm
from datahandlers.input.similarity_input import SimilarityInput
from datahandlers.output.similarity_output import SimilarityOutput
from processor.task import Task


class ImageSimilarityTask(Task):

    def __init__(self, algorithm: IImageAlgorithm, similarity_input: SimilarityInput):
        super().__init__()
        self.__algorithm = algorithm
        self.__similarity_input = similarity_input

    def process(self) -> SimilarityOutput:
        # Start the stopwatch / counter
        start = time.perf_counter()
        score = self.__algorithm.calculate_similarity(
            self.__similarity_input.first_image,
            self.__similarity_input.second_image,
        )
        # Stop the stopwatch / counter
        end = time.perf_counter()
        processing_time = end - start
        return SimilarityOutput(
            self.__similarity_input.first_image,
            self.__similarity_input.second_image,
            score,
            processing_time
        )


    def __str__(self):
        return 'ImageSimilarityTask(Algorithm: %s, input: %s)' % (self.__algorithm.name(), self.__similarity_input)
