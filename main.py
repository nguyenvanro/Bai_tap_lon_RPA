import datetime
# from ten_file import function_name
# from baitapbuoi4 import function_name
from Chapter_3.Auto_Crawl.auto_web_genk import crawl_genk

while True:
    # 1. Lấy giờ hiện tại so sánh với 8h
    current_time = datetime.datetime.now()
    print("Giờ hiện tại: ", current_time)
    int_hour = current_time.hour
    print(int_hour)
    if int_hour == 13:
        # 2. Lấy dữ liệu tại trang genk/24h
        print("2. Lấy dữ liệu tại trang genk/24h")
        crawl_genk()

