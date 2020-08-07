import bs4, requests

def getBHPrice(productURL):
    res = requests.get(productURL)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    priceList = soup.select('.price_1DPoToKrLP8uWvruGqgtaY')
    # first element
    return priceList[0].text.strip()




price = getBHPrice('https://www.bhphotovideo.com/c/product/1582549-REG/sony_wh1000xm4_b_wh_1000xm4_wireless_noise_canceling_over_ear.html')
print('The current price is ' + price)
