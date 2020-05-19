import requests
import os
import yaml

def yaml_data(yaml_path):
    #curpath=os.path.dirname(os.path.realpath(__file__))
    #print(curpath)
    #yaml_path=os.path.join(curpath,"market_buylist.yml")
    #print(yaml_path)
    f=open(yaml_path,"r",encoding="utf-8")
    fp=f.read()
    #print(fp)
    yaml_data1=yaml.load(fp)
    #print(yaml_data1)
    f.close()
    return yaml_data1

if __name__=="__main__":
    curpath=os.path.dirname(os.path.realpath(__file__))
    yaml_path=os.path.join(curpath,"market_buylist.yml")
    yaml_data1=yaml_data(yaml_path)
    print(yaml_data1)
