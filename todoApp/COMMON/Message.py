from typing import Final

class Message:
    def __init__(self):
        self.SUCCESS_MSG1: Final[str] = "todoが追加されました。"
        self.SUCCESS_MSG2: Final[str] = "todoが更新されました。"
        self.SUCCESS_MSG3: Final[str] = "todoが削除されました。"
        
        self.ERROR_MSG1: Final[str] = "ログインに失敗しました。社員コードもしくはパスワードが間違っています。"
        self.ERROR_MSG2: Final[str] = "パスワードの変更に失敗しました。社員コードもしくは現在のパスワードが間違っています。"
    
    def msg001(self, param: str) -> str:
        return f"{param}を入力してください。"
    
    def msg002(self, param1: str, param2: str) -> str:
        return f"「{param1}」と「{param2}」が等しいです。"
    
    def msg003(self, param: str, minSize: int, maxSize: int) -> str:
        return f"「{param}」の文字数を{minSize}文字以上{maxSize}文字以下にしてください。"
    
    def msg004(self, param: str) -> str:
        return f"「{param}」に記号が含まれています。"

    def msg005(self, param: str) -> str:
        return f"「{param}」は既に使用されています。"