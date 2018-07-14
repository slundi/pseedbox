import os

def get_free_space():
    statvfs = os.statvfs(os.path.realpath(__file__))
    #statvfs.f_frsize * statvfs.f_blocks     # Size of filesystem in bytes
    #statvfs.f_frsize * statvfs.f_bfree      # Actual number of free bytes
    return statvfs.f_frsize * statvfs.f_bavail     # Number of free bytes that ordinary users are allowed to use (excl. reserved space)

def get_used_space(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size
