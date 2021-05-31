import discord
from discord.ext import commands

from chatterbot import ChatBot
import analyser.reply_generator as ds

BOT_KEY = "ODQ4Nzc1MzM1ODIyODg0ODk0.YLRhoQ.TWI1Ib8d__wXs2_LdKooqjgjUpY"
client = commands.Bot(command_prefix=">")

chatbot = ChatBot('Quotes Bot',read_only = True, logic_adapters=[
        "chatterbot.logic.BestMatch","chatterbot.logic.MathematicalEvaluation"
    ])

@client.event
async def on_ready():
    print("Bot is raedy")

@client.command()
async def bot(ctx,arg):
    texts = str(ds.get_response(arg))
    print(ctx)
    #await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))
    await ctx.send(texts)

client.run(BOT_KEY)
