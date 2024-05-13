import sys
import pandas as pd
import requests
from lxml import html
import xml.etree.ElementTree as ET 

website = "https://www.serebii.net/"

def main():
	args = sys.argv
	gen = args[1]
	if gen == '9':
		initialize9()

def initialize9():
	mon_links = pd.read_csv("mon_links.csv",index_col="Names")









#def link_df_creator():
#	paldea = requests.get("https://www.serebii.net/scarletviolet/paldeapokedex.shtml")
#	paldea_tree = html.fromstring(paldea.content)
#	mons = {}
#	for i in range(2,402):
#		imon = paldea_tree.xpath("/html/body/div[1]/div[2]/main/table[2]/tr[{}]/td[3]/a".format(i))[0]
#		mons[imon.text]=website[:-1]+imon.attrib["href"]
#	kitakami = requests.get("https://www.serebii.net/scarletviolet/kitakamipokedex.shtml")
#	kitakami_tree = html.fromstring(kitakami.content)
#	for j in range(2,202):
#		jmon = kitakami_tree.xpath("/html/body/div[1]/div[2]/main/table[2]/tr[{}]/td[3]/a".format(j))[0]
#		if jmon.text not in mons.keys():
#		   mons[jmon.text]=website[:-1]+jmon.attrib["href"]
#	blueberry = requests.get("https://www.serebii.net/scarletviolet/blueberrypokedex.shtml")
#	blueberry_tree = html.fromstring(blueberry.content)
#	for k in range(2,245):
#		kmon = blueberry_tree.xpath("/html/body/div[1]/div[2]/main/table[2]/tr[{}]/td[3]/a".format(k))[0]
#		if kmon.text not in mons.keys():
#		   mons[kmon.text]=website[:-1]+kmon.attrib["href"]
#	mon_links = pd.DataFrame.from_dict(mons, orient='index',columns=["Links"])
#	mon_links.to_csv("C:/Users/jaxon/OneDrive/Desktop/PythonPokedex/mon_links.csv",)
	



	#for it in sprig.iter():
	#print(sprig.attrib)
	#print(sprig.text)





if __name__ == "__main__":
	main()


#/html/body/div[1]/div[2]/main/table[2]/tbody