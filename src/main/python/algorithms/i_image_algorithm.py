from abc import ABC, abstractmethod


class IImageAlgorithm(ABC):

    @abstractmethod
    def name(self) -> str:
        """
        Unique name of algorithm
        :return:
        """

    @abstractmethod
    def calculate_similarity(self, first_image: str, second_image: str) -> float:
        """
        Find visualization similarity between two images.
        Efficiency of algorithm is subjective.
        One algorithm may perform better for few cases while other algorithm may perform better in different cases.

        * Note: Relative scoring is up to the implementor but it should it provide consistent result for same inputs.
        :param first_image:
        :param second_image:
        :return: 0 if both images are identical, 1 if both are completely different.
                Any floating number between (0, 1) presents relative score of how much similarity exists between images.
        """
