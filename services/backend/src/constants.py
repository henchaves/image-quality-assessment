import os

HOME_DIR_PATH = os.path.join("/", "app")

DATA_DIR_PATH = os.path.join(HOME_DIR_PATH, "data")

RAW_DIR_PATH = os.path.join(DATA_DIR_PATH, "raw")
INTERIM_DIR_PATH = os.path.join(DATA_DIR_PATH, "interim")
PROCESSED_DIR_PATH = os.path.join(DATA_DIR_PATH, "processed")