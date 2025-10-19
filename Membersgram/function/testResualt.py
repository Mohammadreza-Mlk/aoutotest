import json
from function.bot import send_telegram_message

def result(file_path='test_results.json'):
    with open(file_path, 'r') as f:
        data = json.load(f)

    pass_count = 0
    fail_count = 0
    unknown_count = 0
    failed_tests = []

    for key, value in data.items():
        if isinstance(value, dict) and 'status' in value:
            status = value['status'].lower()
            if status == 'pass':
                pass_count += 1
            elif status == 'failed':
                fail_count += 1
                failed_tests.append(key)
            else:
                unknown_count += 1

    total_count = pass_count + fail_count + unknown_count

    print(f"📊 Total tests: {total_count}")
    print(f"✅ Passed: {pass_count}")
    print(f"❌ Failed: {fail_count}")
    
    if failed_tests:
        print("📛 Failed tests:")
        for name in failed_tests:
            print(f" - {name}")
    
    if unknown_count > 0:
        print(f"❓ Unknown status: {unknown_count}")
     
    if fail_count == 0:
        send_telegram_message(f"✅ تعداد تست‌های انجام‌شده: {total_count}\nهمه تست‌ها با موفقیت پاس شدند.")
    else:
        failed_list = "\n".join([f"- {name}" for name in failed_tests])
        send_telegram_message(
            f"🛎 تعداد تست‌های انجام‌شده: {total_count}\n"
            f"❌ تعداد تست‌های فیلد شده: {fail_count}\n"
            f"📛 تست‌های فیلد شده:\n{failed_list}"
        )
