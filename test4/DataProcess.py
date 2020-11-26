import numpy as np
import pandas as pd
def Process():
    fileNameStr='MyData.csv'
    orig_df = pd.read_csv(fileNameStr, encoding='utf-8', dtype=str)
    #对于计算不出单价或总价的那一行数据 删除
    orig_df=orig_df.drop(orig_df[(orig_df['unitprice'].isnull()) &(orig_df['allprice'].isnull())].index)

    #去除空格
    orig_df['name']=orig_df['name'].str.strip()
    orig_df['location_1'] = orig_df['location_1'].str.strip()
    orig_df['location_2'] = orig_df['location_2'].str.strip()
    orig_df['location_3'] = orig_df['location_3'].str.strip()
    orig_df['kind']=orig_df['kind'].str.strip()
    orig_df['area']=orig_df['area'].str.strip()

    #area处理
    orig_df['area']=orig_df['area'].str.replace("建面 ","")
    orig_df['area'] = orig_df['area'].str.replace("㎡", "")
    orig_df['area'] = orig_df['area'].str.split('-').str[0]
    orig_df['area'] = orig_df['area'].astype(np.float)

    #单价和总价的处理
    orig_df['unitprice'] = orig_df['unitprice'].astype(np.float)
    orig_df['allprice'] = orig_df['allprice'].astype(np.float)

    key=orig_df[(orig_df['unitprice'].isnull()) &(orig_df['area'].notnull()) &(orig_df['allprice'].notnull())].index
    orig_df.loc[key, 'unitprice'] = orig_df.loc[key, 'allprice'] * 10000 / orig_df.loc[key, 'area']


    key_1=orig_df[(orig_df['allprice'].isnull()) &(orig_df['area'].notnull()) &(orig_df['unitprice'].notnull())].index
    orig_df.loc[key_1,'allprice']=orig_df.loc[key_1,'unitprice']*orig_df.loc[key_1,'area']/10000



    orig_df['unitprice'] =  orig_df['unitprice'].astype(np.int64)
    orig_df['allprice'] = orig_df['allprice'].astype(np.float64)

    all_max=orig_df['allprice'].idxmax()#总价最贵的房子的索引值
    all_min = orig_df['allprice'].idxmin()#总价最便宜的房子的索引值
    formater = "{0:.04f}".format
    orig_df['allprice'] = orig_df['allprice'].apply(formater)

    print("总价最贵的房子:")
    print("名字:" + orig_df.loc[all_max, 'name'])
    print("地段:" + orig_df.loc[all_max, 'location_1'] + " " + orig_df.loc[all_max, 'location_2'] + " " + orig_df.loc[
        all_max, 'location_3'])
    print("面积:" + str(orig_df.loc[all_max, 'area']) + "m²")
    print("单价:" + str(orig_df.loc[all_max, 'unitprice']) + "元/m²")
    print("总价:" + str(orig_df.loc[all_max, 'allprice']) + "万元")

    #总价最便宜的房子
    print("\n总价最便宜的房子:")
    print("名字:" + orig_df.loc[all_min, 'name'])
    print("地段:" + orig_df.loc[all_min, 'location_1'] + " " + orig_df.loc[all_min, 'location_2'] + " " + orig_df.loc[
        all_min, 'location_3'])
    print("面积:" + str(orig_df.loc[all_min, 'area']) + "m²")
    print("单价:" + str(orig_df.loc[all_min, 'unitprice']) + "元/m²")
    print("总价:" + str(orig_df.loc[all_min, 'allprice']) + "万元")

    unit_max=orig_df['unitprice'].idxmax()#单价最贵的房子的索引值
    unit_min=orig_df['unitprice'].idxmin()#单价最便宜的房子的索引值

    print("\n\n单价最贵的房子:")
    print("名字:" + orig_df.loc[unit_max, 'name'])
    print("地段:" + orig_df.loc[unit_max, 'location_1'] + " " + orig_df.loc[unit_max, 'location_2'] + " " + orig_df.loc[
        unit_max, 'location_3'])
    print("面积:" + str(orig_df.loc[unit_max, 'area']) + "m²")
    print("单价:" + str(orig_df.loc[unit_max, 'unitprice']) + "元/m²")
    print("总价:" + str(orig_df.loc[unit_max, 'allprice']) + "万元")

    print("\n单价最便宜的房子:")
    print("名字:" + orig_df.loc[unit_min, 'name'])
    print("地段:" + orig_df.loc[unit_min, 'location_1'] + " " + orig_df.loc[unit_min, 'location_2'] + " " + orig_df.loc[
        unit_min, 'location_3'])
    print("面积:" + str(orig_df.loc[unit_min, 'area']) + "m²")
    print("单价:" + str(orig_df.loc[unit_min, 'unitprice']) + "元/m²")
    print("总价:" + str(orig_df.loc[unit_min, 'allprice']) + "万元")


    print("\n总价的中位数："+str(orig_df['allprice'].median()))
    print("单价的中位数："+str(int(orig_df['unitprice'].median())))

    orig_df[orig_df['area'].isnull()]=0
    orig_df['area'] = orig_df['area'].astype(np.int)
    orig_df.to_csv("result-cy-2020.csv", encoding="utf-8-sig",index=False)