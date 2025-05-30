import subprocess
import threading
import time


def ping(ip):
    result = subprocess.run(["ping", "-c", "1", ip], capture_output=True)
    print(f"{ip} is {'up' if result.returncode == 0 else 'down'}")

ips = ["23.236.62.147", "109.70.26.37", "216.239.32.21", "23.227.38.32", 
       "74.125.22.132", "1.179.201.18", "1.32.194.195", "1.55.188.25", 
       "41.55.189.76", "2.16.10.106"]


def posled(ips):
    start_time = time.time()
    for ip in ips:
        ping(ip)
    posled_time = time.time() - start_time
    print(f"Последовательная проверка справилась за: {posled_time:.2f} секунд\n")
    return posled_time


def potoki(ips):
    threads = []
    start_time_potoki = time.time()
    for ip in ips:
        thread = threading.Thread(target=ping, args=(ip,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    potoki_time = time.time() - start_time_potoki
    print(f"Проверка с потоками заняла: {potoki_time:.2f} секунд\n")
    return potoki_time


posled_time = posled(ips)
potoki_time = potoki(ips)

print(f"Разница во времени: {posled_time - potoki_time:.2f} секунд")
