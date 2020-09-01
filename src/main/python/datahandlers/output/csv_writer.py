import csv
import threading

from datahandlers.output.i_output import IOutput
from datahandlers.output.similarity_output import SimilarityOutput

from utils.logger import Logger

logger = Logger.get_logger(__file__)


class CSVWriter(IOutput):
    """Write to given CSV file"""
    __lock = threading.Lock()


    def __init__(self, csv_file_path):
        self.__csv_file_path = csv_file_path
        if not self.__csv_file_path:
            raise Exception("Output CSV file path not specified")
        self.__file = None
        self.__csv_writer = None


    def __enter__(self):
        # take a lock and handle concurrency at file-level for file creation & header write
        self.__file = open(self.__csv_file_path, 'w')
        field_names = ['image1', 'image2', 'similar', 'elapsed']
        self.__csv_writer = csv.DictWriter(self.__file, fieldnames=field_names)

        # write headers only one-time
        self.__write_row({
            'image1': "image1",
            'image2': "image2",
            'similar': "similar",
            'elapsed': "elapsed"
        })

        return self


    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.__file.close()


    def __write_row(self, row):
        # take a lock and handle concurrency at row-level instead of file level
        with CSVWriter.__lock:
            self.__csv_writer.writerow(row)
            # Flush right away to avoid data corruption
            # https://stackoverflow.com/questions/3976711/csvwriter-not-saving-data-to-file-the-moment-i-write-it
            self.__file.flush()
            return True


    def write(self, output: SimilarityOutput) -> bool:
        # take a lock and handle concurrency at row-level instead of file level
        return self.__write_row({
            'image1': output.first_image,
            'image2': output.second_image,
            'similar': output.similarity_score,
            'elapsed': float("{:.4f}".format(output.time_taken_in_seconds))
        })
