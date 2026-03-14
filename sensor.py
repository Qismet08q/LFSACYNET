import time
from datetime import datetime

class SleepDetector:
    def __init__(self):
        self.motion_threshold = 0.5
        self.sleep_time = None
        
    def check_motion(self):
        # Akselerometr məlumatı
        try:
            with open('/sys/bus/iio/devices/iio:device0/in_accel_x_raw') as f:
                x = float(f.read())
            with open('/sys/bus/iio/devices/iio:device0/in_accel_y_raw') as f:
                y = float(f.read())
            return abs(x) + abs(y)
        except:
            return 0
            
    def detect_sleep(self):
        print("SCAYNET - Yuxu Sensoru Aktiv...")
        no_motion_count = 0
        
        while True:
            motion = self.check_motion()
            
            if motion < self.motion_threshold:
                no_motion_count += 1
                print(f"Hərəkətsizlik: {no_motion_count} saniyə")
            else:
                no_motion_count = 0
                print("Hərəkət var - istifadəçi oyaqdır")
                
            if no_motion_count >= 30:
                print("⚠️ İstifadəçi yuxuladı!")
                self.sleep_time = datetime.now()
                break
                
            time.sleep(1)

detector = SleepDetector()
detector.detect_sleep()

