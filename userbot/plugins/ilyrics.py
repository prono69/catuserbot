# Made by @o_s_h_o_r_a_j
# Change credit and you gay.

from telethon import functions

from ..core.managers import edit_delete
from ..helpers.functions import deEmojify, hide_inlinebot
from ..helpers.utils import reply_id
from . import catub

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
        return await edit_delete(event, "`What should I download? Give a song name`")
    await event.delete()
    await hide_inlinebot(event.client, bot, music, event.chat_id, reply_to_id)


# By @FeelDeD


@catub.cat_cmd(
    pattern="fsong ?(.*)",
    command=("fsong", plugin_category),
    info={
        "header": "Fast song downloader",
        "usage": [
            "{tr}fsong <song name>",
        ],
    },
)
async def wave(odi):
    "Song Downloader"
    song = "".join(odi.text.split(maxsplit=1)[1:])
    reply_to_id = await reply_id(odi)
    await odi.edit("`Downloading ...`")
    if not song:
        await edit_delete(odi, "`Give me a song name`")
    chat = "@WaveyMusicBot"
    async with odi.client.conversation(chat) as conv:
        try:
            await odi.client(functions.contacts.UnblockRequest(conv.chat_id))
            start = await conv.send_message("/start")
            await conv.get_response()
            end = await conv.send_message(song)
            music = await conv.get_response()
            if not music.media:
                await odi.edit(f"`No result found for {song}`")
            else:
                result = await odi.client.send_file(
                    odi.chat_id, music, reply_to=reply_to_id, caption=False
                )
                await odi.delete()
            msgs = []
            for _ in range(start.id, end.id + 2):
                msgs.append(_)
            await odi.client.delete_messages(conv.chat_id, msgs)
            await odi.client.send_read_acknowledge(conv.chat_id)
        except result:
            await odi.reply("`Something went Wrong`")


@catub.cat_cmd(
    pattern="lits?(.*)",
    command=("lits", plugin_category),
    info={
        "header": "Get part of a song",
        "examples": "{tr}lits I love you",
        "usage": [
            "{tr}lits <key-word>",
        ],
    },
)
async def lisong(event):
    "Little Song"
    if event.fwd_from:
        return
    bot = "@MeloBot"
    song = event.pattern_match.group(1)
    song = deEmojify(song)
    reply_to_id = await reply_id(event)
    if not song:
        return await edit_delete(event, "Give me a text")
    await event.delete()
    await hide_inlinebot(event.client, bot, song, event.chat_id, reply_to_id)


@catub.cat_cmd(
    pattern="mev ?(.*)",
    command=("mev", plugin_category),
    info={
        "header": "Searches and uploads the meme voice.",
        "usage": "{tr}mev <input>",
        "examples": "{tr}mev bruh",
    },
)
async def nope(event):
    mafia = event.pattern_match.group(1)
    lol = deEmojify(mafia)
    bot = "@myinstantsbot"
    reply_to_id = await reply_id(event)
    if not lol:
        if event.is_reply:
            (await event.get_reply_message()).message
        else:
            lol = "bruh"
    await hide_inlinebot(event.client, bot, lol, event.chat_id, reply_to_id)
    await event.delete()
