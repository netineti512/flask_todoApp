import datetime
import csv

from flask import Flask,render_template, request, session, flash, Blueprint
from typing import Final

from COMMON.Common import Common
from COMMON.Message import Message
from COMMON.A010Common import A010Common
from COMMON.A011Common import A011Common
from DAO.MUserDAO import MUserDAO
from DAO.TodoDAO import TodoDAO

common: Final[Common] = Common()
msg: Final[Message] = Message()

a010common: Final[A010Common] = A010Common()
a011common: Final[A011Common] = A011Common()

muserDao: Final[MUserDAO] = MUserDAO()
todoDao: Final[TodoDAO] = TodoDAO()

todoDao.updatedeleteFlg()