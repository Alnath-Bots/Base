import discord
import os
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()


class Aqua(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(command_prefix='?', intents=intents)

    async def setup_hook(self):
        await self.load_commands()
        await self.tree.sync()

    async def load_commands(self):
        for dirpath, _, filenames in os.walk('./cogs'):
            for filename in filenames:
                if filename.endswith('.py'):
                    relative_path = os.path.relpath(dirpath, './cogs')
                    if relative_path == '.':
                        module_name = f'cogs.{filename[:-3]}'
                    else:
                        module_name = f'cogs.{relative_path.replace(os.sep, '.')}.{
                            filename[:-3]}'

                    try:
                        await self.load_extension(module_name)
                    except Exception as e:
                        print(f'Falha ao carregar {module_name}: {e}')


Aqua().run(os.getenv('BOT_TOKEN'))
