__author__ = 'miha_focsa'

import discord 
from discord.ext import commands


TOKEN = 'NzgwNzI0NjE0Nzk5NTU2NjA4.X7zQdQ.plWb_Cp_KBsH4NZgmLm37Y0wx7w'
PREFIX = 'stp '

bot = commands.Bot(command_prefix=PREFIX)

@bot.event
async def on_ready():
	print("Logged in as: " + bot.user.name + "\n")
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Saft"))



if __name__ == '__main__':
	bot.run(TOKEN)