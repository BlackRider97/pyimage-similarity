from datahandlers.output.i_output import IOutput
from datahandlers.output.similarity_output import SimilarityOutput

from utils.logger import Logger
logger = Logger.get_logger(__file__)


class CMDWriter(IOutput):
    """Write to console output"""

    def __init__(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def write(self, output: SimilarityOutput) -> bool:
        output_lines = list()
        output_lines.append("\n")
        output_lines.append(("*"*40) + " Similarity output " + ("*"*40))
        output_lines.append("first image: {}".format(output.first_image))
        output_lines.append("second image: {}".format(output.second_image))
        output_lines.append("similarity score: {}".format(output.similarity_score))
        output_lines.append("time taken: {0:.4f} secs".format(output.time_taken_in_seconds))
        output_lines.append("*" * 100)
        output_lines.append("\n")
        print("\n".join(output_lines))
        return True


