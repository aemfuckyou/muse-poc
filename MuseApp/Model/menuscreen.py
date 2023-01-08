from dbconnection import dbcon
from dbconnection import dbmodel

class MenuScreenModel:

    def __init__(self, username):
        self._observers = []
        dbcon.pg_db.connect(reuse_if_open=True)
        self.user = dbmodel.User.select().where(dbmodel.User.user_name==username).get()
        dbcon.pg_db.close()

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for x in self._observers:
            x.model_is_changed()