# About repository
It is PyBuilder  https://pybuilder.io/ project.
A helper utility to compare visualization of images.
Provides set of choices for input and output streams
Efficient parallel processing to take advantage of available CPUs


# Architecture Diagram


# Installation Docker (Windows, Linux, MacOS)

# Installation Virtualenv (Linux, MacOS)

Python3.8+
`sudo apt-get install python3-pip`

Required c-library for `scikit-image` SSIM algorithm
`sudo apt install libgl1-mesa-glx`

make sure pip is up-to-date 

`python3 -m pip install --user --upgrade pip`

Use of virtual environment is highly recommended

`python3 -m pip install --user virtualenv`

Create a virtual environment and activate virtual environment at root of the project
`virtualenv venv`
`source venv/bin/activate`

## Installing PyBuilder 
`source venv/bin/activate`

` pip install pybuilder==0.12.8`



## Code Directory Structure

```
$ tree src/ -I "*.pyc"
src/
├── main
│   ├── python
│   │   ├── algorithms
│   │   │   ├── i_image_algorithm.py
│   │   │   ├── image_hashing_algorithm.py
│   │   │   └── ssim_algorithm.py
│   │   ├── conf
│   │   │   ├── config.Development.yaml
│   │   │   ├── config.py
│   │   │   └── config_manager.py
│   │   ├── datahandlers
│   │   │   ├── __pycache__
│   │   │   ├── input
│   │   │   │   ├── cmd_reader.py
│   │   │   │   ├── csv_reader.py
│   │   │   │   ├── i_input.py
│   │   │   │   └── similarity_input.py
│   │   │   └── output
│   │   │       ├── cmd_write.py
│   │   │       ├── csv_writer.py
│   │   │       ├── i_output.py
│   │   │       └── similarity_output.py
│   │   ├── image_similarity.py
│   │   ├── processor
│   │   │   ├── consumer
│   │   │   │   └── queue_consumer.py
│   │   │   ├── image_similarity_task.py
│   │   │   ├── parallel_processor.py
│   │   │   ├── producer
│   │   │   │   └── queue_producer.py
│   │   │   ├── task.py
│   │   │   └── tasks_queue.py
│   │   └── utils
│   │       └── logger.py
│   └── scripts
└── unittest
    └── python
        └── hello_word_tests.py
```