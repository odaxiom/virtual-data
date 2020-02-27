import numpy as np
import os
import unittest
from sklearn.ensemble import RandomForestRegressor
import shutil
import random

from vdata import Data


random.seed(42)


class DataModelTests(unittest.TestCase):
    def tearDown(self):
        shutil.rmtree('data', ignore_errors=True)

    def test_model_saving(self):
        model = RandomForestRegressor(random_state=42)

        MODEL = Data(name='my_model', type='model')

        for _ in range(10):
            x = random.randint(0, 1000)
            y = x * 2

            model.fit([[x]], [y])
            MODEL.save(model)

        self.assertTrue(os.path.join('data', 'model', 'my_model.0'))
        self.assertTrue(os.path.join('data', 'model', 'my_model.9'))

    def test_model_loading(self):
        model = RandomForestRegressor(random_state=42)

        MODEL = Data(name='my_model', type='model')

        X = [[random.randint(0, 100)] for _ in range(1000)]
        y = [np.multiply(x, 2) for x in X]

        model.fit(X, y)

        MODEL.save(model)
        del model

        model = MODEL.get()
        predict = model.predict([[1]])

        self.assertEqual(predict, [2])
