import unittest
import pytest
import tests


if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromModule(tests))
    runner = unittest.TextTestRunner(verbosity=3)
    results = runner.run(suite)



