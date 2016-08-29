#-*- coding: UTF-8 -*- 

from nose.tools import *
from ex49.ex49 import *
#dai hui c shi shangceng daoru
from ex49.ex48 import *
lexicon=lex()

#在这里声明会出问题，多次使用会改变word_list
#word_list = lexicon.scan('kill the bear')
#word_list2 = lexicon.scan('the bear goes north')


def test_peek():
    word_list = lexicon.scan('kill the bear')
    word_list2 = lexicon.scan('the bear go north')
    # assert_equal(peek([('verb','go'),('noun','bear'),('stop','of')]),'verb')
    assert_equal(peek(word_list),'verb')
    assert_equal(peek([]),None)

def test_match():
    word_list = lexicon.scan('kill the bear')
    word_list2 = lexicon.scan('the bear go north')
    assert_equal(match(word_list,'verb'),('verb','kill'))
    assert_equal(match(word_list2,'verb'),None)

#函数没有返回值 测试要注意测试副作用
def test_skip():
    # assert_equal(skip(word_list, 'verb'),('verb','kill'))
    word_list = lexicon.scan('kill the bear')
    word_list2 = lexicon.scan('the bear go north')
    skip(word_list, 'verb')
    assert_equal(word_list[0][0],('stop'))
    
def test_parse_verb():
    word_list = lexicon.scan('kill the bear')
    word_list2 = lexicon.scan('the bear go north')
    assert_equal(parse_verb(word_list),('verb','kill'))
    assert_raises(ParserError,parse_verb, word_list2)
   
def test_parse_object():
    word_list = lexicon.scan('kill the bear')
    word_list2 = lexicon.scan('the bear go north')
    assert_equal(parse_object(word_list2), ('noun','bear'))
    assert_raises(ParserError, parse_object, word_list)





#报错，<ex49.ex49.Sentence object at 0x000000000319A470> != <ex49.ex49.Sentence object at 0x000000000319A4A8>
def test_parse_subject():
    word_list = lexicon.scan('kill the bear')
    word_list2 = lexicon.scan('the bear go north')
    
    verb = parse_verb(word_list)
    obj = parse_object(word_list)
    assert_equal(verb,('verb','kill') )
    assert_equal(obj,('noun','bear') )   
    word_list = lexicon.scan('kill the bear')
    assert_equal(parse_subject(word_list, ('noun','player')),Sentence(('noun','player'), verb, obj))





def test_parse_sentence():
    word_list = lexicon.scan('kill the bear')
    word_list2 = lexicon.scan('the bear go north')
    assert_equal(parse_sentence(word_list2),parse_subject([('verb','go'),('direction','north')], ('noun','bear')))

    #require error test here
  






















    
