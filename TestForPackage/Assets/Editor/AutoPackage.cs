using System.Collections.Generic;
using UnityEditor;
using UnityEngine;
using System;
using System.IO;
using LitJson;


public class AutoPackage : EditorWindow
{
    static readonly string jsonPath = "C:/Users/hp/Desktop/AutoPackageTest/BuildPackageConfig.txt";

    static BuildPlayerOptions m_buildOption;

    public static void BuildApk()
    {
        Debug.Log("Build Apk ... ");

        ReadBuildConfig();

        BuildPipeline.BuildPlayer(m_buildOption);
    }

    public static void BuildBundle()
    {
        Debug.Log("Build Bundle ... ");

        Framework.Resource.CustomBundleBuilder.CallBuildByCMD();
    }

    [MenuItem("A/AAA")]
    private static void ReadBuildConfig()
    {
        Debug.Log("Start Read Build Config ... ");

        m_buildOption = new BuildPlayerOptions();

        JsonDataEx jd;

        if (File.Exists(jsonPath))
        {
            string str = File.ReadAllText(jsonPath);

            jd = JsonMapper.ToObject<JsonDataEx>(str);
        }
        else
        {
            Debug.LogError("There is no Json at : " + jsonPath);
            return;
            #region ForTest
            //jd = new JsonDataEx();

            //jd["productName"] = "test";
            //jd["companyName"] = "justTEST";

            //jd["packagePath"] = "C:/Users/hp/Desktop/AutoPackageTest/";
            //jd["packageName"] = "test.apk";

            //jd["version"] = "1.0.0";

            //jd["scenePath"] = "Assets/";

            //jd["defineInAndriod"] = "fuck1;fuck2";
            //jd["defineInIOS"] = "fuck3;fuck4";

            //jd["targetPlatform"] = "A";

            //jd["senceList"] = new JsonDataEx
            //{
            //    "1.unity",
            //    "2.unity"
            //};

            //File.WriteAllText("C:/Users/hp/Desktop/AutoPackageTest/jsonConfig.txt", jd.ToJson());
            #endregion
        };

        //名字
        Debug.Log("包名 ：" + jd["productName"]);
        PlayerSettings.productName = jd["productName"].ToString();

        Debug.Log("公司名 ：" + jd["companyName"]);
        PlayerSettings.companyName = jd["companyName"].ToString();

        //打包版本号
        Debug.Log("打包版本 ：" + jd["version"]);
        PlayerSettings.bundleVersion = jd["version"].ToString();

        //添加宏定义
        Debug.Log("安卓宏定义 : " + jd["defineInAndriod"]);
        PlayerSettings.SetScriptingDefineSymbolsForGroup(BuildTargetGroup.Android, jd["defineInAndriod"].ToString());

        Debug.Log("苹果宏定义 : " + jd["defineInIOS"]);
        PlayerSettings.SetScriptingDefineSymbolsForGroup(BuildTargetGroup.iOS, jd["defineInIOS"].ToString());

        //打包需要的各个场景
        Debug.Log("场景路径 : " + jd["scenePath"]);
        string scenePath = jd["scenePath"].ToString();
        List<string> tmp = new List<string>();
        for (int i = 0; i < jd["senceList"].Count; i++)
        {
            Debug.Log("需打入场景 ：" + jd["senceList"][i].ToString());
            tmp.Add(scenePath + jd["senceList"][i].ToString());
        }
        m_buildOption.scenes = tmp.ToArray();

        //打包平台
        Debug.Log("目标平台 : " + jd["targetPlatform"]);
        m_buildOption.target = jd["targetPlatform"].ToString() == "A" ? BuildTarget.Android : BuildTarget.iOS;

        //打包路径 + 包名
        Debug.Log("包路径 ： " + jd["packagePath"] + jd["packageName"]);
        m_buildOption.locationPathName = jd["packagePath"].ToString() + jd["packageName"].ToString();

        //屏幕方向
        PlayerSettings.defaultInterfaceOrientation = UIOrientation.LandscapeLeft;

        //打包环境
        ApiCompatibilityLevel api = ApiCompatibilityLevel.NET_2_0;
        string apis = jd["APILevel"].ToString();
        if (!String.IsNullOrEmpty(apis))
        {
            if (apis.Contains("2_0_S"))
            {
                api = ApiCompatibilityLevel.NET_2_0_Subset;
            }
            else if (apis.Contains("2_0"))
            {
                api = ApiCompatibilityLevel.NET_2_0;
            }
            else if (apis.Contains("4_6"))
            {
                api = ApiCompatibilityLevel.NET_4_6;
            }
            else if (apis.Contains("Micro"))
            {
                api = ApiCompatibilityLevel.NET_Micro;
            }
            else if (apis.Contains("Web"))
            {
                api = ApiCompatibilityLevel.NET_Web;
            }
        }
        Debug.Log("API兼容 ：" + api.ToString());
        PlayerSettings.SetApiCompatibilityLevel
            (jd["targetPlatform"].ToString() == "A" ? BuildTargetGroup.Android : BuildTargetGroup.iOS, api);

        //Andriod 设置
        AndroidTargetDevice dev = AndroidTargetDevice.ARMv7;
        string devices = jd["AndroidTarget"].ToString();
        if (!String.IsNullOrEmpty(devices))
        {
            if (devices.Contains("FAT"))
            {
                dev = AndroidTargetDevice.FAT;
            }
            else if (devices.Contains("ARMv7"))
            {
                dev = AndroidTargetDevice.ARMv7;
            }
            else if (devices.Contains("x86"))
            {
                dev = AndroidTargetDevice.x86;
            }
        }
        Debug.Log("AndroidTargetDevice : " + dev.ToString());
        PlayerSettings.Android.targetDevice = dev;

        int bundleVersionCode = 63374379;
        int.TryParse(jd["AndroidBundleVersion"].ToString(), out bundleVersionCode);
        Debug.Log("AndroidBundleVersion : " + bundleVersionCode);
        PlayerSettings.Android.bundleVersionCode = bundleVersionCode;

        AndroidSdkVersions sdkV = AndroidSdkVersions.AndroidApiLevel19;
        string version = jd["AndroidSdkMinVersion"].ToString();
        try
        {
            sdkV = (AndroidSdkVersions)Enum.Parse(typeof(AndroidSdkVersions), version);
        }
        catch
        {
            Debug.Log("读取AndroidSdkVersions失败， 默认：AndroidApiLevel19");
        }
        Debug.Log("AndroidSdkMinVersion : " + sdkV.ToString());
        PlayerSettings.Android.minSdkVersion = sdkV;

        Debug.Log("keystoreName : " + jd["keystoreName"]);
        PlayerSettings.Android.keystoreName = jd["keystoreName"].ToString();

        Debug.Log("keyaliasName : " + jd["keyaliasName"]);
        PlayerSettings.Android.keyaliasName = jd["keyaliasName"].ToString();

        //密码
        Debug.Log("keyaliasPass : " + jd["keyaliasPass"]);
        PlayerSettings.keyaliasPass = jd["keyaliasPass"].ToString();
        Debug.Log("keystorePass : " + jd["keystorePass"]);
        PlayerSettings.keystorePass = jd["keystorePass"].ToString();

        Debug.Log("Read Build Config End !");
    }
}

///JsonData拓展类
public class JsonDataEx : LitJson.JsonData
{
    public new LitJson.JsonData this[string key]
    {
        get
        {
            try
            {
                return (this as JsonData)[key];
            }
            catch (Exception e)
            {
                Debug.LogError("The KEY : " + key + " 出错!!!  ||  " + e);
                return "";
            }
        }
        set
        {
            (this as JsonData)[key] = value;
        }
    }
}


