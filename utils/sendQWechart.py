import json

import requests


class sendQWechart():

    def send_msg_txt(self):
        headers = {"Content-Type": "text/plain"}
        send_url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=a53afaa4-8037-4769-9f55-1c9552c8bff5"
        send_data = {
            "msgtype": "text",  # 消息类型，此时固定为text
            "text": {
                "content": "上海今日天气：32度，大部分多云，降雨概率：10%",  # 文本内容，最长不超过2048个字节，必须是utf8编码
                "mentioned_list": ["@all"],
                # userid的列表，提醒群中的指定成员(@某个成员)，@all表示提醒所有人，如果开发者获取不到userid，可以使用mentioned_mobile_list
                "mentioned_mobile_list": ["@all"]  # 手机号列表，提醒手机号对应的群成员(@某个成员)，@all表示提醒所有人
            }
        }

        res = requests.post(url=send_url, headers=headers, json=send_data)
        print(res.text)

    def send_msg_markdown(self, testsRun, success_count, failure_count):
        headers = {"Content-Type": "text/plain"}
        send_url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=a53afaa4-8037-4769-9f55-1c9552c8bff5"
        send_data = {
            "msgtype": "markdown",  # 消息类型，此时固定为markdown
            "markdown": {
                "content": "# **提醒！接口自动化结果请关注** \n" +  # 标题 （支持1至6级标题，注意#与文字中间要有空格）
                           "#### **请相关同事注意，及时跟进！**\n" +  # 加粗：**需要加粗的字**
                           "> 总用例：<font color=\"info\">{}</font> \n".format(testsRun) +  # 引用：> 需要引用的文字
                           "> 执行成功用例：<font color=\"warning\">{}</font> \n".format(success_count) +  # 字体颜色(只支持3种内置颜色)
                           "> 执行失败用例：<font color=\"warning\">{}</font> \n".format(failure_count) +
                           "> 具体测试报告如下：<font color=\"warning\">{}</font>".format('www.baidu.com')
                # 绿色：info、灰色：comment、橙红：warning
            }
        }

        res = requests.post(url=send_url, headers=headers, json=send_data)
        print(res.text)

    def send_msg_txt_img(self):
        headers = {"Content-Type": "text/plain"}
        send_url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=a53afaa4-8037-4769-9f55-1c9552c8bff5"
        send_data = {
            "msgtype": "news",  # 消息类型，此时固定为news
            "news": {
                "articles": [  # 图文消息，一个图文消息支持1到8条图文
                    {
                        "title": "中秋节礼品领取",  # 标题，不超过128个字节，超过会自动截断
                        "description": "今年中秋节公司有豪礼相送",  # 描述，不超过512个字节，超过会自动截断
                        "url": "www.baidu.com",  # 点击后跳转的链接。
                        "picurl": "http://res.mail.qq.com/node/ww/wwopenmng/images/independent/doc/test_pic_msg1.png"
                        # 图文消息的图片链接，支持JPG、PNG格式，较好的效果为大图 1068*455，小图150*150。
                    },
                    {
                        "title": "我的CSDN - 魏风物语",  # 标题，不超过128个字节，超过会自动截断
                        "description": "坚持每天写一点点",  # 描述，不超过512个字节，超过会自动截断
                        "url": "https://blog.csdn.net/itanping",  # 点击后跳转的链接。
                        "picurl": "http://res.mail.qq.com/node/ww/wwopenmng/images/independent/doc/test_pic_msg1.png"
                        # 图文消息的图片链接，支持JPG、PNG格式，较好的效果为大图 1068*455，小图150*150。
                    }
                ]
            }
        }

        res = requests.post(url=send_url, headers=headers, json=send_data)
        print(res.text)


if __name__ == '__main__':
    sendQWechart().send_msg_markdown()
