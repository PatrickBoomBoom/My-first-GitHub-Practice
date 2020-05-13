import os
import time
import platform
import config_autoPackage


def __kill_unity():
    os.system('taskkill /IM Unity.exe /F')


def __clean_log():
    if os.path.exists(config_autoPackage.package_log):
        os.remove(config_autoPackage.package_log)


def __start_build_package():
    platform_ = platform.system()

    if platform_ == "Windows":
        cmd = 'start %s -projectPath %s -logFile %s -executeMethod %s -batchmode -quit' % \
              (config_autoPackage.unity_exe, config_autoPackage.project_path,
               config_autoPackage.package_log, config_autoPackage.package_fuc)
        print('run cmd:  ' + cmd)
        os.system(cmd)
    elif platform == "Mac":
        shell = ''
        print('run shell:   ' + shell)
        os.system(shell)


def __monitor_unity_log():
    path = config_autoPackage.package_log
    pos = 0

    while True:
        if os.path.exists(path):
            break
        else:
            time.sleep(0.1)
    while True:
        fd = open(path, 'r', encoding='UTF-8')
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
    __kill_unity()
    time.sleep(1)
    __clean_log()
    time.sleep(1)
    __start_build_package()
    __monitor_unity_log()


if __name__ == '__main__':
    start_package()

