import os
import time
import platform
import config_autoPackage


def __kill_unity():
    os.system('taskkill /IM Unity.exe /F')


def __clear_log():
    if P.if_mac:
        P.log_path = config_autoPackage.bundle_log_mac
    else:
        P.log_path = config_autoPackage.bundle_log


    if os.path.exists(P.log_path):
        os.remove(P.log_path)


def __start_build_bundle():
    if P.if_mac:
        cmd = '%s -projectPath %s -executeMethod %s -logFile %s -batchmode -quit' \
              % (config_autoPackage.unity_app, config_autoPackage.project_path_mac,
                 config_autoPackage.bundle_fuc, config_autoPackage.bundle_log_mac)
    else:
        cmd = '%s -projectPath %s -executeMethod %s -logFile %s -batchmode -quit' \
              % (config_autoPackage.unity_exe, config_autoPackage.project_path,
                 config_autoPackage.bundle_fuc, config_autoPackage.bundle_log)

    print(cmd)
    os.system(cmd)


def __monitor_unity_log():
    print("__monitor_unity_log")
    pos = 0

    while True:
        if os.path.exists(P.log_path):
            break
        else:
            time.sleep(0.1)
    while True:
        fd = open(P.log_path, 'r', encoding='utf-8')
        if 0 != pos:
            fd.seek(pos, 0)
        while True:
            line = fd.readline()
            pos = fd.tell()
            if 'Exiting batchmode successfully' in line:
                print('Bundle 成功 ：Exiting batchmode successfully')
                fd.close()
                return
            if 'Scripts have compiler errors.' in line:
                print('代码编译错误！！！')
                fd.close()
                return
            if line.strip():
                print(line)
            else:
                break
        fd.close()


def start_bundle():
    m_platform = platform.system()
    if m_platform == 'Darwin':
        P.if_mac = True
    else:
        P.if_mac = False

    if not P.if_mac:
        __kill_unity()
        time.sleep(1)

    __clear_log()
    time.sleep(1)
    __start_build_bundle()
    __monitor_unity_log()
    print('Build_Bundle_Done')


class P:
    if_mac = False
    log_path = ''


if __name__ == "__main__":
    start_bundle()

