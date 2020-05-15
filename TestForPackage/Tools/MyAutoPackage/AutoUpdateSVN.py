import os
import config_autoPackage
import platform

__cmdCleanup = ' && svn cleanup && svn revert --recursive .'
__cmdUpdate = ' && svn update'


def __prepare_cleanup_SVN():
    print('开始cleanup')

    if P.if_mac:
        P.get_dic_cmd = "cd / && cd " + config_autoPackage.project_path_mac
    else:
        path1 = config_autoPackage.project_path.split('/')[0]
        path2 = config_autoPackage.project_path.split(':/')[1]
        print("盘符： " + path1)
        print("路径： " + path2)
        get_dic_cmd = path1 + " && cd / && cd " + path2

    cmd = P.get_dic_cmd + __cmdCleanup

    print(cmd)
    t = os.system(cmd)

    print("prepare_cleanup_SVN  ：" + str(t))

    __prepare_revert_SVN()


def __prepare_revert_SVN():
    print('开始revert')

    cmd = '%s && svn revert %s -R && svn revert %s -R' % \
          (P.get_dic_cmd, config_autoPackage.external_link1, config_autoPackage.external_link2)

    print(cmd)
    t = os.system(cmd)

    print("prepare_revert_SVN ：" + str(t))

    __update_SVN()


def __update_SVN():
    print('开始update')

    cmd = P.get_dic_cmd + __cmdUpdate

    print(cmd)
    t = os.system(cmd)

    if t == 0:
        return True
    else:
        return False


def start_update():
    m_platform = platform.system()

    print('Current platform : ' + m_platform)

    if m_platform == 'Darwin':
        P.if_mac = True
    else:
        P.if_mac = False

    __prepare_cleanup_SVN()


class P:
    if_mac = False
    get_dic_cmd = ''


if __name__ == '__main__':
    start_update()
