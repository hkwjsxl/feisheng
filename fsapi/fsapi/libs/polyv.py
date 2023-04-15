import time
import requests
import hashlib


class PolyvPlayer(object):
    def __init__(self, userId, secretkey, tokenUrl):
        """初始化，提供用户id和秘钥"""
        self.userId = userId
        self.secretKey = secretkey
        self.tokenUrl = tokenUrl

    def tomd5(self, value):
        """取md5值"""
        return hashlib.md5(value.encode()).hexdigest()

    # 获取播放加密视频数据的token
    def get_video_token(self, videoId, viewerIp, viewerId=None, viewerName='', extraParams='HTML5'):
        """
        :param videoId: 视频id
        :param viewerId: 看视频用户id
        :param viewerIp: 看视频用户ip
        :param viewerName: 看视频用户昵称
        :param extraParams: 扩展参数
        :param sign: 加密的sign
        :return: 返回点播的视频的token
        """
        ts = int(time.time() * 1000)  # 时间戳
        plain = {
            "userId": self.userId,
            'videoId': videoId,
            'ts': ts,
            'viewerId': viewerId,
            'viewerIp': viewerIp,
            'viewerName': viewerName,
            'extraParams': extraParams
        }

        # 按照ASCKII升序 key + value + key + value... + value 拼接
        plain_sorted = {}
        key_temp = sorted(plain)
        for key in key_temp:
            plain_sorted[key] = plain[key]
        print(plain_sorted)

        plain_string = ''
        for k, v in plain_sorted.items():
            plain_string += str(k) + str(v)
        print(plain_string)

        # 首尾拼接上秘钥
        sign_data = self.secretKey + plain_string + self.secretKey

        # 取sign_data的md5的大写
        sign = self.tomd5(sign_data).upper()

        # 新的带有sign的字典
        plain.update({'sign': sign})
        # python 提供的发送http请求的模块  requests.get
        result = requests.post(
            url=self.tokenUrl,
            headers={"Content-type": "application/x-www-form-urlencoded"},
            data=plain
        ).json()

        ret = {} if isinstance(result, str) else result.get("data", {})

        return ret["token"]
