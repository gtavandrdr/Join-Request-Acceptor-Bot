import asyncio 
from pyrogram import Client, filters, enums
from config import LOG_CHANNEL, API_ID, API_HASH, NEW_REQ_MODE
from plugins.database import db
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

LOG_TEXT = """<b>#NewUser
    
ID - <code>{}</code>

Nᴀᴍᴇ - {}</b>
"""

# Function to send notification to a designated channel or user
async def send_admin_notification(client, user_id, chat_id, chat_name):
    notification_message = f"🚀 New member approved: [{user_id}](tg://user?id={user_id}) in {chat_name}"
    await client.send_message(LOG_CHANNEL, notification_message)

@Client.on_message(filters.command('start'))
async def start_message(c, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id, m.from_user.first_name)
        await c.send_message(LOG_CHANNEL, LOG_TEXT.format(m.from_user.id, m.from_user.mention))
    await m.reply_photo("https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg",
        caption=f"<b>Hello {m.from_user.mention} 👋\n\nI Am Join Request Acceptor Bot. I Can Accept All Old Pending Join Request.\n\nFor All Pending Join Request Use - /accept</b>",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton('💝 Telegram Channel', url='https://t.me/XclusivePRF')
            ],[
                InlineKeyboardButton("❣️ ᴅᴇᴠᴇʟᴏᴘᴇʀ", url='https://t.me/XclusiveO'),
                InlineKeyboardButton("🤖 ᴜᴘᴅᴀᴛᴇ", url='https://t.me/XclusiveO')
            ]]
        )
    )

@Client.on_chat_join_request(filters.group | filters.channel)
async def approve_new(client, m):
    if NEW_REQ_MODE == False:
        return 
    try:
        if not await db.is_user_exist(m.from_user.id):
            await db.add_user(m.from_user.id, m.from_user.first_name)
        await client.approve_chat_join_request(m.chat.id, m.from_user.id)
        
        # Notify the user directly
        welcome_message = f"**Hello {m.from_user.mention}!\nWelcome To {m.chat.title}\n\n__Powered By : @XclusiveO __**"
        try:
            await client.send_message(m.from_user.id, welcome_message)
            # Send notification after approval
            await send_admin_notification(client, m.from_user.id, m.chat.id, m.chat.title)
        except Exception as e:
            print(f"Error sending welcome message to user: {e}")
        
    except Exception as e:
        print(f"Error during join request approval: {e}")
