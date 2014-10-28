# -*- coding: utf-8 -*-

# Scrapy settings for informatique project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'informatique'

SPIDER_MODULES = ['informatique.spiders']
NEWSPIDER_MODULE = 'informatique.spiders'
ITEM_PIPELINES = {
	'informatique.pipelines.JsonExportPipeline' : 300,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'informatique (+http://www.yourdomain.com)'
