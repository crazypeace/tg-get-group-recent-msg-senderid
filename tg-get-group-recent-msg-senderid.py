from telethon import TelegramClient
from telethon.tl.types import Message
from collections import Counter

# 到这里申请 https://my.telegram.org/apps
api_id = 12345678
api_hash = 'f9847f9847f9847f9847f9847f984747'

# 群组的 username 或 ID
#group = -100xxxxxxxxxx #私有群是负整数
group = 'groupusername' #公开群的username字符串

# 登录的用户的手机号
phone_number = '+8613812345678'
# 如果统计私有群, 则该用户需要已入群

# 要获取的消息条数
MESSAGE_LIMIT = 1000

client = TelegramClient('session_' + phone_number, api_id, api_hash)

async def main():
    await client.start(phone=phone_number)

    # 获取群实体
    entity = await client.get_entity(group)

    # 统计用户ID
    counter = Counter()
    
  # 获得群组中最近的消息
    async for msg in client.iter_messages(entity, limit=MESSAGE_LIMIT):
        # 过滤掉进群离群的系统消息
        if isinstance(msg, Message) and msg.sender_id:
            counter[msg.sender_id] += 1

    print(f'共统计到 {len(counter)} 个用户')
    for uid, count in counter.most_common():
        print(uid)

with client:
    client.loop.run_until_complete(main())
