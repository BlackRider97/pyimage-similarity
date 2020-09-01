# About repository
It is [PyBuilder](https://pybuilder.io/) project.

A helper utility to compare visualization of images.

Provides set of choices for input and output streams

Efficient parallel processing to take advantage of available CPUs


# Architecture Diagram



# Installation Docker (Windows, Linux, MacOS)


# Installation Virtualenv (Linux, MacOS)


### Python3.8+
`sudo apt-get install python3-pip`

### Required c-library for `scikit-image` SSIM algorithm

`sudo apt install libgl1-mesa-glx`


### Pip
make sure pip is up-to-date 

`python3 -m pip install --user --upgrade pip`

### Virtual environment
Use of virtual environment is highly recommended

`python3 -m pip install --user virtualenv`

Create a virtual environment and activate virtual environment at root of the project.

`virtualenv venv`
`source venv/bin/activate`

## Installing PyBuilder 

	```
  	source venv/bin/activate
  	pip install pybuilder==0.12.8
	```

## Building project

### Install dependencies
`pyb install_dependencies`

**Sample output**

	```
	PyBuilder version 0.12.8
	Build started at 2020-09-01 22:09:04
	------------------------------------------------------------
	[INFO]  Building pyimage_similarity version 0.0.1
	[INFO]  Executing build in /mnt/c/Users/ramithar/Desktop/pyimage-similarity
	[INFO]  Going to execute task install_dependencies
	[INFO]  Processing plugin packages 'coverage~=5.2' to be installed with {'upgrade': True}
	[INFO]  Processing plugin packages 'flake8~=3.7' to be installed with {'upgrade': True}
	[INFO]  Processing plugin packages 'pypandoc~=1.4' to be installed with {'upgrade': True}
	[INFO]  Processing plugin packages 'setuptools>=38.6.0' to be installed with {'upgrade': True}
	[INFO]  Processing plugin packages 'twine>=1.15.0' to be installed with {'upgrade': True}
	[INFO]  Processing plugin packages 'unittest-xml-reporting~=3.0.2' to be installed with {'upgrade': True}
	[INFO]  Processing plugin packages 'wheel>=0.34.0' to be installed with {'upgrade': True}
	[INFO]  Creating target 'build' VEnv in '/mnt/c/Users/ramithar/Desktop/pyimage-similarity/target/venv/build/cpython-3.8.5.final.0'
	
	[INFO]  Processing dependency packages 'requirements.txt' to be installed with {}
	[INFO]  Creating target 'test' VEnv in '/mnt/c/Users/ramithar/Desktop/pyimage-similarity/target/venv/test/cpython-3.8.5.final.0'
	[INFO]  Processing dependency packages 'requirements.txt' to be installed with {}
	[INFO]  Installing all dependencies
	[INFO]  Processing dependency packages 'requirements.txt' to be installed with {}
	------------------------------------------------------------
	BUILD SUCCESSFUL
	------------------------------------------------------------
	Build Summary
	             Project: pyimage_similarity
	             Version: 0.0.1
	      Base directory: /mnt/c/Users/ramithar/Desktop/pyimage-similarity
	        Environments:
	               Tasks: prepare [51672 ms] install_dependencies [3220 ms]
	Build finished at 2020-09-01 22:10:26
	Build took 81 seconds (81908 ms)
	```

### Build project (run tests, coverage, scripts, packaging etc.)
` pyb -v`

**Sample output**

	```
     .....
	[INFO]  Overall pyimage_similarity partial branch coverage is 100%
	[INFO]  Building binary distribution in /mnt/c/Users/ramithar/Desktop/pyimage-similarity/target/dist/pyimage_similarity-0.0.1
	[INFO]  Running Twine check for generated artifcats
	------------------------------------------------------------
	BUILD SUCCESSFUL
	------------------------------------------------------------
	Build Summary
	             Project: pyimage_similarity
	             Version: 0.0.1
	      Base directory: /mnt/c/Users/ramithar/Desktop/pyimage-similarity
	        Environments:
	               Tasks: prepare [48596 ms] compile_sources [0 ms] run_unit_tests [716 ms] package [271 ms] run_integration_tests [0 ms] verify [0 ms] coverage [3727 ms] publish [5318 ms]
	Build finished at 2020-09-01 21:50:36
	Build took 86 seconds (86272 ms)
	```


## How to use the Docker image

### Always pull latest image from public Dockerhub

https://hub.docker.com/repository/docker/rajneeshmitharwal/pyimage-similarity 

### Docker pull command
`docker push rajneeshmitharwal/pyimage-similarity:latest`

### Volume mounting

- `Input` Volume

  `docker run -v /path/to/input/folder:/input` (Linux/Mac OS)

  `docker run -v C:\Users\user\input\folder:/input` (Windows)

- `Output` Volume

  `docker run -v /path/to/output/folder:/output` (Linux/Mac OS)

  `docker run -v C:\Users\user\output\folder:/output` (Windows)


### How to use this docker image

#### Print Usages command

	```
	docker run rajneeshmitharwal/pyimage-similarity:latest
	usage: image_similarity.py [-h] [-m {CSV,CMD}]
	                           [--input-csv INPUT_CSV_FILE_PATH]
	                           [--output-csv OUTPUT_CSV_FILE_PATH]
	                           [--first-image FIRST_IMAGE_FILE_PATH]
	                           [--second-image SECOND_IMAGE_FILE_PATH]
	
	Find similarity between images
	
	optional arguments:
	  -h, --help            show this help message and exit
	  -m {CSV,CMD}, --mode {CSV,CMD}
	                        Mode of program (Default: CSV)
	  --input-csv INPUT_CSV_FILE_PATH
	                        Input CSV file path (Required when mode=CSV)
	  --output-csv OUTPUT_CSV_FILE_PATH
	                        Output CSV file path (Required when mode=CSV)
	  --first-image FIRST_IMAGE_FILE_PATH
	                        First image file path (Required when mode=CMD)
	  --second-image SECOND_IMAGE_FILE_PATH
	                        Second image file path (Required when mode=CMD)
	```

### CSV line input & output

```
docker run -v C:\Users\ramithar\Desktop\pyimage-similarity\input:/input -v  C:\Users\ramithar\Desktop\pyimage-similarity\output:/output rajneeshmitharwal/pyimage-similarity:latest --mode CSV  --input-csv /input/input_csv.csv  --output-csv /output/output_csv.csv
Successfully run script :-)

PS C:> cat C:\Users\ramithar\Desktop\pyimage-similarity\output\output_csv.csv
image1,image2,similar,elapsed
/input/taj-mahal.jpg,/input/taj-mahal.png,0.0,1.0554
```

### Command line input & output


```
docker run -v C:\Users\ramithar\Desktop\pyimage-similarity\input:/input rajneeshmitharwal/pyimage-similarity:latest --mode CMD  --first-image /input/taj-mahal.jpg --second-image /input/taj-mahal.png


**************************************** Similarity output ****************************************
first image: /input/taj-mahal.jpg
second image: /input/taj-mahal.png
similarity score: 0.0
time taken: 0.4790 secs
****************************************************************************************************


Successfully run script :-)
```
 


## How to use program ( via Virtual environment)

### Build and create target

- `source venv/bin/activate`
- ` $ pyb -v`
- `cd target/dist/pyimage_similarity-0.0.1/`
-  Check usages

	```
	python image_similarity.py -h
	usage: image_similarity.py [-h] [-m {CSV,CMD}] [--input-csv INPUT_CSV_FILE_PATH] [--output-csv OUTPUT_CSV_FILE_PATH] [--first-image FIRST_IMAGE_FILE_PATH] [--second-image SECOND_IMAGE_FILE_PATH]
	
	Find similarity between images
	
	optional arguments:
	  -h, --help            show this help message and exit
	  -m {CSV,CMD}, --mode {CSV,CMD}
	                        Mode of program (Default: CSV)
	  --input-csv INPUT_CSV_FILE_PATH
	                        Input CSV file path (Required when mode=CSV)
	  --output-csv OUTPUT_CSV_FILE_PATH
	                        Output CSV file path (Required when mode=CSV)
	  --first-image FIRST_IMAGE_FILE_PATH
	                        First image file path (Required when mode=CMD)
	  --second-image SECOND_IMAGE_FILE_PATH
	                        Second image file path (Required when mode=CMD)
	```



### Sample commands
  
	```
	python image_similarity.py --mode CMD  --first-image /mnt/c/Users/ramithar/Desktop/pyimage-similarity/input/taj-mahal.jpg --second-image /mnt/c/Users/ramithar/Desktop/pyimage-similarity/input/taj-mahal.png
	
	
	**************************************** Similarity output ****************************************
	first image: /mnt/c/Users/ramithar/Desktop/pyimage-similarity/input/taj-mahal.jpg
	second image: /mnt/c/Users/ramithar/Desktop/pyimage-similarity/input/taj-mahal.png
	similarity score: 0.0
	time taken: 0.6938 secs
	****************************************************************************************************
	```


	```
    python image_similarity.py --mode CSV  --input-csv /mnt/c/Users/ramithar/Desktop/pyimage-similarity/input/input_csv.csv  --output-csv /mnt/c/Users/ramithar/Desktop/pyimage-similarity/output/output_csv.csv

	Successfully run script :-)

	**** (Verify output ) ***
	cat /mnt/c/Users/ramithar/Desktop/pyimage-similarity/output/output_csv.csv
	image1,image2,similar,elapsed
	/mnt/c/Users/ramithar/Desktop/pyimage-similarity/input/taj-mahal.jpg,/mnt/c/Users/ramithar/Desktop/pyimage-similarity/input/taj-mahal.png,0.0,0.914
    ```


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