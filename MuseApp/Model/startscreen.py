from dbconnection import dbcon
from dbconnection import dbmodel

class StartScreenModel:

    def __init__(self):
        self._observers = []
        self.users = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def new_user_name(self, value):
        dbcon.pg_db.connect(reuse_if_open=True)
        dbmodel.User.create(user_name=value)
        dbcon.pg_db.close()
        self.get_all_users()

    def get_all_users(self):
        dbcon.pg_db.connect(reuse_if_open=True)
        self.users = [user.user_name for user in dbmodel.User.select()]
        dbcon.pg_db.close()
        self.notify_observers()

    def notify_observers(self):
        for x in self._observers:
            x.model_is_changed()