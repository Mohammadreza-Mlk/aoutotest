import json
import os
from persiantools.jdatetime import JalaliDateTime

_current_run_data = {}  # رکوردهای همان اجرا
_file_path_global = "results.json"  # مسیر فایل پیشفرض

def save_to_json(key: str, status_value: str, file_path: str = None):
    """
    اضافه کردن رکورد به اجرای فعلی و ذخیره خودکار در فایل
    - هر بار اجرای برنامه، یک {} جدید به آرایه اضافه میشه
    """
    global _current_run_data, _file_path_global

    if file_path:
        _file_path_global = file_path

    now = JalaliDateTime.now()
    date_str = now.strftime("%Y/%m/%d")
    time_str = now.strftime("%H:%M:%S")

    # اضافه کردن رکورد به اجرای فعلی
    _current_run_data[key] = {
        "status": status_value,
        "date": date_str,
        "time": time_str
    }

    # خواندن فایل موجود یا ایجاد لیست جدید
    if os.path.exists(_file_path_global) and os.path.getsize(_file_path_global) > 0:
        with open(_file_path_global, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
                if not isinstance(data, list):
                    data = []
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    # اضافه کردن رکورد فعلی به آرایه
    data.append(_current_run_data)

    # نوشتن در فایل JSON
    with open(_file_path_global, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    # پاک کردن رکوردهای فعلی برای اجرای بعدی
    _current_run_data = {}

    print(f"✅ رکورد '{key}' ذخیره شد در {_file_path_global}")



# def save_to_json(new_data: dict, file_path: str):
#     import json, os
#     from persiantools.jdatetime import JalaliDateTime

#     # اگه فایل وجود داشت، بخون
#     if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
#         with open(file_path, 'r', encoding='utf-8') as f:
#             try:
#                 data = json.load(f)
#                 if not isinstance(data, dict):
#                     data = {}
#             except json.JSONDecodeError:
#                 data = {}
#     else:
#         data = {}

#     # تایم استمپ جلالی
#     timestamp = JalaliDateTime.now().strftime("%Y/%m/%d    %H:%M:%S")

#     # اضافه کردن رکوردهای جدید
#     for k, v in new_data.items():
#         data[k] = f"{v} {timestamp}"

#     # نوشتن دوباره در فایل
#     with open(file_path, 'w', encoding='utf-8') as f:
#         json.dump(data, f, ensure_ascii=False, indent=4)

#     print(f"✅ داده‌ها ذخیره شدند در {file_path}")
























































# import json , os

# def save_to_json(new_data, file_path):
    
   
#     try:
#         # مرحله ۱: خواندن محتوا یا ایجاد لیست جدید
#         if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
#             with open(file_path, 'r', encoding='utf-8') as file:
#                 try:
#                     data = json.load(file)
#                     if not isinstance(data, list):
#                         data = [data]
#                 except json.JSONDecodeError:
#                     data = []
#         else:
#             data = []

#         # مرحله ۲: اضافه کردن timestamp به مقادیر
#         timestamp = JalaliDateTime.now().strftime("%Y/%m/%d %H:%M:%S")
#         new_record = {key: f"{value} {timestamp}" for key, value in new_data.items()}

#         # مرحله ۳: اضافه کردن رکورد جدید به لیست
#         data.append(new_record)

#         # مرحله ۴: نوشتن دوباره فایل
#         with open(file_path, 'w', encoding='utf-8') as file:
#             json.dump(data, file, ensure_ascii=False, indent=4)

#         print(f"✅ داده‌ها با موفقیت در {file_path} ذخیره شدند.")

#     except Exception as e:
#         print(f"❌ خطا در ذخیره‌سازی فایل JSON: {e}")