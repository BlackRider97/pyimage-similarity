from enum import Enum
from algorithms.i_image_algorithm import IImageAlgorithm
from PIL import Image
import imagehash


class HashingAlgorithm(Enum):
    AverageHashComputation = 0
    PerceptualHashComputation = 1
    WaveletHashComputation = 2


class ImageHashAlgorithm(IImageAlgorithm):
    """
    Calculate pixel by pixel hash of overall of both the images.
    Take normalized difference between two images.

    Read more about PerceptualHashComputation algorithm here
    http://www.hackerfactor.com/blog/index.php?/archives/432-Looks-Like-It.html
    """


    def __init__(self):
        self.__hashing_algorithm = HashingAlgorithm.PerceptualHashComputation
        self.__hashing_function = self.__get_hashing_function(self.__hashing_algorithm)


    def name(self) -> str:
        return "HASH"


    def calculate_similarity(self, first_image: str, second_image: str) -> float:
        hash1 = self.__hashing_function(Image.open(first_image))
        hash2 = self.__hashing_function(Image.open(second_image))
        # Total compared bits are 8 * 8 = 64. Dividing by 64 to normalize
        normalized_diff = round((hash1 - hash2) / 64, 4)  # rounding-off till 4th decimal place
        similarity = normalized_diff
        return similarity


    @staticmethod
    def __get_hashing_function(hashing_algorithm: HashingAlgorithm):
        if hashing_algorithm == HashingAlgorithm.AverageHashComputation:
            return imagehash.average_hash
        elif hashing_algorithm == HashingAlgorithm.PerceptualHashComputation:
            return imagehash.phash
        elif hashing_algorithm == HashingAlgorithm.WaveletHashComputation:
            return imagehash.whash
        return None
