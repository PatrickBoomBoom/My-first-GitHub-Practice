import os
import time
import platform
import config_autoPackage


def __kill_unity():
    os.system('taskkill /IM Unity.exe /F')


def __clear_log():
    if os.path.exists(config_autoPackage.bundle_log):
        os.remove(config_autoPackage.bundle_log)


def __start_build_bundle():
    cmd = '%s -projectPath %s -executeMethod %s -logFile %s -batchmode -quit' \
          % (config_autoPackage.unity_exe, config_autoPackage.project_path,
             config_autoPackage.bundle_fuc, config_autoPackage.bundle_log)

    os.system(cmd)


def __monitor_unity_log(target_log):

    path = config_autoPackage.bundle_log
    pos = 0

    while True:
        if os.path.exists(path):
            break
        else:
            time.sleep(0.1)
    while True:
        fd = open(path, 'r', encoding='utf-8')
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
    __kill_unity()
    time.sleep(1)
    __clear_log()
    time.sleep(1)
    __start_build_bundle()
    __monitor_unity_log('Exiting batchmode successfully')

