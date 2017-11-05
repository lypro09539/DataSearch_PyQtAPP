# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')


from PyQt4 import QtCore, QtGui
import pandas as pd
import time
from sqlalchemy.orm import sessionmaker

class directSearch(QtCore.QThread):

    finishSignal = QtCore.pyqtSignal(list)

    def __init__(self,engine,flag,reg,fund_names_list_,sql,parent=None):
        super(directSearch,self).__init__(parent)
        self.engine =engine
        self.fund_names_list_ = fund_names_list_
        self.sql = sql
        self.flag = flag
        self.reg = reg

    def run(self):
        if not self.flag:
            self.finishSignal.emit([-1])
            return
        if not self.fund_names_list_:
            #self.sql_box.setText('暂不支持无基金名查询')
            self.finishSignal.emit([0,'暂不支持无基金名查询'])
            return

        #print self.sql

        self.DB_Session = sessionmaker(bind=self.engine)
        self.session = self.DB_Session()
        ress = self.session.execute(self.sql).fetchall()

        #print ress
        resdict = {}
        for i in self.fund_names_list_:
            name = i.replace('%', '').replace(' or', '').replace(' fund_name like ', ''). \
                                                                replace('\'', '').replace(' fund_name =', '')
            j = 0
            for res in ress:
                #if self.checkBox.isChecked():
                if self.reg:#'完全匹配'
                    if '{}'.format(name)==res[1].encode('utf8'):
                        j += 1
                        #print j
                else:#'模糊'
                    if '{}'.format(name) in res[1].encode('utf8'):
                        j += 1
                        #print j

            resdict[name]=j
        #print resdict
        print 'done'
        self.finishSignal.emit([1, resdict])




class ac_export(QtCore.QThread):

    finishSignal = QtCore.pyqtSignal(list)
    def __init__(self,form_name, engine, flag, reg, fund_names_list_, sql, parent=None):
        super(ac_export, self).__init__(parent)
        self.engine = engine
        self.fund_names_list_ = fund_names_list_
        self.sql = sql
        self.flag = flag
        self.reg = reg
        self.form_name = form_name
    def run(self):
        try:
            df = pd.read_sql(sql="SELECT * FROM {} limit 500".format(self.form_name),con=self.engine)
            #print df
            self.finishSignal.emit([1, df])
        except Exception,e:
            self.finishSignal.emit([0,e])

