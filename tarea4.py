import psutil
import logging

def check_disk_space():
    root_usage = psutil.disk_usage("/")
    percent_used = root_usage.percent
    
    if percent_used > 80:
        logging.error("Espacio ocupado en la raíz es mayor que 80%")
    elif percent_used > 60:
        logging.warning("Espacio ocupado en la raíz es mayr que 60% pero menor que 80%")
    else:
        logging.info("Espacio ocupado en la raíz es menor que 60%")

def main():
    logging.basicConfig(filename="/home/antonio/logs/espacio.log", level=logging.INFO)
    check_disk_space()

if __name__ == "__main__":
    main()
