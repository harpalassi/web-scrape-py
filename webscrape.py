import bs4
import requests

# grabs the price of an item on the bhphotovideo.com website.


def get_bh_price(product_url):
    result = requests.get(product_url)
    result.raise_for_status()

    soup = bs4.BeautifulSoup(result.text, 'html.parser')
    price_list = soup.select('.price_1DPoToKrLP8uWvruGqgtaY')
    # grab first element
    return price_list[0].text.strip()


price = get_bh_price(
    'https://www.bhphotovideo.com/c/product/1495319-REG'
    '/sony_wf1000xm3_b_wf1000xm3_wireless_noise_canceling_headphones.html')
print('The current price is ' + price)
