import discord
from discord import app_commands
from discord.ext import commands
import os
from os import getenv

from goseki_io import _resist_goseki
from goseki_io import _resist_kaii
from fileio import _resist_csv

SIMU_URL = "https://mhrise.wiki-db.com/sim/" # （泣）シミュのURL

intents = discord.Intents.default()
intents.message_content = True  # メッセージコンテントのintentはオンにする
# bot = MyBot(command_prefix="!", intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents)

### test プログラム
# ピンポンの返答
@bot.command(name='ping')
async def _ping(ctx):
    await ctx.reply("Pong!")


# 複数argsのテスト
@bot.command(name='testargs')
async def _testargs(ctx, *args):
    arguments = ', '.join(args)
    _resist_goseki(arguments)
    await ctx.send(f'{len(args)} arguments: {arguments}')


### gosekiコマンド !gr とか, gで始まるコマンド

# 護石の登録
@bot.command(name="gr")
async def _resister(ctx, *args):
    # 護石
    resist_list = []
    print(len(args))

    if len(args) == 0:
        await ctx.send(f'護石情報をコマンドのあとに続けて記入してください。\n例 : `!r 弱点特効2超会心2スロ321 地質学1 散弾・拡散矢UP2スロ4`')
        return

    for a in args:
        resist_list.append(_resist_goseki(a))

    resist_str = '\n'.join(resist_list)
    csv_path = _resist_csv(ctx, resist_str)

    await ctx.send(f'護石を登録しました\n```{resist_str}```')
    # await ctx.send(f'これまでの登録と合わせたCSVはこちら', file=discord.File(csv_path))


# 護石CSVの削除
@bot.command(name="gremove")
async def _remove_csv(ctx, *args):
    csv_path = f"./data/{ctx.author.id}/goseki.csv"

    if os.path.exists(csv_path):
        os.remove(csv_path)
        await ctx.send(f'護石情報を削除しました。')


# 護石CSVの表示
@bot.command(name="ge")
async def _export_csv(ctx, *args):
    csv_path = f"./data/{ctx.author.id}/goseki.csv"

    if os.path.exists(csv_path):
        os.remove(csv_path)
        await ctx.send(f'護石情報のCSVはこちらです', file=discord.File(csv_path))
    else:
        await ctx.send(f'登録している護石情報はありません。`!gr` で護石情報を登録してください。')

    

### シミュレータURL表示 !s

@bot.command(name="s")
async def _simulator(ctx):
    await ctx.reply(f"泣シミュのURLはこちらです！\n{SIMU_URL}")
    

### 説明 !h

@bot.command(name="s")
async def _simulator(ctx):
    command_path = f"./help/commands.txt"

    with open(command_path, "r") as f:
        help_message = f.read()
    await ctx.reply(f"{}")



token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
