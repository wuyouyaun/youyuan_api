from customer_line.market_list import buy_buniess
from customer_line.read_yaml import yaml_data
import os
import requests
import pytest
curpath=os.path.dirname(os.path.realpath(__file__))
yaml_path=os.path.join(curpath,"market_buylist.yml")
yaml_data1=yaml_data(yaml_path)['buy_buniess']
print(type(yaml_data1))
print(yaml_data1)


@pytest.mark.parametrize("ricingModel,bdPremiumPrice,bdnPremiumPriceCeiling,bdPremiumPriceFloor,"
                         "limitChoosePositionDate,expected",
                    yaml_data1,
                    ids=[
                        "修改id,添加所属板块1",
                        "修改id,添加所属板块2",
                        "修改id,添加所属板块3"
                        ]
                    )

def test_BuyListThree(unlogin_fixture,ricingModel,bdPremiumPrice,bdnPremiumPriceCeiling,
                      bdPremiumPriceFloor,limitChoosePositionDate,expected):
    #url ="http://192.168.7.162:16031/mgtshowgroup/setObjectVal"
    #s=requests.session()
    s=unlogin_fixture
    r=buy_buniess(s,ricingModel=ricingModel,bdPremiumPrice=bdPremiumPrice,bdnPremiumPriceCeiling=bdnPremiumPriceCeiling,
                  bdPremiumPriceFloor=bdPremiumPriceFloor,limitChoosePositionDate=limitChoosePositionDate)
    print(r.json())
    assert r.json()['succeed']==expected['succeed']
    assert r.json()['errorMsg']==expected["errorMsg"]


