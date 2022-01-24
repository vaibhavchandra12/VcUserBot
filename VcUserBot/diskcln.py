from pyrogram import Client, emoji, filters
from config import HNDLR, SUDO_USERS
from pyrogram.types import Message
import os

downloads = os.path.realpath("downloads")
raw = os.path.realpath("raw_files")

@Client.on_message(filters.command(["cleardl"], prefixes=f"{HNDLR}") & filters.user(SUDO_USERS))
async def cleardisk(client, m: Message):
    if ls_dir := os.listdir(downloads):
        for file in os.listdir(downloads):
            os.remove(os.path.join(downloads, file))
        await m.reply_text("**Removed All Downloads**")
    else:
        await m.reply_text("**NO FILES FOUND**")
        
        
@Client.on_message(filters.command(["clearjpg"], prefixes=f"{HNDLR}") & filters.user(SUDO_USERS))
async def clearjpg(client, m: Message):
    pth = os.path.realpath(".")
    if ls_dir := os.listdir(pth):
        for dta in os.listdir(pth):
            os.system("rm -rf *.jpg")
        await m.reply_text("**Removed All JPG Files**")
    else:
        await m.reply_text("**NO FILES FOUND**")
