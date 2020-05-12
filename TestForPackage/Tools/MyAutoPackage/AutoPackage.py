import os
import time
import platform

# 设置你本地的Unity安装目录
unity_exe = 'F:/unity/Editor/Unity.exe'
# unity工程目录，当前脚本放在unity工程根目录中
project_path = 'E:/U_Project/My-first-GitHub-Practice/TestForPackage'
# 日志
log_file = 'C:/Users/hp/Desktop/AutoPackageTest' + '/unity_log.log'

static_func = 'AutoPackage.BuildApk'


# 杀掉unity进程
def kill_unity():
    os.system('taskkill /IM Unity.exe /F')


def clear_log():
    if os.path.exists(log_file):
        os.remove(log_file)


# 调用unity中我们封装的静态函数
def call_unity_static_func(func):
    kill_unity()
    time.sleep(1)
    clear_log()
    time.sleep(1)

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


# 实时监测unity的log, 参数target_log是我们要监测的目标log, 如果检测到了, 则跳出while循环    
def monitor_unity_log(target_log):
    pos = 0
    while True:
        if os.path.exists(log_file):
            break
        else:
            time.sleep(0.1)
    while True:
        fd = open(log_file, 'r')
        if 0 != pos:
            fd.seek(pos, 0)
        while True:
            line = fd.readline()
            pos = pos + len(line)
            if target_log in line:
                print(u'监测到unity输出了目标log: ' + target_log)
                fd.close()
                return
            if line.strip():
                print(line)
            else:
                break
        fd.close()


def start_package():
    call_unity_static_func(static_func)
    monitor_unity_log('Exiting batchmode successfully')
    print(' Done!!! ')


if __name__ == '__main__':
    call_unity_static_func(static_func)
    monitor_unity_log('Exiting batchmode successfully')
    print('done')
