import os

# 找到目标目录
cmdGetTarget = 'E: && cd U_Project\PigRun\Client\PigRun'

# svn cleanup
cmdCleanup = 'svn cleanup && svn revert --recursive .'
# svn revert自身
cmdRevertSelf = 'svn revert Assets -R'
# svn revert外链
cmdRevertSharedAssets = 'svn revert Assets\SharedAssets -R'
# svn revert外链
cmdRevertVarietyStore = 'svn revert Assets\VarietyStore -R'
# svn update
cmdUpdate = 'svn update'


def __prepare_cleanup_SVN():
    print('开始cleanup')
    cmd = cmdGetTarget + " && " + cmdCleanup

    # t = subprocess.popen(cmd, 'r', 1)
    t = os.system(cmd)

    print("prepare_cleanup_SVN  ：" + str(t))

    return __prepare_revert_SVN()


def __prepare_revert_SVN():
    print('开始revert')
    cmd = cmdGetTarget + " && " + cmdRevertSelf + " && " + cmdRevertSharedAssets + " && " + cmdRevertVarietyStore

    t = os.system(cmd)

    print("prepare_revert_SVN ：" + str(t))

    return __update_SVN()


def __update_SVN():
    print('开始update')

    cmd = cmdGetTarget + " && " + cmdUpdate

    t = os.system(cmd)

    if t == 0:
        return True
    else:
        return False


def start_update():
    __prepare_cleanup_SVN()


if __name__ == '__main__':
    __prepare_cleanup_SVN()
