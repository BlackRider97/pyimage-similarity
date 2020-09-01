from typing import List

from processor.task import Task

from utils.logger import Logger

logger = Logger.get_logger(__file__)


class Producer:

    def __init__(self, tasks_queue: List[Task]):
        super().__init__()
        self.__tasks_queue = tasks_queue


    def enqueue_task(self, task: Task):
        logger.info("Queuing task : %s", task)
        self.__tasks_queue.put(task)
