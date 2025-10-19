# import json
# import os

# def create_or_overwrite_result(test_name, status, file_path='test_results.json'):
#     # اگر فایل وجود نداشت، یا خالی بود → بساز
#     if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
#         data = {}
#     else:
#         # اگر فایل وجود داره → محتوا رو بخون
#         with open(file_path, 'r') as f:
#             try:
#                 data = json.load(f)
#             except json.JSONDecodeError:
#                 data = {}

#     # مقدار جدید رو اضافه کن
#     data[test_name] = status

#     # ذخیره در فایل
#     with open(file_path, 'w') as f:
#         json.dump(data, f, indent=4)









import json
import os
from datetime import datetime

def create_or_overwrite_result(test_name, status, file_path='test_results.json'):
    # اگر فایل وجود نداشت، یا خالی بود → بساز
    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        data = {}
    else:
        # اگر فایل وجود داره → محتوا رو بخون
        with open(file_path, 'r') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = {}

    # زمان فعلی
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # مقدار جدید رو اضافه کن، شامل status و time
    data[test_name] = {
        "status": status,
        "time": current_time
    }

    # ذخیره در فایل
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)
