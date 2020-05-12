from telethon import events
from datetime import datetime
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="fuck"))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    await event.edit("Admin has fucked for!")
    end = datetime.now()
    n = (end - start).microseconds / 1000
    await event.edit("Admin is fucked for!\n{}".format(n)ms)
