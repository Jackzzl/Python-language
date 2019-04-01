import tensorflow as tf
from tensorflow_datasets import my_dataset
import tensorflow_datasets.testing as tfds_test


class MyDatasetTest(tfds_test.DatasetBuilderTestCase):
  DATASET_CLASS = my_dataset.MyDataset
  SPLITS = {  # Expected number of examples on each split from fake example.
      "train": 12,
      "test": 12,
  }
  # If dataset `download_and_extract`s more than one resource:
  DL_EXTRACT_RESULT = {
      "name1": "path/to/file1",  # Relative to fake_examples/my_dataset dir.
      "name2": "file2",
  }

if __name__ == "__main__":
  tfds_test.test_main()