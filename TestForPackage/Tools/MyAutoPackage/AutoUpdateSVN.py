import os
import config_autoPackage


__cmdCleanup = 'svn cleanup && svn revert --recursive .'
__cmdUpdate = 'svn update'


def __prepare_cleanup_SVN():
    print('开始cleanup')

    global path1
    path1 = config_autoPackage.project_path.split('/')[0]
    global path2
    path2 = config_autoPackage.project_path.split(':/')[1]

    print("盘符： " + path1)
    print("路径： " + path2)

    cmd = path1 + " && " + path2

    t = os.system(cmd)

    print("prepare_cleanup_SVN  ：" + str(t))

    __prepare_revert_SVN()


def __prepare_revert_SVN():
    print('开始revert')

    cmd = '%s && %s && svn revert %s -R && svn revert %s -R' % \
          (path1, path2, config_autoPackage.external_link1, config_autoPackage.external_link2)

    t = os.system(cmd)

    print("prepare_revert_SVN ：" + str(t))

    __update_SVN()


def __update_SVN():
    print('开始update')

    cmd = path1 + " && " + path2 + __cmdUpdate

    t = os.system(cmd)

    if t == 0:
        return True
    else:
        return False


def start_update():
    __prepare_cleanup_SVN()


if __name__ == '__main__':
    __prepare_cleanup_SVN()
