# Made by @o_s_h_o_r_a_j
# Change credit and you gay.
from userbot import catub

from ..core.managers import edit_delete
from ..helpers.functions import deEmojify, hide_inlinebot
from ..helpers.utils import reply_id

plugin_category = "extra"


@catub.cat_cmd(
    pattern="ilyrics ?(.*)",
    command=("ilyrics", plugin_category),
    info={
        "header": "Sends lyrics [inline] of a song along with Spotify & Youtube links\n•Add artist name if you getting different lyrics\n•you can also type a line of a song to search",
        "usage": [
            "{tr}ilyrics <song name>",
            "{tr}ilyrics <song name - artist>",
        ],
    },
)
async def GayIfUChangeCredit(event):
    "Lyrics Time"
    if event.fwd_from:
        return
    bot = "@ilyricsbot"
    song = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if not song:
        return await edit_delete(event, "`Gimme a song u baka!`", 15)
    await event.delete()
    results = await event.client.inline_query(bot, song)
    await results[0].click(event.chat_id, reply_to=reply_to_id)


@catub.cat_cmd(
    pattern="isong ?(.*)",
    command=("isong", plugin_category),
    info={
        "header": "Kinda inline music downloader",
        "usage": [
            "{tr}isong <song name>",
        ],
    },
)
async def music(event):
    "Download song through @Deezermusicbot"
    if event.fwd_from:
        return
    bot = "@deezermusicbot"
    music = event.pattern_match.group(1)
    music = deEmojify(music)
    reply_to_id = await reply_id(event)
    if not music:
        return await edit_delete(
            event, "`What should I download? Give a song name`", 15
        )
    await event.delete()
    await hide_inlinebot(event.client, bot, music, event.chat_id, reply_to_id)