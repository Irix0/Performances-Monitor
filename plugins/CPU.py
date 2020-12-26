import psutil
import cpuinfo
import platform



def get_usage():
    """Return a float representing the current system-wide CPU utilization as a percentage.
        Interval = 1"""
    return psutil.cpu_percent(interval=1)


def get_user_usage():
    """Provides utilization percentage for USER specific CPU time
        Interval = 1"""
    return psutil.cpu_times_percent(interval=1).user


def get_system_usage():
    """Provides utilization percentage for SYSTEM specific CPU time
        Interval = 1"""
    return psutil.cpu_times_percent(interval=1).system


def get_idle_usage():
    """Provides utilization percentage for IDLE specific CPU time
        Interval = 1"""
    return psutil.cpu_times_percent(interval=1).idle


def get_cpu_count():
    """Return the number of logical CPUs in the system
        LOGICAL NOT COUNTED"""
    return psutil.cpu_count(logical=False)


def get_logical_cpu_count():
    """Return the number of logical CPUs in the system
        LOGICAL COUNTED"""
    return psutil.cpu_count()


def get_cpu_freq():  # TODO : Need improvements
    OS = platform.system()
    if OS == "Linux":
        return psutil.cpu_freq().current
    elif OS == "Darwin" or OS == "Windows":
        a = cpuinfo.get_cpu_info()['hz_actual']
        b, c = a
        b /= 10 ** 6
        return b


def get_cpuinfo():  # FOR DEV USE ONLY /!\ SHOULD BE COMMENTED FOR BUILD
    """Return raw information directly from cpuinfo function
        Shouldn't be used in BUILD"""
    return cpuinfo.get_cpu_info()


def get_cpu_brand():
    """Return a string with the brand of the CPU
        Example : Intel(R) Core(TM) i7-7700K CPU @ 4.20GHz"""
    return cpuinfo.get_cpu_info()['brand_raw']


def get_bits():
    return cpuinfo.get_cpu_info()['bits']


if __name__ == '__main__':
    # print("CPU Usage: ", get_usage())
    # print("CPU User Usage: ", get_user_usage())
    # print("CPU System Usage: ", get_system_usage())
    # print("CPU Idle Usage: ", get_idle_usage())
    # print("Logical CPU Count: ", get_cpu_count())
    # print("Physic CPU Count: ", get_logical_cpu_count())
    # print("CPU Freq: ", get_cpu_freq())
    # print(get_cpuinfo())
    # print(get_bits())
    pass
