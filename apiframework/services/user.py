from apiframework.models.dbmanager.user_manager import UserMgr


res = UserMgr.select_all()
print(res)