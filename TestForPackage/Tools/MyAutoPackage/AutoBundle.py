import os

# 设置你本地的Unity安装目录
unity_exe = 'F:/unity/Editor/Unity.exe'
# unity工程目录，当前脚本放在unity工程根目录中
project_path = 'E:/U_Project/My-first-GitHub-Practice/TestForPackage'
# 日志
logFile_path = 'C:/Users/hp/Desktop/AutoPackageTest' + '/unity_log.log'
# 方法
bundle_method = 'AutoPackage.BuildBundle'

if __name__ == '__main__':

    if os.path.exists(logFile_path):
        os.remove(logFile_path)

    cmd = '%s -projectPath %s -executeMethod %s -logFile %s -batchmode -quit' \
          % (unity_exe, project_path, bundle_method, logFile_path)
    a = os.system(cmd)
    print(a)
