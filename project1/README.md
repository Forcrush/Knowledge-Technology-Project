# Judging blending word and finding its components

The goal of this project is to develop and critically assess methods for detecting blending words among frequent terms in Twitter data, and to find the possible two components which can construct the word. Some pre-processes have been done (the details can be seen in `data/README.txt`)

## Environment

- Win 10
- Python 3.5.x

## Required Packages

- `pickle`
- `textdistance`
- `tqdm` (not necessary)

## Details

- `data` contains the initial data such as `dictionary.txt`, `blends.txt`, etc. which are important for constructing the model
- `evaluation_data` contains the evaluation results of the first and second task in this project
- `data_processing.py` is about the core algorithms
- `evaluate.py` is the file to evaluate the model
- `main.py` is the entrance of execution, some metrics and paths can be attributed in the head of this file 
- `metric.py` about some edit-distance algorithms
- `util.py` mainly about the implementation of BK-Tree
- `visualization_blends.py` visualizes the latent relationship between blending words in `data/blends.txt` under some metrics

## Execution

- Just run `main.py`
- You can choose to evaluate the model or test a new word (set the state of `evaluation`)
- Defalut metric combination is '1237', you can set your own in the head of `main.py` (note: '1' < legal form < '1234567'