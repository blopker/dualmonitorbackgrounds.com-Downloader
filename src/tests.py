import unittest
import GetWallPaper


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        # self.html = GetWallPaper.getHTML("http://dualmonitorbackgrounds.com/abstract/page/2/")
        pass

    def test_getMaxPage(self):
        print GetWallPaper.getMaxPage("abstract")
        assert GetWallPaper.getMaxPage("abstract") == 11

if __name__ == '__main__':
    unittest.main()
