import psutil


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

if __name__ == '__main__':
    print("CPU Usage: ", get_usage())
    print("CPU User Usage: ", get_user_usage())
    print("CPU System Usage: ", get_system_usage())
    print("CPU Idle Usage: ", get_idle_usage())
    print("Logical CPU Count: ", get_cpu_count())
    print("Physic CPU Count: ", get_logical_cpu_count())