#coding:utf8
class lex(object):

    def __init__(self):
        pass
        #self.words = stuff.split()    
        #stuff = raw_input('>')
        #words = lex.split()

    def scan(self,stuff):
        
        #stuff = raw_input('>')
        self.words = stuff.split()
        result = []                     #self.result   globe 
        for word in self.words:
            if (word == 'north') or (word =='south') or (word =='east'):
                word_ = ('direction', word)
                #result.append(('direcion', word))
                result.append(word_)
                
            elif  word == 'go' or 'kill' or 'eat': #可以这样是因为巧合：非数值0，所以满足
                #result + = [('verb', %s)] %word
                #result.append(('verb', %s)) %word    error: %  invalid
                result.append(('verb', word))

            
            elif word == 'the' or word == 'in' or word == 'of':
                #result + = ['stop', %s] %word
                result.append(('stop', word))
                
            elif word == 'bear' or word =='princess':
                #result + = ['noun', %s] %word
                result.append(('noun', word))
                
            else:
                try:
                    word = int(word)
                    result.append(('number', word))
                except ValueError:
                    result.append(('error', word))
        return result #must return !!!!!!!!!!

        






















































#coding:utf8
class lex(object):

    def __init__(self):
        pass
        #self.words = stuff.split()    
        #stuff = raw_input('>')
        #words = lex.split()

    def scan(self,stuff):
        
        #stuff = raw_input('>')
        self.words = stuff.split()
        result = []                     #self.result   globe 
        for word in self.words:
            if (word == 'north') or (word =='south') or (word =='east'):
                word_ = ('direction', word)
                #result.append(('direcion', word))
                result.append(word_)
                
            elif  word == 'go' or word == 'kill' or word == 'eat':
                #result + = [('verb', %s)] %word
                #result.append(('verb', %s)) %word    error: %  invalid
                result.append(('verb', word))

            
            elif word == 'the' or word == 'in' or word == 'of':
                #result + = ['stop', %s] %word
                result.append(('stop', word))
                
            elif word == 'bear' or word =='princess':
                #result + = ['noun', %s] %word
                result.append(('noun', word))
                
            else:
                try:
                    word = int(word)
                    result.append(('number', word))
                except ValueError:
                    result.append(('error', word))
        return result #must return !!!!!!!!!!

