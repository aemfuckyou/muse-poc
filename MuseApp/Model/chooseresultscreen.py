
from dbconnection import dbmodel, dbcon


class ChooseResultModel:

    def __init__(self, user):
        self._observers = []
        self.user = user
        dbcon.pg_db.connect(reuse_if_open=True)
        self.tests = list(dbmodel.Test.select().where(dbmodel.Test.user_id==user).execute())
        dbcon.pg_db.close()
    
    def get_all_tests(self):
        self.notify_observers()

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for x in self._observers:
            x.model_is_changed()