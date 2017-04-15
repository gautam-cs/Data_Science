import numpy
from pandas import DataFrame, Series


def avg_medal_count(data):
    '''
    Using the dataframe's apply method, create a new Series called
    avg_medal_count that indicates the average number of gold, silver,
    and bronze medals earned amongst countries who earned at
    least one medal of any kind at the 2014 Sochi olympics.  Note that
    the countries list already only includes countries that have earned
    at least one medal. No additional filtering is necessary.

    You do not need to call the function in your code when running it in the
    browser - the grader will do that automatically when you submit or test it.
    '''



    # YOUR CODE HERE
    bronze_average=(data.bronze).mean()
    silver_average=(data.silver).mean()
    gold_average=(data.gold).mean()
    avg_medal_count=[]
    for d in range(len(data)):
        if(data.bronze[d]>=bronze_average and data.silver[d]>=silver_average and data.gold[d]>=gold_average and (data.gold[d]+data.silver[d]+data.bronze[d])>=1):
            temp=(data.country_name[d],data.silver[d],data.gold[d])
            avg_medal_count.append(temp)
    return avg_medal_count

if __name__=="__main__":
    countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
                 'Netherlands', 'Germany', 'Switzerland', 'Belarus',
                 'Austria', 'France', 'Poland', 'China', 'Korea',
                 'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
                 'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
                 'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']

    gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
    silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
    bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]

    olympic_medal_counts = {'country_name': countries,
                            'gold': Series(gold),
                            'silver': Series(silver),
                            'bronze': Series(bronze)}
    data = DataFrame(olympic_medal_counts)
    print(avg_medal_count(data))