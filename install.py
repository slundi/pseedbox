import app.modules.database as db
from app.modules.strings import encode
import config
import time

db.create_db(True)
time.sleep(1)
#db.db.connect()

u = db.User()
u.username = 'admin'
u.password = encode(config.SECRET_KEY, 'my-password')
u.status = 'admin'
u.save()
#db.db.commit()
#db.db.close()

