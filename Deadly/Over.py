from OpUstad import UstaD, UstaD2, UstaD3, UstaD4, UstaD5, UstaD6, UstaD7, UstaD8, UstaD9, UstaD10, SUDO_USERS

from telethon import events
import os
import random
import sys

SMEX_USERS = []
for x in SUDO_USERS:
    SMEX_USERS.append(x)

if UstaD:
    @UstaD.on(events.NewMessage(pattern="/over"))
    async def restart(e):
        if e.sender_id in SMEX_USERS:
             text = " ☆𝐂𝐇𝐀𝐊𝐑𝐀 𝐎𝐕𝐄𝐑☆\n𝒀𝑶𝑼𝑹 𝑳𝑰𝑴𝑰𝑻 𝑰𝑺 𝑶𝑽𝑬𝑹"
             await e.reply(text, parse_mode=None, link_preview=None)
             try:
                await UstaD.disconnect()
             except Exception:
                pass
             os.execl(sys.executable, sys.executable, *sys.argv)
             quit()

else:
   pass
 
