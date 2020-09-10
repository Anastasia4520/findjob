# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv
import json

class FindjobPipeline(object):
    def __init__(self):
        self.f = open("jobInfo.csv","a",encoding="utf_8_sig",newline="")
        self.csv_writer = csv.writer(self.f)
        self.title = ['job_name','salary','company_name','companysize','companyind','company_type','workarea',
                             'experience','degree','recruit_num','welfare','updatedate']
        self.csv_writer.writerow(self.title)
    def process_item(self, item, spider):
        info_list = []
        info_list.append(item['job_name'])
        info_list.append(item['salary'])
        info_list.append(item['company_name'])
        info_list.append(item['companysize'])
        info_list.append(item['companyind'])
        info_list.append(item['company_type'])
        info_list.append(item['workarea'])
        info_list.append(item['experience'])
        info_list.append(item['degree'])
        info_list.append(item['recruit_num'])
        info_list.append(item['welfare'])
        info_list.append(item['updatedate'])
        print(info_list)
        self.csv_writer.writerow(info_list)
        return item

    def close_spider(self,spider):
        self.f.close()
