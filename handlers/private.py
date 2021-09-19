from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""**Hey, 𝗜'𝗔𝗺 𝗔𝗻 𝗔𝗱𝘃𝗮𝗻𝗰𝗲 𝗛𝗶𝗴𝗵 𝗤𝘂𝗮𝗹𝗶𝘁𝘆 𝗦𝘂𝗽𝗲𝗿𝗙𝗮𝘀𝘁 𝗠𝘂𝘀𝗶𝗰 𝗕𝗼𝘁 {bn} 😋
𝗜 𝗖𝗮𝗻 𝗣𝗹𝗮𝘆 𝗠𝘂𝘀𝗶𝗰 𝗜𝗻 𝗬𝗼𝘂𝗿 𝗦𝗲𝘅𝘆 𝗚𝗿𝗼𝘂𝗽'𝘀 𝗩𝗰. 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗱 𝗕𝘆 [𝗖𝗼𝗯𝗿𝗮](https://t.me/xd_lif).

Add me to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🤞 𝗠𝘆 𝗢𝘄𝗻𝗲𝗿 🤞", url="https://t.me/XD_LIF")
                  ],[
                    InlineKeyboardButton(
                        "✨ 𝗦𝘂𝗽𝗽𝗼𝗿𝘁 𝗚𝗿𝗼𝘂𝗽", url="https://t.me/MISTY_SUPORTER"
                    ),
                    InlineKeyboardButton(
                        "⚡ 𝗦𝘂𝗽𝗽𝗼𝗿𝘁 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url="https://t.me/MISTY_SUPORT"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ 𝗔𝗱𝗱 𝗠𝗲 𝗧𝗼 𝗬𝗼𝘂𝗿 𝗚𝗿𝗼𝘂𝗽 ➕", url="https://t.me/JEGroupMusicPlayerBot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Group Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚡ 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url="https://t.me/MISTY_SUPORT")
                ]
            ]
        )
   )


