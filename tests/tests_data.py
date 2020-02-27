import os
import pandas as pd
import shutil
import unittest

from vdata import Data


class DataTests(unittest.TestCase):
    def tearDown(self):
        shutil.rmtree('.vdata', ignore_errors=True)

    def test_save_is_variable_created(self):
        """
        Check if a file is created when save is called.
        """
        a = 42

        data = Data(name='my_variable', namespace='raw')
        data.save(data=a)

        self.assertTrue(os.path.isfile(os.path.join('.vdata', 'raw', 'my_variable.0.vdata')))

    def test_get_variable(self):
        """
        Check if a file is created when save is called.
        """
        a = 42
        data = Data(name='my_variable', namespace='raw')
        data.save(data=a)

        del a

        a = data.get()

        self.assertEqual(a, 42)

    def test_get_versions(self):
        """
        Check if we are able to get versions of Data
        """
        data = Data(name='my_variable', namespace='raw')
        data.save(data=10)
        data.save(data=100)

        self.assertEqual(data.get_versions(), [0, 1])

    def test_get_max_version(self):
        """
        Check if we are able to get max version of Data
        """
        data = Data(name='my_variable', namespace='raw')
        data.save(data=10)
        data.save(data=100)

        self.assertEqual(data.get_max_version(), 1)

    def test_save_file(self):
        """
        Save a file from path.
        """
        data = Data(name="job", namespace="raw")

        data.save(file_path='tests/tests.csv')

        self.assertTrue(os.path.isfile(os.path.join('.vdata', 'raw', 'job.0.csv')))

    def test_save_file_load_dataframe(self):
        """
        Save CSV file and load in dataframe.
        """
        data = Data(name="job", namespace="raw")

        data.save(file_path='tests/tests.csv')
        df = pd.read_csv(data.get())

        a = df.iloc[0]['a']

        self.assertTrue(a, 42)

    def test_save_file_ext_and_reload(self):
        data = Data(name="job", namespace="raw")

        data.save(file_path='tests/tests.csv')

        del data

        data = Data(name="job", namespace="raw")
        df = pd.read_csv(data.get())

        a = df.iloc[0]['a']

        self.assertTrue(a, 42)
