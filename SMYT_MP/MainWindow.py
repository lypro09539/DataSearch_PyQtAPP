# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from multiprocessing import Process,Manager,Pool
import multiprocessing
import pandas as pd

from ui import Ui_MainWindow

from PyQt4 import QtCore, QtGui
from sqlalchemy import create_engine
#from sqlalchemy.orm import sessionmaker
import re
import time

MYSQL_HOST_BASE = "******"
MYSQL_POST_BASE = "******"
MYSQL_USER_BASE = "******"
MYSQL_PASSWD_BASE = "******"

#类方法不能被多进程调用
def process_run(q, lock, fund_names_list_,typestandard_code,df):
    print '调用函数'
    #try:
    if typestandard_code:
        df = df.loc[df['typestandard_code']==int(typestandard_code)].copy()

    #print df
    #print '上面是仅筛选分类代码后结果'
    df_ = pd.DataFrame({},columns=df.columns.tolist())
    for name in fund_names_list_:
        #不合理，应该用格式化前的数据
        name = name.replace('%', '').replace(' or', '').replace(' fund_name like ', ''). \
            replace('\'', '').replace(' fund_name =', '')
        #print name
        #self.df['reg'] = self.df['fund_name'].map(lambda x:True if name in str(x) else False)
        df_byname = df.loc[df['fund_name'].map(lambda x:True if str(name) in str(x) else False)].copy()
        df_byname['name_you_searched']=''
        idxs = df_byname.index
        idxs = idxs.tolist()

        if idxs:
            df_byname.ix[idxs[0], 'name_you_searched'] = str(name)
        else:
                #空的dataframe添加一行空白数据
            datadict ={}
            for key in df_byname.columns.tolist():
                datadict[key]=''
            new = pd.DataFrame(datadict,index=[0])
            df_byname = df_byname.append(new,ignore_index=True)
            df_byname['name_you_searched'] = str(name)

        df_ = pd.concat([df_,df_byname])

    lock.acquire()
    q.put(df_)
    lock.release()




