import datetime
from pathlib import Path
from dbconnection import dbcon
from dbconnection import dbmodel
import datetime
import time

class VisualTestModel:

    def __init__(self, user):
        self._observers = []
        self.user = user
        self.test = None
        self.raw_data = [] #array of tuples [(timestamp, [resultset])]

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def load_text(self):
        path = Path("MuseApp/Assets/shrew_text.txt").resolve()
        with open(path, "r") as file:
            self.reading_text = file.read()
        self.notify_observers()

    def notify_observers(self):
        for x in self._observers:
            x.model_is_changed()

    def save_raw_data_entries(self):
        with dbcon.pg_db.atomic():
            self.test_type = dbmodel.Testtype.select().where(dbmodel.Testtype.type_name == 'visual').get()
            self.test = dbmodel.Test.create(user_id = self.user, 
                                        test_type_id = self.test_type, 
                                        start_time = datetime.datetime.fromtimestamp(time.time())
                                        )
            self.test.save()
            added_test_to_data = list(map(lambda x:x + (self.test,),self.raw_data))
            dbmodel.RawDataEntry.insert_many(added_test_to_data, fields=[
                                                dbmodel.RawDataEntry.raw_time_stamp,
                                                dbmodel.RawDataEntry.tp9,
                                                dbmodel.RawDataEntry.af7,
                                                dbmodel.RawDataEntry.af8,
                                                dbmodel.RawDataEntry.tp10,
                                                dbmodel.RawDataEntry.auxr,
                                                dbmodel.RawDataEntry.test_id,
                                            ]
                                            ).execute()