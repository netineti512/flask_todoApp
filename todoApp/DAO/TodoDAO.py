import sqlite3
import copy
import datetime

from typing import Final

from COMMON.Common import Common

common: Final[Common] = Common()

class TodoDAO:
    
    def __init__(self) -> None:
        self.__dbname: Final[str] = './DB/Todo.db'
        
        self.TABLENAME: Final[str] = "Todo"
        
        self.SHAINCD: Final[str] = "shainCd"
        self.TODONO: Final[str] = "todoNo"
        self.TODO: Final[str] = "todo"
        self.DELETEFLG: Final[str] = "deleteFlg"
        self.CREATEDATE: Final[str] = "createDate"
        self.CREATEUSER: Final[str] = "createUser"
        self.UPDATEDATE: Final[str] = "updateDate"
        self.UPDATEUSER: Final[str] = "updateUser"

        self.DELETEFLG_0: Final[str] = "0"
        self.DELETEFLG_1: Final[str] = "1"
        
        self.dic: Final[dict] = {
                    f"{self.SHAINCD}": common.BLANK,
                    f"{self.TODONO}": common.BLANK,
                    f"{self.TODO}": common.BLANK,
                    f"{self.DELETEFLG}": common.BLANK,
                    f"{self.CREATEDATE}": common.BLANK,
                    f"{self.CREATEUSER}": common.BLANK,
                    f"{self.UPDATEDATE}": common.BLANK,
                    f"{self.UPDATEUSER}": common.BLANK
                   }
        
    def createTodoTable(self) -> None:
        today = datetime.datetime.now()
        conn = sqlite3.connect(self.__dbname)
        
        cur = conn.cursor()
        
        sql: str = f'CREATE TABLE {self.TABLENAME} ( \
                {self.SHAINCD} STRING , \
                {self.TODONO} INTEGER, \
                {self.TODO} STRING, \
                {self.DELETEFLG} STRING, \
                {self.CREATEDATE} STRING, \
                {self.CREATEUSER} STRING, \
                {self.UPDATEDATE} STRING, \
                {self.UPDATEUSER} STRING, \
                PRIMARY KEY ({self.SHAINCD}, {self.TODONO}))'
                
        cur.execute(sql)
        
        sqlList: list = [f'INSERT INTO {self.TABLENAME} values("admin", 1, "文書作成", "0", "{str(today)}", "admin", "", "")',
                   f'INSERT INTO {self.TABLENAME} values("admin", 2, "プログラミング作業", "0", "{str(today)}", "admin", "", "")',
                   f'INSERT INTO {self.TABLENAME} values("admin", 3,  "テーブルふき", "0", "{str(today)}", "admin", "", "")',
                   f'INSERT INTO {self.TABLENAME} values("admin", 4, "車洗い", "0", "{str(today)}", "admin", "", "")',
                   f'INSERT INTO {self.TABLENAME} values("admin", 5, "買い物", "0", "{str(today)}", "admin", "", "")',
                   f'INSERT INTO {self.TABLENAME} values("admin", 6, "就寝", "0", "{str(today)}", "admin", "", "")']
        
        for sql in sqlList:
            cur.execute(sql)
            common.writeDaoLog(sql)
            
        conn.commit()
        
        cur.close()
        conn.close()
        
        common.writeDaoLog(sql)
        
        
    def selectTodo(self) -> None:
        conn = sqlite3.connect(self.__dbname)
        cur = conn.cursor()
        
        sql: str = f'SELECT * FROM {self.TABLENAME} WHERE deleteFlg = 0'

        cur.execute(sql)

        for data in cur.fetchall():
            print(data)

        cur.close()
        conn.close()
        
        common.writeDaoLog(sql)
    
    def selectAll(self) -> list:
        selectAll: list = []
        sql: str = f"SELECT * FROM {self.TABLENAME} WHERE deleteFlg = 0"
        
        conn = sqlite3.connect(self.__dbname)
        cur = conn.cursor()
        cur.execute(sql)
        
        for low in sorted(cur.fetchall()):
            dic = copy.copy(self.dic)
            for i in range(len(low)):
                dic[list(dic)[i]] = low[i]
            selectAll.append(dic)
        
        cur.close()
        conn.close()
        
        common.writeDaoLog(sql)
        
        return selectAll
    
    def selectAllKensu(self, shainCd: str) -> int:
        conn = sqlite3.connect(self.__dbname)
        cur = conn.cursor()
        
        sql: str = f"SELECT COUNT(*) FROM {self.TABLENAME} WHERE shainCd = '{shainCd}'"

        cur.execute(sql)

        kensu = cur.fetchall()

        cur.close()
        conn.close()
        
        common.writeDaoLog(sql)
        
        return kensu[0][0]
    
    def insertTodoInfo(self, shainCd: str, todo: str) -> None:
        today = datetime.datetime.now()
        conn = sqlite3.connect(self.__dbname)
        
        kensu = self.selectAllKensu(shainCd) + 1
        
        cur = conn.cursor()
        
        sql: str = f'INSERT INTO {self.TABLENAME} values("{shainCd}", {kensu}, "{todo}", "0", "{str(today)}", "{shainCd}", "", "")'
        
        cur.execute(sql)
        common.writeDaoLog(sql)
            
        conn.commit()
        
        cur.close()
        conn.close()
        
        common.writeDaoLog(sql)
        
    def updateTodoInfo(self, shainCd: str, todoNo: int, todo: str) -> None:
        today = datetime.datetime.now()
        conn = sqlite3.connect(self.__dbname)
        
        cur = conn.cursor()
        
        sql: str = f'UPDATE {self.TABLENAME} SET todo = "{todo}", updateDate = "{today}", updateUser = "{shainCd}" WHERE shainCd = "{shainCd}" AND todoNo = {todoNo}'
        
        cur.execute(sql)
        common.writeDaoLog(sql)
            
        conn.commit()
        
        cur.close()
        conn.close()
        
        common.writeDaoLog(sql)
        
    def updatedeleteFlg(self) -> None:
        today = datetime.datetime.now()
        conn = sqlite3.connect(self.__dbname)
        
        cur = conn.cursor()
        
        sql: str = f'UPDATE {self.TABLENAME} SET deleteFlg = "0", updateDate = "{today}", updateUser = "system"'
        
        cur.execute(sql)
        common.writeDaoLog(sql)
            
        conn.commit()
        
        cur.close()
        conn.close()
        
        common.writeDaoLog(sql)
        
    def deleteTodoInfo(self, shainCd: str, todoNo: str) -> None:
        today = datetime.datetime.now()
        conn = sqlite3.connect(self.__dbname)
        
        cur = conn.cursor()
        
        sql: str = f'UPDATE {self.TABLENAME} SET deleteFlg = "1", updateDate = "{today}", updateUser = "{shainCd}" WHERE shainCd = "{shainCd}" AND todoNo = {todoNo}'
        
        cur.execute(sql)
        common.writeDaoLog(sql)
            
        conn.commit()
        
        cur.close()
        conn.close()
        
        common.writeDaoLog(sql)