class MyWindow(Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow,self).__init__(parent)
        self.setupUi(self)
        self.MYSQL_DBNAME_BASE = 'base'
        self.engine_base = create_engine( \
            'mysql+mysqldb://{}:{}@{}:{}/{}'.format(MYSQL_USER_BASE, MYSQL_PASSWD_BASE, MYSQL_HOST_BASE, \
                                                    MYSQL_POST_BASE, self.MYSQL_DBNAME_BASE),
            connect_args={'charset': 'utf8'})
        #self.DB_Session_Base = sessionmaker(bind=self.engine_base)
        #self.session = self.DB_Session_Base()
        print '连接初始化........'
        self.pushButton.clicked.connect(self.generate_sql)
        self.pushButton_2.clicked.connect(self.copy_sql)
        self.search.clicked.connect(self.search_)
        self.activate_export.clicked.connect(self.read_all)
        self.form_name.textChanged.connect(self.creat_engine_again)
        self.export_excel.setDisabled(True)
        self.export_excel.clicked.connect(self.export_to_excel)


    def generate_sql(self):
        self.pushButton.setDisabled(True)
        form_name = self.form_name.text()
        sql_form_name = 'SELECT * FROM {} WHERE'.format(form_name)

        fund_names = self.fund_names_box.toPlainText()
        fund_names = str(fund_names)
        if re.findall(r'\%',fund_names) or re.findall(r';',fund_names):
            self.sql_box.setText('不要使用非法符号')
            self.pushButton.setDisabled(False)
            return 0

        fund_names = fund_names.split('\n')#remained to figure out,and \r\n is wrong
        global fund_names_list_
        fund_names_list = filter(lambda x:x.strip()!='',fund_names)
        fund_names_list_ = fund_names_list

        for i in range(len(fund_names_list)):
            if self.checkBox_2.isChecked():
                fund_names_list[i] =' fund_name like ' +'\'%' +  fund_names_list[i] + '%\'' +' '+'or'
            else:
                fund_names_list[i] = ' fund_name =' + '\'' + fund_names_list[i] + '\'' + ' ' + 'or'
        if fund_names_list:
            fund_names_list[-1] = fund_names_list[-1][:-3]
            fund_names_sql = ''.join(fund_names_list)
            sql_fund_names = '(' +fund_names_sql +')'
        else:
            sql_fund_names = ''

        other_requires = str(self.other_requires.toPlainText())
        other_requires = other_requires.split('\n')
        other_requires_list = filter(lambda x:x.strip()!='',other_requires)
        for i in range(len(other_requires_list)):
            other_requires_list[i] =' and '  +  other_requires_list[i]

        global sql_other_requires
        if other_requires_list:
            other_requires_sql = ''.join(other_requires_list)
            sql_other_requires = other_requires_sql
        else:
            sql_other_requires = ''
        global sql
        if not sql_fund_names and not sql_other_requires:
            sql = '无搜索条件'
        elif not sql_fund_names and sql_other_requires:
            sql_other_requires = sql_other_requires[4::]
            sql = sql_form_name + sql_fund_names + sql_other_requires
        else:
            sql = sql_form_name + sql_fund_names +sql_other_requires

        if self.checkBox_2.isChecked() and self.checkBox.isChecked()or (not self.checkBox_2.isChecked() and not self.checkBox.isChecked()):
            sql = '左方请选中单一匹配方式'
        if not self.checkBox_2.isChecked() and self.checkBox.isChecked():
            sql = sql.replace('%','')

        self.sql_box.setText(sql)
        self.pushButton.setDisabled(False)
        return 1



    def  search_(self):
        self.search.setDisabled(True)
        self.tableWidget.clearContents()
        self.generate_sql()
        flag = 1
        if not self.generate_sql() or sql.replace('SELECT', '') == sql:
            flag = 0
        reg = 0
        if self.checkBox.isChecked():
            reg = 1

        from mythreads import directSearch
        self.searchThread = directSearch(engine=self.engine_base,flag=flag,reg=reg,fund_names_list_=fund_names_list_,sql=sql)
        self.searchThread.finishSignal.connect(self.search_show)
        self.searchThread.start()

    def search_show(self,reslist):
        if not reslist[0]+1:
            self.search.setEnabled(True)
            return
        elif not reslist[0]:
            self.sql_box.setText(reslist[1])
            self.search.setEnabled(True)
            return

        else:
            k=0
            infos = reslist[1]
            for name in infos.keys():
                nameItem = QtGui.QTableWidgetItem(name)
                self.tableWidget.setItem(k, 0, nameItem)
                countItem = QtGui.QTableWidgetItem(str(infos[name]))
                self.tableWidget.setItem(k, 1, countItem)
                k += 1
            print 'done'
            self.search.setEnabled(True)



    def read_all(self):
        self.activate_export.setDisabled(True)
        self.generate_sql()
        flag = 1
        if not self.generate_sql() or sql.replace('SELECT', '') == sql:
            flag = 0
        reg = 0
        if self.checkBox.isChecked():
            reg = 1

        form_name = self.form_name.text()

        from mythreads import ac_export
        self.acThread = ac_export(form_name=form_name,engine=self.engine_base,flag=flag,\
                                  reg=reg,fund_names_list_=fund_names_list_,sql=sql)
        self.acThread.finishSignal.connect(self.export_show)
        self.acThread.start()
        self.sql_box.setText('正在启用导出功能，请耐心等候......')

    def export_show(self,reslist):

        if reslist[0]:
            self.export_excel.setEnabled(True)
            self.sql_box.setText('导出功能已启用')
            global data
            data = reslist[1]
            return
        else:
            self.sql_box.setText(reslist[1])
            self.activate_export.setEnabled(True)
            return

    def export_to_excel(self):
        print type(self)
        self.sql_box.setText('正在导出，请耐心等候')
        #print df
        self.export_excel.setDisabled(True)
        self.generate_sql()
        if not self.generate_sql() or sql.replace('SELECT', '') == sql:
            flag = 0
        reg = 0
        if self.checkBox.isChecked():
            reg = 1

        typestandard_code = str(self.other_requires.toPlainText())
        typestandard_code_ = ''
        if typestandard_code:
            for code in typestandard_code:
                if code.isdigit():
                    typestandard_code_ = code
                    break
                else:
                    continue
            if not typestandard_code_:
                self.sql_box.setText('请正确设置typestandard_code')
                self.export_excel.setEnabled(True)
                return
        if not fund_names_list_:
            self.sql_box.setText('暂不支持无基金名查询')
            self.export_excel.setEnabled(True)
            return
        df = data
        size=len(fund_names_list_)/4
        manage=Manager()
        q=manage.Queue()
        lock=manage.Lock()
        p=multiprocessing.Pool(processes=4)
        if size<10:
            print '数据量较小，单进程执行'
            p.apply_async(process_run,(q, lock, fund_names_list_, typestandard_code_, df, ))
            p.close()
            p.join()

        else:
            print '数据量大，多进程执行'
            p.apply_async(process_run,(q,lock, fund_names_list_[0:size], typestandard_code_, df))
            p.apply_async(process_run,(q,lock, fund_names_list_[size:2*size], typestandard_code_, df))
            p.apply_async(process_run, (q,lock, fund_names_list_[2*size:3*size], typestandard_code_, df))
            p.apply_async(process_run, (q,lock, fund_names_list_[3*size::], typestandard_code_, df))
            p.close()
            p.join()

        df = q.get(block = False)
        for _ in range(3):
            if not q.empty():
                df = pd.concat([df, q.get(block = False)])
            else:
                break
        try:
            err=''
            # move the column to head of list using index, pop and insert
            cols = list(df)
            cols.insert(0, cols.pop(cols.index('fund_name')))
            cols.insert(0, cols.pop(cols.index('name_you_searched')))
            df = df.ix[:, cols]
            df.to_excel('C://hehe_{}.xlsx'.format(time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))),sheet_name='Sheet1')
        except Exception,e:
            err = e
        if not err:
            self.sql_box.setText('导出成功，位于C盘根目录下')
        else:
            self.sql_box.setText(str(err))
        self.export_excel.setEnabled(True)


    def process_run_class(self,q, lock, fund_names_list_, typestandard_code, df):
        print '调用函数'
        # try:
        if typestandard_code:
            df = df.loc[df['typestandard_code'] == int(typestandard_code)].copy()

        # print df
        # print '上面是仅筛选分类代码后结果'
        df_ = pd.DataFrame({}, columns=df.columns.tolist())
        for name in fund_names_list_:
            # 不合理，应该用格式化前的数据
            name = name.replace('%', '').replace(' or', '').replace(' fund_name like ', ''). \
                replace('\'', '').replace(' fund_name =', '')
            # print name
            # self.df['reg'] = self.df['fund_name'].map(lambda x:True if name in str(x) else False)
            df_byname = df.loc[df['fund_name'].map(lambda x: True if str(name) in str(x) else False)].copy()
            df_byname['name_you_searched'] = ''
            idxs = df_byname.index
            idxs = idxs.tolist()

            if idxs:
                df_byname.ix[idxs[0], 'name_you_searched'] = str(name)
            else:
                # 空的dataframe添加一行空白数据
                datadict = {}
                for key in df_byname.columns.tolist():
                    datadict[key] = ''
                new = pd.DataFrame(datadict, index=[0])
                df_byname = df_byname.append(new, ignore_index=True)
                df_byname['name_you_searched'] = str(name)

            df_ = pd.concat([df_, df_byname])

        lock.acquire()
        q.put(df_)
        lock.release()

    def creat_engine_again(self):
        form_name = self.form_name.text()
        dbname = re.search(r'(.+?)\.',str(form_name)).group(1)
        self.MYSQL_DBNAME_BASE = '{}'.format(dbname)
        self.engine_base = create_engine( \
            'mysql+mysqldb://{}:{}@{}:{}/{}'.format(MYSQL_USER_BASE, MYSQL_PASSWD_BASE, MYSQL_HOST_BASE, \
                                                    MYSQL_POST_BASE, self.MYSQL_DBNAME_BASE),
            connect_args={'charset': 'utf8'})
        #self.DB_Session_Base = sessionmaker(bind=self.engine_base)
        #self.session = self.DB_Session_Base()

    def copy_sql(self):
        sql = self.sql_box.toPlainText()
        QtGui.QApplication.clipboard().setText(sql)




if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    #新建类对象
    window = MyWindow()
    #显示类对象
    window.show()
    sys.exit(app.exec_())