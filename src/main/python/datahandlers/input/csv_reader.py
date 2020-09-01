import csv
import os

from datahandlers.input.i_input import IInput
from datahandlers.input.similarity_input import SimilarityInput

from utils.logger import Logger
logger = Logger.get_logger(__file__)


class CSVReader(IInput):
    """Read from given CSV file"""

    def __init__(self, csv_file_path):
        self.__csv_file_path = csv_file_path
        if not self.__csv_file_path or not os.path.isfile(self.__csv_file_path):
            raise Exception("Input CSV file not found")
        self.__file = None
        self.__csv_reader = None
        self.__input_csv_dir_path = os.path.dirname(os.path.realpath(self.__csv_file_path))

    def __enter__(self):
        self.__file = open(self.__csv_file_path, 'r')
        self.__csv_reader = csv.DictReader(self.__file)
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.__file.close()

    def __iter__(self):
        return self

    def __next__(self) -> SimilarityInput:
        row = self.__csv_reader.__next__()
        image1_absolute_path = os.path.join(self.__input_csv_dir_path, row["image1"])
        image2_absolute_path = os.path.join(self.__input_csv_dir_path, row["image2"])
        return SimilarityInput(image1_absolute_path, image2_absolute_path)
