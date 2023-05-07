import time

def focus(minutes):
    """
    让程序运行一段时间，让你专注于工作。

    参数：
    minutes -- 专注的时间，单位为分钟。
    """
    seconds = minutes * 60
    time.sleep(seconds)
    print(f"已经专注了 {minutes} 分钟，现在可以休息一下了！")
    
  while True:
    focus(5)
