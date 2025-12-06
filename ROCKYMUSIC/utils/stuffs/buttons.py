# ===========================================================
# ©️ 2025-26 All Rights Reserved by Team Rocky (Im-Notcoder) 🚀
# 
# This source code is under MIT License 📜
# ❌ Unauthorized forking, importing, or using this code
#    without giving proper credit will result in legal action ⚠️
# 
# 📩 DM for permission : @MrRockytg
# ===========================================================

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 
import config

class BUTTONS(object):
    ABUTTON = [
    [
        InlineKeyboardButton("˹ sυᴘᴘσʀᴛ ˼", url="https://t.me/Rockyxsupport"),
        InlineKeyboardButton("˹ υᴘᴅᴧᴛєs ˼", url="https://t.me/Rockyxupdate")
    ],
    [
        InlineKeyboardButton(text="˹ ❍ᴡηєʀ ˼", user_id=config.OWNER_ID),
        InlineKeyboardButton("• ʙᴧᴄᴋ •", callback_data="settingsback_helper")
    ]
]

    INFO_BUTTON = [
    [
        InlineKeyboardButton("˹ ʀєᴘσ ˼", callback_data="gib_source"),
        InlineKeyboardButton("˹ ʏᴛ-ᴀᴘɪ ˼", callback_data="bot_info_data"),
        InlineKeyboardButton("˹ ʟᴧηɢᴜᴧɢє ˼", callback_data="LG"),
    ],
    [
        
        InlineKeyboardButton("˹ ᴅᴘ sᴛʏʟɪsʜ  ˼", url="https://t.me/DpStylish"),
        InlineKeyboardButton("• ʙᴧᴄᴋ •", callback_data="settingsback_helper"),
    ]
    ]
    


    INFO_NEW = [
    [
        InlineKeyboardButton("• ʙᴧᴄᴋ •", callback_data="settings_back_helper"),
        InlineKeyboardButton("• sᴛʏʟɪsʜ ғᴏɴᴛ •", url="https://t.me/NameBioFont")
    ],
    ]
    
    

# ===========================================================
# ©️ 2025-26 All Rights Reserved by Team Rocky (Im-Notcoder) 😎
# 
# 🧑‍💻 Developer : t.me/mrrockytg
# 🔗 Source link : t.me/rockyxsupport
# 📢 Telegram channel : t.me/rockyxupdate
# ===========================================================
