import re
import csv
import sys


def Remove_Internal_Links(article):

	all_internal_links_list = re.findall('<a href="https://moneyguideking.+?(?=</a>)</a>', article)
	for full_link in all_internal_links_list:
		anchor=re.findall('>.+?(?=</a>)',full_link)
		for anchorz in anchor:
			anchorz=anchorz.replace('>','')
			article = article.replace(full_link,anchorz)
	return article

def replace_nth(base_str, find_str, replace_str, n):
    return base_str.replace(find_str, "xxxxx", n-1).replace(find_str, replace_str, 1).replace("xxxxx", find_str)


def Add_Prirority_Links(article,article_link):
	nth=3
	#loop through the csv list
	for row in csv_file:
	    #if current rows 2nd value is equal to input, print that row
	    if article_link == row[0]:
	         article=replace_nth(article,'\n\n','<p> <strong>Related Article: </strong><a href="'+row[1]+'"> '+row[2]+' </a> \n\n </p>',nth)
	         nth=nth+0

	return article



csv_file = csv.reader(open('4_internal_links.csv', "r"), delimiter=",")
f1 = open('1_raw_article.txt', encoding='utf-8')
f2 = open('2_article_link.txt', encoding='utf-8')
f3 = open('3_output.txt','w',encoding='utf-8')

article = f1.read()
article_link = f2.readline()
article_link=article_link.replace("\n","")


article = Remove_Internal_Links(article)
article = Add_Prirority_Links(article,article_link)
f3.write(article)



#input("Enter any key")
print(" \n Complete ... \n")
f3.close()
f2.close()
f1.close()