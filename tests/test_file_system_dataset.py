"""
Notes:
* The metadata dictionary should probably

"""

import unittest
import os
import inspect

import great_expectations as ge

class TestFileSystemDataset(unittest.TestCase):

    def setUp(self):
        filepath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))+"/test_fixtures/"
        self.D = ge.dataset.FileSystemDataSet(filepath)

    def test_expect_file_to_be_csv_parseable(self):
        self.assertEqual(
            self.D.expect_file_to_be_csv_parseable("test_csv_parseable.csv"),
            {"success": True}
        )

if __name__ == "__main__":
    unittest.main()
