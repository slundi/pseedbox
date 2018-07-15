from peewee import SqliteDatabase, Model, DoesNotExist
from peewee import CharField, ForeignKeyField, DateTimeField, BigIntegerField, SmallIntegerField, BooleanField, TextField
from datetime import date, datetime
import os
import config
from app.modules import strings

db = SqliteDatabase('pseedbox.db')
db.connect()

def create_db(overwrite = False):
    if overwrite:
        if not os.path.isfile('pseedbox.db'):
            os.remove('pseedbox.db')
        db.create_tables([User, TrackerAccount, Torrent, File])
        db.commit()
        db.close()



class User(Model):
    username = CharField(unique=True, max_length = 16)
    password = CharField()
    status = CharField()

    class Meta:
        database = db
        table_name = 'user'


class TrackerAccount(Model):
    tracker = CharField()
    username = CharField()
    password = CharField()
    owner = ForeignKeyField(User, backref='accounts')

    class Meta:
        database = db
        table_name = 'tracker_account'


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
        table_name = 'torrent'


class File(Model):
    path = CharField()
    size = BigIntegerField()
    completed = BooleanField(default = False)
    mediainfo = TextField() #JSON
    torrent = ForeignKeyField(Torrent, backref='files')

    class Meta:
        database = db
        table_name = 'file'


#db.create_tables([User, TrackerAccount, Torrent, File])
#create_db(True)

def get_user(username, clear_password):
    try:
        return User.get(User.username == username, User.password == strings.encode(config.SECRET_KEY, clear_password))
    except DoesNotExist:
        return None
