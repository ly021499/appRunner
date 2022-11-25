# @Time   : 2022/11/11 10:37
# @Author : LOUIE
# @Desc   : GM命令调用

import requests
import setting


def __execute_command(cmd):
    """
    执行GM命令，执行前必须配置好GM_COOKIE
    :param cmd:
    :return:
    """
    url = setting.GM_URL
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": setting.GM_COOKIE
    }
    data = {
        "id": 0,
        "server_type": "test",
        "server_id": 80002990,
        "exec_type": 1,
        "platform_id": 80,
        "game_id": 9,
        "action": "save",
        "command": cmd,
        "csv_file": ""
    }
    try:
        requests.post(url=url, data=data, headers=headers)
        return True
    except:
        raise requests.exceptions.HTTPError


def clear_hero(pid: int):
    """
    清空英雄
    :param pid: 玩家编号
    :return:
    """
    cmd = f'clearHero {pid}'
    __execute_command(cmd)


def clear_item(pid: int):
    """
    清空道具
    :param pid: 玩家编号
    :return:
    """
    cmd = f'clearItem {pid}'
    __execute_command(cmd)


def complete_activity(pid: int, activity_id: int, reward_id: int, count: int):
    """
    完成活动进度
    :param pid: 玩家编号
    :param activity_id: 活动ID
    :param reward_id: 奖励ID
    :param count:
    :return:
    """

    cmd = f'addActivityProgress {pid} {activity_id} {reward_id} {count}'
    __execute_command(cmd)


def complete_target_task(pid: int, task_id: int, count: int):
    """
    完成指定活动进度
    :param pid: 玩家编号
    :param task_id: 任务ID
    :param count:
    :return:
    """

    cmd = f'addTaskProgress {pid} {task_id} {count}'
    __execute_command(cmd)


def set_main_task(pid: int, plot_id: int):
    """
    重置主线剧情到指定的剧情
    :param pid: 玩家编号
    :param plot_id: 剧情ID
    :return:
    """

    cmd = f'setMainTask {pid} {plot_id}'
    __execute_command(cmd)


def set_dungeon_progress(pid: int, level_type: int, chapter_index: int, level_count: int):
    """
    重置关卡到指定关卡(用完gm命令需要重新登录)
    :param pid: 玩家编号
    :param level_type: 关卡类型: 1.普通 2.精英
    :param chapter_index: 章节索引
    :param level_count: 通关关卡数量
    :return:
        example: setDungeonProgress 95756 1 11 6
    """

    if level_type not in [1, 2]:
        return
    cmd = f'setDungeonProgress {pid} {level_type} {chapter_index} {level_count}'
    __execute_command(cmd)


def set_hero_star(pid: int, count: int):
    """
    设置英雄星级
    :param pid: 玩家编号
    :param count: 星级数量
    :return:
    """

    cmd = f'batchSetHeroAttr {pid} 505 {count}'
    __execute_command(cmd)


def set_hero_up(pid: int, count: int):
    """
    设置英雄进阶
    :param pid: 玩家编号
    :param count: 进阶数量
    :return:
    """

    cmd = f'batchSetHeroAttr {pid} 502 {count}'
    __execute_command(cmd)


def set_hero_level(pid: int, count: int):
    """
    设置英雄等级
    :param pid: 玩家编号
    :param count: 等级数量
    :return:
    """

    cmd = f'batchSetHeroAttr {pid} 501 {count}'
    __execute_command(cmd)


def clear_player(pid: int):
    """
    清除账号信息
    :param pid: 玩家编号
    :return:
    """

    cmd = f'batchSetHeroAttr {pid}'
    __execute_command(cmd)


def set_server_time(pid: int, time_fmt: str):
    """
    设置服务器时间
    :param pid: 玩家编号
    :param time_fmt: 时间日期字符串
    :return:
    """

    # 对时间日期字符串进行判断是否为指定格式
    if time_fmt:
        pass
    year, month, day, hour, minute, second = time_fmt
    cmd = f'setServerTime {pid} {year} {month} {day} {hour} {minute} {second}'
    __execute_command(cmd)


def add_value(pid: int, res_type: int, count: int):
    """
    增加资源
    :param pid: 玩家编号
    :param res_type: 声望类型
    :param count: 声望值
    :return:
    """

    cmd = f'addValue {pid} 1009 {res_type} {count}'
    __execute_command(cmd)


def add_res(pid: int, res_type: int, point: int):
    """
    添加普通资源
    :param pid: 玩家编号
    :param res_type: 声望类型
    :param point: 声望值
    :return:
    """

    cmd = f'addRes {pid} {res_type} {point}'
    __execute_command(cmd)


def add_hero(pid: int, hero_type: int = 199999, count: int = 1):
    """
    添加资源命令
    :param pid: 玩家编号: 我的编号 55561040
    :param hero_type: 英雄类型 : 199999 - 秒杀英雄
    :param count: 数量
    :return:
    """

    cmd = f'addHero {pid} {hero_type} {count}'
    __execute_command(cmd)


def add_item(pid: int, res_type: int, point: int):
    """
    添加资源命令
    :param pid: 玩家编号
    :param res_type: 声望类型
    :param point: 声望值
    :return:
    """

    cmd = f'addItem {pid} {res_type} {point}'
    __execute_command(cmd)


def refresh_opponent(pid: int, opponent_id: int):
    """
    添加资源命令
    :param pid: 玩家编号
    :param opponent_id: 对手ID
    :return:
    """

    cmd = f'refreshOpponent {pid} {opponent_id}'
    __execute_command(cmd)


def set_arena_score(pid: int, score: int):
    """
    设置竞技场积分
    :param pid: 玩家编号
    :param score: 积分数
    :return:
    """

    cmd = f'setArenaScore {pid} {score}'
    __execute_command(cmd)


def buy_gift_bag(pid: int, score: int):
    """
    购买礼包
    :param pid: 玩家编号
    :param score: 积分数
    :return:
    """

    cmd = f'buyGiftBag {pid} {score}'
    __execute_command(cmd)


if __name__ == '__main__':
    play_id = 55561040
    add_value(play_id, 10021, 10)
    # add_hero(play_id)



