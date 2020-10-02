import discord

import log_an

with open("token.txt", "r") as token_file:
    TOKEN = token_file.read()
CLIENT = discord.Client()
LOGGER = log_an.LogAn()


@CLIENT.event
async def on_ready():
    print(f"{CLIENT.user} has connected")


@CLIENT.event
async def on_message(message):
    await LOGGER.log_message(message)


@CLIENT.event
async def on_raw_message_delete(payload):
    LOGGER.log_deletion(payload)


@CLIENT.event
async def on_raw_message_edit(payload):
    LOGGER.log_partial_edit(payload)


@CLIENT.event
async def on_message_edit(before, after):
    LOGGER.log_full_edit(before, after)


CLIENT.run(TOKEN)
