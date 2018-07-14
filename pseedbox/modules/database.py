from peewee import *
from datetime import date, datetime
import os

db = SqliteDatabase('pseedbox.db')

def create_db(overwrite = False):
    if overwrite:
        if not os.path.isfile('pseedbox.db'):
            os.remove('pseedbox.db')
        db.create_tables([User, TrackerAccount, Torrent, File])



class User(Model):
    username = CharField(unique=True, max_length = 16)
    password = CharField()
    status = CharField()

    class Meta:
        database = db


class TrackerAccount(Model):
    tracker = CharField()
    username = CharField()
    password = CharField()
    owner = ForeignKeyField(User, backref='accounts')

    class Meta:
        database = db


class Torrent(Model):
    name = CharField()
    tracker =  CharField() #last part of the URL (excludes subdomains)
    category = CharField()
    added = DateTimeField(default=datetime.now)
    deleted = DateTimeField(null = True)
    file_size = BigIntegerField()
    file_count = SmallIntegerField()
    owner = ForeignKeyField(User, backref='torrents')

    class Meta:
        database = db


class File(Model):
    path = CharField()
    size = BigIntegerField()
    completed = BooleanField(default = False)
    mediainfo = TextField() #JSON
    torrent = ForeignKeyField(Torrent, backref='files')

    class Meta:
        database = db


#db.create_tables([User, TrackerAccount, Torrent, File])
#create_db(True)
