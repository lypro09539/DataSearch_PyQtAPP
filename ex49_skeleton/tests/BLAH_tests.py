from nose.tools import *
from ex46.ex49 import *
#dai hui c shi shangceng daoru
from ex46.ex48 import *
lexicon=lex()
word_list=lexicon.scan('kill the bear')

def test_peek():
    assert_equal(peek([('verb','go'),('noun','bear'),('stop','of')]),'verb')
    assert_equal(peek(word_list),'verb')
