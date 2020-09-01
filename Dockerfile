FROM python:3.8.5-alpine

# Install Required c-library for scikit-image SSIM algorithm
RUN apt-get update && apt-get install \
    libgl1-mesa-glx

# Install PyBuilder
RUN pip install pybuilder==0.12.8

WORKDIR /app
COPY *.py ./
COPY requirements.txt .
COPY images.csv .
COPY images ./images/
COPY results ./results/

RUN pip install -r requirements.txt

# CMD [ "python", "./image_comparator.py" ]
ENTRYPOINT ["/bin/bash"]