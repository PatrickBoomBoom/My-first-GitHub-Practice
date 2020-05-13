import os
import config_autoPackage


__cmdCleanup = ' && svn cleanup && svn revert --recursive .'
__cmdUpdate = ' && svn update'


def __prepare_cleanup_SVN():
    print('开始cleanup')

    path1 = config_autoPackage.project_path.split('/')[0]
    path2 = config_autoPackage.project_path.split(':/')[1]

    print("盘符： " + path1)
    print("路径： " + path2)

    global get_dic_cmd
    get_dic_cmd = path1 + " && cd/ && cd " + path2

    cmd = get_dic_cmd + __cmdCleanup

    print(cmd)
    t = os.system(cmd)

    print("prepare_cleanup_SVN  ：" + str(t))

    __prepare_revert_SVN()


def __prepare_revert_SVN():
    print('开始revert')

    cmd = '%s && svn revert %s -R && svn revert %s -R' % \
          (get_dic_cmd, config_autoPackage.external_link1, config_autoPackage.external_link2)

    print(cmd)
    t = os.system(cmd)

    print("prepare_revert_SVN ：" + str(t))

    __update_SVN()


def __update_SVN():
    print('开始update')

    cmd = get_dic_cmd + __cmdUpdate

    print(cmd)
    t = os.system(cmd)

    if t == 0:
        return True
    else:
        return False


def start_update():
    __prepare_cleanup_SVN()


if __name__ == '__main__':
    __prepare_cleanup_SVN()
