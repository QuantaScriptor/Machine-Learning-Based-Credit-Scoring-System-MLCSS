
import unittest
import numpy as np
import pandas as pd
from mlcss import CreditScoringSystem

class TestMLCSS(unittest.TestCase):
    def setUp(self):
        self.data = pd.DataFrame({
            'income': np.random.rand(100) * 100000,
            'debt': np.random.rand(100) * 50000,
            'age': np.random.randint(18, 70, 100),
            'credit_history': np.random.randint(0, 10, 100)
        })
        self.target = np.random.randint(2, size=100)
        self.mlcss = CreditScoringSystem()

    def test_train_model(self):
        self.mlcss.train_model(self.data, self.target)
        self.assertIsNotNone(self.mlcss.model)

    def test_predict_credit_score(self):
        self.mlcss.train_model(self.data, self.target)
        predictions = self.mlcss.predict_credit_score(self.data[:5])
        self.assertEqual(len(predictions), 5)

if __name__ == '__main__':
    unittest.main()
