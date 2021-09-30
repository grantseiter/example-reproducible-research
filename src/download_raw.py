"""
This script downloads the data needed for analysis from the ONS
API. It uses series that are in the yaml config file.
"""
from pathlib import Path
import seaborn as sns


def get_and_save_raw_data():
    """ Saves the raw data to disk.
    """
    df = sns.load_dataset("car_crashes")
    df.to_csv(Path("raw/raw_data.csv"))


if __name__ == "__main__":
    get_and_save_raw_data()
