import os
import time
import platform
import subprocess
import config_autoPackage


def __kill_unity():
    os.system('taskkill /IM Unity.exe /F')


def __clean_log():
    if P.if_mac:
        P.log_path = config_autoPackage.bundle_log_mac
    else:
        P.log_path = config_autoPackage.bundle_log

    if os.path.exists(P.log_path):
        os.remove(P.log_path)


def __start_build_package():
    if P.if_mac:
        cmd = '%s -projectPath %s -logFile %s -executeMethod %s -batchmode -quit' % \
              (config_autoPackage.unity_app, config_autoPackage.project_path_mac,
               P.log_path, config_autoPackage.package_fuc)
    else:
        cmd = '%s -projectPath %s -logFile %s -executeMethod %s -batchmode -quit' % \
              (config_autoPackage.unity_exe, config_autoPackage.project_path,
               P.log_path, config_autoPackage.package_fuc)

    print("run :  " + cmd)
    subprocess.Popen(cmd)


def __monitor_unity_log():
    pos = 0

    while True:
        if os.path.exists(P.log_path):
            break
        else:
            time.sleep(0.1)
    while True:
        fd = open(P.log_path, 'r', encoding='UTF-8')
        if 0 != pos:
            fd.seek(pos, 0)
        while True:
            line = fd.readline()
            pos = fd.tell()
            if line.strip():
                print(line)
            if 'is an incorrect path for a scene file: Build Failed' in line:
                print('打包失败 ：错误的场景路径 看Log！！！')
                fd.close()
                return
            if 'Scripts have compiler errors.' in line:
                print('代码编译错误！！！')
                fd.close()
                return
            if 'DisplayProgressNotification: Build Failed' in line:
                print('打包失败 看Log！！！')
                fd.close()
                return
            if 'There is no Json at' in line:
                print('目标路径 缺少配置Json文件！！！')
                fd.close()
                return
            if 'Exiting batchmode successfully' in line:
                print('Package成功 : Exiting batchmode successfully')
                fd.close()
                return
            else:
                break
        fd.close()


def start_package():
    m_platform = platform.system()
    if m_platform == 'Darwin':
        P.if_mac = True
    else:
        P.if_mac = False

    if not P.if_mac:
        __kill_unity()
        time.sleep(1)

    __clean_log()
    time.sleep(1)
    __start_build_package()
    __monitor_unity_log()


class P:
    if_mac = False
    log_path = ''


if __name__ == '__main__':
    start_package()

