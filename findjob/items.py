# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FindjobItem(scrapy.Item):
    largest_page = scrapy.Field()

    job_name = scrapy.Field() # 公司名称
    updatedate = scrapy.Field() # 更新日期
    salary = scrapy.Field() #工资
    workarea = scrapy.Field() # 工作区域
    experience = scrapy.Field() # 工作经验
    degree = scrapy.Field() # 学历要求
    recruit_num = scrapy.Field() # 招聘数量
    welfare = scrapy.Field() # 福利待遇
    company_name = scrapy.Field() # 公司名称
    companysize = scrapy.Field() # 公司大小
    companyind = scrapy.Field() # 公司经营领域
    company_type = scrapy.Field() # 公司类型
