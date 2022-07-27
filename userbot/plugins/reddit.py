"""Get a Image Post from Reddit"""
# 👍 https://github.com/D3vd for his awesome API
#
# Copyright (C) 2020 BY - GitHub.com/code-rgb [TG - @DeletedUser420]
# All rights reserved.

import re

import requests
from telethon.errors import MessageNotModifiedError

from userbot import catub

from ..core.logger import logging
from ..core.managers import edit_delete
from ..helpers.functions import age_verification, unsavegif
from ..helpers.utils import reply_id
from . import BOTLOG, BOTLOG_CHATID

LOGS = logging.getLogger(__name__)
API = "https://meme-api.herokuapp.com/gimme"

plugin_category = "misc"

REDDIT_REGEX = r"(?:^|\s+)(\/?r\/\S+)"


@catub.cat_cmd(
    pattern="re(?:\s|$)([\s\S]*)",
    command=("re", plugin_category),
    info={
        "header": "Get a random reddit post.",
        "usage": "{tr}re <subreddit>",
        "examples": "{tr}re dankmemes",
    },
)
async def reddit_fetch(event):
    """Random reddit post"""
    reply_to = await reply_id(event)
    sub_r = event.pattern_match.group(1)
    subreddit_api = f"{API}/{sub_r}" if sub_r else API
    try:
        cn = requests.get(subreddit_api)
        r = cn.json()
    except ValueError:
        return await edit_delete(event, "Value error!.")
    if "code" in r:
        if BOTLOG:
            code = r["code"]
            code_message = r["message"]
            await event.client.send_message(
                BOTLOG_CHATID, f"**Error Code: {code}**\n`{code_message}`"
            )
            await edit_delete(event, f"**Error Code: {code}**\n`{code_message}`")
    else:
        if "url" not in r:
            return await edit_delete(
                event,
                "Coudn't Find a post with Image, Please Try Again",
            )
        postlink = r["postLink"]
        subreddit = r["subreddit"]
        title = r["title"]
        media_url = r["url"]
        author = r["author"]
        upvote = r["ups"]
        captionx = f"**{title}**\n"
        captionx += f"`Posted by u/{author}`\n"
        captionx += f"↕️ `{upvote}`\n"
        if r["spoiler"]:
            captionx += "⚠️ Post marked as SPOILER\n"
        if r["nsfw"]:
            captionx += "🔞 Post marked Adult \n"

            if await age_verification(event, reply_to):
                return

        await event.delete()
        captionx += f"Source: [r/{subreddit}]({postlink})"
        sandy = await event.client.send_file(
            event.chat_id, media_url, caption=captionx, reply_to=reply_to
        )
        if media_url.endswith(".gif"):
            await unsavegif(event, sandy)


@catub.cat_cmd(outgoing=True)
async def subreddit(e):
    message = e.text
    matches = re.findall(REDDIT_REGEX, message)
    if matches:
        print("REDDIT")
        for match in matches:
            sub_name = match.split("/")[-1]
            link = f"[{match}](https://reddit.com/r/{sub_name})"
            message = e.text.replace(match, link)

        try:
            await e.edit(message)
        except MessageNotModifiedError:
            pass
