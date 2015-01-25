# -*- coding: utf-8 -*-

# Scrapy settings for project project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'Alternate'

SPIDER_MODULES = ['Alternate.spiders']
NEWSPIDER_MODULE = 'Alternate.spiders'
ITEM_PIPELINES = {
	'Alternate.pipelines.JsonExportPipeline' : 400,
	 
}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'project (+http://www.yourdomain.com)'
