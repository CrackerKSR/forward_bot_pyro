# creating filter: from pyrogram import filters
filter1 = filters.create(lambda _, __, m: m.text == "pyrogram")
