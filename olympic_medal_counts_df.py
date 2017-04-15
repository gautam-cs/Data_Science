import pandas as pd
import numpy as np
def create_dataframe(medals):
    # print(medals.dtypes)
    # print("")
    # print(medals.describe())
    # print("")
    # print(medals.head())
    # print("")
    # print(medals.tail())
    # print(medals)
    bronze_avegare=(medals.bronze).mean()
    avg_bronze_at_least_one_gold=[]
    for d in range(len(medals)):
        if(medals.bronze[d]>bronze_avegare and medals.gold[d]>=1 ):
            avg_bronze_at_least_one_gold.append(medals.countries[d])
    return avg_bronze_at_least_one_gold

if __name__== "__main__":
    data = {'countries': ['Russian Fed.', 'Norway', 'Canada', 'United States', 'Netherlands', 'Germany', 'Switzerland',
                          'Belar', 'Austria', 'France', 'Poland', 'China', 'Korea', 'Sweden', 'Czech Republic',
                          'Slovenia', 'Japan', 'Finland', 'Great Britain', 'Ukraine', 'Slovakia', 'Italy', 'Latvia',
                          'Australia', 'Croatia', 'Kazakhstan'],
            'gold': [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
            'silver': [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0],
            'bronze': [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]}
    medals = pd.DataFrame(data)
    list=create_dataframe(medals)
    print(list)
