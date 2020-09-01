import argparse
import sys

from conf.config_manager import ConfigManager
from datahandlers.input.cmd_reader import CMDReader
from datahandlers.input.csv_reader import CSVReader
from datahandlers.output.cmd_write import CMDWriter
from datahandlers.output.csv_writer import CSVWriter
from processor.image_similarity_task import ImageSimilarityTask
from processor.parallel_processor import ParallelProcessor
from utils.logger import Logger

logger = Logger.get_logger(__file__)

parser = argparse.ArgumentParser(description='Find similarity between images')

parser.add_argument('-m', '--mode', dest='mode', type=str, default="CSV", choices=['CSV', 'CMD'],
                    help='Mode of program (Default: CSV)')

# mode CSV
parser.add_argument('--input-csv', dest='input_csv_file_path', type=str,
                    help='Input CSV file path (Required when mode=CSV)')
parser.add_argument('--output-csv', dest='output_csv_file_path', type=str,
                    help='Output CSV file path (Required when mode=CSV)')

# mode CMD
parser.add_argument('--first-image', dest='first_image_file_path', type=str,
                    help='First image file path (Required when mode=CMD)')

parser.add_argument('--second-image', dest='second_image_file_path', type=str,
                    help='Second image file path (Required when mode=CMD)')

if __name__ == '__main__':
    args = parser.parse_args()
    logger.info("Executing program with following arguments: %s", args)

    input_handler, output_handler = None, None
    if args.mode == "CSV":
        input_handler = CSVReader(args.input_csv_file_path)
        output_handler = CSVWriter(args.output_csv_file_path)
        # any writer can be added
        # output_handler = CMDWriter()
    elif args.mode == "CMD":
        input_handler = CMDReader(args.first_image_file_path, args.second_image_file_path)
        output_handler = CMDWriter()

    with output_handler as output_handler:
        algorithm = ConfigManager.get_instance().get_algorithm()
        logger.info("Selected image similarity algorithm: %s", algorithm.name())
        processor = ParallelProcessor(output_handler)
        with input_handler as in_handler:
            for input_message in in_handler:
                if input_message.is_valid():
                    task = ImageSimilarityTask(algorithm, input_message)
                    processor.handle_task(task)
                else:
                    logger.warning("*** Invalid input: %s found so skipping it's processing", input_message)

        processor.shutdown()
        processor.join()
    sys.exit(0)
