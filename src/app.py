from src.ui_window import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from pathlib import Path
from rutube import Rutube

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.browse_button.clicked.connect(self._browse_directory)
        self.ui.download_button.clicked.connect(self._download)
        self.dir = str(Path.home())
        self.ui.file_textedit.setText(str(self.dir))
        self.rt = None
        self.ui.url_textedit.textChanged.connect(self._on_change)

    def _browse_directory(self):
        self.dir = QFileDialog.getExistingDirectory(self, 'Open Directory')
        self.ui.file_textedit.setText(str(self.dir))

    def _on_change(self):
        self.ui.comboBox.clear()
        if self.ui.url_textedit.toPlainText() != '':
            self.rt = Rutube(self.ui.url_textedit.toPlainText())
            playlist = [f'({x.title.split("(")[1]}' for x in self.rt.playlist ]
            self.ui.comboBox.addItems(playlist)

    def _download(self):
        video = self.rt.playlist[self.ui.comboBox.currentIndex()]
        video.download(self.ui.file_textedit.toPlainText())

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()