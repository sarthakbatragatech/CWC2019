# CWC 2019

A Deep Learning Image Classifier that takes an input image and predicts the cricket player in it. Currently optimized for a single player.

## Running the Project

Run the following statements in bash/zsh to create a new python environment, activate it, and install all project dependencies in it. To do the same in Windows, [click here](https://docs.python.org/3/library/venv.html).

```python3
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Downloading Image Data

To download data for the 15 squad players in each nation, run the script 'download_data.py'. Please note that the images downloaded from the package [google-images-download](https://github.com/hardikvasa/google-images-download) may be subject to copyright. You should ensure that you use them under fair means.

#### Sample Data
![Aaron Finch](https://github.com/sarthakbatragatech/CWC2019/blob/master/data/sample_data/Aaron%20Finch/Aaron_Finch_0.jpg)
