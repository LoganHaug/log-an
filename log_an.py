"""Holds the bot class"""
import discord
import pymongo


class LogAn:
    def __init__(self):
        self.db = pymongo.MongoClient().log_an

    async def log_message(self, message: discord.message) -> None:
        self.db[str(message.guild.id)].insert_one(
            {
                "type": "message",
                "user_id": message.author.id,
                "user_name": message.author.name
                + "#"
                + str(message.author.discriminator),
                "nick_name": message.author.nick,
                "channel_id": message.channel.id,
                "channel_name": message.channel.name,
                "message_id": message.id,
                "message_content": message.content,
                "time": message.created_at.timestamp(),
            }
        )

    def log_deletion(self, deletion_payload: discord.RawMessageDeleteEvent) -> None:
        self.db[str(deletion_payload.guild_id)].insert_one(
            {
                "type": "deletion",
                "channel_id": deletion_payload.channel_id,
                "message_id": deletion_payload.message_id,
            }
        )

    def log_partial_edit(self, edit_payload):
        self.db[str(edit_payload.data["guild_id"])].insert_one(
            {
                "type": "partial_edit",
                "channel_id": edit_payload.channel_id,
                "message_id": edit_payload.message_id,
            }
        )

    def log_full_edit(self, before, after):
        self.db[str(before.guild.id)].insert_one(
            {
                "type": "full_edit",
                "user_id": before.author.id,
                "user_name": before.author.name
                + "#"
                + str(before.author.discriminator),
                "nick_name": before.author.nick,
                "channel_id": before.channel.id,
                "channel_name": before.channel.name,
                "message_id": before.id,
                "before_message_content": before.content,
                "after_message_content": after.content,
                "time": before.created_at.timestamp(),
            }
        )
