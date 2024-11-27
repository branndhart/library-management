import time

def sleep_txt(txt: str):
    for i in txt:
        print(i, end="", flush=True)
        time.sleep(0.007)
    return ""
