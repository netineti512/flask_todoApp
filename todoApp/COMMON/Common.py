import os
import datetime

from typing import Final

class Common:
    def __init__(self) -> None:
        self.SYSTEM: Final[str] = "system"
        
        self.ID: Final[str] = "id"
        self.NAME: Final[str] = "name"
        self.FAILED: Final[str] = "failed"
        self.SUCCESS: Final[str] = "success"
        
        self.STR_TRUE: Final[str] = "True"
        self.STR_FALSE: Final[str] = "False"
        
        self.POST: Final[str] = "POST"
        self.GET: Final[str] = "GET"
        
        self.BLANK: Final[str] = ""
        
        self.INT_ZERO: Final[int] = 0
        self.INT_ONE: Final[int] = 1
        self.INT_TWO: Final[int] = 2
        self.INT_THREE: Final[int] = 3
        self.INT_FOUR: Final[int] = 4
        self.INT_NINE: Final[int] = 9
        self.INT_TEN: Final[int] = 10

        self.TABLE_HEIGHT: Final[int] = 200

        self.MIN_SIZE: Final[int] = 7
        self.MAX_SIZE: Final[int] = 17
        
        self.SLASH: Final[str] = "/"
        
        self.GMN_ID: Final[str] = "gmnId"
        self.USER_ID: Final[str] = "USER_ID"
        self.DICT_TORIHIKISAKI_INFO: Final[str] =  "dictTorihikisakiInfo"
        self.HIDDEN_SHAIN_CD: Final[str] = "hiddenShainCd"
        self.DATAS: Final[str] = "datas"
        
        self.SYMBOL_LIST: Final[list] = ['¥¥', '!', '¥"', '¥', "#", "$", "&", "¥'", "//", "/", "(", ")", "-", "=", "~", "^", "|", "[", "]", "@", "`", ";", "+", ":", "*", "}", "{", ",", "<", ".", ">", "?", "_", "", " ", "　", "！", "”", "＃", "＄", "％", "＆", "’", "（", "）", "＝", "ー", "＾", "〜", "＼", "｜", "＠", "｀", "「", "『", "」", "』", "；", "＋", "：", "：", "、", "＜", "。", "＞", "・", "？", "＿", "_", "\n", "\t"]
    
    def checkBLANK(self, param: str) -> bool:
        return param == self.BLANK
    
    def checkStrSize(self, param: str, minSize: int, maxSize: int) -> bool:
        return len(param) > maxSize or len(param) < minSize
    
    def checkEqual(self, param1: str, param2: str) -> bool:
        return param1 == param2
    
    def checkSymbol(self, param: str) -> bool:
        for p in param:
            if p in self.SYMBOL_LIST:
                return True
        return False
    
    def writeDaoLog(self, sql: str) -> None:
        now = datetime.date.today()
        
        filename: str = "./log/" + str(now.year) + str(now.month) + str(now.day) + "Dao.txt"
        date: str = str(datetime.datetime.now().time()) + "：" + sql
        
        if os.path.isfile(filename):
            with open(filename, mode='a') as f:
                f.write("\n" + date)
        else:
            with open(filename, mode='w') as f:
                f.write(date)