#!/bin/sh
#this script is for running all the scraper stuff at once

cd /Users/luukschoenmakers/Documents/studie/INFPRJ56/pc_builder_crawler/Informatique
PATH=$PATH:/usr/local/bin
export PATH
scrapy crawl cases
scrapy crawl fans
scrapy crawl harddisks
scrapy crawl motherboards
scrapy crawl powersupply
scrapy crawl ramddr1
scrapy crawl ramddr2
scrapy crawl ramddr3
scrapy crawl ramddr4
scrapy crawl soundcards

cd /Users/luukschoenmakers/Documents/studie/INFPRJ56/pc_builder_crawler/Alternate

scrapy crawl alternatecases
scrapy crawl alternateharddisk
scrapy crawl alternatemoederbord
scrapy crawl alternatevoeding
scrapy crawl alternatekoeling
scrapy crawl alternateram1
scrapy crawl alternateram2
scrapy crawl alternateram3
scrapy crawl alternateram4
scrapy crawl alternategeluidskaart