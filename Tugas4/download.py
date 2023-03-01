import wget

ln_count =1
count = 0
text_file = open("list.txt","r")
lines = text_file.readlines()

for line in lines:
    wget.download ( line, 'crawl/' +str(count) + '.html')
    print(int(ln_count))
	
    ln_count += 1
    count += 1

text_file.close()
