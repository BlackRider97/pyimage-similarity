"""
The code here abstracts consumer capabilities for the queueing mechanism
It consumes tasks from the queue, processes them and acknowledges that the task has been processed successfully
As a part of the processing, it also stores data in a file
Ideally, storage should be abstracted too, but for now it just writes to a file
"""

from __future__ import (absolute_import, division, print_function)
import time
from multiprocessing import Process

from datahandlers.output.i_output import IOutput
from utils.logger import Logger

logger = Logger.get_logger(__file__)


class Consumer(Process):

    def __init__(self, tasks_queue, output_handler: IOutput):
        super().__init__()
        self.__tasks_queue = tasks_queue
        self.__output_handler = output_handler


    def run(self):
        logger.debug("Starting process: %s", self.name)
        # keep the process running until all task are processed
        while True:
            task_to_execute = self.__tasks_queue.get()
            if task_to_execute is None:
                # Poison pill means shutdown the process
                logger.info('Exiting process: %s' % self.name)
                self.__tasks_queue.task_done()
                break
            time_in_queue = int((time.time()) * 1000) - task_to_execute.creation_timestamp
            logger.debug('Going to process task: %s with-in process :%s, time_in_queue: %s milli secs',
                         task_to_execute, self.name, time_in_queue)

            # safe execution of task
            try:
                output = task_to_execute()
                self.__output_handler.write(output)
                logger.info('Processed task: %s with-in process :%s, processing time: %s secs',
                            task_to_execute, self.name, task_to_execute.processing_time)
            except Exception as e:
                logger.exception("Caught exception while processing task: %s process: %s error: %s",
                                 task_to_execute, self.name, str(e))

            # acknowledge task done so no other consumer picks it up again.
            self.__tasks_queue.task_done()
