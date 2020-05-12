import AutoPackage
import AutoBundle
import AutoUpdateSVN

if AutoUpdateSVN.start_update():
    print("SVN 更新很成功！")
else:
    print("SVN 更新应该出了一些问题 看看Log吧 ... ")

AutoBundle.start_bundle()

AutoPackage.start_package()

print("All Done!")
