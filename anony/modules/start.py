from pyrogram import filters, types

from anony import app, buttons, db


@app.on_message(filters.command(["start"]) & filters.private)
async def f_start(_, m: types.Message):
    caption = f"""
👋 ʜᴇʟʟᴏ {m.from_user.first_name} !  
❍ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ {app.mention} . 🥳  
✦━━━━━━━━━━━━━━━━━━━━━✦  
🛠 ғᴇᴀᴛᴜʀᴇs :  
❍ ɢᴇɴᴇʀᴀᴛᴇ ʏᴏᴜʀ sᴛʀɪɴɢ sᴇssɪᴏɴ ғᴏʀ ᴘʏʀᴏɢʀᴀᴍ  
❍ ɢᴇɴᴇʀᴀᴛᴇ ʏᴏᴜʀ sᴛʀɪɴɢ sᴇssɪᴏɴ ғᴏʀ ᴛᴇʟᴇᴛʜᴏɴ ᴀʟsᴏ  
✦━━━━━━━━━━━━━━━━━━━━━✦  
➤ ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : ˹ᴍɪsᴛᴇʀ ꭙ sᴛᴀʀᴋ˼  
➤ ᴘᴏᴡᴇʀᴇᴅ ʙʏ : ˹ᴄᴀʀᴇʟᴇss ꭙ ᴄᴏᴅᴇʀ˼  
╰─━━━  ✦ ❀ ✦ ❖ ✦ ❀ ✦   ━━━─╯
"""

    await m.reply_photo(
        photo="https://files.catbox.moe/dgelfj.jpg",
        caption=caption,
        
        has_spoiler=True,
        reply_markup=buttons.start_key(),
    )

    await db.add_user(m.from_user.id)
