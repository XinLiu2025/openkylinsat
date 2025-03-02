import tkinter as tk
import hashlib
import os
import stat
import subprocess
from tkinter import messagebox  # 单独导入 messagebox 模块
import compileall

class FolderEncryptionGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("文件夹加密/解密与编译工具")

        self.folder_path = "/home/nuc/桌面/NUC_openkylin/漏洞扫描"
        self.password = None
        self.identity = None  # 用于存储身份

        self.create_widgets()

    def create_widgets(self):
        # 第一行：密码输入框和标签
        tk.Label(self.root, text="输入密码:").grid(row=0, column=0)
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.grid(row=0, column=1)

        # 第二行：加密、解密按钮
        self.encrypt_button = tk.Button(self.root, text="加密", command=self.encrypt_folder)
        self.encrypt_button.grid(row=1, column=0)
        self.decrypt_button = tk.Button(self.root, text="解密", command=self.decrypt_folder)
        self.decrypt_button.grid(row=1, column=1)

        # 第三行：编译按钮
        self.compile_button = tk.Button(self.root, text="编译", command=self.compile_files)
        self.compile_button.grid(row=2, column=0)

        # 第四行：身份认证按钮
        self.identity_button = tk.Button(self.root, text="身份认证", command=self.authenticate_identity)
        self.identity_button.grid(row=3, column=0)

    def authenticate_identity(self):
        identities = ["管理员", "普通用户"]  # 示例身份
        self.identity = tk.StringVar()
        tk.Label(self.root, text="选择身份:").grid(row=4, column=0)
        tk.OptionMenu(self.root, self.identity, *identities).grid(row=4, column=1)
        self.root.bind("<<ComboboxSelected>>", self.show_permission_info)  # 绑定选项改变事件

    def show_permission_info(self, event):  # 新增方法来显示权限信息
        self.set_folder_permissions(False)

    def encrypt_folder(self):
        password = self.password_entry.get()
        if password:
            self.password = hashlib.sha256(password.encode()).hexdigest()
            self.set_folder_permissions(False)
            messagebox.showinfo("加密结果", "文件夹已加密，无法直接访问。")
        else:
            messagebox.showwarning("错误", "请输入加密密码")

    def decrypt_folder(self):
        password = self.password_entry.get()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if hashed_password == self.password:
            self.set_folder_permissions(True)
            messagebox.showinfo("解密结果", "文件夹已解密，可以访问。")
        else:
            messagebox.showwarning("错误", "密码错误，解密失败。")

    def compile_files(self):
        current_dir = os.path.dirname(__file__)
        print(current_dir)
        compile_dir = os.path.join(current_dir, "漏洞扫描")
        try:
            compileall.compile_dir(compile_dir, legacy=True)
            messagebox.showinfo("编译结果", "编译成功")
        except Exception as e:
            messagebox.showerror("错误", f"编译过程中发生错误: {e}")

    def set_folder_permissions(self, accessible):
        mode = 0
        if self.identity.get() == "管理员":
            mode = stat.S_IRWXU
            messagebox.showinfo("权限信息", "当前目录权限：管理员权限（读写执行）")
        elif self.identity.get() == "普通用户":
            mode = stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH
            messagebox.showinfo("权限信息", "当前目录权限：普通用户权限（只读）")
        else:
            messagebox.showerror("错误", "未选择有效身份")
            return
        os.chmod(self.folder_path, mode)

if __name__ == "__main__":
    gui = FolderEncryptionGUI()
    gui.root.mainloop()