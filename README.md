# 腾讯小程序教程爬虫
## 简介
- 通过使用scrapy框架创建CrawlSpider爬虫，爬取腾讯小程序教程，代码量少，代码简单。
- CrawlSpider继承自Spider，可以自定义爬取的url的规则，更为简洁。
- 仅作为新手学习使用
## 爬取字段
- `title`：教程标题
- `author`：作者
- `pub_time`：发布时间
- `article_introduce`：教程简介
- `url`：详情链接
## 爬取过程展示
![image](https://github.com/guli732/Tencent_applet_tutorial_spider/raw/master/img/tencent_app_spider.png)
## json结果展示
- `app_tutorial.json`为保存的结果文件
![image](https://github.com/guli732/Tencent_applet_tutorial_spider/raw/master/img/tencent_app_spider_result.png)
## 使用方法
1. 下载该项目
2. 安装scrapy库`pip3 install scrapy`
3. 运行`start.py`