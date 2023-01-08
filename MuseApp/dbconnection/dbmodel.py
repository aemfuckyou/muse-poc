from peewee import *
from .dbcon import pg_db

class BaseModel(Model):
    class Meta:
        database = pg_db
        schema = 'muse'
        


class User(BaseModel):
    user_id = AutoField(primary_key=True)
    user_name = TextField(null=False)
    class Meta:
        db_table='user_data'

class Testtype(BaseModel):
    type_id = IntegerField(primary_key=True)
    type_name = TextField(null=False)
    class Meta:
        db_table='test_type'

class Test(BaseModel):
    test_id = AutoField(primary_key=True)
    user_id = ForeignKeyField(User, backref='tests')
    test_type_id = ForeignKeyField(Testtype)
    start_time = DateTimeField(null=False)
    end_time = DateTimeField()
    interrupt = BooleanField()
    class Meta:
        db_table='tests'

class RawDataEntry(BaseModel):
    raw_data_id = AutoField(primary_key=True)
    test_id = ForeignKeyField(Test, backref='raw_data_entries')
    raw_time_stamp = DateTimeField(null=False)
    tp9 = FloatField(null=False)
    af7 = FloatField(null=False)
    af8 = FloatField(null=False)
    tp10 = FloatField(null=False)
    auxr = FloatField(null=False)
    class Meta:
        db_table='raw_data'
