from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup as bs



epicUrl = 'https://store-site-backend-static-ipv4.ak.epicgames.com/freeGamesPromotions?locale=ko&country=KR&allowCountries=KR'

r = requests.get(epicUrl)

data = r.json()


def dataBot():
    
    for item in data['data']['Catalog']['searchStore']['elements']:
        

    
    

        offers = item['promotions'],
   
    
    
    

        wideThum = item['keyImages']
    
        if offers is not None:
    
            for offer in offers:
            
                if offer is not None:
                
                    offerItem = offer['promotionalOffers']

                    try:
                        nowDiscount = offer['promotionalOffers'][0]['promotionalOffers'][0]['discountSetting']['discountPercentage']
                        #upcomingDiscount = offer['upcomingPromotionalOffers'][0]['promotionalOffers'][0]['discountSetting']['discountPercentage']
                    except:
                        pass
                
                    
                    
                    
                    if offerItem:
                    
                        if nowDiscount == 0:
                        
                            print("무료 기간")
                            print(item['title'])
                            print(item['customAttributes'][0]['value'])
                            print()
                            print(offer['promotionalOffers'][0]['promotionalOffers'][0]['startDate'])
                            print(offer['promotionalOffers'][0]['promotionalOffers'][0]['endDate'])                        
                            print(item['keyImages'][1]['url'])
                            print("\n")
                            print(item['urlSlug'])
                            print('=========================')
                        
                
                
                
                
                    #elif upcomingDiscount == 0:
                    #
                    #    print("(곧 출시)출시 후 무료 배포 예정")
                    #    print(item['title'])
                    #    print(item['customAttributes'][1]['value'])
                    #    print()
                    #    print(offer['upcomingPromotionalOffers'][0]['promotionalOffers'][0]['startDate'])
                    #    print(offer['upcomingPromotionalOffers'][0]['promotionalOffers'][0]['endDate'])
                    #    print(item['keyImages'][2]['url'])
                    #    print("\n")
                    #    print(item['urlSlug'])
                    #    print('=========================')
                
                  
        else: pass


    
    
def main():
    dataBot()
    
main()



            




    
