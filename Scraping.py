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
     'https://tyresnmore.com/all/car-tyres/toyota/innova.html?product_list_limit=30',
    'https://tyresnmore.com/all/car-tyres/maruti/brezza.html?product_list_limit=30',
    'https://tyresnmore.com/all/car-tyres/maruti/alto.html?product_list_limit=30',
    'https://tyresnmore.com/all/car-tyres/honda/amaze.html?product_list_limit=30',
    'https://tyresnmore.com/all/car-tyres/hyundai/eon.html?product_list_limit=300',
    'https://tyresnmore.com/all/car-tyres/hyundai/santro.html?product_list_limit=30',
    'https://tyresnmore.com/all/car-tyres/honda/city.html?product_list_limit=30',
    'https://tyresnmore.com/all/car-tyres/mahindra/thar.html?product_list_limit=30',
    'https://tyresnmore.com/all/car-tyres/mahindra/xuv-500.html?product_list_limit=30',
    'https://tyresnmore.com/all/car-tyres/ford/figo.html?product_list_limit=30',
    'https://tyresnmore.com/all/car-tyres/ford/aspire.html?product_list_limit=30',
    'https://tyresnmore.com/all/car-tyres/nissan/micra.html?product_list_limit=30',
     'https://tyresnmore.com/all/car-tyres/nissan/sunny.html?product_list_limit=30',
     'https://tyresnmore.com/all/car-tyres/tata/indica.html?product_list_limit=30',
    'https://tyresnmore.com/all/car-tyres/tata/indica.html?product_list_limit=30',
     'https://tyresnmore.com/all/car-tyres/tata/nano.html?product_list_limit=30',
     'https://tyresnmore.com/all/car-tyres/skoda/laura.html?product_list_limit=30',
     'https://tyresnmore.com/all/car-tyres/skoda/slavia.html?product_list_limit=30',
     'https://tyresnmore.com/all/car-tyres/renault/duster.html?product_list_limit=30',
     'https://tyresnmore.com/all/car-tyres/renault/lodgy.html?product_list_limit=30',
     'https://tyresnmore.com/all/car-tyres/mitsubishi/lancer.html?product_list_limit=30',
     'https://tyresnmore.com/all/car-tyres/mitsubishi/pajero.html?product_list_limit=30',
     'https://tyresnmore.com/all/car-tyres/mercedes-benz/a-class.html?product_list_limit=30',
     'https://tyresnmore.com/all/car-tyres/mercedes-benz/e-class.html?product_list_limit=30',
    'https://tyresnmore.com/all/car-tyres/fiat/punto.html?product_list_limit=30?product_list_limit=30',
     'https://tyresnmore.com/all/car-tyres/fiat/linea.html?product_list_limit=30',
     'https://tyresnmore.com/all/car-tyres/jaguar/f.html?product_list_limit=30',
     'https://tyresnmore.com/all/car-tyres/jaguar/xk.html?product_list_limit=30',
     'https://tyresnmore.com/all/car-tyres/chev/spark-all-models.html?product_list_limit=30',
     'https://tyresnmore.com/all/car-tyres/chev/beat.html?product_list_limit=30',
     'https://tyresnmore.com/all/car-tyres/bmw/7-series.html?product_list_limit=30',
     'https://tyresnmore.com/all/car-tyres/bmw/x6.html?product_list_limit=30',
     'https://tyresnmore.com/all/car-tyres/audi/a7.html?product_list_limit=30',
     'https://tyresnmore.com/all/car-tyres/audi/q8.html?product_list_limit=30',
     'https://tyresnmore.com/all/car-tyres/kia/carnival.html?product_list_limit=30',
     'https://tyresnmore.com/all/car-tyres/kia/ev6.html?product_list_limit=30',
     'https://tyresnmore.com/all/car-tyres/mg/hector.html?product_list_limit=30',
     'https://tyresnmore.com/all/car-tyres/mg/astor.html?product_list_limit=30',
     'https://tyresnmore.com/all/car-tyres/jeep/grand-cherokee.html?product_list_limit=30',
     'https://tyresnmore.com/all/car-tyres/jeep/compass.html?product_list_limit=30',
     'https://tyresnmore.com/all/car-tyres/volvo/s80.html?product_list_limit=30',
     'https://tyresnmore.com/all/car-tyres/volvo/v40.html?product_list_limit=30',
     'https://tyresnmore.com/all/car-tyres/volkswagen/passat.html?product_list_limit=30',
     'https://tyresnmore.com/all/car-tyres/volkswagen/beetle.html?product_list_limit=30']

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
    price = [i.replace('₹','') for i in price]
    price = [i.replace(' ','') for i in price]
    price = [i.replace(',','') for i in price]

    
driver.quit()
df_final=pd.DataFrame({'Car Model':vehicle,'Brand':brand,'Product Name':prod_name,'Price':price,'Features':final_f})
    
df_final.to_csv('final_data1.csv',index=False)