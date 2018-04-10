from multiprocessing import Pool
from web_two import fiftyeight
from web_two import get_item_info
from web_two import get_attrations
from web_one import channel_list


def get_all_attrations(chanel):
    for i in range(1, 100):
        get_attrations(chanel, i)
if __name__ == '__main__':
    pool = Pool()
    # pool.map(get_all_attrations, channel_list.split())

    for i in fiftyeight.find().limit(500):
        # print(i['url'])
        print(pool.map(get_item_info, i['url'].split()))
    # for i in range(1, 50):
    #     print(pool.map(func, str(i)))
