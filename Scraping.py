#import libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
#install driver
driver = webdriver.Chrome(ChromeDriverManager().install())
#manually enter the url of required pages to be scrape
url=['https://tyresnmore.com/all/car-tyres/toyota/fortuner/4wd.html?category_id=46&product_list_limit=30',
     'https://tyresnmore.com/all/car-tyres/toyota/innova.html?product_list_limit=30']

#declaring lists
prod_name=[]
vehicle=[] 
final_f=[]
price=[]
brand=[]


for i in url:
    driver.get(i)
    time.sleep(10)
  
    
    v_name=driver.find_element(By.XPATH,'//*[@id="maincontent"]/div[2]/div[1]/div[2]/div[1]/h1')
    name=driver.find_elements(By.XPATH,'//a[@class="product-item-link"]')
    pname=[]
    
    for i in name:
        a=i.text
        prod_name.append(a)
        pname.append(a)
        s=v_name.text.split()
        s=s[0]+" "+s[1]
        vehicle.append(s)
    for h in pname:
        h=h.split()
        h=h[0]
        brand.append(h)
    #df=pd.DataFrame({'Car Model':vehicle,'Brand':brand,'Product':prod_name})
    #final=get_features()
    f=[]
    features=driver.find_elements(By.XPATH,'//div[@class="clsProductFeature"]')
    for i in features:
        a=i.text
        f.append(a)
    prod_f = [i.split('\n\n') for i in f]

    for i in prod_f:
        sum=""
        for n in i:
            sum=sum+n+"      "
        final_f.append(sum)
    #df2=get_price()
    price_list=driver.find_elements(By.XPATH,'//span[@class="amt_price price-final_price tax weee"]')
    for i in price_list:
        z=i.text.replace(' Price\n','')
        price.append(z)
    
    old="Special"
    x=0
    for i in price:
        if old in i:
            del price[x-1]
            x+=1
        else:
            x+=1
    price = [i.replace('Special', '') for i in price]
    
driver.quit()
df_final=pd.DataFrame({'Car Model':vehicle,'Brand':brand,'Product Name':prod_name,'Price':price,'Features':final_f})
    
df_final.to_csv('final_data.csv',index=False)