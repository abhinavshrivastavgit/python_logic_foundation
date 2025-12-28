import psutil
import time

def check_robot_health():
    print("--- 🤖 Initializing Robot System Check ---")
    
    # Get CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)
    
    # Get Memory/RAM usage
    memory = psutil.virtual_memory()
    memory_usage = memory.percent

    print(f"System Status: ONLINE")
    print(f"CPU Load: {cpu_usage}%")
    print(f"Memory Usage: {memory_usage}%")

    # The "Product Manager" Logic: Alerting on constraints
    if cpu_usage > 80:
        print("⚠️ WARNING: CPU Overloaded. Robot processing may lag.")
    elif memory_usage > 85:
        print("⚠️ WARNING: Memory Full. High risk of system crash.")
    else:
        print("✅ Status: All systems optimal.")

if __name__ == "_main_":
    # Runs the check 5 times every 2 second
    for _ in range(5):
        check_robot_health()
        print("-" * 30)
        time.sleep(2)