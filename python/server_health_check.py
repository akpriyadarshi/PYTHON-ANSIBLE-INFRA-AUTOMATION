import os
import platform

def check_disk():
    print("Disk Usage:")
    os.system("df -h")

def check_memory():
    print("\nMemory Usage:")
    os.system("free -m")

def system_info():
    print("\nSystem Info:")
    print("OS:", platform.system())
    print("Hostname:", platform.node())

if __name__ == "__main__":
    system_info()
    check_disk()
    check_memory()
