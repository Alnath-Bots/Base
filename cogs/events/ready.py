from discord.ext import commands


class OnReady(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Online em {self.bot.user.display_name}')


async def setup(bot: commands.Bot):
    await bot.add_cog(OnReady(bot))
