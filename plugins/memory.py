import psutil


def get_memory_total():
    return psutil.virtual_memory().total / 1e+9


def get_memory_used():
    return psutil.virtual_memory().used / 1e+9


def get_memory_used_percent():
    return psutil.virtual_memory().percent / 1e+9


print(get_memory_total())
