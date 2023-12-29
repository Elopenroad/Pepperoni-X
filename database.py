from peewee import *



db = SqliteDatabase('database.db')

class BaseModel(Model):
    class Meta:
        database = db

class Server(BaseModel):
    serverGuild = CharField(max_length=250)
    MessageId = CharField(max_length=250)
    channelId = CharField(max_length=250)
    theme  = CharField(max_length=200)
    notification = BooleanField(default=False)
    channelNotification = CharField(max_length=1000)
    numberNotification = IntegerField()
    
class WeeklyReport(BaseModel):
    saturday = IntegerField()
    sunday = IntegerField()
    monday = IntegerField()
    tuesday = IntegerField()
    wednesday = IntegerField()
    thursday = IntegerField()
    friday = IntegerField()
from database import Server



db.connect()
db.create_tables([Server])