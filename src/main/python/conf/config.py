import os
import yaml

from algorithms.i_image_algorithm import IImageAlgorithm
from algorithms.image_hashing_algorithm import ImageHashAlgorithm
from algorithms.ssim_algorithm import ImageSSIMAlgorithm


class ImageSimilarityConfig:
    def __init__(self):
        self.__env = os.environ.get("ENV", "Development")
        self.__file_name = "config.{env}.yaml".format(env=self.__env)
        self.__dataMap = {}
        self.__load()

    def __load(self):
        current_dir = os.path.dirname(__file__)
        file_path = os.path.join(current_dir, self.__file_name)
        self.__dataMap = yaml.safe_load(open(file_path))

    def log_level(self) -> str:
        return self.__dataMap.get("log_level", "debug")

    def consumers_count(self) -> int:
        return self.__dataMap.get("consumers_count", 0)

    def get_algorithm(self) -> IImageAlgorithm:
        algorithm_name = self.__dataMap.get("image_similarity_algorithm", "SSIM")
        if algorithm_name == "HASH":
            return ImageHashAlgorithm()
        elif algorithm_name == "SSIM":
            return ImageSSIMAlgorithm()
        else:
            raise Exception("Unknown image similarity algorithm: {} found !!".format(algorithm_name))
