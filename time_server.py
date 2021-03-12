from binance_client import client
import time
import pandas as pd


interval = [0, 15, 30, 45]


def server_tm():
    time_srv = client.get_server_time()
    time = pd.to_datetime(time_srv["serverTime"], unit = "ms")
    min_ = time.strftime("%M")
    min_ = int(min_)
    sec_ = time.strftime("%S")
    sec_ = int(sec_)
    for i in interval:
        if min_ == i and sec_ == 3:
            print("Searching for opportunities ...")
            # run strategy

            time.sleep(5)
