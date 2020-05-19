import requests

def buy_buniess(s,ricingModel='premiumPrice',bdPremiumPrice=500,
                bdnPremiumPriceCeiling=100,bdPremiumPriceFloor=-100,limitChoosePositionDate=4):
    url ="http://192.168.7.162:16031/mgtshowgroup/setObjectVal"
    body={
        "formJSON": {
            "id": "35661400904667200",
            "showGroupObjectModel": "situationMarket",
            "mallPlate": "buyPlate",
            "pricingModel": ricingModel,
            "bdPremiumPrice": bdPremiumPrice,
            "bdnPremiumPriceCeiling": bdnPremiumPriceCeiling,
            "bdPremiumPriceFloor": bdPremiumPriceFloor,
            "limitChoosePositionDate":limitChoosePositionDate
        },
        "requestAttrMap": {
            "userNo": "zhangsan"
        }
    }
    s=requests.session()
    r=s.post(url,json=body,verify=False)
    # print(r.json())
    return r

if __name__=="__main__":
    #url ="http://192.168.7.162:16031/mgtshowgroup/setObjectVal"
    s=requests.session()
    r=buy_buniess(s,ricingModel='premiumPrice',bdPremiumPrice=500,bdnPremiumPriceCeiling=100,
                bdPremiumPriceFloor=-100,limitChoosePositionDate=4)
    print(r.json())





















































