# Copyright (c) 2024 Meier Yang(杨素)
# All rights reserved.
#
# This code is licensed under the MIT license.
#
# The CounterPaint application will expire in the following year:
expiry_year = 2024
# Modify this value to extend the expiration date.

from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QFileDialog, QMessageBox, QMenuBar, QVBoxLayout
from PyQt6.QtGui import QPixmap, QPainter, QPen, QImage, QColor, QFont, QAction
from PyQt6.QtCore import Qt, QPoint, QSize, QEvent
import sys
from datetime import datetime

class ImageEditor(QWidget):
    def __init__(self, imagePath=None):
        super().__init__()
        self.current_image_path = None  # 添加属性来存储当前图片路径
        self.is_modified = False
        # Windows Platform value
        # x = -15
        # y = -15
        # MacOS Platform value
        # x = -25
        # y = -15
        self.mouse_offset_x = -25
        self.mouse_offset_y = -15
        self.initUI()
        self.marked_points = []  # 初始化标记点列表
        
        if imagePath:
            self.loadImage(imagePath)

    def initUI(self):
        self.menuBar = self.createMenuBar()
        self.imageLabel = QLabel(self)
        self.imageLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout = QVBoxLayout(self)
        layout.setMenuBar(self.menuBar)
        layout.addWidget(self.imageLabel)

        self.setWindowTitle('Counter Paint')
        self.setGeometry(150, 30, 1000, 1000)

        self.image = QImage()
        self.counter = 0
        self.target_size = QSize(2000, 2000)  # 图片固定大小

    def createMenuBar(self):
        menuBar = QMenuBar(self)
        
        # 菜单
        fileMenu = menuBar.addMenu("&文件")
        editMenu = menuBar.addMenu("&编辑")
        helpMenu = menuBar.addMenu("&帮助")

        # 选项
        # 文件菜单
        openAction = QAction("&打开", self)
        openAction.setShortcut("Ctrl+O")
        openAction.triggered.connect(self.openImage)
        fileMenu.addAction(openAction)

        saveAction = QAction("&保存", self)
        saveAction.setShortcut("Ctrl+S")
        saveAction.triggered.connect(self.saveImage)
        fileMenu.addAction(saveAction)

        closeAction = QAction("&关闭", self)
        closeAction.setShortcut("Ctrl+W")
        closeAction.triggered.connect(self.close)
        fileMenu.addAction(closeAction)

        # 编辑菜单
        undoAction = QAction("&撤销", self)
        undoAction.setShortcut("Ctrl+Z")
        undoAction.triggered.connect(self.undo)
        editMenu.addAction(undoAction)
        
        # 帮助菜单
        #settingsAction = QAction("&设置", self)
        #settingsAction.triggered.connect(self.openSettings)
        #helpMenu.addAction(settingsAction)

        aboutAction = QAction("&关于", self)
        aboutAction.triggered.connect(self.showAboutDialog)
        helpMenu.addAction(aboutAction)

        return menuBar

    def showAboutDialog(self):
        # mess = 
        QMessageBox.information(self, "关于", f"我是本软件的作者——杨素，是上海雷帕罗义齿有限公司的一位基层员工。\n本软件的编写目的是为了完成特定工作任务。\n\n 本软件是免费软件，且已在github开源，\n 地址：https://github.com/Meieryang/CounterPaint \n 如果您付费购买了本软件，请立即协商退款。\n\n伯乐你好，如果你能给我提供一份好的工作，请联系我！\n联系邮箱: sundayisnowy@gmail.com \n 联系电话：17343425191\n\n软件到期时间: {expiry_year}年10月22日",
                                QMessageBox.StandardButton.Ok)
        
    def loadImage(self, imagePath=None):
        if imagePath is None:
            imagePath, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Images (*.png *.xpm *.jpg *.jpeg)")
        if imagePath:
            self.image = QImage(imagePath)
            self.current_image_path = imagePath
            self.displayImage()

    def displayImage(self):
        if not self.image.isNull():
            # 图片固定显示大小
            self.scaled_image = self.image.scaled(self.target_size, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            self.imageLabel.setPixmap(QPixmap.fromImage(self.scaled_image))

    def openImage(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "打开文件", "", "Images (*.png *.xpm *.jpg *.bmp *.gif)")
        if fileName:
            self.loadImage(fileName)

    def saveImage(self):
        if self.current_image_path and self.is_modified:
            self.image.save(self.current_image_path)  # 保存到当前路径
            self.is_modified = False
            self.updateWindowTitle()
        else:
            self.saveImageAs()

    # appended
    def saveImageAs(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save Image As", "", "PNG Files (*.png);;JPEG Files (*.jpg *.jpeg);;All Files (*)")
        if filePath:
            self.image.save(filePath)
            self.current_image_path = filePath  # 更新文件路径
            self.is_modified = False
            self.updateWindowTitle()

    def closeEvent(self, event):
        if self.is_modified:
            reply = QMessageBox.question(self, '保存更改', "图片已修改，是否保存更改？",
                                         QMessageBox.StandardButton.Save | QMessageBox.StandardButton.Discard | QMessageBox.StandardButton.Cancel,
                                         QMessageBox.StandardButton.Save)
            if reply == QMessageBox.StandardButton.Save:
                self.saveImage()
                event.accept()
            elif reply == QMessageBox.StandardButton.Cancel:
                event.ignore()
            else:
                event.accept()
        else:
            event.accept()

    def updateWindowTitle(self):
        if self.is_modified:
            self.setWindowTitle("Counter Paint - 未保存")
        else:
            self.setWindowTitle("Counter Paint")

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.counter += 1
            self.markImage(event.pos(), self.mouse_offset_x, self.mouse_offset_y)
            self.is_modified = True
            self.updateWindowTitle()

    def markImage(self, position, mouse_offset_x, mouse_offset_y):
        if self.image.isNull():
            return

        # 转换坐标到 QLabel 中的缩放图像上
        real_x = position.x() - (self.imageLabel.width() - self.scaled_image.width()) // 2
        real_y = position.y() - (self.imageLabel.height() - self.scaled_image.height()) // 2
        if real_x < 0 or real_y < 0 or real_x >= self.scaled_image.width() or real_y >= self.scaled_image.height():
            return  # 如果点击位置在图片外，不进行标记

        # 计算真实图像坐标
        scale_x = self.image.width() / self.scaled_image.width()
        scale_y = self.image.height() / self.scaled_image.height()
        image_x = int(real_x * scale_x) + mouse_offset_x
        image_y = int(real_y * scale_y) + mouse_offset_y

        # 存储标记的点和数字
        self.marked_points.append((image_x, image_y, self.counter))

        painter = QPainter(self.image)
        pen = QPen(QColor(255, 0, 0))
        painter.setPen(pen)

        font = QFont()
        font.setPointSize(15)
        painter.setFont(font)

        painter.drawText(QPoint(image_x, image_y), str(self.counter))
        painter.end()

        self.displayImage()

    def undo(self):
        if self.marked_points:
            self.marked_points.pop()  # 移除最后一个标记
            self.counter -= 1
            self.redrawImage()

    def redrawImage(self):
        self.image = QImage(self.current_image_path)  # 重新加载原始图像
        painter = QPainter(self.image)
        pen = QPen(QColor(255, 0, 0))
        painter.setPen(pen)

        font = QFont()
        font.setPointSize(15)
        painter.setFont(font)

        # 重新绘制所有标记
        for point in self.marked_points:
            painter.drawText(QPoint(point[0], point[1]), str(point[2]))
        painter.end()

        self.displayImage()


class MyApp(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.editor = None
    
    def event(self, e):
        if e.type() == QEvent.Type.FileOpen:
            if self.editor:
                self.editor.loadImage(e.file())
        return super().event(e)

def run():

    app = MyApp(sys.argv)

    # Check if the software is expired before initializing QApplication
    expiry_date = datetime(expiry_year, 10, 22)
    if datetime.now() > expiry_date:
        QMessageBox.critical(None, "错误", "软件已过期\n请联系作者杨素\nsundayisnowy@gmail.com")
        sys.exit(1)
    
    if len(sys.argv) > 1 and not sys.argv[1].startswith('-psn'):
        imagePath = sys.argv[1]
    else:
        imagePath = None
    editor = ImageEditor(imagePath)
    app.editor = editor
    editor.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    run()