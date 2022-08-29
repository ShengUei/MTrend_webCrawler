import threading
from datetime import datetime, timezone, timedelta

#設定目錄
dir_path = '/home/'

def show_pid():
    pid = threading.get_native_id()
    filename = 'pid_output.txt'

    now = datetime.now(timezone.utc)
    local_datetime = now + timedelta(hours = 8)

    f = open(dir_path + filename, 'a')
    f.write('PID: %s at %s \n' % (pid, local_datetime.strftime('%Y/%m/%d %H:%M:%S')))
    f.close()