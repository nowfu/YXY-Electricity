import requests

# 通过 Fiddler抓包易校园APP可以获取到Cookie和请求参数

# 只要每天使用就不会过期
SHIRO_JID = "你的易校园Cookie"

# Server 酱的SendKey
# 官网：https://sct.ftqq.com/sendkey
SERVER_CHAN_SECRET = "你的SendKey"

url = 'https://application.xiaofubao.com/app/electric/queryRoomSurplus'
headers = {
    'Content-Type': 'application/json',
    'Cookie': f'shiroJID={SHIRO_JID}'
}

json_data = {
    # 学校ID
    "areaId": "你的学校ID",
    # 楼号
    "buildingCode": "你的楼号",
    # 楼层
    "floorCode": "你的楼层",
    "platform": "YUNMA_APP",
    # 房间ID
    "roomCode": "你的房间ID",
    # Cookie用户账号ID
    "ymId": "你的Cookie用户账号ID"
}


def send_server_notification(title: str, content: str) -> None:
    """
    使用 Server 酱发送通知。
    """
    server_data = {"text": title, "desp": content.replace("\n", "\n\n")}
    server_url = f'https://sctapi.ftqq.com/{SERVER_CHAN_SECRET}.send' if SERVER_CHAN_SECRET.startswith(
        "SCT") else f'https://sc.ftqq.com/{SERVER_CHAN_SECRET}.send'
    server_response = requests.post(server_url, data=server_data).json()

    if server_response.get("errno") == 0 or server_response.get("code") == 0:
        print("Server酱推送成功！")
    else:
        print(f'Server酱推送失败！错误码：{server_response.get("message", "未知错误")}')


try:
    response = requests.post(url, headers=headers, json=json_data)
    response.raise_for_status()
    data = response.json()

    # 解析数据
    data_inner = data.get('data', {})
    surplus = data_inner.get('surplus')
    display_room_name = data_inner.get('displayRoomName')
    record_time = data_inner.get('recordTime')

    message = f"{display_room_name}电费：{surplus}"

    print(message)

    # 当电费小于10元时发送提醒
    if surplus < 10:
        send_server_notification("电费提醒", message)

except requests.exceptions.RequestException as e:
    send_server_notification("查询电费失败", f"请求错误: {e}")
except ValueError as e:
    send_server_notification("查询电费失败", f"JSON解析错误: {e}")
except Exception as e:
    send_server_notification("查询电费失败", f"发生了一个错误: {e}")
