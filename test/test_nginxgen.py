import unittest
from src import NginxGen

class TestStringMethods(unittest.TestCase):


    def test_configFromYml(self):
        yml = """   host: testhost
                    domain: test.com """
        
        nGen = NginxGen(yml)



if __name__ == '__main__':
    unittest.main()