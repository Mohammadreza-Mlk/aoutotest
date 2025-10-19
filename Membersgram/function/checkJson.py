import json
from bot import send_telegram_message

def check_failed_tests(file_path='test_results.json'):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)

        failed_tests = [name for name, status in data.items() if status.lower() == "failed"]

        if failed_tests:
            print(f"❌ تعداد تست‌های ناموفق: {len(failed_tests)}")
            
            print("🔻 نام تست‌های ناموفق:")
              
            send_telegram_message(f"❌ تعداد تست‌های ناموفق: {len(failed_tests)}   ,     :  {failed_tests}" )
        else:
            print("✅ همه تست‌ها موفق بودند.")
    
    except FileNotFoundError:
        print("⚠️ فایل نتیجه پیدا نشد.")
    except json.JSONDecodeError:
        print("⚠️ فایل نتیجه خراب یا خالی است.")
check_failed_tests()