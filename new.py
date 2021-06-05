from bs4 import BeautifulSoup as bs
import requests

freq = {}
def CountFrequency(my_list):
  
   
    for item in my_list:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1

clist=[]
url_list = ["https://webgeeks-2.herokuapp.com/","https://webgeeks-2.herokuapp.com/sonnet1.html","https://webgeeks-2.herokuapp.com/sonnet2.html","https://webgeeks-2.herokuapp.com/sonnet3.html","https://webgeeks-2.herokuapp.com/trial.html","https://webgeeks-2.herokuapp.com/web4.html","https://webgeeks-2.herokuapp.com/web5.html"]
for url in url_list:
   
    r = requests.get(url)
    soup = bs(r.content,'lxml')

    
    tags = {tag.name for tag in soup.find_all() }
    for tag in tags:
    
        
        for i in soup.find_all( tag ):
    
            
            if i.has_attr( "class" ):
    
                if len( i['class'] ) != 0:
                    clist.append(" ".join( i['class']))
    
CountFrequency(clist)

sort_orders = sorted(freq.items(), key=lambda x: x[1],reverse=True)
items=[]
for i in sort_orders:
    if(i[1]>5):
        print("%s : %d"%(i[0], i[1]))
        items.append(i[0])
            
string = ' '.join(items)       
print(string)