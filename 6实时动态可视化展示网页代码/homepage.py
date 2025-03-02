import wx
import subprocess
import webbrowser
import threading
import os
import time
import psutil

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(1200, 800))

        icon_path = "/home/nuc/桌面/NUC_openkylin/图标~1.ico"

        # 2. 创建 wx.Icon 对象
        icon = wx.Icon(icon_path, wx.BITMAP_TYPE_ICO)

        # 3. 将图标设置给窗体
        self.SetIcon(icon)
        # 计算屏幕中心位置
        screen_width = wx.DisplaySize()[0]
        screen_height = wx.DisplaySize()[1]
        frame_x = (screen_width - self.GetSize()[0]) / 2
        frame_y = (screen_height - self.GetSize()[1]) / 2
        self.SetPosition((int(frame_x), int(frame_y)))

        self.panel = wx.Panel(self)

        # 设置背景图片
        bmp = wx.Bitmap("2.jpg")
        self.background = wx.StaticBitmap(self.panel, -1, bmp)

        # 基线板块标题
        baseline_label = wx.StaticText(self.panel, label="基线板块")
        font = wx.Font(24, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        baseline_label.SetFont(font)

        # 基线检查相关，增大文字描述字号
        font_big = wx.Font(18, wx.DEFAULT, wx.NORMAL, wx.BOLD)  # 创建新的大字号字体对象
        font_text = wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        self.baseline_check_button = wx.Button(self.panel, label="基线检查")
        self.baseline_check_button.SetFont(font_big)  # 设置按钮文字描述为大字号
        self.baseline_check_upload_button = wx.Button(self.panel, label="上传云库")
        self.baseline_check_upload_button.SetFont(font_big)  # 设置按钮文字描述为大字号
        self.baseline_check_report_button = wx.Button(self.panel, label="查看报告")
        self.baseline_check_report_button.SetFont(font_big)  # 设置按钮文字描述为大字号

        # 基线检测修复相关，增大文字描述字号
        self.baseline_fix_button = wx.Button(self.panel, label="基线检测修复")
        self.baseline_fix_button.SetFont(font_big)  # 设置按钮文字描述为大字号
        self.baseline_fix_upload_button = wx.Button(self.panel, label="上传云库")
        self.baseline_fix_upload_button.SetFont(font_big)  # 设置按钮文字描述为大字号
        self.baseline_fix_report_button = wx.Button(self.panel, label="查看报告")
        self.baseline_fix_report_button.SetFont(font_big)  # 设置按钮文字描述为大字号

        # 漏洞板块标题
        vulnerability_label = wx.StaticText(self.panel, label="漏洞板块")
        vulnerability_label.SetFont(font)

        # 内核漏洞相关，增大文字描述字号
        self.kernel_vulnerability_button = wx.Button(self.panel, label="内核漏洞")
        self.kernel_vulnerability_button.SetFont(font_big)  # 设置按钮文字描述为大字号
        self.kernel_vulnerability_upload_button = wx.Button(self.panel, label="上传云库")
        self.kernel_vulnerability_upload_button.SetFont(font_big)  # 设置按钮文字描述为大字号
        self.kernel_vulnerability_report_button = wx.Button(self.panel, label="查看报告")
        self.kernel_vulnerability_report_button.SetFont(font_big)  # 设置按钮文字描述为大字号

        # 内核漏洞修复相关，增大文字描述字号
        self.kernel_vulnerability_fix_button = wx.Button(self.panel, label="内核漏洞修复")
        self.kernel_vulnerability_fix_button.SetFont(font_big)  # 设置按钮文字描述为大字号
        self.kernel_vulnerability_fix_upload_button = wx.Button(self.panel, label="上传云库")
        self.kernel_vulnerability_fix_upload_button.SetFont(font_big)  # 设置按钮文字描述为大字号
        self.kernel_vulnerability_fix_report_button = wx.Button(self.panel, label="查看报告")
        self.kernel_vulnerability_fix_report_button.SetFont(font_big)  # 设置按钮文字描述为大字号

        # 系统漏洞相关，增大文字描述字号
        self.system_vulnerability_button = wx.Button(self.panel, label="系统漏洞")
        self.system_vulnerability_button.SetFont(font_big)  # 设置按钮文字描述为大字号
        self.system_vulnerability_upload_button = wx.Button(self.panel, label="上传云库")
        self.system_vulnerability_upload_button.SetFont(font_big)  # 设置按钮文字描述为大字号
        self.system_vulnerability_report_button = wx.Button(self.panel, label="查看报告")
        self.system_vulnerability_report_button.SetFont(font_big)  # 设置按钮文字描述为大字号

        # 系统漏洞修复相关，增大文字描述字号
        self.system_vulnerability_fix_button = wx.Button(self.panel, label="系统漏洞修复")
        self.system_vulnerability_fix_button.SetFont(font_big)  # 设置按钮文字描述为大字号
        self.system_vulnerability_fix_upload_button = wx.Button(self.panel, label="上传云库")
        self.system_vulnerability_fix_upload_button.SetFont(font_big)  # 设置按钮文字描述为大字号
        self.system_vulnerability_fix_report_button = wx.Button(self.panel, label="查看报告")
        self.system_vulnerability_fix_report_button.SetFont(font_big)  # 设置按钮文字描述为大字号

        # 其它板块
        qita_label = wx.StaticText(self.panel, label="其它板块")
        qita_label.SetFont(font)

        # 在线网页查看按钮
        self.online_view_button = wx.Button(self.panel, label="在线网页查看")
        self.online_view_button.SetFont(font_big)
        # 一键上传云库
        self.all_upload_button = wx.Button(self.panel, label="一键上传云库")
        self.all_upload_button.SetFont(font_big)
        # 一键删除云库
        self.all_delete_button = wx.Button(self.panel, label="一键删除云库")
        self.all_delete_button.SetFont(font_big)

        # 控制台输出文本框，增加宽度
        self.output_text = wx.TextCtrl(self.panel, size=(1000, 450), style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.output_text.SetFont(font_text)
        self.output_text.SetBackgroundColour(wx.Colour(80, 80, 80))

        # 布局
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        baseline_sizer = wx.GridSizer(2, 3, 10, 10)  # 2 行 3 列，水平和垂直间距为 10
        baseline_sizer.Add(self.baseline_check_button, 0, wx.ALL | wx.EXPAND)
        baseline_sizer.Add(self.baseline_check_upload_button, 0, wx.ALL | wx.EXPAND)
        baseline_sizer.Add(self.baseline_check_report_button, 0, wx.ALL | wx.EXPAND)
        baseline_sizer.Add(self.baseline_fix_button, 0, wx.ALL | wx.EXPAND)
        baseline_sizer.Add(self.baseline_fix_upload_button, 0, wx.ALL | wx.EXPAND)
        baseline_sizer.Add(self.baseline_fix_report_button, 0, wx.ALL | wx.EXPAND)

        vulnerability_sizer = wx.GridSizer(4, 3, 10, 10)  # 4 行 3 列，水平和垂直间距为 10
        vulnerability_sizer.Add(self.kernel_vulnerability_button, 0, wx.ALL | wx.EXPAND)
        vulnerability_sizer.Add(self.kernel_vulnerability_upload_button, 0, wx.ALL | wx.EXPAND)
        vulnerability_sizer.Add(self.kernel_vulnerability_report_button, 0, wx.ALL | wx.EXPAND)
        vulnerability_sizer.Add(self.kernel_vulnerability_fix_button, 0, wx.ALL | wx.EXPAND)
        vulnerability_sizer.Add(self.kernel_vulnerability_fix_upload_button, 0, wx.ALL | wx.EXPAND)
        vulnerability_sizer.Add(self.kernel_vulnerability_fix_report_button, 0, wx.ALL | wx.EXPAND)
        vulnerability_sizer.Add(self.system_vulnerability_button, 0, wx.ALL | wx.EXPAND)
        vulnerability_sizer.Add(self.system_vulnerability_upload_button, 0, wx.ALL | wx.EXPAND)
        vulnerability_sizer.Add(self.system_vulnerability_report_button, 0, wx.ALL | wx.EXPAND)
        vulnerability_sizer.Add(self.system_vulnerability_fix_button, 0, wx.ALL | wx.EXPAND)
        vulnerability_sizer.Add(self.system_vulnerability_fix_upload_button, 0, wx.ALL | wx.EXPAND)
        vulnerability_sizer.Add(self.system_vulnerability_fix_report_button, 0, wx.ALL | wx.EXPAND)

        qita_sizer = wx.GridSizer(1, 3, 10, 10)  # 4 行 3 列，水平和垂直间距为 10
        qita_sizer.Add(self.online_view_button, 0, wx.ALL | wx.EXPAND)
        qita_sizer.Add(self.all_upload_button, 0, wx.ALL | wx.EXPAND)
        qita_sizer.Add(self.all_delete_button, 0, wx.ALL | wx.EXPAND)


        main_sizer.Add(baseline_label, 0, wx.ALL | wx.EXPAND, 5)
        main_sizer.Add(baseline_sizer, 0, wx.ALL | wx.EXPAND, 10)
        main_sizer.Add(vulnerability_label, 0, wx.ALL | wx.EXPAND, 5)
        main_sizer.Add(vulnerability_sizer, 0, wx.ALL | wx.EXPAND, 10)
        main_sizer.Add(qita_label, 0, wx.ALL | wx.EXPAND, 10)
        main_sizer.Add(qita_sizer, 0, wx.ALL | wx.EXPAND, 10)
        main_sizer.Add(self.output_text, 0, wx.ALL | wx.EXPAND, 10)  # 添加控制台输出文本框

        self.panel.SetSizer(main_sizer)

        # 绑定事件
        self.baseline_check_button.Bind(wx.EVT_BUTTON, self.run_baseline_check)
        self.baseline_check_upload_button.Bind(wx.EVT_BUTTON, self.upload_baseline_check)
        self.baseline_check_report_button.Bind(wx.EVT_BUTTON, self.view_baseline_check_report)
        self.baseline_fix_button.Bind(wx.EVT_BUTTON, self.run_baseline_fix)
        self.baseline_fix_upload_button.Bind(wx.EVT_BUTTON, self.upload_baseline_fix)
        self.baseline_fix_report_button.Bind(wx.EVT_BUTTON, self.view_baseline_fix_report)
        self.kernel_vulnerability_button.Bind(wx.EVT_BUTTON, self.run_kernel_vulnerability)
        self.kernel_vulnerability_upload_button.Bind(wx.EVT_BUTTON, self.upload_kernel_vulnerability)
        self.kernel_vulnerability_report_button.Bind(wx.EVT_BUTTON, self.view_kernel_vulnerability_report)
        self.kernel_vulnerability_fix_button.Bind(wx.EVT_BUTTON, self.run_kernel_vulnerability_fix)
        self.kernel_vulnerability_fix_upload_button.Bind(wx.EVT_BUTTON, self.upload_kernel_vulnerability_fix)
        self.kernel_vulnerability_fix_report_button.Bind(wx.EVT_BUTTON, self.view_kernel_vulnerability_fix_report)
        self.system_vulnerability_button.Bind(wx.EVT_BUTTON, self.run_system_vulnerability)
        self.system_vulnerability_upload_button.Bind(wx.EVT_BUTTON, self.upload_system_vulnerability)
        self.system_vulnerability_report_button.Bind(wx.EVT_BUTTON, self.view_system_vulnerability_report)
        self.system_vulnerability_fix_button.Bind(wx.EVT_BUTTON, self.run_system_vulnerability_fix)
        self.system_vulnerability_fix_upload_button.Bind(wx.EVT_BUTTON, self.upload_system_vulnerability_fix)
        self.system_vulnerability_fix_report_button.Bind(wx.EVT_BUTTON, self.view_system_vulnerability_fix_report)

        self.online_view_button.Bind(wx.EVT_BUTTON, self.view_online)
        self.all_upload_button.Bind(wx.EVT_BUTTON, self.all_upload)
        self.all_delete_button.Bind(wx.EVT_BUTTON, self.all_delete)

    def run_baseline_check(self, event):
        # self.baseline_check_button.SetBackgroundColour((200, 100, 100))  # 改变按钮背景颜色
        self.run_file("/home/nuc/桌面/NUC_openkylin/基线检查/baseline/pythoncode/baseline_check.py")

    def upload_baseline_check(self, event):
        self.run_file("/home/nuc/桌面/NUC_openkylin/DB/baselineDB.py")

    def view_baseline_check_report(self, event):
        webbrowser.open("http://152.136.142.183:39010/baseline")

    # 基线检测修复
    def run_baseline_fix(self, event):
        self.run_file("/home/nuc/桌面/NUC_openkylin/基线检查/baseline/pythoncode/repair_baseline.py")

    def upload_baseline_fix(self, event):
        self.run_file("/home/nuc/桌面/NUC_openkylin/DB/baselinerepairDB.py")

    def view_baseline_fix_report(self, event):
        webbrowser.open("http://152.136.142.183:39010/baselinerepair")
    # 内核漏洞扫描
    def run_kernel_vulnerability(self, event):
        self.run_file("/home/nuc/桌面/NUC_openkylin/漏洞扫描/1内核漏洞检测.py")

    def upload_kernel_vulnerability(self, event):
        self.run_file("/home/nuc/桌面/NUC_openkylin/DB/nbugDB.py")

    def view_kernel_vulnerability_report(self, event):
        webbrowser.open("http://152.136.142.183:39010/nbug")
    # 内核漏洞扫描修复
    def run_kernel_vulnerability_fix(self, event):
        self.run_file("/home/nuc/桌面/NUC_openkylin/漏洞扫描/2内核漏洞检测修复.py")

    def upload_kernel_vulnerability_fix(self, event):
        self.run_file("/home/nuc/桌面/NUC_openkylin/DB/nbugrepairDB.py")

    def view_kernel_vulnerability_fix_report(self, event):
        webbrowser.open("http://152.136.142.183:39010/nbugrepair")
    # 系统漏洞扫描
    def run_system_vulnerability(self, event):
        self.run_file("/home/nuc/桌面/NUC_openkylin/漏洞扫描/3系统漏洞检测.py")

    def upload_system_vulnerability(self, event):
        self.run_file("/home/nuc/桌面/NUC_openkylin/DB/xbugDB.py")

    def view_system_vulnerability_report(self, event):
        webbrowser.open("http://152.136.142.183:39010/xbug")
    # 系统漏洞扫描修复
    def run_system_vulnerability_fix(self, event):
        self.run_file("/home/nuc/桌面/NUC_openkylin/漏洞扫描/4系统漏洞检测修复.py")
    def upload_system_vulnerability_fix(self, event):
        self.run_file("/home/nuc/桌面/NUC_openkylin/DB/xbugrepairDB.py")
    def view_system_vulnerability_fix_report(self, event):
        webbrowser.open("http://152.136.142.183:39010/xbugrepair")
    # 在线查看
    def view_online(self, event):
        webbrowser.open("http://152.136.142.183:8080/baseline")
    def all_upload(self, event):
        self.run_file("/home/nuc/桌面/NUC_openkylin/database.py")
    def all_delete(self, event):
        self.run_file("/home/nuc/桌面/NUC_openkylin/DB/allDelete.py")
    def run_file(self, file_path):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, file_path)
        process = subprocess.Popen(["python", file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        progress = 0
        expected_total_output = 1000  # 假设预计的总输出量，可根据实际情况调整
        current_output = 0  # 当前已获取的输出量

        start_time = time.time()
        last_update_time = start_time

        while True:
            output = process.stdout.readline()
            if output == b'' and process.poll() is not None:
                break
            if output:
                self.output_text.AppendText(output.decode('utf-8'))  # 将输出添加到文本框
                current_output += len(output)  # 根据输出的字节长度增加当前输出量

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(None, "openkylin操作系统安全分析工具(中北大学软件学院 & 麒麟软件)")
    frame.Show()
    app.MainLoop()