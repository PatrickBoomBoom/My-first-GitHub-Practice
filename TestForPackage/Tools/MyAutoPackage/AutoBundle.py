import os
import time

# 设置你本地的Unity安装目录
unity_exe = 'F:/unity/Editor/Unity.exe'
# unity工程目录，当前脚本放在unity工程根目录中
project_path = 'E:/U_Project/My-first-GitHub-Practice/TestForPackage'
# 日志
log_file = 'C:/Users/hp/Desktop/AutoPackageTest/' + 'unity_bundle_log.log'
# 方法
bundle_method = 'AutoPackage.BuildBundle'


def kill_unity():
    os.system('taskkill /IM Unity.exe /F')


def clear_log():
    if os.path.exists(log_file):
        os.remove(log_file)


def start_build_bundle():

    if os.path.exists(log_file):
        os.remove(log_file)

    cmd = '%s -projectPath %s -executeMethod %s -logFile %s -batchmode -quit' \
          % (unity_exe, project_path, bundle_method, log_file)

    os.system(cmd)


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


def start_bundle():
    kill_unity()
    time.sleep(1)
    clear_log()
    time.sleep(1)
    start_build_bundle()
    return monitor_unity_log('Exiting batchmode successfully')

