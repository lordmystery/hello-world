from nonebot import get_plugin_config
from nonebot.plugin import PluginMetadata
from nonebot import on_command
from nonebot.adapters import Message
from nonebot.params import CommandArg
from nonebot.adapters.onebot.v11 import MessageSegment
from .models import RaceInfo
from .config import Config
from .API import *


__plugin_meta__ = PluginMetadata(
    name="hyc_race",
    description="",
    usage="",
    config=Config,
)

config = get_plugin_config(Config)


def gen_message(data: list[RaceInfo]) -> str:
    output = ""
    for i in data:
        output += f"比赛名称：{i.title}\n"
        output += f"开始时间：{i.start_time}\n"
        output += f"Link🌈：{i.url}\n\n"

    return output


AtCoderRaceHandler = on_command("近期at")


@AtCoderRaceHandler.handle()
async def AtCoderRaceHandleFunciton():
    await AtCoderRaceHandler.finish(gen_message(await fetchAtcoderRaces()))


CodeforcesRaceHandler = on_command("近期cf")


@CodeforcesRaceHandler.handle()
async def CodeforcesRaceHandleFunction():
    await CodeforcesRaceHandler.finish(gen_message(await fetchCodeforcesRaces()))


NowcoderRaceHandler = on_command("近期nk")


@NowcoderRaceHandler.handle()
async def NowcoderRaceHandleFunction():
    await NowcoderRaceHandler.finish(gen_message(await fetchNowcoderRaces()))


CodeforcesUserInfoHandler = on_command("cf")


@CodeforcesUserInfoHandler.handle()
async def CodeforcesUserInfohandleFunction(args: Message = CommandArg()):
    if username := args.extract_plain_text():
        users = await fetchCodeforcesUserInfo([username])
        pic = await genCodeforcesUserProlfile(users[0], 114514)
        await CodeforcesUserInfoHandler.finish(MessageSegment.image(pic))
    else:
        await CodeforcesUserInfoHandler.finish("请输入用户名")
