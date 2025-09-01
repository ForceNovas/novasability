import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.message_content = True  # required to read messages

bot = commands.Bot(command_prefix="!", intents=intents)

heroes = [
    "dark willow", "phantom assassin", "hoodwink", "techies", "snapfire", "shadow shaman",
    "phantom lancer", "razor", "arc warden", "storm spirit", "warlock", "vengeful spirit",
    "keeper of the light", "earth spirit", "mars", "bounty hunter", "venomancer", "dark seer",
    "muerta", "pugna", "juggernaut", "queen of pain", "riki", "outworld destroyer", "troll warlord",
    "alchemist", "elder titan", "pangolier", "axe", "disruptor", "puck", "ursa", "grimstroke",
    "wraith king", "lion", "drow ranger", "shadow demon", "mirana", "underlord", "faceless void",
    "death prophet", "abaddon", "centaur warrunner", "anti-mage", "naga siren", "clinkz",
    "monkey king", "batrider", "leshrac", "lina", "omniknight", "tidehunter", "tiny", "dawnbreaker",
    "ringmaster", "winter wyvern", "lich", "sand king", "tusk", "bristleback", "earthshaker",
    "zeus", "dragon knight", "treant protector", "chen", "meepo", "timbersaw", "bloodseeker",
    "oracle", "ember spirit", "marci", "gyrocopter", "magnus", "snapfire", "sniper", "muerta",
    "rubick", "invoker", "beastmaster", "pudge", "jakiro", "skywrath mage", "viper", "silencer",
    "chaos knight", "lifestealer", "medusa", "weaver", "tinker", "void spirit", "broodmother",
    "nature's prophet", "night stalker", "phoenix", "windranger", "outworld destroyer",
    "necrophos", "spectre", "enchantress", "bane", "lion", "kez", "crystal maiden", "sven",
    "shadow fiend", "lycan", "lone druid", "ogre magi", "riki"]

@bot.command(name="say")
async def say(ctx, *, message: str):
    await ctx.send(message)

@bot.command(name="unmain")
async def unmain(ctx, *, hero_name: str):
    hero_name = hero_name.lower().strip()

    if hero_name not in heroes:
        await ctx.send(f"❌ Hero `{hero_name}` not found. Check the spelling or use `!list_heroes`.")
        return

    role_name = f"main: {hero_name}"
    role = discord.utils.get(ctx.guild.roles, name=role_name)

    if role is None:
        await ctx.send(f"⚠️ Role `{role_name}` does not exist on this server.")
        return

    if role not in ctx.author.roles:
        await ctx.send(f"ℹ️ You don't have the role `{role_name}`.")
        return

    try:
        await ctx.author.remove_roles(role)
        await ctx.send(f"🗑️ Role `{role_name}` removed.")
    except Exception as e:
        await ctx.send(f"❌ Failed to remove role: {str(e)}")

@bot.command(name="main")
async def main(ctx, *, hero_name: str):
    hero_name = hero_name.lower().strip()

    if hero_name not in heroes:
        await ctx.send(f"❌ Hero `{hero_name}` not found. Check the spelling or use `!list_heroes`.")
        return

    role_name = f"main: {hero_name}"
    role = discord.utils.get(ctx.guild.roles, name=role_name)

    if role is None:
        await ctx.send(f"⚠️ Role `{role_name}` does not exist.")
        return

    if role in ctx.author.roles:
        await ctx.send(f"🧙 You already main `{hero_name}`!")
        return

    try:
        await ctx.author.add_roles(role)
        await ctx.send(f"✅ You now main `{hero_name}`!")
    except Exception as e:
        await ctx.send(f"❌ Failed to assign role: {str(e)}")

@bot.command(name="list_heroes")
async def list_heroes(ctx):
    chunk_size = 30
    chunks = [heroes[i:i+chunk_size] for i in range(0, len(heroes), chunk_size)]
    for i, chunk in enumerate(chunks, start=1):
        await ctx.send(f"📜 Heroes ({(i-1)*chunk_size+1}-{(i-1)*chunk_size+len(chunk)}):\n" +
                       ", ".join([f"`{h}`" for h in chunk]))

@bot.event
async def on_ready():
    print(f"Bot is running as {bot.user}")

bot.run("")