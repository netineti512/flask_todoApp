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

app = Flask(__name__, template_folder="templates")
app.secret_key = 'user'

initheight = 200

#初期表示時
@app.route(common.SLASH)
def init():    
    return render_template(a010common.URL_HTML)  

####### 「A010 ログイン画面」#######################################
# A010
# ログイン画面
@app.route(a010common.A010_ACTION, methods=[common.POST])
def A010Gmn():
    actionId: Final[str] = request.form[a010common.A010_ACTION_ID]
    confirmFlg: Final[str] = request.form[a010common.A010_CONFIRM_FLG]
    
    shainCd: Final[str] = request.form[a010common.A010_SHAINCD]
    
    if confirmFlg == "False":
        return render_template(a010common.URL_HTML, shainCd=shainCd)
        
    if actionId == a010common.A010_LOGIN:
        password: Final[str] = request.form[a010common.A010_PASSWORD]
        
        blErrorFlg: bool = False

        if common.checkBLANK(shainCd):
            blErrorFlg: bool = True
            flash(msg.msg001(a010common.JP_A010_SHAINCD), common.FAILED)
        if common.checkBLANK(password):
            blErrorFlg: bool = True
            flash(msg.msg001(a010common.JP_A010_PASSWORD), common.FAILED)
            
        if blErrorFlg:
            return render_template(a010common.URL_HTML, shainCd=shainCd)
        
        mUserDao: Final[MUserDAO] = MUserDAO()
        
        if mUserDao.blSelectShainInfo(shainCd, password):
            
            return render_template(a011common.URL_HTML, shainCd=shainCd)
        else:
            flash(msg.ERROR_MSG1, common.FAILED)
            return render_template(a010common.URL_HTML, shainCd=shainCd)

####### 「A011 TODO管理画面」#######################################
# A011
# TODO管理画面
@app.route(a011common.A011_ACTION, methods=[common.POST])
def A011():
    actionId: Final[str] = request.form[a011common.A011_ACTION_ID]
    confirmFlg: Final[str] = request.form[a011common.A011_CONFIRM_FLG]
    shainCd: Final[str] = request.form[a011common.A011_HIDDEN_SHAINCD]
    todoNo: Final[str] = request.form[a011common.A011_SELECTED_TODO_NO]
    todoField: Final[str] = request.form[a011common.A011_TODO_FIELD]
    updateTodoField: str = common.BLANK
    
    todoDao: Final[TodoDAO] = TodoDAO()
    
    if confirmFlg == "True" and actionId == a011common.A011_BACK:
        return render_template(a010common.URL_HTML)
    
    if confirmFlg == "False" or actionId == common.BLANK:
        data, kensu = __search(todoDao)
        return render_template(a011common.URL_HTML, shainCd = shainCd, data=data, height= initheight + 50 * kensu, A011TodoField = todoField, A011UpdateTodoField=updateTodoField)
    
    if actionId == a011common.A011_SEARCH:
        todoField = common.BLANK
        pass
    
    if actionId == a011common.A011_INSERT:
        todoDao.insertTodoInfo(shainCd, todoField)
        todoField = common.BLANK
        flash(msg.SUCCESS_MSG1, common.SUCCESS)
    
    if actionId == a011common.A011_UPDATE:
        updateTodoField: str = request.form[a011common.A011_UPDATE_TODO_FIELD]
        todoDao.updateTodoInfo(shainCd, todoNo, updateTodoField)
        updateTodoField = common.BLANK
        flash(msg.SUCCESS_MSG2, common.SUCCESS)
    
    if actionId == a011common.A011_DELETE:
        todoDao.deleteTodoInfo(shainCd, todoNo)
        flash(msg.SUCCESS_MSG3, common.SUCCESS)
    
    data, kensu = __search(todoDao)
    return render_template(a011common.URL_HTML, shainCd = shainCd, data=data, height=initheight + 50 * kensu, A011TodoField = todoField, A011UpdateTodoField=updateTodoField)

def __search(todoDao: TodoDAO):
    todoNo = []
    todo = []
    createDate = []
    updateDate = []
    
    all = todoDao.selectAll()
    
    for i in all:
        todoNo.append(i[todoDao.TODONO])
        todo.append(i[todoDao.TODO])
        createDate.append(i[todoDao.CREATEDATE])
        updateDate.append(i[todoDao.UPDATEDATE])
    
    return zip(todoNo, todo, createDate, updateDate), len(all)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8000)