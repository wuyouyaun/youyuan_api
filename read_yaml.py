import os
import yaml

def yaml_path(curpathread):
    f=open(curpathread,"r",encoding="utf-8")
    yamlpath=f.read()
    #print(yamlpath)
    d=yaml.load(yamlpath)
    # print(yamlpath1['test_add_acconut'])
    return d
#print(yaml_path(curpathread))
if __name__=="__main__":
    curpath=os.path.dirname(os.path.realpath(__file__))
    print(curpath)
    curpathread=os.path.join(curpath,"tes_dem.yml")
    print(curpathread)
    yaml_test=yaml_path(curpathread)#["test_add_acconut"]
    print(yaml_test)
    #print(yaml_test["tes_add_acconut"])
    print(type(yaml_test))
