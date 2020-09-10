import scrapy
from urllib.parse import quote
import re
import json
import time
from findjob.items import FindjobItem


class JobspiderSpider(scrapy.Spider):
    name = 'jobSpider'
    allowed_domains = ['search.51job.com']
    job_name = quote(quote(input()))
    offset = 8
    # 要爬取的基础网页,防止网页抓取到的网页有什么变动,我加上了后面一长串的后缀
    base_url = "https://search.51job.com/list/020000,000000,0000,00,9,99,{},2,{}.\
html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm\
=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
    start_urls = [base_url.format(job_name,offset)]

    def parse(self, response):
        print("*" * 50 + str(self.offset) + "*" * 50)
        # 刚开始爬取写入文件,方便分析错误
        with open("51job.txt","w",encoding="utf-8") as f:
            f.write(response.text)
        text = response.xpath('//script[@type="text/javascript"]//text()').extract()[0]
        info = re.findall(r".*?(\{.*\}).*",text)[0]
        j_info = json.loads(info)
        largest_page = j_info['total_page']

        target_list = j_info["engine_search_result"]
        num = 0
        for i in target_list:
            num += 1
            item = FindjobItem()
            job_name = i['job_name']
            company_name = i['company_name']
            salary = i['providesalary_text']
            workarea = i['workarea_text']
            updatedate = i['updatedate']
            company_type = i['companytype_text']
            welfare = i['jobwelf']
            temp = i['attribute_text']
            if len(i['attribute_text']) == 3:
                if temp[1] in ['大专', '硕士', '本科', '在校生/应届生']:
                    degree = temp[1]
                    recruit_num = temp[2]
                    experience = '-'
                else:
                    experience = temp[1]
                    recruit_num = temp[2]
                    degree = '-'
            if len(temp) == 4:
                experience = temp[1]
                degree = temp[2]
                recruit_num = temp[3]
            companysize = i['companysize_text']
            companyind = i['companyind_text']

            item['job_name'] =  job_name
            item['salary'] = salary
            item['company_name'] = company_name
            item['companysize'] = companysize
            item['companyind'] = companyind
            item['company_type'] = company_type
            item['workarea'] = workarea
            item['experience'] = experience
            item['degree'] = degree
            item['recruit_num'] = recruit_num
            item['welfare'] = welfare
            item['updatedate'] = updatedate
            yield item
        time.sleep(10)
        self.offset += 1
        if self.offset <= int(largest_page):
            url = self.base_url.format(self.job_name,self.offset)
            yield scrapy.Request(url,callback=self.parse)


