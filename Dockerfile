# =================== Start of Base ====================
FROM python:3.8.5-slim-buster AS base

# Install Required c-library for scikit-image SSIM algorithm
RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    libgl1-mesa-glx \
    gcc \
    libc-dev \
    libffi-dev \
    python3-dev
# =================== End of Base ====================

# =================== Start of DEPS ====================
FROM base AS dependencies

# Install PyBuilder
RUN pip install pybuilder==0.12.8

# Create app directory
WORKDIR /app

COPY requirements.txt ./
COPY build.py ./
# Install app dependencies
# To ensure docker cache install dependencied first
RUN pyb install_dependencies

# Now copy everything except .dockerignore
COPY . /app
RUN pyb
# =================== End of DEPS ====================


# =================== Start of release ====================
FROM base AS release
# Create app directory
WORKDIR /app
COPY --from=dependencies /app/target/dist/pyimage_similarity-0.0.1 .
COPY --from=dependencies /root/.cache /root/.cache

# install from setup.py
RUN pip install .
# Clean cache to minimize the docker image size
RUN rm -rf /root/.cache

CMD [ "python", "image_similarity.py"]
ENTRYPOINT ["/bin/bash"]
# =================== End of release ====================