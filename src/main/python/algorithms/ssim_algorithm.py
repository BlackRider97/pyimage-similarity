from algorithms.i_image_algorithm import IImageAlgorithm
from skimage.measure import compare_ssim
import cv2
import warnings
warnings.filterwarnings("ignore")


class ImageSSIMAlgorithm(IImageAlgorithm):
    """
    Structural Similarity Index Measure (SSIM)
    https://en.wikipedia.org/wiki/Structural_similarity

    The Structural Similarity Index (SSIM) is a perceptual metric that quantifies the image quality degradation that is
    caused by processing such as data compression or by losses in data transmission. This metric is basically a full
    reference that requires 2 images from the same shot, this means 2 graphically identical images to the human eye.
    The second image generally is compressed or has a different quality, which is the goal of this index.

    """


    def __init__(self):
        pass


    def name(self) -> str:
        return "SSIM"


    def calculate_similarity(self, first_image: str, second_image: str) -> float:
        # Load the two input images
        image1, image2 = cv2.imread(first_image), cv2.imread(second_image)

        # Convert the images to gray scale
        gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

        # Compute the Structural Similarity Index (SSIM) between the two
        # images, ensuring that the difference image is returned
        (score, diff) = compare_ssim(gray1, gray2, full=True)
        return round(1-score, 4) # round-off till 4 decimal place
