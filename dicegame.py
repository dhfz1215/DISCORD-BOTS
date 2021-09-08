import discord
from discord.ext import commands
import asyncio
import ccxt

binance = ccxt.binance({
    'apiKey': 'FGq3IvGfVqNv36tvcAbWLCGOgKWa7tJjapmgMr5iw8F0fGduLA8eFrkGE0lzNtzf',
    'secret': 'IE4Hum9XosOnKSePEC7907Cfhqcw713uAz6Sojy2I3CRoNTFSLb9dNLgroHfXRmQ',
})
balance = binance.fetch_balance()
free_coin = balance['USDT']['free']
used_coin = balance['USDT']['used']
total_coin = balance['USDT']['total']

bot = commands.Bot(command_prefix='>')

@bot.event
async def on_ready():
	print("We have logged in as {0.user}".format(bot))

@bot.command()
async def account(ctx):
        embed = discord.Embed(title= "current coin you got")
        embed.add_field(name="free", value=f"** {free_coin} **")
        embed.add_field(name="used", value=f"** {used_coin} **")
        embed.add_field(name="total", value=f"** {total_coin} **")
        await ctx.send(embed=embed)

bot.run("ODY2NTI3OTM2OTE5NzY1MDMy.YPffT3Bw.zf5T6COPmROnPr3vS1GDM4k3aq0")