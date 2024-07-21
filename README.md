# CounterPaint
---
CounterPaint 是一个轻量化的、用于 **在图像上添加数字编号** 标记的小工具，由**Meieryang(杨素)** 编写。
你可以在资源管理器（或者访达）中通过直接打开文件的方式使用此程序，也可以从软件中打开文件。
> *“轻量、绿色、实用”是本工具的目标，所以没有其他臃肿的功能。*
---

<br>

## 软件下载
本软件提供编译好的可执行文件以供下载，请下载适用于自己系统的 **'CounterPaint'** 版本。

<br>

 - Windows版下载地址：
[下载 CounterPaint.exe (for Windows)](https://github.com/Meieryang/CounterPaint/releases/download/v1.0.0/CounterPaint.exe)

<br>

 - macOS版下载地址：
[下载 CounterPaint.dmg (for macOS)](https://github.com/Meieryang/CounterPaint/releases/download/v1.0.0/CounterPaint.dmg)
<br>

## 使用方法

1. **打开文件：** 在资源管理器（或者访达）中选中一个图片文件，右键选择 **“打开方式...”** ，选择通过该程序打开图片文件。

<br>

2. **点击计数：** 点击图片上的某一点即可按照**自然数的顺序**生成数字并在**点击位置**标记生成的数字。
**（该软件会直接编辑图片文件，重要文件请做好备份！！）**

<br>

3. **撤销：** 按下快捷键 **"Ctrl+Z"** 可以撤销上一次的点按计数。

<br>

4. **保存：** 编辑结束后，按下快捷键 **"Ctrl+S"** 保存文件，或者点击菜单栏中的“文件”菜单，点击“保存”选项。
你也可以直接关闭窗口（点击关闭窗口按钮或者按下快捷键 **"Ctrl+W"** ），在弹出的对话框中选择 **"Save"** ，也能实现保存功能。

 > - *备注：如果你不希望保存文件，请关闭窗口，在弹出的对话框中选择 "Don't Save"。*

<br>
<br>

---
## 尝试自己构建应用程序

<br>

 - ### 项目结构

**CounterPaint/**
├── CounterPaint.py       # 主程序文件
├── README.md             # 项目介绍文件
├── requirements.txt      # 依赖文件
└── …                   # 其他文件和目录

<br>

 - ### 克隆源码

1. **克隆此仓库到本地：**

    ```bash
    git clone https://github.com/Meieryang/CounterPaint.git
    ```

2. **进入项目目录：**

    ```bash
    cd CounterPaint
    ```

3. **安装所需依赖：**

    ```bash
    pip install -r requirements.txt
    ```

<br>

 - ### 尝试运行

1. **运行程序：**

    ```bash
    python CounterPaint.py
    ```

<br>

 - ### 编译构建

1. **安装所需依赖：**
    我们使用pyinstaller库进行python程序的编译，首先我们需要安装它。
    ```bash
    pip install pyinstaller
    ```

2. **编译：**
    使用`pyinstaller`命令进行编译构建。

    ```bash
    pyinstaller -F -w CounterPaint.py
    ```
    > - **参数解释：**
    > - **-F** 表示将所有依赖打包为一个可执行文件。
    > - **-w** 表示编译为无控制台的窗口程序。

3. **找到编译完成的程序：**
    打开项目目录下的 **"dist/"** 目录，可执行文件就在这里。
    windows程序的后缀名为   ".exe"
    macOS程序的后缀名为  ".app"

<br>
<br>

---

## 联系方式

如果你有任何问题或建议，请通过以下方式联系我：

- **邮箱:** sundayisnowy@gmail.com
- **电话:** 17343425191

---

## 贡献

如果你想贡献代码，请遵循以下步骤：

1. Fork 本仓库
2. 创建一个新的分支 (`git checkout -b feature-branch`)
3. 提交你的更改 (`git commit -am 'Add some feature'`)
4. 推送到分支 (`git push origin feature-branch`)
5. 创建一个新的 Pull Request

---

## 许可

本项目代码基于 MIT 许可证开源。有关更多信息，请参见 [LICENSE](LICENSE) 文件。
