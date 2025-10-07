# tg-get-group-recent-msg-senderid
Telegram 机器人 获得群组最近1000条发言的senderid

<img width="674" height="412" alt="image" src="https://github.com/user-attachments/assets/8e4a8740-d4a1-424a-b0a9-ec00c05db213" />

api_id, api_hash 需要自己申请  
https://my.telegram.org/apps  
具体步骤不写了, 自己去问 google 和 gpt  


## 搭环境
```
apt install -y python3-pip
pip3 install telethon --break-system-packages
```

## 运行
```
python3 tg-get-group-recent-msg-senderid.py
```

## 运行结果示例
```
共统计到 85 个用户
391932510
5612162712
5043772938
7287227103
6989120610
以下略
```

