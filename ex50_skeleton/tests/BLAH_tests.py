#-*- coding: UTF-8 -*- 
from nose.tools import *
from ex49.ex49 import *
#dai hui c shi shangceng daoru
from ex49.ex48 import *
lexicon=lex()
word_list = lexicon.scan('kill the bear')
word_list2 = lexicon.scan('the bear goes north')


def test_peek():
    # assert_equal(peek([('verb','go'),('noun','bear'),('stop','of')]),'verb')
    assert_equal(peek(word_list),'verb')
    assert_equal(peek([]),None)

def test_match():
    assert_equal(match(word_list,'verb'),('verb','kill'))
    assert_equal(match(word_list2,'verb'),None)

#函数没有返回值 测试要注意测试副作用
def test_skip():
    # assert_equal(skip(word_list, 'verb'),('verb','kill'))
    skip(word_list, 'verb')
    assert_equal(word_list[0][0],('stop'))
    
def test_parse_verb():
    assert_equal(parse_verb(word_list),('verb','kill'))
    assert_raises(ParserError,parse_verb(word_list2), parse_verb, word_list2)
   
def test_parse_object():
    assert_equal(parse_object(word_list2), ('noun','bear'))
    assert_raises(ParserError, parse_object, word_list)

def test_parse_subject():
    assert_equal(parse_subject(word_list, 'player'),Sentence('player',parse_verb(word_list),parse_object(word_list)))

def test_parse_sentence():
    assert_equal(parse_sentence(word_list2),parse_subject(word_list2, match(word_list2, 'noun')))
    assert_equal(parse_sentence(word_list),parse_subject(word_list, ('noun', 'player')))

    #require error test here























    
