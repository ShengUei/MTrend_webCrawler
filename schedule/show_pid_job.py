import threading

#設定目錄
dir_path = '/home/'

def show_pid():
    pid = threading.get_native_id
    filename = 'pid_output.txt'
    f = open(dir_path + filename, 'w')
    f.write('PID: %s' % pid)
    f.close()