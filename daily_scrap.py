import feedparser
import csv
from datetime import date,datetime
import pandas as pd

"""This get daily feed of articles regarding each keyword url based and saves it to dataframe n csv file datewise"""

url_metaljunction = 'https://www.metaljunction.com/news/newslist/'
url_steelmint = 'https://www.steelmint.com/ajax_calls.php?getMoreNews=true'
url_steelorbis = 'https://www.steelorbis.com/taxonomy/steel-news/?page=1'
#url_alerts = 'https://www.google.co.in/alerts/feeds/13465962862743070888/10799556217080318438'

#d_steel = feedparser.parse(url_alerts)

today = date.today()
month = today.strftime("%B")
day = today.strftime("%d")

output = []

for x in range(0,len(d_steel.entries)):
    t = datetime(*d_steel.entries[x].published_parsed[:3])
    output.append([t.strftime('%d/%m/%Y'),d_steel.entries[x].title])

for x in range(0,len(d_steel_price.entries)):
    t = datetime(*d_steel_price.entries[x].published_parsed[:3])
    output.append([t.strftime('%d/%m/%Y'),d_steel_price.entries[x].title])

#for x in range(0,len(d_coal.entries)):
#    t = datetime(*d_coal.entries[x].published_parsed[:3])
    #output.append([t.strftime('%d/%m/%Y'),d_coal.entries[x].title])

#for x in range(0,len(d_iron.entries)):
#    t = datetime(*d_iron.entries[x].published_parsed[:3])
    #output.append([t.strftime('%d/%m/%Y'),d_iron.entries[x].title])

data = pd.DataFrame(output,columns =['date','title']).drop_duplicates()
data.to_csv('data_' + day +'_' +month +'.csv',index=False)

"""This part gets daily price for iron ore to check our model"""

option = webdriver.ChromeOptions()
option.binary_location = "/opt/god ogle/chrome"
chrome_driver_binary = "/usr/bin/chromedriver"
driver = webdriver.Chrome(chrome_driver_binary)

driver.get("https://www.steelmint.com/spongeiron-prices-indian-domestic")
timeout = 20

try:
    WebDriverWait(driver,timeout).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='tblPrices_DOM_SPONGE_IRON']/tbody/tr[1]/td[5]")))
except TimeoutException:
    print("Timed out waiting for page to load")
    driver.quit()

price = driver.find_element_by_xpath("//*[@id='tblPrices_DOM_SPONGE_IRON']/tbody/tr[1]/td[5]")

today = date.today()
price_file = open('prices_iron.csv', 'a')
with price_file:
    writer = csv.writer(price_file, delimiter = ',')
    #for list_ in output_data:
    writer.writerow([today.strftime('%Y-%m-%d'),price.text])
    price_file.close()

driver.close()
