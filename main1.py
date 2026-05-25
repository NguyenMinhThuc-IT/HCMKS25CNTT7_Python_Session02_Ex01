print("--- EMERGENCY TRIAGE SYSTEM ---")
heart_rate = int(input("Enter patient's heart rate (bpm): "))

print("\n" + "="*45)
print("PROCESSING TRIAGE RESULT...".center(45))
print("="*45)

if heart_rate > 120:
    print("Priority: RED - Critical condition! Immediate action required.")
    print("Phân loại: ĐỎ (Nguy kịch, cấp cứu ngay lập tức!)")

elif heart_rate > 100:
    print("Priority: YELLOW - Abnormal. Monitor closely.")
    print("Phân loại: VÀNG (Bất thường, cần theo dõi sát)")

elif heart_rate < 60:
    print("Priority: BLUE - Bradycardia. Require ultrasound.")
    print("Phân loại: XANH DƯƠNG (Nhịp tim chậm, kiểm tra thêm)")

else:
    print("Priority: GREEN - Stable. Please wait in the lobby.")
    print("Phân loại: XANH LÁ (Ổn định, chờ theo thứ tự)")

print("-" * 45)
print("Triage process completed successfully.")