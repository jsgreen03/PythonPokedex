import sys
import pandas as pd
import requests
from lxml import html
import xml.etree.ElementTree as ET 

def main():
	args = sys.argv
	gen = args[1]
	if gen == '9':
		initialize9()

def initialize9():
	pass
	response = requests.get("https://www.serebii.net/scarletviolet/paldeapokedex.shtml")
	tree = html.fromstring(response.content)

	print(tree.xpath("/html/body/div[1]/div[2]/main/table[2]")[0])





if __name__ == "__main__":
	main()


#/html/body/div[1]/div[2]/main/table[2]/tbody