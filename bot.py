import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from discord import Intents
from discord.utils import get

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

intents = Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

### ------------------------- !map -------------------- ###


@bot.command(require_var_positional=True)
@commands.has_any_role("The Iron Throne", "Hand of the King", "10mancounsel")
async def map(ctx, *args):
    await ctx.message.delete()
    await ctx.send("`WORKSHOP MAP POOL VOTE`")

    for i in args:
        maps = await ctx.send("{}".format(i))
        await maps.add_reaction(":plusone:795489944335941632")


@map.error
async def command_error(ctx, error):
    if isinstance(error, commands.MissingAnyRole):
        await ctx.send("```You don't have permission to use the !" + ctx.command.name + " command```")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("```Insufficient Arguments\n!map <map1> <map2> <map3> ...```")

### ------------------------- !vote10mc -------------------- ###


@bot.command(require_var_positional=True)
@commands.has_any_role("The Iron Throne", "Hand of the King")
async def vote10mc(ctx, *args):
    await ctx.send("<@&795859792207020032>, Voting for new 10mancounsel members: ")

    for i in args:
        votes10mc = await ctx.send("`{}`".format(i))
        await votes10mc.add_reaction(":plusone:795489944335941632")
        await votes10mc.add_reaction(":1_:776854696257388555")


@vote10mc.error
async def command_error(ctx, error):
    if isinstance(error, commands.MissingAnyRole):
        await ctx.send("```You don't have permission to use the !" + ctx.command.name + " command```")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("```Insufficient Arguments\n!vote10mc <name1> <name2> <name3>...```")

### ------------------------- !vote -------------------- ###


@bot.command()
@commands.has_any_role("The Iron Throne", "Hand of the King")
async def vote(ctx, arg):
    # change the @id to @10mancounsel later, this is just for testing
    votes = await ctx.send("<@&795859792207020032>, Vote to remove `{}` from 10mans, <:plusone:795489944335941632> for YES and <:1_:776854696257388555> for NO".format(arg))
    await votes.add_reaction(":plusone:795489944335941632")
    await votes.add_reaction(":1_:776854696257388555")


@vote.error
async def command_error(ctx, error):
    if isinstance(error, commands.MissingAnyRole):
        await ctx.send("```You don't have permission to use the !" + ctx.command.name + " command```")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("```Insufficient Arguments\n!vote <name>```")

### ------------------------- !clear -------------------- ###


@bot.command()
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)

### ------------------------- Say "Welcome" After Someone Joins -------------------- ###


@bot.event
async def on_member_join(member):
    ment = member.mention
    await bot.get_channel(797272268962660363).send(f"is that really him, is that rlly Bt, is that really {ment}. no no its the pokemon cards guy, no pokemon in here, get em OUT OF HERE!!!!")

### ------------------------- BOT Online -------------------- ###


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("Voting 10man's"))
    print("Bot is ready!")

### ------------------------- BOT Token -------------------- ###

bot.run(TOKEN)
import discord
from discord.ext import commands
from discord import Intents
from discord.utils import get

intents = Intents.default()
intents.members = True

bot = commands.Bot(command_prefix = "!" , intents = intents)

### ------------------------- !map -------------------- ###

@bot.command(require_var_positional = True)
@commands.has_any_role("The Iron Throne", "Hand of the King", "10mancounsel")
async def map(ctx, *args):
    await ctx.message.delete()
    await ctx.send("`WORKSHOP MAP POOL VOTE`")

    for i in args:
        maps = await ctx.send("{}".format(i))
        await maps.add_reaction(":plusone:795489944335941632")

@map.error
async def command_error(ctx, error):
    if isinstance(error, commands.MissingAnyRole):
        await ctx.send("```You don't have permission to use the !" + ctx.command.name + " command```")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("```Insufficient Arguments\n!map <map1> <map2> <map3> ...```")

### ------------------------- !vote10mc -------------------- ###

@bot.command(require_var_positional = True)
@commands.has_any_role("The Iron Throne", "Hand of the King")
async def vote10mc(ctx, *args):
    await ctx.send("<@&795859792207020032>, Voting for new 10mancounsel members: ")

    for i in args:
        votes10mc = await ctx.send("`{}`".format(i))
        await votes10mc.add_reaction(":plusone:795489944335941632")
        await votes10mc.add_reaction(":1_:776854696257388555")

@vote10mc.error
async def command_error(ctx, error):
    if isinstance(error, commands.MissingAnyRole):
        await ctx.send("```You don't have permission to use the !" + ctx.command.name + " command```")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("```Insufficient Arguments\n!vote10mc <name1> <name2> <name3>...```")

### ------------------------- !vote -------------------- ###

@bot.command()
@commands.has_any_role("The Iron Throne", "Hand of the King")
async def vote(ctx, arg):
    votes = await ctx.send("<@&795859792207020032>, Vote to remove `{}` from 10mans, <:plusone:795489944335941632> for YES and <:1_:776854696257388555> for NO".format(arg)) #change the @id to @10mancounsel later, this is just for testing
    await votes.add_reaction(":plusone:795489944335941632")
    await votes.add_reaction(":1_:776854696257388555")

@vote.error
async def command_error(ctx, error):
    if isinstance(error, commands.MissingAnyRole):
        await ctx.send("```You don't have permission to use the !" + ctx.command.name + " command```")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("```Insufficient Arguments\n!vote <name>```")

### ------------------------- !clear -------------------- ###

@bot.command()
async def clear(ctx, amount = 10):
    await ctx.channel.purge(limit = amount)

### ------------------------- Say "Welcome" After Someone Joins + Tally Counter  -------------------- ###

@bot.event
async def on_member_join(member):
    ment = member.mention
    await bot.get_channel(797272268962660363).send(f"is this really him, is that rlly Bt, is that really {ment}. no no its the pokemon cards guy, no pokemon in here, get em OUT OF HERE!!!!")

### ------------------------- BOT Online -------------------- ###

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("Voting 10man's"))
    print("Bot is ready!")

### ------------------------- BOT Token -------------------- ###

bot.run(TOKEN)
