# Tweets-geolocation Classifier

This project is aimed to predict the geolocation of a certain of tweet

## Environment

- Win 10
- Python 3.5.x

## Required Packages

- `pickle`
- `liac-arff`
- `scikit-learn`
- `csv`
- `tqdm` (not necessary)

## Details

- Details of dataset can be found in `/data`

- unzip the dataset file in `/data` for later training process

- Main Entrance is main.py

- All the model will be trained and saved in `/model` (run traning process in main.py)

- The results of different model on different dataset are saved in `result.txt`

- If you want to do prediction with different model on different dataset, just modify parameters `best/most` `10/20/50/200` `<model-name>` in the prediction part in main.py and run prediction process (before this, run training process or you won't have the model to predict)