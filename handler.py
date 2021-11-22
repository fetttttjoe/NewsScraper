import Newspaper as news
import json
CONFIG_FILENAME = "Newspaper_Dist.json" 
OUTPUT_FILENAME = "scraped_articles.json"
newspaper = []
endSentence = [".","?","!"]
def showArtikels(my_dict):
    global newspaper
    for key, value in my_dict.items():
        if(isinstance(value, dict)): # base case
            if key == "newspapers":
                showArtikels(value) # call function recursively
                continue
            newspaper.append(key)
            
            showArtikels(value)
            continue
        if key == "link" or key == "rss":
            continue
        #print(my_dict[key])
        if key == "newspapers":
            continue
        if key == 'articles':
            for element in my_dict[key]:
                print(f"Artikel Published in: {newspaper[0]}")
                for k, entry in element.items():
                    
                    
                    if k == None:
                        continue
                    if k == "link":
                        continue
                    if k == "Story continues below advertisement Advertisement": # remove the anoying adds
                        continue
                    if k == "published":
                        temp = entry.replace("T", " ").split(" ") # beauty date and time
                        print(" On Date: ", temp[0], "with time:", temp[1], '\n')
                        continue
                    if k == "title":
                        print("Title: ", entry, "\n")
                        continue
                    temp =entry.replace("\n", "").replace('".', '".\n').replace('."', '."\n').replace(". ", ".\n\t").replace("! ", "!\n\t").replace("? ", "?\n\t")
                    print(f"\t{temp}")
                    print("\n")
                    #print(f"{entry}\n")
        print('\n\n')
        newspaper.pop(0) # remove first element in list, because we already used it
def main():
    menue = {
            "Search New Articel"        : f'news.main() {CONFIG_FILENAME}',
            "Show Artikel Information"  : 'showArtikels',
            "Open Artikel"              : 'openArtikel(f"{name}")'
            }
    for element in enumerate(menue):
        print(element)
    lMenue = list(menue.values())
    #name = 'test'
    #print(lMenue[2](name))
    #news.main()
    with open(OUTPUT_FILENAME, 'r') as file:
        data = json.load(file)
        showArtikels(data)
if __name__ == "__main__":
    main()
