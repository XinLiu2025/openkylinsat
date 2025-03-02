[toc]

# 项目报告
# 仓库信息
本仓库为--2023全国大学生计算机系统能力大赛操作系统设计赛--系统功能赛道--选题238-openKylin操作系统安全分析工具--华南理工大学naus队--的选题仓库

## 目标描述
基于openkylin操作系统，编写一个可以检查客户机上安全基线和漏洞的程序，并可以由用户自己选择检查项目，最终用户可以看到可视化的报告。

## 功能演示视频

阿里云盘链接：演示视频.mp4
https://www.aliyundrive.com/s/GWiX9rnedQ2


提取码：w9jl
## 完成情况
1.题目1

功能一：实现系统安全配置基线检查	检查项覆盖操作系统通用安全需求(参考SCAP标准/等保安全配置基线标准),需生成可视化报告 ，已完成

功能二：安全基线检查给出修复建议		需生成可视化报告 ，已完成

功能三：实现基线检查项可配置	每项检测项可供配置，可根据配置文件/参数进行检查配置 ，已完成

功能四：实现模块化、跨平台 检查功能要求模块化，可通过命令行、命令交互或配置文件进行插拔使用，工具能够跨平台 ，已完成

2.题目2
功能一：实现安全漏洞（POC/EXP）检查功能	检查功能要求模块化，基于安全漏洞poc/exp检测 已完成

功能二：给出对应的系统安全漏洞的修复建议		需生成可视化报告 已完成

功能三：工具误报率小于10%		要求工具检测安全漏洞的准确率要高于90% 已完成

功能四：集成有效系统安全漏洞poc/exp数量达到200+		poc/exp能够通过模块化添加 部分完成，漏洞数目在50+

3.增加功能：

功能一：图形化界面显示报告，报告数据分析

功能二：基线，漏洞一键修复功能，可通过配置文件配置

功能三：图形化界面操作检测功能和修复功能


## 文档清单

### 安全基线检查其他文档
[安全基线检查开发文档和操作手册](基线检查/%E5%AE%89%E5%85%A8%E5%9F%BA%E7%BA%BF%E6%A3%80%E6%9F%A5%E5%BC%80%E5%8F%91.md)

[openkylin基线配置文档](基线检查/openkylin%E5%9F%BA%E7%BA%BF%E9%85%8D%E7%BD%AE%E6%96%87%E6%A1%A3.md)

### 漏洞检测其他文档
[漏洞检测操作手册](漏洞扫描/README.MD)

### 可视化报告其他文档
[可视化操作手册](检查报告可视化/%E6%A3%80%E6%9F%A5%E6%8A%A5%E5%91%8A%E5%8F%AF%E8%A7%86%E5%8C%96%E9%A1%B9%E7%9B%AE%E5%BC%80%E5%8F%91.md)

## 比赛题目分析和相关资料调研
版本信息：
openkylin操作系统统一使用优麒麟22.04增强版：

![image](/uploads/b7d7eac342ed8a8340b799dd02dd1467/image.png)


<center> 

图1 优麒麟版本信息 

</center>

下载路径如下：
[unbuntukylin](https://www.ubuntukylin.com/downloads/)

后端项目，统一采用python3.10，django 4.1.7 （如果有用到框架比如vue，bootstrap 须在issue或者readme中注明)

参考网址：

