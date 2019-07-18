import unittest
import json
from .translator import Translator
from .exceptions import ChineseCharsNotFound

class TestTranslator(unittest.TestCase):
    def setUp(self):
        self.tra = Translator("繁簡轉換器")

    def test_check(self):
        self.assertIsNotNone(self.tra.text_input)
    
        with self.assertRaises(SystemExit):
            Translator.check_text("hello")

    def test_segment(self):
        simp = self.tra.list_sim
        trad = self.tra.list_trad

        self.assertIsInstance(simp, list)
        self.assertIsInstance(trad, list)
        
        self.assertIn("繁简", simp)
        self.assertNotIn("繁简", trad)

        self.assertIn("转换器", simp)
        self.assertNotIn("转换器", trad)

        self.assertEqual(len(simp), len(trad))

        for ab in zip(simp, trad):
            a, b = ab
            self.assertEqual(len(a), len(b))

    def test_romanize(self):
        py = self.tra.list_py

        self.assertIsInstance(py, list)

        self.assertEqual(len(py), len(self.tra.list_sim))
        
        self.assertIn("fánjiǎn", py)
        self.assertIn("zhuǎnhuànqì", py)

    def test_definition(self):
        defi = self.tra.list_def
        
        def1 = ['complicated and simple', 'traditional and simplified form of Chinese characters']
        def2 = ['converter', 'transducer']

        self.assertIsInstance(defi, list)

        self.assertEqual(len(defi), len(self.tra.list_sim))
        
        self.assertIn(def1, defi)
        self.assertIn(def2, defi)

    def test_json(self):
        file = self.tra.jsonify_attributes()

        self.assertIsInstance(file, str)
        
        attr = json.loads(file)
        self.assertEqual(len(attr), 5)

if __name__== "__main__":
    unittest.main()