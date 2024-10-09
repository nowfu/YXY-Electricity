# YXY-Electricity
## 项目简介

**易校园宿舍电费查询提醒脚本** 是一个旨在帮助用户便捷查询并提醒宿舍电费余额的脚本。通过该脚本，用户可以自动获取当前电费信息，并在电费余额不足时发送提醒，以避免因电费不足导致的断电问题。

## 功能特点

- **自动查询**：定期自动查询宿舍电费余额。
- **余额提醒**：当电费余额低于设定阈值时，通过Server 酱在微信上发送提醒。

## 使用说明

### 环境要求

- **[Fiddler](https://www.telerik.com/fiddler/fiddler-classic)**
- **[Server 酱](https://sct.ftqq.com/sendkey)**
- **[青龙面板](https://github.com/whyour/qinglong)**

### 安装步骤

1. **通过 Fiddler抓包易校园APP获取Cookie和请求**：

   通过下面的URL可以在Fiddler中筛选出查询电费的请求

   ```bash
   https://application.xiaofubao.com/app/electric/queryRoomSurplus
   ```

2. **通过青龙面板或其它脚本管理器来启动脚本**：
	
	**使用青龙面板**

	- 在脚本管理中新建文件并粘贴脚本内容或者上传拉取到本地的YXY-Electricity.py脚本
	
	- 在定时任务中添加任务
	
		**名称：**
	
		易校园宿舍电费检查
		
		**命令/脚本：**
		
		```
		task YXY-Electricity.py
   		```
		**定时规则：**
		
		- 通过链接生成Cron表达式[Cron在线表达式生成器](https://cron.ciding.cc/)
		
		- 或者直接使用下面的Cron表达式
		```
		0 0 15 * * ? 
		```
	
3. **配置脚本**：

**修改脚本头部的代码，设置您的请求信息。**

**示例配置**

```python
# 通过 Fiddler抓包易校园APP可以获取到Cookie和请求参数

# 只要每天使用就不会过期
SHIRO_JID = "你的易校园Cookie"

# Server 酱的SendKey
# 官网：https://sct.ftqq.com/sendkey
SERVER_CHAN_SECRET = "你的SendKey"

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

```

4. **运行脚本**：
	- 在定时任务中手动点击运行
	
	- 或者等待到固定的时间自动运行

## 贡献指南

我们欢迎任何形式的贡献，包括但不限于：

- 修复现有问题
- 添加新功能
- 优化代码结构
- 改进文档

## 联系我们

如果您在使用过程中遇到任何问题或有任何建议，请通过以下方式联系我：

- GitHub Issues: https://github.com/nowfu/YXY-Electricity/issues

## 版权信息

本项目遵循 [MIT 许可证](https://github.com/nowfu/YXY-Electricity/blob/main/LICENSE) 进行开源。