[genmai](https://gitee.com/openkylin/genmai)

[LinEnum](https://github.com/rebootuser/LinEnum)

[linuxprivchecker](https://github.com/sleventyeleven/linuxprivchecker)

[linux-exploit-suggester](https://github.com/The-Z-Labs/linux-exploit-suggester)


1.安全基线检查脚本
将不同的安全基线分别写成配置文件，
再写一个解析该配置文件检查的脚本，
将检查情况录入json文件，向后端发送，
后端收到json，将检查结果可视化，
根据检查结果，查询建议数据库，给出建议

2.漏洞检测
流程与检查类似
分析漏洞的yaml文件，提取并整合出测试poc方法

3.可视化页面
在用户使用时，可以在麒麟操作系统上启动该项目（最好项目文件不需要配置其他环境 下载可用）
用户运行脚本后，服务器收到json文件并将结果展示，给出建议

![image](/uploads/800d55a18bf91b12391fb17ac6aba104/image.png)

  <center>

  图2 题目要求

  </center>

该题实际上涉及到了麒麟操作系统的各项服务，需要对linux命令，常见的安全基线标准，常见的漏洞有一定的了解，同时要使用到web编程或者图形化编程之类的知识去完成可视化报告的呈现，综合考察了学生对于操作系统底层原理，对于图形化界面设计的理解与应用。


## 系统框架设计

### 总体框架设计

<img src="readme_src/总体项目架构.png" width="100%">

    
<center>

图3 总体框架设计

</center>

总体框架如图3所示，项目总体流程如下：

1.用户通过登录麒麟操作系统，下载项目，通过命令行运行django服务器，即可从网页访问历史报告记录

2.用户可以通过查看检查项目配置文件，安全基线检查配置文件为Baseline.yaml,漏洞检查配置文件为SystemPOC.yaml,KernelPOC.yaml等文件进行查看已有检查项目，通过检查说明手册来决定增加或者减少某个检查项目。在确认好检查项目后，用户可以通过命令行运行脚本，对应结果将存储在本地result文件中，同时django服务端将收到本次检查结果报告。

3.用户可以在django服务器上查看安全检查分数，安全检查项目建议，如果想要获得更详细的内容可以在安全基线检查手册上查看每个项目的运行原理，每个项目的安全等级，完整解决方案等。


### 各部分设计思路：

#### 安全基线检查和修复：



<img src="readme_src/baseline/baseline架构.png" width="60%">
<img src="readme_src/baseline/BASELINE修复架构.png" width = "60%">


<center>
    
图4 安全基线检查和修复项目架构设计
    
</center>

安全基线检查项目设计如图4所示 ， 安全基线检查项目设计说明如下：

1.用户进入安全基线检查/baseline/data/Baseline.yaml中查看配置项目文件，通过查看基线项目配置手册了解配置项目编号对应具体项目信息，确定需要的检查项目，完成项目配置

2.用户通过运行/baseline/pythoncode/baseline_check.py文件对本地主机进行检查，脚本首先检查配置文件，根据配置文件到/baseline/data/Baseline 文件夹下查看具体某个检查项目的运行配置参数，运行对应检查脚本，获取检查结果，生成建议并存储到检查结果中。

3.检查后可以在result文件夹下查看检查结果的json/yaml文件，同时脚本会将本次检查结果法相django服务器端，可以通过服务器端报告记录进行查看

安全基线修复项目设计如下：
1.用户进入安全基线检查/baseline/repair_code/repair.yaml中查看修复配置项目文件，通过查看基线项目配置手册了解配置项目编号对应具体项目信息，确定需要的修复项目，完成修复项目配置

2.用户通过运行/baseline/pythoncode/repair_baseline.py文件对本地主机进行修复，脚本首先检查配置文件，根据配置文件到/baseline/repair_code 文件夹下查看具体某个修复项目的运行配置参数，运行对应修复脚本，获取修复结果，并存储到结果文件中。

3.检查后可以在result文件夹下查看检查结果的json/yaml文件，同时脚本会将本次修复结果发向服务器端，可以通过服务器端报告记录进行查看

#### 漏洞检测

<img src="readme_src/poc/结构.png" width="60%">

<center>
    
图5 漏洞检测项目设计
    
</center>

漏洞检测项目设计如图5所示 ， 漏洞检测项目设计说明如下：

1.安装沙盒

1.使用沙盒运行poc文件目录下的kernelpoc_detect.py和systempoc_detect.py

2.等待检测完成

3.将检测结果发送至前端界面

4.将检测结果本地留档存于kernelpoc.json和systempoc.json文件

5.若用户需要进行漏洞修复，运行poc文件目录下的kernelpoc_repair.py和systempoc_repair.py

本项目的漏洞来源于genmai项目

本项目使用的漏洞表：

内核漏洞：

- CVE-2021-2255：

    漏洞描述：Linux 内核中 netfilter 子系统中的兼容 IPT_SO_SET_REPLACE/IP6T_SO_SET_REPLACE setsockopt 实现允许本地用户通过用户命名空间获得权限或导致拒绝服务（堆内存损坏）CVE-2016-3134 （CVSSv3 8.4 High） 和 CVE-2016-4997 （CVSSv3 7.8 High） 非常相似。
    
    漏洞利用和验证：可以通过部分覆盖结构的指针并实现释放后使用来利用此漏洞。这足以在绕过KASLR，SMAP和SMEP的同时获得内核代码执行，m_list->nextmsg_msg。在本项目的漏洞利用程序通过pipe-primitive实现。在执行利用程序后检测id如果为uid=0(root)则证明该漏洞未被修补。

- CVE-2022-2588:
    
    漏洞描述:在Linux 内核的 net/sched/cls_route.c 实现的 route4_change 中发现了一个存在 use-after-free 缺陷漏洞，该漏洞源于释放后重用，本地攻击者利用该漏洞会导致系统崩溃，可能会造成本地特权升级问题。

    漏洞利用和验证:漏洞利用代码利用这两个双重释放功能来演示对任务凭据（即将推出的 kmalloc-192 双重释放）和打开文件凭据（利用 kmalloc-256 双重释放）的攻击。执行漏洞利用程序输出结果为success即为漏洞验证成功。

- CVE-2022-2639：

    漏洞描述：在 openvswitch 内核模块中发现整数强制错误。给定足够多的操作，在为新流的新操作复制和预留内存时，reserve_sfa_size（） 函数不会按预期返回 -EMSGSIZE，这可能会导致越界写入访问。此缺陷允许本地用户崩溃或可能提升其在系统上的权限。

    漏洞利用和验证:执行漏洞利用程序后输入whoami，若结果为root表示系统中存在此漏洞。

    漏洞修复原理：修复openvswitch中的reserve_sfa_size（）中的OOB访问给定足够多的操作，在复制和为新流的新操作保留内存，如果next_offset大于MAX_ACTIONS_BUFSIZE，函数 reserve_sfa_size（） 确实没有按预期返回 -EMSGSIZE，但它分配了MAX_ACTIONS_BUFSIZE字节actions_len增加 req_size。然后，这可能会导致OOB写入访问权限，尤其是在需要复制进一步操作时，通过重新排列流操作大小检查来修复它。
    
- CVE-2022-0847:

    漏洞描述：在 Linux 内核中的 copy_page_to_iter_pipe 和push_pipe函数中，新管道缓冲区结构的“flags”成员缺乏正确的初始化方式中发现了一个缺陷，因此可能包含过时的值。非特权本地用户可利用此缺陷写入由只读文件支持的页面缓存中的页面，从而提升其在系统上的权限。

    漏洞利用和验证:使用Max Kellermann对Dirty Pipe的运用，但修改为覆盖/etc/passwd中的root密码字段，并在弹出根shell后恢复。即执行漏洞利用程序后，输入whoami结果为root

- CVE-2021-4204:

    漏洞描述：由于输入验证不正确，在Linux内核的eBPF中发现了越界（OOB）内存访问缺陷。此漏洞允许具有特殊权限的本地攻击者使系统崩溃或泄漏内部信息

    漏洞利用和验证:v5.8 ≤ linux-kernel ≤ 5.16被影响，执行漏洞利用程序后输入whoami结果为root即为成功。
    
- CVE-2022-24122:

    漏洞描述：Linux kernel 5.14至5.16.4版本存在内存错误引用漏洞，该漏洞源于名称空间被禁用后，ucounts对象依然存在。当非权限用户的名称空间被启用时，攻击者可利用该漏洞提升权限。

    漏洞利用和验证:v5.14-v5.16.4，当接受到输出[!] DESTROYED SHARED MEMORY后输入whoami结果为root即为成功
    
- CVE-2022-1679:

    漏洞描述： Linux kernel 存在安全漏洞，该漏洞源于在Athero无线适配器驱动程序发现了一个释放后重用缺陷，用户强制 ath9k_htc_wait_for_target 函数失败并显示一些输入消息。攻击者利用该漏洞提升系统上的权限。

    漏洞利用和验证: Linux kernel 5.10版本被影响，执行检测程序得到">?:mitigation completed you are now save from CVE 2022-1679"即为成功。
    
- CVE-2022-32250:

     Linux kernel 5.18.1版本及之前版本存在安全漏洞，该漏洞源于net/netfilter/nf_tables_api.c允许本地用户将权限升级为root用户，攻击者利用该漏洞可导致释放后重用。

    漏洞利用和验证:kernel(<=5.18.1s)，当利用程序被执行后输出I am root，输入whoami如果结果为root即为成功
    
- CVE-2022-23222:

    漏洞描述： 由于 Linux 内核的 BPF 验证器存在一个空指针漏洞，没有对 *_OR_NULL 指针类型进行限制，允许这些类型进行指针运算。攻击者可利用该漏洞在获得低权限的情况下，构造恶意数据执行空指针引用攻击，最终获取服务器 root 权限。

    漏洞利用和验证:  kernel(>=5.8 && <=5.16)，当利用程序被执行后输出enjoy root，输入whoami如果结果为root即为成功
    
- CVE-2022-0185:

    漏洞描述： Linux kernel 存在输入验证错误漏洞，该漏洞源于在 Linux kernel 的 Filesystem Context 中的 legacy_parse_param 函数验证提供的参数长度的方式中发现了一个基于堆的缓冲区溢出缺陷。 非特权（在启用非特权用户命名空间的情况下，否则需要命名空间的 CAP_SYS_ADMIN 特权）本地用户能够打开不支持文件系统上下文 API 的文件系统（因此回退到遗留处理）可以使用此缺陷来提升他们在系统上的权限。

    漏洞利用和验证:Linux kernel 5.1-rc1~5.16.2.当利用程序被执行后输入whoami如果结果为root即为成功。
    
- CVE-2021-26708:

    漏洞描述：Linux kernel 5.10.13之前版本存在本地权限提升漏洞。该漏洞源于net/vmw_vsock/af_vsock.c中的错误锁定导致AF_VSOCK实现中的多个竞争条件。目前没有详细的漏洞细节提供。

    漏洞利用和验证:v5.5 ≤ linux-kernel ≤ 5.10.13，当利用程序被执行后输出waitting for sshd，输入id如果结果为uid=0(root) gid=0(root) groups=0(root)即为成功
    

系统漏洞:

- CVE-2022-0714:

    漏洞描述： Heap-based Buffer Overflow in GitHub repository vim/vim prior to 8.2.4436.

    漏洞利用和验证: vim < 8.2.4436，执行命令：vim -u - NONE -i - NONE -n -X -Z -e -m -s -S CVE-2022-0714 -c ":qa!"如果有输出"aleph="即为成功

    
- CVE-2023-0054:

    漏洞描述： GitHub仓库vim/vim在9.0.1145之前版本存在越界写入。

    漏洞利用和验证: vim < 9.0.1145，执行命令：vim -u - NONE -i - NONE -n -X -Z -e -m -s -S CVE-2023-0054.dat -c ":qa!"如果有输出"signal: aborted (core dumped)"即为成功

    
- KVE-2022-0206:

    漏洞描述： org.ukui.kds方法toggleCameraDevice接口存在命令注入漏洞。普通用户可以以root权限执行任意命令

    漏洞利用和验证: kylin-display-switch< 3.0.13，执行KVE-2022-0206.sh后出现结果"successfully"即为成功
    
- KVE-2022-0231:

    漏洞描述：该软件包未对导入文件操作的合法性进行严格限制，因此造成系统配置文件所在目录被导入非法配置文件，从而造成普通用户本地权限提升。

    漏洞利用和验证:kylin-activation < 1.3.11-23、kylin-activation < 1.30.10-5.p23，执行KVE-2022-0231.sh后出现"successfully"即为成功

    
- KVE-2022-0210:

    漏洞描述：com.kylin.software.properties.interface.setMainSource接口存在任意文件写入漏洞。实现方法是调用命令"cp file /etc/apt/sources.list"。但如果传递的参数为"['-t /etc /path/to/evil.txt']，由于开发者在实现时会将这个字符串按空格进行分割，并作为参数传递到cp命令，因此就会触发命令 "cp -t /etc /path/to/evil.txt /etc/apt/sources.list"，从而实现任意文件夹的任意文件写入，导致权限提升。任意命令。

    漏洞利用和验证:kylin-software-properties< 0.0.1-127，执行命令python3 KVE-2022-0210.py后结果为"successfully"即为成功
    
- KVE-2022-0207:

    漏洞描述：com.kylin.software.properties.interface.changedSource接口存在任意文件写入漏洞。可任意替换文件任意行内容。导致权限提升。

    漏洞利用和验证:kylin-software-properties< 0.0.1-127，执行命令python3 KVE-2022-0207.py后结果为"successfully"即为成功
      
- KVE-2022-0205:

    漏洞描述： com.kylin.assistant.systemdaemon服务的restore_all_sound_file方法存在路径穿越，导致任意文件写入，导致权限提升。

    漏洞利用和验证: youker-assistant< 3.0.2-0kylin6k64~rc2，执行命令python3 KVE-2022-0205.py.py后结果为"restore_all_sound_file.txt"即为成功

- CVE-2022-1292:

    漏洞描述： OpenSSL 存在操作系统命令注入漏洞，该漏洞源于c_rehash 脚本未正确清理 shell 元字符导致命令注入。攻击者利用该漏洞执行任意命令。

    漏洞利用和验证:   OpenSSL 1.0.2、OpenSSL 1.1.1、OpenSSL 3.x，执行命令 CVE-2022-1292.sh后结果为"System is Vulnerable! Please fix asap"即为成功

    
- CVE-2021-44142:

    漏洞描述：Samba官方发布安全公告，4.13.17之前的所有Samba 版本中存在一个代码执行漏洞（CVE-2021-44142），该漏洞存在于Samba中vfs_fruit模块的默认配置中，在smbd解析EA元数据时，对文件扩展属性具有写访问权限的远程攻击者（可以是guest或未认证用户）可越界写入并以root身份执行任意代码。

    漏洞利用和验证: 4.13.x < Samba < 4.13.17、4.14.x < Samba < 4.14.12、4.15.x < Samba < 4.15.5，执行命令python3 CVE-2021-44142.py "127.0.0.1" "445" TimeMachineBackup root后结果为"successful"即为成功

    
- CVE-2021-3560:

    漏洞描述：Polkit（PolicyKit）是类Unix系统中一个应用程序级别的工具集，通过定义和审核权限规则，实现不同优先级进程间的通讯。pkexec是Polkit开源应用框架的一部分，可以使授权非特权用户根据定义的策略以特权用户的身份执行命令。发现polkit可能被欺骗，绕过D-Bus请求的凭据检查，将请求者的权限提升到root用户。

    漏洞利用和验证:0.105 ≥ policykit ≥ 0.113，执行命令python3 CVE-2021-3560.py后等待输出"bash: no job control in this shell"输入whoami，结果为root时成功
    
- CVE-2021-4034:

    漏洞描述：polkit pkexec 中对命令行参数处理有误，导致参数注入，能够导致本地提权。pkexec应用程序为Linux系统预装工具，攻击者可通过构造特定的参数诱导pkexec执行任意代码，从而获取本地管理员权限。
    ScopeOfInfluence:


    漏洞利用和验证: 2009年5月至2022年1月发布的所有 Polkit 版本，执行命令python3 CVE-2021-4043.py后等待输出"[+] Calling execve()"输入whoami，结果为root时成功
    
- CVE-2021-3156：

    漏洞描述： Sudo 是一个用于类 Unix 计算机操作系统的程序，它能够使用户能够以另一个用户（默认是超级用户）的安全权限运行程序。sudoedit 功能用于以另外一个用户身份编辑文件。Sudo before 1.9.5p2 存在缓冲区错误漏洞，攻击者可使用sudoedit -s和一个以单个反斜杠字符结束的命令行参数升级到root。

    漏洞利用和验证: 小于1.9.5p2，执行命令 CVE-2021-3156.sh后输出 "sudoedit; /: not a regular file"即为成功
    
- CVE-2022-0543：

    漏洞描述：Debian 以及 Ubuntu 发行版的源在打包 Redis 时，不慎在 Lua 沙箱中遗留了一个对象package，攻击者可以利用这个对象提供的方法加载动态链接库 liblua 里的函数，进而逃逸沙箱执行任意命令。我们借助 Lua 沙箱中遗留的变量package的loadlib函数来加载动态链接库/usr/lib/x86_64-linux-gnu/liblua5.1.so.0里的导出函数luaopen_io。在 Lua 中执行这个导出函数，即可获得io库，再使用其执行命令。

    漏洞利用和验证:2.2 <= redis < 5.0.13，执行命令python3 CVE-2022-0543.py后输入whoami，结果为root时成功
    
- CVE-2021-41773：

    漏洞描述：Apache 披露了一个在 Apache HTTP Server 2.4.49 上引入的漏洞，称为 CVE-2021-41773。同时发布了2.4.50更新，修复了这个漏洞。该漏洞允许攻击者绕过路径遍历保护，使用编码并读取网络服务器文件系统上的任意文件。运行此版本 Apache 的 Linux 和 Windows 服务器都受到影响。此漏洞是在 2.4.49 中引入的，该补丁旨在提高 URL 验证的性能。可以通过对“.”进行编码来绕过新的验证方法。如果 Apache 网络服务器配置未设置为“要求全部拒绝”，则漏洞利用相对简单。通过对这些字符进行编码并使用有效负载修改 URL，可以实现经典的路径遍历。

    漏洞利用和验证: Apache HTTP = 2.4.49，执行命令python3 CVE-2021-41773.py "127.0.0.1"后输出”Server 127.0.0.1 IS VULNERABLE“时成功
    
- CVE-2022-0417：

    漏洞描述：vim存在安全漏洞，该漏洞源于这个漏洞允许攻击者可利用该漏洞输入一个特别制作的文件，导致崩溃或代码执行。

    漏洞利用和验证:vim < 8.2.4245，执行命令：vim -u - NONE -i - NONE -n -X -Z -e -m -s -S CVE-2022-0417 -c ":qa!"如果有输出"0"即为成功
    
- CVE-2022-0359：

    漏洞描述： vim 存在安全漏洞，该漏洞源于在8.2之前的vim中基于堆的缓冲区溢出。

    漏洞利用和验证: vim < 8.2，执行命令：vim -u - NONE -i - NONE -n -X -Z -e -m -s -S CVE-2022-0359 -c ":qa!"如果有输出"signal: aborted (core dumped)"即为成功
    
- CVE-2022-0413：

    漏洞描述：vim 存在资源管理错误漏洞，该漏洞源于这个漏洞允许攻击者可利用该漏洞输入一个特别制作的文件，导致崩溃或代码执行。

    漏洞利用和验证:vim < 8.2，执行命令：vim -u - NONE -i - NONE -n -X -Z -e -m -s -S CVE-2022-0413 -c ":qa!"如果有输出"signal: aborted (core dumped)"即为成功
    
- CVE-2022-0572：

    漏洞描述：vim 存在安全漏洞，该漏洞源于在8.2之前的GitHub库vim中基于堆的缓冲区溢出

    漏洞利用和验证:vim < 8.2，执行命令：vim -u - NONE -i - NONE -n -X -Z -e -m -s -S CVE-2022-0572 -c ":qa!"如果有输出"signal: segmentation fault (core dumped)"即为成功
    
- CVE-2022-0685：

    漏洞描述：vim 8.2.4418之前版本存在安全漏洞，该漏洞源于vim中使用超出范围的指针偏移量。

    漏洞利用和验证:vim < 8.2.4418，执行命令：vim -u - NONE -i - NONE -n -X -Z -e -m -s -S CVE-2022-0685 -c ":qa!"如果有输出"signal: segmentation fault (core dumped)"即为成功
    
- CVE-2022-0729：

    漏洞描述：Vim 中存在缓冲区错误漏洞，该漏洞源于产品 src/regexp_bt.c 文件未对内存边界进行有效检查。攻击者可通过该漏洞导致缓冲区溢出。以下产品及版本受到影响：Vim 8.2.4440 之前版本。

    漏洞利用和验证:vim<8.2.4440，执行命令：vim -u - NONE -i - NONE -n -X -Z -e -m -s -S CVE-2022-0729 -c ":qa!"如果有输出"signal: segmentation fault (core dumped)"即为成功
    
- CVE-2022-1771：

    漏洞描述： Vim 8.2.4975 之前版本存在安全漏洞，该漏洞源于可能存在基于堆栈的缓冲区溢出问题。

    漏洞利用和验证: vim < 8.2.4975，执行命令：vim -u - NONE -e  -s -S CVE-2022-1771 如果有输出"signal: segmentation fault (core dumped)"即为成功
    
- CVE-2022-2598：

    漏洞描述：Vim 9.0.0100 之前版本存在安全漏洞，该漏洞源于 API 输入的未定义行为。

    漏洞利用和验证:vim<9.0.0100，执行命令：vim -u - NONE -i - NONE -n -X -Z -e -m -s -S CVE-2022-2598 -c ":qa!"如果有输出"signal: segmentation fault (core dumped)"即为成功
    
- CVE-2019-7304: 

    漏洞描述：snapd 2.28到2.37错误地验证并解析了远程套接字在UNIX套接字上执行访问控制时的地址。一个本地攻击者可以使用它来访问特权套接字API并获得管理员特权。

    漏洞利用和验证: Snapd < 2.37.1、Ubuntu_linux 14.04 LTS、Ubuntu_linux 16.04 LTS、Ubuntu_linux 18.04 LTS、Ubuntu_linux 18.10，执行命令：python3 CVE-2019-7304.py后结果为”Success! You can now `su“即为成功

    
- CVE-2019-18634:

    漏洞描述：在 1.8.26 之前的 Sudo 中，如果在 /etc/sudoers 中启用 pwfeedback，用户可以在特权 sudo 进程中触发基于堆栈的缓冲区溢出。（pwfeedback 是 Linux Mint 和 elementary OS 的默认设置；然而，它不是上游和许多其他包的默认设置，并且只有在管理员启用时才会存在。）攻击者需要向标准输入传递一个长字符串tgetpass.c 中的 getln()。权套接字API并获得管理员特权。

    漏洞利用和验证:sudo < 1.8.26,执行命令：python3  CVE-2019-18634.py后等待输出为”interactive mode“时输入whoami返回为root即为成功
    
- CVE-2022-3602:

    漏洞描述： Openssl 3.0.x版本在X.509证书验证过程中存在4个字节的邮箱地址缓存溢出问题，可能导致内存损坏，攻击者可能能够在执行计算的计算机上触发远程代码执行。

    漏洞利用和验证:openssl 3.0.0~openssl 3.0.6,执行命令：python3 CVE-2022-3602.py -t 127.0.0.1:3000后等待输出为”Vulnerable“即为成功
    
- CVE-2023-0051:

    漏洞描述： GitHub存储库vim/vim在9.0.1144之前存在基于堆的缓冲区溢出

    漏洞利用和验证: vim < 9.0.1144,执行命令：vim -u - NONE -i - NONE -n -X -Z -e -m -s -S CVE-2023-0051 -c ":qa!" 如果有输出"be killed"即为成功
    
- CVE-2023-0288:

    漏洞描述：GitHub存储库vim/vim在9.0.1182版本存在堆buffer溢出漏洞。

    漏洞利用和验证:vim < 9.0.1182,执行命令：vim -u - NONE -i - NONE -n -X -Z -e -m -s -S CVE-2023-0288.dat -c ":qa!" 如果有输出"signal: segmentation fault (core dumped)"即为成功
    


#### 可视化界面

##### 系统功能需求分析

主要功能为接收扫描结果并生成可视化页面。

##### 系统设计及实现思路

系统设计包括三部分：数据库设计，前端页面设计，视图函数设计。

1. **数据库设计**

    根据功能及扫描结果数据格式，数据库设计如下图：

    <div align="center">
    <img src="readme_src/ReportVisual/database.png" width="60%">
    <div>图6 数据库设计uml图</div>
    </div>

      - 历史记录表：AllRecord
  
      - 基线扫描结果逐项表：BaselineTestRes
   
      - 内核漏洞扫描结果逐项表：KernelPocRes
  
      - 系统漏洞扫描结果逐项表：SystemPocRes

2. **页面及功能设计**

    设计如下四个页面:

    <div align="center">
    <img src="readme_src/ReportVisual/design.jpg" width="60%">
    <div>图7 页面功能分配图</div>
    </div>

    - 工作台页面

        本页面需要展示历史检查记录、实现站内导航、实现检查功能的调用。

    - 基线检查报告页面

        本页面需要展示检查结果详情、实现站内导航、实现基线检查修复功能的调用。

    - 漏洞检查报告页面

        本页面需要展示检查结果详情、实现站内导航、实现漏洞检查修复功能的调用。

    - 功能说明页面

        本页面需要展示各功能的说明并实现站内导航。

3. **视图函数设计**
   
   对于设计的四个页面，分别分配路由，并设计视图函数，从数据库中查询相应数据，并将数据显示到页面中。

   另分配六个路由及相应视图函数，分别用于接收基线检查、内核漏洞检查、系统漏洞检查的检查结果及修复结果，并存入对应数据库中。

## 开发计划
### 第一阶段（5月10日—5月14日）

总体任务：完成本项目初版设计，通过http接口接收存储安全检查结果的yaml文件，并将检查结果内容展示到页面中，写中期检查报告。

* 5月10日
  
  * 进行初版功能需求分析。

    本项目需要分别接收存储安全基线检查结果和安全漏洞检查结果的yaml文件，并将文件内容展示到页面中。

    故设计两个页面，分别用于展示安全基线检查结果、安全漏洞检查结果。
  
  * 了解安全基线的定义
    
    每个组织都会面临安全威胁。 但是，一个组织最关心的安全威胁类型可能不同于另一个组织。 例如，电子商务公司可能专注于保护其面向 Internet 的 Web 应用，而医院可能专注于保护患者的机密信息。 所有组织共有的需求是使其应用和设备保持安全。 这些设备必须符合由组织定义的安全标准（或安全基线）。

    安全基线是一组固定类型用户建议的配置设置，用于解释其安全隐患。 这些设置基于来自安全工程团队、产品组、合作伙伴和客户的反馈。 

  * 对接收数据的http接口分发路由。

    使用路由“baseline_test/”接收安全基线检查结果，使用路由“vulnerability_test/”接收安全漏洞检查结果。

* 5月11日

  * 设计检查单个项目配置文件，检查项目总体配置文件，和检查结果文件的yaml格式，示例如下
    ```yaml
    Belong: 2账号口令
    FormatVer: 20230523
    Id: '2_1'
    Power: root
    SiteInfo:
      Name: 检查是否以设置口令生存周期
    SiteRequests:
      Implement:
        Condition: None
        ImArray:
        - Args: null
          Exec: ../data/BaseLine/shellcode/2/2_1.sh
        Inter:
        - ''
    ```
    ```yaml
    CheckTime: '2023-05-25  15:32:38'
    Hostname: yujiahong-vmwarevirtualplatform
    ScanProject:
    - Advice: 长期不修改密码会增加密码暴露风险，除入域服务器或服务器超管账号分段管理无需配置外，应对服务器密码最长使用期限进行限制。此检查项建议调整<=90
      Belong: 2账号口令
      Id: '2_1'
      JudgeResult: FAIL
      Result: '99999'
      SiteInfo_Name: 检查是否以设置口令生存周期
    - Advice: 密码复杂度过低会增加密码被爆破风险，按照企业密码管理要求与等级保护标准，密码复杂度应包含特殊字符、大小写字母。此检查项建议调整至少有1个大写字母、1个小写字母、1个数字、1个特殊字符
      Belong: 2账号口令
      Id: '2_4'
      JudgeResult: FAIL
      Result: 'null'
    ```




  * 进行基于python的检查主程序识别yaml配置测试
    基于本项目已约定的yaml文件格式，分别读取存储安全基线检查配置项目和安全漏洞检查配置项目的yaml文件信息。

    经过测试，yaml文件读取成功。

  * 进行yaml文件的读取测试。

    基于本项目已约定的yaml文件格式，分别读取存储安全基线检查结果和安全漏洞检查结果的yaml文件，并将其中内容存放在变量中输出到控制台。

    经过测试，yaml文件读取成功。
  
  * 完成初版视图函数的设计并分发路由。

    对于展示安全基线检查结果的页面分配路由“baseline”，使用视图函数读取存储安全基线检查结果的yaml文件，并将其中数据输出到控制台中。
    对于展示安全漏洞检查结果的页面分配路由“vulnerability”，使用视图函数读取存储安全漏洞检查结果的yaml文件，并将其中数据输出到控制台中。

* 5月12日
  * 设计好总体检查配置文件
        
    ```yaml
    ConfigFilePrefix: ../data/BaseLine/
    Type: baseline
    ExplorerItems:
      - ConfigFile: UserAnalysis/checkUser.yaml #检测root权限用户
      - ConfigFile: UserAnalysis/checkGid.yaml #检测特权组用户

    ```

  * 完成初版页面内容的编写。

    对于展示安全基线检查结果的页面和展示安全漏洞检查结果的页面，设计模板文件，并将视图函数中的数据传入模板文件中进行显示。

* 5月13日-5月14日
  * 约定检查程序文件目录
    ```
    ─安全基线检查 ------ 存储安全基线检查的脚本和检查项目数据库
    ├─data.yaml
    ├─openkylin基线配置文档.md  ------- 基线配置文档，可以在里面获取检查基线项目的具体内容，检测命令，修复建议等等。
    ├─requirements.txt   ------ 运行脚本需要的库及对应版本
    ├─安全基线检查开发.md   ------ 该部分的开发记录，说明文档
    ├─baseline  ------ 存储代码
    |    ├─tmp  ------  存储运行时产生的临时文件
    |    ├─result ------- 存储检测结果文件，有yaml和json格式
    |    |   ├─data.json
    |    |   └data.yaml
    |    ├─pythoncode  ------- 存储运行的主要python脚本，自动生成配置数据库，检测脚本的jupyter脚本
    |    |     ├─baseline_check.py
    |    |     └mainpro.ipynb
    |    ├─data  ------ 存储检测项目配置文件，检测项目配置数据库，检测脚本数据库
    |    |  ├─Baseline
    |    |  |    ├─Baseline.rar ------ 配置文件备份压缩包
    |    |  |    ├─BaseLine.yaml ------ 配置文件
    ```
  
  * 编写python测试脚本
    ```python

    import yaml
    import os
    import datetime
    import socket
    import re

    def readyaml(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            data = yaml.load(stream=f, Loader=yaml.FullLoader)
            print("format{}".format(type(data)))
            return data
    def initilizeyamldata():
        #

        #构造yaml文件
        #初始化空字典
        yamldata = {}
        #1获取系统时间
        nowtime = datetime.datetime.now()
        yamldata['CheckTime'] = nowtime.strftime('%Y-%m-%d')
        #2获取主机名称
        hostname = socket.gethostname()
        yamldata['Hostname'] = hostname
        #3获取扫描种类
        yamldata['ScanType'] = 'BaseLine'
        #4获取扫描信息返回结果
        yamldata['ScanProject'] = []
        
        
    def writeyaml(data):
        #curpath = os.path.dirname(os.path.realpath(__file__))
        yamlpath ="../result/data.yaml"
        # 写入到yaml文件
        with open(yamlpath, "w", encoding="utf-8") as f:
            yaml.dump(data, f, allow_unicode=True)
        
    def printproinfo(proinfo):
        print("打印本次检查项目信息")
        print("FormatVer:{}".format(proinfo['FormatVer']))
        print("Id:{}".format(proinfo['Id']))
        print("Belong:{}".format(proinfo['Belong']))
        print("SiteInfo:{}".format(proinfo['SiteInfo']['Name']))
        print("Power :{}".format(proinfo['Power']))
    ```
    readyaml函数读取yaml文件，initializeyamldata负责初始化结果文件，wirteyaml负责写入结果yaml，printproinfo负责测试打印项目信息。
  * 完善初版页面样式。

    页面效果如图8。

    <div align="center">
    <img src="readme_src/ReportVisual/页面初版效果图.png" width="60%">
    <div>图8 初版页面样式图</div>
    </div>

  * 对项目进行整体测试。

    经过在虚拟机上的测试，本项目能基本完成所需功能。

### 第二阶段（5月15日-5月21日）

总体目标：根据需求，设计数据库存储检查结果数据，并完善本项目所需功能及页面的设计。

* 5月15日-5月16日
  * 编写第二章检查配置文件和脚本，编写第二章基线检查手册
  ```yaml
  Belong: 2账号口令
  FormatVer: 20230523
  Id: '2_2'
  Power: root
  SiteInfo:
    Name: 检查是否设置口令最小长度
  SiteRequests:
    Implement:
      Condition: None
      ImArray:
      - Args: null
        Exec: ../data/BaseLine/shellcode/2/2_2.sh
      Inter:
      - ''
  ```
  ```bash
  #"账号口令-2.1：检查是否设置口令生存周期"
  index=$(($index+1))
  #在文件etc/login.defs中搜索pass_max_days的值，并且去掉#自开头的值
  passmax=`cat /etc/login.defs | grep PASS_MAX_DAYS | grep -v ^#`
  if [ -n "$passmax" ]; then
    days=`echo $passmax | awk '{print $2}'`
    if [ "$days" -gt 90 ]; then
      echo "	长期不修改密码会增加密码暴露风险，除入域服务器或服务器超管账号分段管理无需配置外，应对服务器密码最长使用期限进行限制。此检查项建议调整	<=90	$days	FAIL	 	 "
      fail=$((fail+1))
    else
      pass=$(($pass+1))
      echo "	长期不修改密码会增加密码暴露风险，除入域服务器或服务器超管账号分段管理无需配置外，应对服务器密码最长使用期限进行限制。此检查项建议调整	<=90	$days	TRUE	 	 "
    fi
  else
    fail=$(($fail+1))
    echo "	长期不修改密码会增加密码暴露风险，除入域服务器或服务器超管账号分段管理无需配置外，应对服务器密码最长使用期限进行限制。此检查项建议调整	<=90	无此配置	FAIL	 	 "
  fi

  ```

  * 完善页面功能的需求分析。

    分别接收存储安全基线检查结果和安全漏洞检查结果的json数据，将结果数据存入数据库中，并展示历史检查记录统计结果和单次检查报告的详细信息。

  * 完善页面功能的分配。

    设计如图9的四个页面。

    <div align="center">
    <img src="readme_src/ReportVisual/安全检查报告功能分析.png" width="60%">
    <div>图9 页面功能分配图</div>
    </div>

    * 历史安全基线检查报告页面

        本页面需要实现接收数据、统计并展示历史检查记录的功能。

    * 历史安全漏洞检查报告页面

        本页面需要实现接收数据、统计并展示历史检查记录的功能，还需要实现页内导航，以便查看。

    * 单次安全基线检查报告页面

        本页面需要实现页内导航，并展示具体单次报告。

    * 单次安全漏洞检查报告页面

        本页面需要实现展示具体单次报告的功能。

* 5月17日-5月18日
  
  * 编写第三章检查配置文件和脚本，编写第三章基线检查手册
  ```yaml
  Belong: 3认证授权
  FormatVer: 20230523
  Id: '3_1_1'
  Power: root
  SiteInfo:
    Name: 检查/etc/csh.cshrc中umask设置
  SiteRequests:
    Implement:
      Condition: None
      ImArray:
      - Args: null
        Exec: ../data/BaseLine/shellcode/3/3_1_1.sh
      Inter:
      - ''

  ```
    
  ```bash
  #"认证授权-3.1.1:检查用户umask设置"
  #设置flag=1，若有一项不合格，则flag=0
  cd /etc
  umask1=`ls -a|cat csh.cshrc`
  #/bin/cat /etc/csh.cshrc | grep umask | /bin/awk -F 'umask' 'NR==1{print $2}'

  if [ -z "$umask1"];then
  echo "	umask配置后，创建系统用户时所赋予的权限为最高权限减去umask设置的权限，保证所创建用户不可创建其他权限用户。此检查项建议调整	077/027	null	TRUE"

  else
    if [ "$umask1" -eq 077 ] || [ "$umask1" -eq 027 ]; then
      echo "	umask配置后，创建系统用户时所赋予的权限为最高权限减去umask设置的权限，保证所创建用户不可创建其他权限用户。此检查项建议调整	077/027	$umask1	TRUE		"
    else
      echo "	umask配置后，创建系统用户时所赋予的权限为最高权限减去umask设置的权限，保证所创建用户不可创建其他权限用户。此检查项建议调整	077/027	$umask1	FAIL		"
    fi
  fi

  ```

  * 完成数据库设计。

    数据库设计如图10。

    <div align="center">
    <img src="readme_src/ReportVisual/数据库设计uml图.png" width="60%">
    <div>图10 数据库设计uml图</div>
    </div>
  
    安全基线扫描记录表：AllBaselineTestResRecord

    安全基线扫描结果逐项表：BaselineTestRes

    内核安全漏洞扫描记录表：AllKernelPocResRecord

    内核安全漏洞扫描结果逐项表：KernelPocRes

    系统安全漏洞扫描记录表：AllSystemPocResRecord

    系统安全漏洞扫描结果逐项表：SystemPocRes

* 5月19日-5月21日
  * 编写第四章检查配置文件和脚本，编写第四章基线检查手册
  ```yaml
  Belong: 4日志审计
  FormatVer: 20230523
  Id: '4_1'
  Power: root
  SiteInfo:
    Name: 检查是否配置远程日志功能
  SiteRequests:
    Implement:
      Condition: None
      ImArray:
      - Args: null
        Exec: ../data/BaseLine/shellcode/4/4_1.sh
      Inter:
      - ''
  ```
  ```bash
  #/var/log/secure"
  secure_file=`find /var/log/secure`
  if [ -n "$secure_file" ]; then
    secure=`stat -c %a /var/log/secure`
    if [ "$secure" -ge 755 ]; then
      echo "	应配置日志文件非全局可写，保证日至不可篡改。此检查项建议调整	>=755	$secure	TRUE		"
    else
      echo "	应配置日志文件非全局可写，保证日至不可篡改。此检查项建议调整	>=755	$secure	FAIL		"
      flag3=0
    fi
  else
    echo "	应配置日志文件非全局可写，保证日至不可篡改。此检查项建议调整	>=755	文件不存在	TRUE		"

  fi

  ```
  * 对各个页面重新分配路由并完成视图函数的编写。

    * 历史安全基线检查报告页面

        分配路由"",视图函数如下:

        ```python
        def baseline_test(request):
          queryset = models.AllBaselineTestResRecord.objects.all()
          return render(request, '../templates/reports/baseline_test.html', locals())
        ```

        该函数查询数据库中安全基线扫描记录表的所有记录，并传入html中显示出来。

    * 历史安全漏洞检查报告页面

      分配路由"vulnerability/",视图函数如下:

      ```python
      def vulnerability_test(request):
        SystemQueryset = models.AllSystemPocResRecord.objects.all()
        KernelQueryset = models.AllKernelPocResRecord.objects.all()
        return render(request, '../templates/reports/vulnerability_test.html', locals())
      ```

      该函数查询数据库中内核安全漏洞扫描记录表和系统安全漏洞扫描记录表的所有记录，并传入html中显示出来。

    * 单次安全基线检查报告页面

      分配路由"baseline_res/",视图函数如下:

      ```python
      def baseline_res(request):
          host_id = request.GET['id']
          record = models.AllBaselineTestResRecord.objects.filter(id=host_id)
          checkTime = record.first().checkTime
          hostName = record.first().hostName
          queryset = [list()] * 5
          querysetName = ['账号口令', '认证授权', '日志审计', '协议安全', '其他配置操作']
          circleRange = range(0, 5)
          ScanProjectNum = 0
          FalseNum = 0
          for i in circleRange:
              tempset = models.BaselineTestRes.objects.filter(host_id=host_id, belong=str(i + 2))
              ScanProjectNum += len(tempset)
              for item in tempset:
                  if not item.judgeResult:
                      FalseNum += 1
              queryset[i] = tempset
          setZip = zip(querysetName, queryset)
          return render(request, '../templates/reports/baseline_res.html', locals())
      ```

      该函数通过GET方式获取要显示的检查报告的主机ID（host_id），从安全基线扫描记录表中将该主机的扫描记录查询，在安全基线扫描结果逐项表查询该主机的逐项检查结果，并在for循环中计算未通过检查的项数，最后通过html页面展示结果。

    * 单次安全漏洞检查报告页面

        分配路由"vulnerability_res/",视图函数如下:

      ```python
      def vulnerability_res(request):
          host_id = request.GET['id']
          type = request.GET['type']
          record = []
          queryset = []
          scantype = ''
          if type == "KernelPoc":
              record = models.AllKernelPocResRecord.objects.filter(id=host_id)
              queryset = models.KernelPocRes.objects.filter(host_id=host_id)
              scantype = "内核漏洞"
          else:
              record = models.AllSystemPocResRecord.objects.filter(id=host_id)
              queryset = models.SystemPocRes.objects.filter(host_id=host_id)
              scantype = "系统漏洞"
          checkTime = record.first().checkTime
          hostName = record.first().hostName
          ScanProjectNum = len(queryset)
          FalseNum = 0
          for item in queryset:
              if item.checkResult == 1:
                  FalseNum += 1
          return render(request, '../templates/reports/vulnerability_res.html', locals())
      ```

      该函数通过GET方式获取要显示的检查报告的主机ID（host_id）、检查类型（内核漏洞KernelPoc或系统漏洞SystemPoc），从相应安全漏洞扫描记录表中将该主机的扫描记录查询，在相应安全漏洞扫描结果逐项表查询该主机的逐项检查结果，并在for循环中计算未通过检查的项数，最后通过html页面展示结果。

     * 接收安全基线扫描结果的接口
  
        分配路由"openkylin_scan_res_report/",视图函数如下:

        ```python
        def openkylin_scan_res_report(request):
            if request.method == "POST":
                data = request.body.decode("utf-8").replace("'", '"')
                json_data = json.loads(data)
                checkTime = json_data.get("CheckTime")
                hostName = json_data.get('Hostname')
                ScanProject = json_data.get("ScanProject")
                record = models.AllBaselineTestResRecord(checkTime=checkTime, hostName=hostName)
                record.save()
                for item in ScanProject:
                    judgeResult = False
                    if item['JudgeResult'] == 'TRUE':
                        judgeResult = True
                    belong = item['Belong'][:1]
                    tempItem = models.BaselineTestRes(host_id=record.id,
                                                      advice=item['Advice'],
                                                      belong=belong,
                                                      judgeResult=judgeResult,
                                                      result=item['Result'],
                                                      siteInfo_Name=item['SiteInfo_Name'])
                    tempItem.save()
                return redirect("/")
            else:
                return HttpResponse("0oops,something is wrong")
        ```

        该函数通过POST方式获取要安全基线检查结果的json数据，并将数据存入相应的数据库中，最后重定向回历史安全基线检查报告页面。

     * 接收内核安全漏洞扫描结果的接口
  
        分配路由"kernelpos_scan_res_report/",视图函数如下:

        ```python
        def kernelpos_scan_res_report(request):
            if request.method == "POST":
                data = request.body.decode("utf-8").replace("'", '"')
                json_data = json.loads(data)
                checkTime = json_data[0]["CheckTime"]
                hostName = json_data[1]['Hostname']
                record = models.AllKernelPocResRecord(checkTime=checkTime, hostName=hostName)
                record.save()
                for i in range(2, len(json_data)):
                    for key in json_data[i]:
                        checkResult = json_data[i][key]["CheckResult"]
                        solution = json_data[i][key]["solution"]
                        tempItem = models.KernelPocRes(host_id=record.id,
                                                      checkResult=checkResult,
                                                      solution=solution,
                                                      siteInfo_Name=key)
                        tempItem.save()
                return redirect("/vulnerability/")
            else:
                return HttpResponse("0oops,something is wrong")
        ```

        该函数通过POST方式获取要内核安全检查结果的json数据，并将数据存入相应的数据库中，最后重定向回历史安全漏洞检查报告页面。

     * 接收系统安全漏洞扫描结果的接口

        分配路由"kernelpos_scan_res_report/",视图函数如下:

        ```python
        def systempos_scan_res_report(request):
            if request.method == "POST":
                data = request.body.decode("utf-8").replace("'", '"')
                json_data = json.loads(data)
                checkTime = json_data[0]["CheckTime"]
                hostName = json_data[1]['Hostname']
                record = models.AllSystemPocResRecord(checkTime=checkTime, hostName=hostName)
                record.save()
                for i in range(2, len(json_data)):
                    for key in json_data[i]:
                        checkResult = json_data[i][key]["CheckResult"]
                        solution = json_data[i][key]["solution"]
                        tempItem = models.SystemPocRes(host_id=record.id,
                                                      checkResult=checkResult,
                                                      solution=solution,
                                                      siteInfo_Name=key)
                        tempItem.save()
                return redirect("/vulnerability/")
            else:
                return HttpResponse("0oops,something is wrong")
        ```

        该函数通过POST方式获取要系统安全检查结果的json数据，并将数据存入相应的数据库中，最后重定向回历史安全漏洞检查报告页面。

  * 检测http接口，通过http接口接收json数据，并将json数据存入数据库中。

  * 对各个页面进行逐一测试。

### 第三阶段（5月22日—5月28日）

总体目标：整理项目文件，完成使用报告的编写。

* 5.22-5.24
  * 编写第五章检查配置文件和脚本，编写第五章基线检查手册
  ```YAML
  Belong: 5协议安全
  FormatVer: 20230523
  Id: '5_1'
  Power: root
  SiteInfo:
    Name: 检查系统openssh安全配置
  SiteRequests:
    Implement:
      Condition: None
      ImArray:
      - Args: null
        Exec: ../data/BaseLine/shellcode/5/5_1.sh
      Inter:
      - ''


  ```
  ```BASH
  #"协议安全-5.1:检查系统openssh安全配置"
  index=$(($index+1))
  #if [ "$PermitRootLogin" = "no" ] && [ "$Protocol" -eq 2 ]; then
  if [ "$Protocol" -eq 2 ]; then
    pass=$(($pass+1))
  echo "	openssh是使用加密的远程登录实现，可以有效保护登录及数据的安全。此检查项建议调整	2	$Protocol	TRUE		"
  else
    echo "	openssh是使用加密的远程登录实现，可以有效保护登录及数据的安全。此检查项建议调整	2	null	FAIL		"
    fail=$(($fail+1))
  fi

  ```

  * 整理项目文件。
  * 在虚拟机上运行，对各个页面进行逐一测试。

* 5.25-5.28
  * 编写第六章
  ```yaml
  Belong: 6其他配置操作
  FormatVer: 20230523
  Id: '6_1'
  Power: root
  SiteInfo:
    Name: 检查是否设置命令行界面超时退出
  SiteRequests:
    Implement:
      Condition: None
      ImArray:
      - Args: null
        Exec: ../data/BaseLine/shellcode/6/6_1.sh
      Inter:
      - ''

  ```
  ```bash
  #"其他配置-6.1:检查是否设置命令行界面超时退出"
  index=$(($index+1))

  TMOUT=`cat /etc/profile |grep -i TMOUT | grep -v ^#`
  if [ -z "$TMOUT" ]; then
    echo "	根据等保要求，建议设置超时时间不大于	<=600	null	FAIL		"
    fail=$(($fail+1))
  else
  #echo "$TMOUT"
    if [ "$TMOUT" -gt 600 ]; then
    echo "	根据等保要求，建议设置超时时间不大于	<=600	$TMOUT	FAIL		"
      fail=$(($fail+1))
    else
    echo "	根据等保要求，建议设置超时时间不大于	<=600	$TMOUT	TRUE		"
      pass=$(($pass+1))
    fi
  fi

  ```
  * 完成使用报告的编写。

### 第四阶段（5月29日-6月7日）

将漏洞测试模块，可视化报告模块结合，测试程序

### 第五阶段（7月15日—8月15日）

总体任务：增加修复功能，完善可视化平台设计。

* 7月25日
  
  * 进行初版功能需求分析。

    本项目需实现安全检查功能及修复功能的调用，并通过http接口接收报告，存入数据库并展示。

    故设计三个页面，分别为：
    * 工作台页面：实现检查功能的调用并展示历史检查结果；
    * 报告详情页：展示检查报告详情信息，并实现修复功能的调用；
    * 功能说明页：展示各功能说明；
  
  * 对接收数据的http接口分发路由。

    - 使用路由“openkylin_scan_res_report/”接收基线检查结果；
    - 使用路由“openkylin_repair_res_report/”接收基线修复结果；
    - 使用路由“systempos_scan_res_report/”接收系统漏洞检查结果；
    - 使用路由“systempos_repair_res_report/”接收系统漏洞修复结果；
    - 使用路由“kernelpos_scan_res_report/”接收内核漏洞检查结果；
    - 使用路由“kernelpos_repair_res_report/”接收内核漏洞修复结果；

* 7月26日-7月27日
  
  * 完成工作台页面样式设计。

* 7月28日-7月29日

  * 完成检查结果详情页样式设计。

* 7月30日

  * 完成功能说明页样式设计。

* 7月31日

  * 完善数据库设计。

    数据库设计如下：
  
      - 历史记录表：AllRecord
  
      - 基线扫描结果逐项表：BaselineTestRes
   
      - 内核漏洞扫描结果逐项表：KernelPocRes
  
      - 系统漏洞扫描结果逐项表：SystemPocRes

* 8月1日-8月3日

  * 完成js及视图函数的编写。

* 8月4日-8月5日

  * 对各接口进行测试，完善代码。
    
    经过测试，各接口运行正常。

* 8月6日

  * 在虚拟机上对项目进行整体测试。 
  
    经过测试，本项目各功能实现正常。

* 8月7日-8月9日

  * 测试各功能调用。

    经过测试，各功能调用正常。

* 8月10日

  * 整理项目文件。

* 8月11-12日

  * 编写项目报告及使用说明。




## 比赛过程中的重要进展

5.05 开第一次会议，讨论选择题目和分工，根据队伍里各个队友的所学知识和偏好，最终选择了麒麟操作系统安全基线检查这一题目，并确定了组内各个成员的分工情况，将题目的要求分为三个部分，第一个部分是安全基线检查脚本的撰写，第二个部分是漏洞检查脚本的撰写，第三个部分是前两个部分检查结果的可视化平台编写。各个部分间通过HTTP请求进行通信，有效地将系统各个部分解耦合，加快了开发速度

5.14 开第二次会议，讨论各部分项目进度，交流各部分项目遇到的问题和解决方案。在漏洞检测和安全基线检查方面，主要是检查脚本数据库的建立和编写，由于存在大量的检查项都需要编写对应的脚本，所以需要认真规划编写计划，同时要注意实时编写对应文档和注释，方便后期维护。在可视化方面，参考市面上的安全检查项目页面，讨论安全检查项目的页面构成。

5.15 漏洞检测内核模块完成

5.16 搭建好安全基线检查项目的框架，大概由三部分配置文件，检查项目数据库，检查控制主程序构成。

5.25 漏洞检测系统模块完成

5.25 完成安全基线检查数据库的数据填充。并测试好数据库所有内容都可正常显示和运行。

5.26 开第三次会议，总结统计了目前项目的进度，代码编写工作基本完成，指出了下一阶段的重点方向在于合并三个模块，同时编写测试和开发文档。


## 系统测试情况

### 基线模块
测试模块截图：

![img](readme_src/baseline/baseline_test3.png)

可以看出该脚本运行正常时将输出检测项目的信息，运行的命令和运行情况，最终将输出单个检查的结果信息，使得用户更加了解运行过程。

### 漏洞检测

- kernelPoc测试记录

    <img src="readme_src/poc/kernelpoc.png" width="60%">

    <center>
    
    图11 内核漏洞测试结果
    
    </center>
- systemPoc测试记录

    <img src="readme_src/poc/systempoc.png" width="60%">

     <center>
    
    图12 系统漏洞测试结果
    
    </center>

### 可视化报告

各页面展示效果如下：

- 工作台页面

    <div align="center">
    <img src="readme_src/ReportVisual/index.png" width="60%">
    <div>图13 工作台页面效果</div>
    </div>

- 基线检查报告页面

    <div align="center">
    <img src="readme_src/ReportVisual/baseline.png" width="60%">
    <div>图14 基线检查报告页面效果</div>
    </div>

- 漏洞检查报告页面

    <div align="center">
    <img src="readme_src/ReportVisual/kernel.png" width="60%">
    <div>图15 漏洞检查报告页面效果</div>
    </div>

- 功能说明页面

    <div align="center">
    <img src="readme_src/ReportVisual/help.png" width="60%">
    <div>图16 功能说明页面效果</div>
    </div>

## 遇到的主要问题和解决方法
1.基线检测中的遇到的难题之一是如何将检查项目归类，类内的项目需要保持一定的联系，同时尽量不遗漏重要的安全基线检查项。

解决方法：这里参考了等保安全基线，SCAP安全基线、开源安全基线检查项目和企业安全基线检查的标准，根据重要的必须检查，一般的尽量检查，不重要的做出提醒等原则，根据奥卡姆剃刀原理，思考了用户最紧要的安全问题，最终总结出一份安全基线手册。

2.在基线检测中，因为检测项目比较多，并且需要编写每一个检查项的配置文件，脚本文件，检查项目的个数达到上百个，在比赛时间有限的情况下，如何去规划时间，高效编写代码是一个非常重要的问题。

解决方法：通过网上开源检查项目的启发，通过编写python脚本来生成基线检查配置文件和脚本文件，只需要输入一些脚本编写知识和文件格式就可以大量快速地生成配置文件和脚本文件，大大加快了项目的开发进度。

3.在漏洞检测中，有些漏洞的利用程序在利用失败时会反复运行知道成功为止拖慢运行速度。

解决方法：通过测试每个漏洞的最大执行时间在执行shell命令时加入时间参数。

4.漏洞修复中，可能会设计到对同一个软件的多次修复。

解决方法：使用信号量进行互斥操作


## 分工和协作

俞嘉鸿负责安全基线检查标准制定，安全基线检查、修复脚本编写，并根据结果给出安全建议

杨旭东负责漏洞检查、修复脚本撰写，给出漏洞修复建议

袁小清负责前端界面编写，docker环境搭建

## 提交仓库目录和文件描述

```
├─readme_src ------存储说明文档和报告所需的内部图片

├─安全基线检查 ------ 存储安全基线检查的脚本和检查项目数据库

    ├─data.yaml
    ├─openkylin基线配置文档.md  ------- 基线配置文档，可以在里面获取检查基线项目的具体内容，检测命令，修复建议等等。
    ├─requirements.txt   ------ 运行脚本需要的库及对应版本
    ├─安全基线检查开发.md   ------ 该部分的开发记录，说明文档
    ├─baseline  ------ 存储代码
    |    ├─tmp  ------  存储运行时产生的临时文件
    |    ├─result ------- 存储检测结果文件，有yaml和json格式
    |    |   ├─data.json
    |    |   └data.yaml
    |    ├─pythoncode  ------- 存储运行的主要python脚本，安全基线检查和修复
    |    |     ├─baseline_check.py
    |    |     └ repair_baseline.py
    |    ├─data  ------ 存储检测项目配置文件，检测项目配置数据库，检测脚本数据库
    |    |  ├─Baseline
    |    |  |    ├─Baseline.rar ------ 配置文件备份压缩包
    |    |  |    ├─BaseLine.yaml ------ 配置文件
    |    |  |    ├─6  检查项目第六章配置文件和检查项目信息，
    |    |  |    ├─5 检查项目第5章配置文件和检查项目信息 
    |    |  |    ├─4 检查项目第四章配置文件和检查项目信息 
    |    |  |    ├─3 检查项目第三章配置文件和检查项目信息 
    |    |  |    ├─2 检查项目第二章配置文件和检查项目信息 
    |    ├─recover_code  ------  存储修复配置文件和修复脚本
    |    |  ├─repair.yaml ------修复配置文件
    |    |  ├─repair.yaml
    |    |  |    ├─6  检查项目第六章修复项目脚本
    |    |  |    ├─5 检查项目第5章修复项目脚本
    |    |  |    ├─4 检查项目第四章修复项目脚本
    |    |  |    ├─3 检查项目第三章修复项目脚本
    |    |  |    ├─2 检查项目第二章修复项目脚本



    ```

漏洞检测:

    ├─KernelPoc_detect.py ------内核漏洞检测程序
    ├─requirement.txt ------依赖库
    ├─SystemPoc_detect.py ------系统漏洞检测程序
    ├─KernelPoc_repair.py ------系统漏洞修复程序
    ├─SystemPoc_repair.py ------系统漏洞修复程序
    ├─sandbox.py ------沙盒安装程序
    ├─exp_dir
    |    ├─data
    |    ├─data2
    |    └uaf
    ├─data ------漏洞数据库
    |  ├─SystemPocs ------系统漏洞数据库
    |  |     ├─SystemPocs.yaml ------系统漏洞索引
    |  |     ├─KVE-2022-0231
    |  |     |       ├─KVE-2022-0231.sh
    |  |     |       └KVE-2022-0231.yaml
    |  |     |       └solution.py
    |  |     ├─KVE-2022-0210
    |  |     |       ├─KVE-2022-0210.py
    |  |     |       ├─KVE-2022-0210.yaml
    |  |     |       └set_main_source.txt
    |  |     |       └solution.py
    |  |     ├─KVE-2022-0207
    |  |     |       ├─KVE-2022-0207.py
    |  |     |       └KVE-2022-0207.yaml
    |  |     |       └solution.py
    |  |     ├─KVE-2022-0206
    |  |     |       ├─KVE-2022-0206.sh
    |  |     |       └KVE-2022-0206.yaml
    |  |     |       └solution.py
    |  |     ├─KVE-2022-0205
    |  |     |       ├─KVE-2022-0205.py
    |  |     |       └KVE-2022-0205.yaml
    |  |     |       └solution.py
    |  |     ├─CVE-2023-0288
    |  |     |       ├─CVE-2023-0288.dat
    |  |     |       └CVE-2023-0288.yaml
    |  |     |       └solution.py
    |  |     ├─CVE-2023-0054
    |  |     |       ├─CVE-2023-0054.dat
    |  |     |       └CVE-2023-0054.yaml
    |  |     |       └solution.py
    |  |     ├─CVE-2023-0051
    |  |     |       ├─CVE-2023-0051
    |  |     |       └CVE-2023-0051.yaml
    |  |     |       └solution.py
    |  |     ├─CVE-2022-3602
    |  |     |       ├─CVE-2022-3602.py
    |  |     |       └CVE-2022-3602.yaml
    |  |     |       └solution.py
    |  |     ├─CVE-2022-2598
    |  |     |       ├─CVE-2022-2598
    |  |     |       └CVE-2022-2598.yaml
    |  |     |       └solution.py
    |  |     ├─CVE-2022-1771
    |  |     |       ├─CVE-2022-1771
    |  |     |       └CVE-2022-1771.yaml
    |  |     |       └solution.py
    |  |     ├─CVE-2022-1292
    |  |     |       ├─CVE-2022-1292.sh
    |  |     |       └CVE-2022-1292.yaml
    |  |     |       └solution.py
    |  |     ├─CVE-2022-0729
    |  |     |       ├─CVE-2022-0729
    |  |     |       └CVE-2022-0729.yaml
    |  |     |       └solution.py
    |  |     ├─CVE-2022-0714
    |  |     |       ├─CVE-2022-0714
    |  |     |       └CVE-2022-0714.yaml
    |  |     |       └solution.py
    |  |     ├─CVE-2022-0685
    |  |     |       ├─CVE-2022-0685
    |  |     |       └CVE-2022-0685.yaml
    |  |     |       └solution.py
    |  |     ├─CVE-2022-0572
    |  |     |       ├─CVE-2022-0572
    |  |     |       └CVE-2022-0572.yaml
    |  |     |       └solution.py
    |  |     ├─CVE-2022-0543
    |  |     |       ├─CVE-2022-0543.py
    |  |     |       └CVE-2022-0543.yaml
    |  |     |       └solution.py
    |  |     ├─CVE-2022-0417
    |  |     |       ├─CVE-2022-0417
    |  |     |       └CVE-2022-0417.yaml
    |  |     |       └solution.py
    |  |     ├─CVE-2022-0413
    |  |     |       ├─CVE-2022-0413
    |  |     |       └CVE-2022-0413.yaml
    |  |     |       └solution.py
    |  |     ├─CVE-2022-0359
    |  |     |       ├─CVE-2022-0359
    |  |     |       └CVE-2022-0359.yaml
    |  |     |       └solution.py
    |  |     ├─CVE-2021-44142
    |  |     |       ├─apple.py
    |  |     |       ├─CVE-2021-44142.py
    |  |     |       ├─CVE-2021-44142.yaml
    |  |     |       └solution.py
    |  |     |       ├─smbprotocol_extensions.py
    |  |     |       ├─__pycache__
    |  |     |       |      ├─apple.cpython-310.pyc
    |  |     |       |      ├─apple.cpython-38.pyc
    |  |     |       |      ├─smbprotocol_extensions.cpython-310.pyc
    |  |     |       |      └smbprotocol_extensions.cpython-38.pyc
    |  |     ├─CVE-2021-41773
    |  |     |       ├─CVE-2021-41773.py
    |  |     |       └CVE-2021-41773.yaml
    |  |     |       └solution.py
    |  |     ├─CVE-2021-4034
    |  |     |       ├─CVE-2021-4034.py
    |  |     |       ├─CVE-2021-4034.yaml
    |  |     |       └solution.py
    |  |     |       ├─payload.so
    |  |     |       ├─GCONV_PATH=.%
    |  |     |       |       └exploit
    |  |     |       ├─GCONV_PATH=
    |  |     |       |      └exploit
    |  |     |       ├─GCONV_PATH
    |  |     |       |     └exploit
    |  |     |       ├─exploit
    |  |     |       |    └gconv-modules
    |  |     ├─CVE-2021-3560
    |  |     |       ├─CVE-2021-3560.py
    |  |     |       └CVE-2021-3560.yaml
    |  |     |       └solution.py
    |  |     ├─CVE-2021-3156
    |  |     |       ├─CVE-2021-3156.sh
    |  |     |       └CVE-2021-3156.yaml
    |  |     |       └solution.py
    |  |     ├─CVE-2019-7304
    |  |     |       ├─CVE-2019-7304.py
    |  |     |       └CVE-2019-7304.yaml
    |  |     |       └solution.py
    |  |     ├─CVE-2019-18634
    |  |     |       ├─CVE-2019-18634.py
    |  |     |       └CVE-2019-18634.yaml
    |  |     |       └solution.py
    |  ├─KernelPocs ------内核漏洞数据库
    |  |     ├─KernelPocs.yaml ------内核漏洞索引
    |  |     ├─CVE-2022-32250
    |  |     |       ├─CVE-2022-32250.yaml
    |  |     |       ├─exp
    |  |     |       └exp.c
    |  |     |       └solution.py
    |  |     ├─CVE-2022-2639
    |  |     |       ├─CVE-2022-2639.c
    |  |     |       ├─CVE-2022-2639.yaml
    |  |     |       ├─CVE-2022-2639_x86_64
    |  |     |       ├─exploit
    |  |     |       └result_c.txt
    |  |     |       └solution.py
    |  |     ├─CVE-2022-2588
    |  |     |       ├─CVE-2022-2588.yaml
    |  |     |       ├─CVE-2022-2588_x86_64
    |  |     |       ├─exploit
    |  |     |       ├─exp_file_credential.c
    |  |     |       ├─Makefile
    |  |     |       ├─README.md
    |  |     |       ├─exp_dir
    |  |     |       |    ├─data
    |  |     |       |    ├─data2
    |  |     |       |    └uaf
    |  |     |       └solution.py
    |  |     ├─CVE-2022-24122
    |  |     |       ├─CVE-2022-24122.yaml
    |  |     |       ├─exploit
    |  |     |       └exploit.c
    |  |     |       └solution.py
    |  |     ├─CVE-2022-23222
    |  |     |       ├─bpf.h
    |  |     |       ├─config.h
    |  |     |       ├─CVE-2022-23222.yaml
    |  |     |       ├─CVE-2022-23222_x86_64
    |  |     |       ├─debug.h
    |  |     |       ├─exploit
    |  |     |       ├─exploit.c
    |  |     |       ├─helper.h
    |  |     |       └Makefile
    |  |     |       └solution.py
    |  |     ├─CVE-2022-1679
    |  |     |       ├─CVE-2022-1679.yaml
    |  |     |       └CVE2022-1679.sh
    |  |     |       └solution.py
    |  |     ├─CVE-2022-0847
    |  |     |       ├─CVE-2022-0847
    |  |     |       ├─CVE-2022-0847.c
    |  |     |       └CVE-2022-0847.yaml
    |  |     |       └solution.py
    |  |     ├─CVE-2022-0185
    |  |     |       ├─CVE-2022-0185.yaml
    |  |     |       ├─exploit
    |  |     |       ├─exploit.c
    |  |     |       └Makefile
    |  |     |       └solution.py
    |  |     ├─CVE-2021-4204
    |  |     |       ├─bpf.h
    |  |     |       ├─build_and_run.sh
    |  |     |       ├─config.h
    |  |     |       ├─CVE-2021-4204.yaml
    |  |     |       ├─debug.h
    |  |     |       ├─exploit
    |  |     |       ├─exploit.c
    |  |     |       ├─helper.h
    |  |     |       ├─Makefile
    |  |     |       └README.md
    |  |     |       └solution.py
    |  |     ├─CVE-2021-26708
    |  |     |       ├─CVE-2021-26708.yaml
    |  |     |       ├─cve-2021-26798
    |  |     |       └exploit.c
    |  |     |       └solution.py
    |  |     ├─CVE-2021-22555
    |  |     |       ├─CVE-2021-22555.c
    |  |     |       ├─CVE-2021-22555.yaml
    |  |     |       ├─CVE-2021-22555_x86_64
    |  |     |       └exploit
    |  |     |       └solution.py
└─ 检查报告可视化          ----------实现检查报告可视化的Django项目
   ├─ manage.py            ----------项目的命令行工具
   ├─ reports            ----------存储名为reports的app的相关文件
   ├─ ReportVisual            ----------用于存储项目配置文件等
   ├─ static            ----------用于存储.css和.js文件
   ├─ templates            ----------用于存储.html文件
   └─ 检查报告可视化项目开发.md
```

## 比赛收获

1.通过本次比赛，增强了团队合作和开发的能力，能够合理分解任务，将一个大的项目分成几个子项目交给各个成员负责

2.增强了软件设计与开发的能力，对于一个操作系统的完整功能实现，合理、高效、低耦合的系统架构有利于提高项目开发的效率，同时使得后期项目整体运行时不容易出现兼容性之类的冲突，增强了系统的健壮性

3.学习了麒麟操作系统和linux操作系统的底层知识，对于操作系统的运行过程及其底层原理，可以从安全性的视角来看待操作系统存在的问题，分析用户使用时可能出现的风险。

4.熟悉了搭建Django项目的基本思路及流程，对于URLConf有了更深的了解，实现Django项目中使用http接口完成了检测数据的传输。

5.了解了yaml数据与json数据的格式规范，对比yaml与json在网络通信中的不同之处，综合分析，使用了json进行本系统的网络通信。
