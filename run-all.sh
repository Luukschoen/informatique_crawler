#this script is for running all the scraper stuff at once

#enter Alternate
cd Alternate
scrapy crawl alternatecases
scrapy crawl alternateharddisk
scrapy crawl alternatemoederbord
scrapy crawl alternatevoeding

#go one directory back, pick up the next one
cd ..
cd Informatique
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

