import os
import time
import platform

unity_exe = 'F:/unity/Editor/Unity.exe'
project_path = 'E:/U_Project/My-first-GitHub-Practice/TestForPackage'
log_file = 'C:/Users/hp/Desktop/AutoPackageTest/' + 'unity_package_log.log'
static_func = 'AutoPackage.BuildApk'


def kill_unity():
    os.system('taskkill /IM Unity.exe /F')


def clean_log():
    if os.path.exists(log_file):
        os.remove(log_file)


def call_unity_static_func(func):
    platform_ = platform.system()

    if platform_ == "Windows":
        cmd = 'start %s -projectPath %s -logFile %s -executeMethod %s -batchmode -quit' % (
            unity_exe, project_path, log_file, func)
        print('run cmd:  ' + cmd)
        os.system(cmd)
    elif platform == "Mac":
        shell = ''
        print('run shell:   ' + shell)
        os.system(shell)


def monitor_unity_log(target_log):
    pos = 0
    while True:
        if os.path.exists(log_file):
            break
        else:
            time.sleep(0.1)
    while True:
        fd = open(log_file, 'r', encoding='utf-8')
        if 0 != pos:
            fd.seek(pos, 0)
        while True:
            line = fd.readline()
            pos = pos + len(line)
            if target_log in line:
                print('监测到unity输出了目标log: ' + target_log)
                fd.close()
                return
            if line.strip():
                print(line)
            else:
                break
        fd.close()


def start_package():
    kill_unity()
    time.sleep(1)
    clean_log()
    time.sleep(1)
    call_unity_static_func(static_func)
    monitor_unity_log('Exiting batchmode successfully')
