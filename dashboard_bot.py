import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.command()
async def control_feature(ctx, feature, state):
    # Logic to control the feature
    if state == "on":
        await ctx.send(f"Turned {feature} ON!")
    elif state == "off":
        await ctx.send(f"Turned {feature} OFF!")
    else:
        await ctx.send("Invalid command!")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    # Prevent bot from being stuck in loop when running from Dash callback
    bot.loop.stop()

bot.run('YOUR_DISCORD_BOT_TOKEN', loop=bot.loop)