from multiprocessing import JoinableQueue, cpu_count

from conf.config_manager import ConfigManager
from datahandlers.output.i_output import IOutput
from processor.consumer.queue_consumer import Consumer
from processor.producer.queue_producer import Producer
from processor.task import Task
from utils.logger import Logger

logger = Logger.get_logger(__file__)


class ParallelProcessor:

    def __init__(self, output_handler: IOutput):
        self.tasks_queue = JoinableQueue()
        self.__producers = []
        self.__consumers = []
        self.__output_handler = output_handler
        # first create consumers so that we can start messages as soon as task available
        self.__create_consumers()
        self.__create_producers()

    def __create_producers(self):
        self.__producers = [Producer(self.tasks_queue) for i in range(self.producers_count)]
        logger.info("Total %d producers created", self.producers_count)

    def __create_consumers(self):
        self.__consumers = [Consumer(self.tasks_queue, self.__output_handler) for i in range(self.consumers_count)]
        logger.info("Total %d consumers started", self.consumers_count)
        for consumer in self.__consumers:
            consumer.start()


    @property
    def producers_count(self):
        # since producer enqueue operation is very fast
        # We are creating one producer only as of now
        return 1


    @property
    def consumers_count(self):
        consumers_count = ConfigManager.get_instance().consumers_count()
        return cpu_count() * 2 - 1 if consumers_count == 0 else consumers_count


    def handle_task(self, task: Task):
        self.__producers[0].enqueue_task(task)


    def join(self):
        # Wait for all of the tasks to finish
        self.tasks_queue.join()


    def shutdown(self):
        logger.debug("Sending shut down signal to consumers")

        # Add a poison pill for each consumer so that consumers can stop gracefully
        for i in range(self.consumers_count):
            self.tasks_queue.put(None)
        logger.info("Shutdown of consumers completed")
