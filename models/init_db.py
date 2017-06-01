#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from motor import MotorClient
import tornado
import tornado.web

if __name__ == "__main__":
    client = MotorClient("mongodb://47.93.23.32:27017")
    db = client["media_platform"]
    #添加用户信息
    user_collection = db.user
    user_info = {"name":"lee", "password":"123456", "power":0}
    user_collection.insert(user_info)
    #添加电影信息
    movie_collection = db.movie
    movie_info = {"movie_id":"taochujuemingzhen_2017" \
        , "movie_name":"逃出绝命镇" \
        , "movie_image_path":"images/movie/taochujuemingzhen_2017.jpg" \
        , "movie_born":"2017" \
        , "movie_categeroy":"惊悚" \
        , "movie_score":8.7 \
        , "movie_performer":"丹尼尔·卡卢亚 艾莉森·威廉姆斯 凯瑟琳·基纳 布莱德利·惠特福德 卡赖伯·兰德里·琼斯" \
        , "movie_play_url":[["video/mp4", "http://47.93.23.32:9007/taochujuemingzhen.mp4", "高清"]]
        , "movie_content":"黑人小伙克里斯（丹尼尔·卡卢亚 饰）和他的白人女朋友露丝（艾莉森·威廉姆斯 饰）相处到了见父母的阶段，她邀请他去自己父母家度周末。起初，克里斯把她家人过度热情的行为，解读为他们对女儿的跨种族恋爱的紧张应对。但随着时间的推移，一系列令人不安的发现使他认识到一个难以想象的真相，这一切背后是一个邪恶的种族阴谋。"\
        , "movie_state":"在线"\
        , "movie_area":"欧美"\
        , "movie_language":"英语"}
    movie_collection.insert(movie_info)

    tv_collection = db.tv
    tv_info = {"tv_id":"xibushijie_2017"\
        , "tv_name":"西部世界"\
        , "tv_image_path":"images/tv/xibushijie_2017.jpg"\
        , "tv_born":"2017"\
        , "tv_category":"奇幻 惊悚"\
        , "tv_score":9.6\
        , "tv_performer":"埃文·蕾切尔·伍德 安东尼·霍普金斯 本·巴恩斯 英格丽德·波尔索·贝达尔 小克利夫顿·克林斯"\
        # , "tv_play_url":{1:[["video/mp4", "http://47.93.23.32:9007/tv/xibushijie/1.mp4", "高清"]], 2:[["video/mp4", "http://47.93.23.32:9007/tv/xibushijie/2.mp4", "高清"]]} \
        , "tv_play_url":[[("video/mp4", "http://47.93.23.32:9007/tv/xibushijie/1.mp4", "高清")], [("video/mp4", "http://47.93.23.32:9007/tv/xibushijie/2.mp4", "高清")]]\
        , "tv_index":2\
        , "tv_state":"共10集,更新至第二集"\
        , "tv_area":"美国"\
        , "tv_language":"英语"\
        , "tv_content":"J.J. Abrams的Bad Robot公司将目光由广播网转向了有线网——HBO今天宣布购入该公司开发的新剧试映集《西部世界》（Westworld），故事根据1973年的同名科幻电影改编。在遥远的未来，一座巨型高科技成人乐园建成，其中有西部世界，罗马世界，中世纪世界三大主题版块的机器人世界，它提供给游客杀戮与性欲的满足。这座巨大机械乐园的后台监控渐渐失去了对机器人的控制，游客被机器人杀死，所有想逃离者都被锁定。该剧的主题是：「人工智能获得自主意识」以及「未来世界的罪孽」。过去几年Bad Robot公司一直活跃在广播网上（《危机边缘》、《疑犯追踪》、《革命》和即将播出的《信徒》），这是该公司在有线网上开发的第一个重要项目。1980年，《西部世界》曾被改编成电视剧集《Beyond Westworld》，但该剧很短命。 本剧的评论：POI被砍，乔纳森·见异思迁·诺兰全面转向《疑犯追踪2西部世界》，时代背景设置在POI的未来，围绕“人工智能获得自主意识”、“未来世界的罪孽”的主题，借尸还魂，讲述后撒玛利亚人时代的故事，娓娓道来，填补时间线空白，最终与POI第五季半开放结局完美衔接！诺兰弟POI宇宙从此诞生！掌声经久不绝…" }
    remote_tv_info = {"tv_id":"remote_tv" \
        , "tv_name":"远程电视" \
        , "tv_image_path":"images/tv/xibushijie_2017.jpg" \
        , "tv_born":"2017" \
        , "tv_category":"奇幻 惊悚" \
        , "tv_score":9.6 \
        , "tv_performer":"埃文·蕾切尔·伍德 安东尼·霍普金斯 本·巴恩斯 英格丽德·波尔索·贝达尔 小克利夫顿·克林斯" \
               # , "tv_play_url":{1:[["video/mp4", "http://47.93.23.32:9007/tv/xibushijie/1.mp4", "高清"]], 2:[["video/mp4", "http://47.93.23.32:9007/tv/xibushijie/2.mp4", "高清"]]} \
        , "tv_play_url":[[("remote", "https://jiexi.071811.cc/jx.php?url=http://movie.ks.js.cn/flv/other/1_0.mp4", "高清")]] \
        , "tv_index":1 \
        , "tv_state":"共10集,更新至第二集" \
        , "tv_area":"美国" \
        , "tv_language":"英语" \
        , "tv_content":"J.J. Abrams的Bad Robot公司将目光由广播网转向了有线网——HBO今天宣布购入该公司开发的新剧试映集《西部世界》（Westworld），故事根据1973年的同名科幻电影改编。在遥远的未来，一座巨型高科技成人乐园建成，其中有西部世界，罗马世界，中世纪世界三大主题版块的机器人世界，它提供给游客杀戮与性欲的满足。这座巨大机械乐园的后台监控渐渐失去了对机器人的控制，游客被机器人杀死，所有想逃离者都被锁定。该剧的主题是：「人工智能获得自主意识」以及「未来世界的罪孽」。过去几年Bad Robot公司一直活跃在广播网上（《危机边缘》、《疑犯追踪》、《革命》和即将播出的《信徒》），这是该公司在有线网上开发的第一个重要项目。1980年，《西部世界》曾被改编成电视剧集《Beyond Westworld》，但该剧很短命。 本剧的评论：POI被砍，乔纳森·见异思迁·诺兰全面转向《疑犯追踪2西部世界》，时代背景设置在POI的未来，围绕“人工智能获得自主意识”、“未来世界的罪孽”的主题，借尸还魂，讲述后撒玛利亚人时代的故事，娓娓道来，填补时间线空白，最终与POI第五季半开放结局完美衔接！诺兰弟POI宇宙从此诞生！掌声经久不绝…" }
    tv_collection.insert(tv_info)
    tv_collection.insert(remote_tv_info)

    recomment = db.recomment
    recomment_info = {"media_id":"xibushijie_2017", "media_name":"西部世界"\
        , "media_type":0, "media_tags":"奇幻", "media_image_path":"images/tv/xibushijie_2017.jpg"}
    recomment.insert(recomment_info)
