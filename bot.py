import datetime
import pytz
from datetime import date,timedelta
from channels import data
from pyrogram import Client, filters

app = Client("account_ses") 
tz = pytz.timezone('Asia/Kolkata')

# check if that msg mime type contains image or video string
check = lambda mt: [i for i in ['image','video'] if i in mt]
# create filter: returns bool
iv = filters.create(lambda _,__,m: any(check(m.document.mime_type)) )

# handler
@app.on_message(filters.chat(data.src_channels) & filters.document & ~iv)
async def func(client, message):
    print(message.document.mime_type) #TODO DLETE before deploy
    await message.copy(data.dest_channel, schedule_date=sch_time())


def sch_time():
    tz = pytz.timezone('Asia/Kolkata')
    now = datetime.datetime.now(tz=tz)
    if now.strftime("%H") in range(0,5):
        return 0
    _add = (24-int(now.strftime("%H")))*60 + (60-int(now.strftime("%M")))
    print(_add)
    delay = datetime.timedelta(minutes=_add)
    print(delay)
    future =  now + delay
    print(future)
    unix_time = future.timestamp()
    return int(unix_time)

app.run()