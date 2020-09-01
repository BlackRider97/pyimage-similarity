import time
from abc import ABC, abstractmethod


class Task(ABC):
    """
    Abstract task class
    """


    def __init__(self):
        self.__creation_timestamp = int(time.time() * 1000)  # milli seconds level timestamp
        self.__processing_time = None


    @property
    def creation_timestamp(self):
        return self.__creation_timestamp


    @property
    def processing_time(self):
        return self.__processing_time


    @abstractmethod
    def process(self):
        """
        Process a task.
        :return:
        """


    def __call__(self):
        """
        Entry point to process a task
        :return:
        """
        # Start the stopwatch / counter
        start = time.perf_counter()
        return_value = self.process()
        # Stop the stopwatch / counter
        end = time.perf_counter()
        self.__processing_time = end - start
        return return_value
