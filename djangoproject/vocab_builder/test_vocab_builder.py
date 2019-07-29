import pytest
from .vocab_builder import CNVocabBuilder
import json
from .exceptions import ChineseCharsNotFound
import hanzidentifier as hanzI

cnvb = CNVocabBuilder("繁簡轉換器 300 romans?")
cnvb2 = CNVocabBuilder("繁簡轉換器")
cnvb3 = CNVocabBuilder("300")

text = cnvb.text_input
sim = cnvb.list_sim
trad = cnvb.list_trad
py = cnvb.list_py
defi = cnvb.list_defi

def test_check():
    assert cnvb.text_input is not None

    with pytest.raises(ChineseCharsNotFound):
        CNVocabBuilder.check_text("hello")
    
    attr = ('text_input', 'list_sim', 'list_trad', 'list_py', 'list_defi')
    assert all(x in attr for x in cnvb3.__dict__)

def test_filter():
    assert len(cnvb.list_sim) == len(cnvb2.list_sim)
    
    test = tuple(map(hanzI.identify, cnvb.list_sim))
    assert 0 not in test

def test_segment():
    assert type(sim) is list and type(trad) is list
    
    assert len(sim) == len(trad)

    list_test = ("繁简", "转换器")
    assert all(x in list_test for x in sim)
    assert not all(x in list_test for x in trad)
    
    for st in zip(sim, trad):
        s, t = st
        assert len(s) == len(t)

def test_romanize():
    assert type(py) is list

    assert len(py) == len(sim)

    list_test = ("fánjiǎn", "zhuǎnhuànqì")

    assert all(x in list_test for x in py)

def test_definition():
    assert type(defi) is list

    d1 = ['complicated and simple', 'traditional and simplified form of Chinese characters']
    d2 = ['converter', 'transducer']
    list_test = (d1, d2)
    assert all(x in list_test for x in defi)

    assert len(defi) == len(sim)

if __name__ == "__main__":
    pytest.main([__file__])