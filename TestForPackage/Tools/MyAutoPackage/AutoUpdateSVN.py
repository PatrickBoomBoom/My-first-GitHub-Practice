import os

# 切换盘符
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


def prepare_cleanup_SVN():
    print('开始cleanup')
    cmd = cmdGetTarget + " && " + cmdCleanup

    # t = subprocess.popen(cmd, 'r', 1)
    t = os.system(cmd)

    print("prepare_cleanup_SVN  ：" + str(t))

    return prepare_revert_SVN()


def prepare_revert_SVN():
    print('开始revert')
    cmd = cmdGetTarget + " && " + cmdRevertSelf + " && " + cmdRevertSharedAssets + " && " + cmdRevertVarietyStore

    t = os.system(cmd)

    print("prepare_revert_SVN ：" + str(t))

    return update_SVN()


def update_SVN():
    print('开始update')

    cmd = cmdGetTarget + " && " + cmdUpdate

    t = os.system(cmd)

    print("update_SVN ：" + str(t))

    if t == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    prepare_cleanup_SVN()
