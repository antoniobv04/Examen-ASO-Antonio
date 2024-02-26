import psutil

def main():
    partitions = psutil.disk_partitions()
    
    for partition in partitions:
        usage = psutil.disk_usage(partition.mountpoint)
        percent_used = (usage.used / usage.total) * 100
        percent_formatted = "{:.1f}%".format(percent_used)
        print(f"{partition.device} {percent_formatted}")

if __name__ == "__main__":
    main()
