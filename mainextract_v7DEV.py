
import os
import sys
import zipfile
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QProgressBar, QApplication, QDesktopWidget, QLabel
from PyQt5.QtGui import QMovie, QIcon



if hasattr(sys, '_MEIPASS'):

    script_dir = sys._MEIPASS
else:

    script_dir = os.path.dirname(os.path.abspath(__file__))

class CBZEXwin(QtWidgets.QMainWindow):
    def __init__(self):
        super(CBZEXwin, self).__init__()



        icon_path = os.path.join(script_dir, "script.ico")
        self.setWindowIcon(QIcon(icon_path))

        self.setWindowTitle("CBZ Extractor by squeezebiscuit v1.5")
        self.setGeometry(100, 100, 510, 400)
        self.setFixedSize(510, 400)

        self.setWindowOpacity(0.0)

        self.browse_betlog_btn = QtWidgets.QPushButton(self)
        self.browse_betlog_btn.setText("Browse CBZ")
        self.browse_betlog_btn.setGeometry(20, 20, 100, 30)
        self.browse_betlog_btn.clicked.connect(self.browse_file)

        self.exract_nabetlogan_sakanto = QtWidgets.QPushButton(self)
        self.exract_nabetlogan_sakanto.setText("Extract")
        self.exract_nabetlogan_sakanto.setGeometry(20, 70, 100, 30)
        self.exract_nabetlogan_sakanto.clicked.connect(self.extract_file)

        self.prog_bar_na_malupet_gg_sa_kalaban = QProgressBar(self)
        self.prog_bar_na_malupet_gg_sa_kalaban.setGeometry(150, 70, 300, 30)
        self.prog_bar_na_malupet_gg_sa_kalaban.setStyleSheet("""
            QProgressBar {
                border: 3px solid #000000;
                border-radius: 0px;
                background-color: #ffffff;
                text-align: center;
                color: #000000;
            }

            QProgressBar::chunk {
                background-color: #00ff00;
                width: 10px;
                margin: 0.5px;
            }
        """)

        self.top_label = QtWidgets.QLabel(self)
        self.top_label.setText("CBZ EXTRACTOR by rexif and sqb69\n(will extract any selected .CBZ Files)\n\nPROGRESS:")
        self.top_label.setGeometry(150, 5, 300, 60)
        self.top_label.setAlignment(QtCore.Qt.AlignLeft)
        self.top_label.setStyleSheet("font-size: 12px; font-weight: bold; color: #000000;")


        self.gif_label = QLabel(self)
        self.gif_label.setGeometry(-140, 120, 500, 80)
        self.gif_label.setAlignment(QtCore.Qt.AlignCenter)

        gif_dir = os.path.join(script_dir, 'gifs')

        self.gif_label2 = QLabel(self)
        self.gif_label2.setGeometry(10, 120, 500, 80)
        self.gif_label2.setAlignment(QtCore.Qt.AlignCenter)

        self.gif_label3 = QLabel(self)
        self.gif_label3.setGeometry(150, 120, 500, 80)
        self.gif_label3.setAlignment(QtCore.Qt.AlignCenter)

        self.movie = QMovie(os.path.join(gif_dir, "ganyuuuuahhhhh1023712c.gif"))
        self.movie.setScaledSize(QtCore.QSize(180, 70))
        self.gif_label3.setMovie(self.movie)
        self.movie.start()

        self.movie = QMovie(os.path.join(gif_dir, "ganyumywifeeaagggghhhhheadpattt.gif"))
        self.movie.setScaledSize(QtCore.QSize(90, 90))
        self.gif_label2.setMovie(self.movie)
        self.movie.start()

        self.movie = QMovie(os.path.join(gif_dir, "ganyumywifeeaagggghhhh1231241.gif"))
        self.movie.setScaledSize(QtCore.QSize(200, 200))
        self.gif_label.setMovie(self.movie)
        self.movie.start()


        self.cbz_file_label = QLabel(self)
        self.cbz_file_label.setGeometry(20, 200, 480, 100)
        self.cbz_file_label.setWordWrap(True)
        self.cbz_file_label.setStyleSheet("font-size: 12px; font-weight: bold; color: #000000;")
        self.cbz_file_label.setText("File Selected:")

        self.extract_location_label = QLabel(self)
        self.extract_location_label.setGeometry(20, 270, 480, 100)
        self.extract_location_label.setWordWrap(True)
        self.extract_location_label.setStyleSheet("font-size: 12px; font-weight: bold; color: #000000;")
        self.extract_location_label.setText("Extracted Files Path:")

        self.center_window()
        self.show()


        self.fade_in_effect()

    def fade_in_effect(self):
        self.animation = QtCore.QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(1000)
        self.animation.setStartValue(0.0)
        self.animation.setEndValue(1.0)
        self.animation.start()

    def browse_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select CBZ File", "", "CBZ Files (*.cbz)")
        if file_path:
            self.cbz_file = file_path
            self.cbz_file_label.setText(f"File Selected: {os.path.basename(file_path)}")
            folder_path = os.path.join(os.path.dirname(self.cbz_file), os.path.splitext(os.path.basename(self.cbz_file))[0])
            self.extract_location_label.setText(f"Extracted Files Path: {folder_path}")

    def extract_file(self):
        try:
            with zipfile.ZipFile(self.cbz_file, 'r') as zip_ref:
                folder_path = os.path.join(os.path.dirname(self.cbz_file), os.path.splitext(os.path.basename(self.cbz_file))[0])
                self.prog_bar_na_malupet_gg_sa_kalaban.setMaximum(len(zip_ref.infolist()))
                for i, file in enumerate(zip_ref.infolist(), 1):
                    zip_ref.extract(file, folder_path)
                    self.prog_bar_na_malupet_gg_sa_kalaban.setValue(i)
                    QApplication.processEvents()

                self.extract_location_label.setText(f"Extracted Files Path: {folder_path}")

            QMessageBox.warning(self, "Success", "Extraction completed.\nFIND THE FILE NOW!")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def center_window(self):
        desktop = QApplication.desktop()
        screen_geometry = desktop.availableGeometry()
        window_geometry = self.frameGeometry()
        center_point = screen_geometry.center()
        window_geometry.moveCenter(center_point)
        self.move(window_geometry.topLeft())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CBZEXwin()
    sys.exit(app.exec_())
