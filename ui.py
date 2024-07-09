import sys
sys.path.append('')
from PySide6.QtWidgets import QApplication, QWidget , QVBoxLayout,QHBoxLayout,QLabel,QMainWindow,QFileDialog,QProgressBar,QPushButton,QLineEdit,QMenu,QDialog,QApplication
from PySide6.QtGui import QFont,QPixmap,QDesktopServices,QMouseEvent,QPainter, QPen, QBrush,QColor,QPainterPath,QAction
from PySide6.QtCore import Qt,QTimer,QPropertyAnimation, QRect,QEasingCurve,QThread, Signal,QUrl,QEvent,QObject,QPoint
from Ui_ui import Ui_MainWindow
import socket
import time
import qrcode
from tinyoscquery.query import OSCQueryBrowser, OSCQueryClient
import asyncio
import json
from threading import Event
from pydglab_ws import FeedbackButton, Channel, RetCode, DGLabWSServer,StrengthData,StrengthOperationType
import re


from defaultData import defaultConfig,defaultpatterns
from logger import logger

windowLog =logger("window")
serverLog =logger("OSCserver")
dglabLog = logger("dglabServer")

class Loadingwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init()
        
    def init(self):
        self.btn_init()
        self.run_btn_init()    
        self.config_init()
        self.ui_init()
        self.avatar_judge_init()
        self.page_init()
        self.console_init()       
        self.thread_init()
        

    def btn_init(self):
        self.btn_sty1 = ( "QPushButton {border: none;background-color: rgb(220, 147, 249);background-position: center;background-repeat: no-repeat;border-radius: 25px;"
               "background-image: url(:/forms/icons/cil-media-play.png);}"
               "QPushButton:hover {background-color: rgb(240, 200, 249);}")
        self.btn_sty2 = ("QPushButton {border: none;background-color: rgb(220, 200, 249);background-position: center;background-repeat: no-repeat;border-radius: 25px;"
               "background-image: url(:/forms/icons/cil-media-play.png);}")
        self.btn_sty3 = ("QPushButton {border: none;background-color: rgb(220, 147, 249);background-position: center;background-repeat: no-repeat;border-radius: 25px;"
               "background-image: url(:/forms/icons/cil-media-stop.png);}"
               "QPushButton:hover {background-color: rgb(240, 200, 249);}")
        self.btn_sty4 = ("QPushButton {border: none;background-color: rgb(220, 147, 249);background-position: center;background-repeat: no-repeat;border-radius: 25px;"
               "background-image: url(:/forms/icons/cil-ban.png);}")
        self.channel_on_sty = (
                "QPushButton {"
                "border: no;"
                "background-position: center;"
                "background-repeat: no-repeat; "
                "border-radius: 10px;"
                "background-color: rgb(212, 148, 249);"
                "font: 15pt \"微软雅黑\";"
                "color: rgb(225, 225, 225);"
                "}"
                "QPushButton:hover {"
                    "background-color: rgb(162, 98, 199);"
                    "border: none;"
                "}"         
                )
        self.channel_off_sty = (
                "QPushButton {"
                "border: no;"
                "background-position: center;"
                "background-repeat: no-repeat; "
                "border-radius: 10px;"
                "background-color: rgb(45, 34, 71);"
                "font: 15pt \"微软雅黑\";"
                "color: rgb(225, 225, 225);"
                "}"
                "QPushButton:hover {"
                    "background-color: rgb(162, 98, 199);"
                    "border: none;"
                "}"         
                )        
        self.pattem_on_sty = (
            "QPushButton {"
            "background-image: url(:/forms/icons/heart_rate.png);"
            "border: no;"
            "background-position: center;"
            "background-repeat: no-repeat;" 
            "border-radius: 10px;"
            "background-color: rgb(212, 148, 249);"
            "}"
            "QPushButton:hover {"
                "background-color: rgb(162, 98, 199);"
                "border: none;"
            "}"    
            )
        self.pattem_off_sty = (
            "QPushButton {"
            "background-image: url(:/forms/icons/heart_rate.png);"
            "border: no;"
            "background-position: center;"
            "background-repeat: no-repeat;" 
            "border-radius: 10px;"
            "background-color: rgba(82, 28, 129,0.3);;"
            "}"
            "QPushButton:hover {"
                "background-color: rgb(162, 98, 199);"
                "border: none;"
            "}"    
            )        
        
               
                
    def run_btn_init(self):
        self.ui.run_btn.clicked.connect(self.run_btn_clicked)
        self.restore_timer = QTimer(self)
        self.restore_timer.setSingleShot(True)
        self.restore_timer.timeout.connect(self.btn_restore)        
        
    def run_btn_clicked(self):
        if self.server_end:
            self.server_start()
        else:
            self.server_close()
    
    def btn_signal(self,value:int):
        if value == 1:
            self.ui.run_btn.setStyleSheet(self.btn_sty3)
            self.ui.run_btn.setEnabled(True)
        elif value == 2:
            self.ui.run_btn.setStyleSheet(self.btn_sty4)
            self.ui.run_btn.setEnabled(False)
            self.restore_timer.start(1000)          
      
    def btn_restore(self):
        self.ui.run_btn.setStyleSheet(self.btn_sty1)
        self.ui.run_btn.setEnabled(True)
    

    def thread_init(self):
        self.deserver_end = False
        self.server_end = True
        self.osc_exit_event = Event()
        self.de_exit_event = Event()
        self.de_exit_event.clear()
        self.dgserver=DGLabServerThread(self,self.de_exit_event)
        self.dgserver.console_signal.connect(lambda msg :self.console_signal(msg))
        self.dgserver.img_signal.connect(lambda img,txt :self.qrcode_init(img,txt))
        self.dgserver.start()
        self.write_local_log("DGLabServer start")      
    
    
    def server_start(self):
        self.server_end = False
        self.osc_exit_event.clear()
        self.server=ServerThread(self,self.osc_exit_event,dgServer=self.dgserver)
        self.server.console_signal.connect(lambda msg :self.console_signal(msg))
        self.server.btn_signal.connect(lambda value :self.btn_signal(value))
        self.server.start()
        self.ui.run_btn.setStyleSheet(self.btn_sty2)
        self.ui.run_btn.setEnabled(False)        
 
    def server_close(self):
        self.osc_exit_event.set()
        while not self.server_end:
            pass
        self.ui.run_btn.setStyleSheet(self.btn_sty1) 
    
        
    def config_init(self):
        try:
            with open('config.json', 'r', encoding="utf8") as f:
                self.config = json.load(f)
        except FileNotFoundError:
            with open('config.json', 'w+', encoding="utf8") as f:
                f.write(json.dumps(defaultConfig,ensure_ascii=False))
                self.config=defaultConfig
        try:            
            with open('patterns.json', 'r', encoding="utf8") as f:
                self.patterns = json.load(f)
        except FileNotFoundError:
            with open('patterns.json', 'w+', encoding="utf8") as f:
                self.window_log('正在创建波形文件')
                f.write(json.dumps(defaultpatterns,ensure_ascii=False))
                self.patterns = defaultpatterns                
    
    def console_init(self):
        self.ui.console.setMaximumBlockCount(100)
    
    def console_signal(self,msg):
        self.write(msg)
    
    def qrcode_init(self,img:str,txt:str):
        self.ui.qrcode.setPixmap(QPixmap(img))
        self.ui.dglink_label.setText(txt)     
    
    def write(self, text):
        self.ui.console.appendPlainText(text)
        self.ui.console.ensureCursorVisible()  # 自动滚动到底部
     
    def window_log(self,text):
        windowLog.info(text)
        self.write(text)
        print("windowLog:"+text)
        
    def page_init(self):
        self.ui.home.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.page_home))
        self.ui.console_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.page_console))
        self.ui.setting_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.page_setting))
        self.ui.equalizer_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.page_write))
        
    def avatar_judge_init(self):
        self.ui.avatar_listWidget.currentItemChanged.connect(self.avatar_selected)
        self.ui.judge_listWidget.currentItemChanged.connect(self.judge_selected)
        self.ui.pattem_comboBox.addItems(self.patterns)
        self.ui.server_ip.setText(self.config["ipAddress"])
        self.ui.sleep_time.setText(str(self.config["sleepTime"]))
        for setting in self.config["oscSettings"]:
            self.ui.avatar_listWidget.addItem(setting["avatarParameter"].split("/")[-1]+'('+str(self.ui.avatar_listWidget.count())+')')
        self.ui.avatar_listWidget.setCurrentRow(0)
        self.ui.change_avater_btn.clicked.connect(self.change_avater_btn)
        self.ui.add_avatar_btn.clicked.connect(self.add_avatar_btn)
        self.ui.delect_avatar_btn.clicked.connect(self.delete_avatar_btn)
        self.ui.change_judge_btn.clicked.connect(self.change_judge_btn)
        self.ui.add_judge_btn.clicked.connect(self.add_judge_btn)
        self.ui.delect_judge_btn.clicked.connect(self.delete_judge_btn)
        self.ui.judgemode_comboBox.currentIndexChanged.connect(self.judgemode_change)
        self.ui.pattem_comboBox.currentIndexChanged.connect(self.pattern_change)
        self.ui.channel_comboBox.currentIndexChanged.connect(self.channel_change)
        self.ui.intensity.textChanged.connect(self.intensity_change)
        self.ui.intensity_slider.valueChanged.connect(self.intensity_slider_change)
        self.ui.Ticks.textChanged.connect(self.Ticks_change)
        self.ui.Ticks_slider.valueChanged.connect(self.Ticks_slider_change)
        
    def avatar_selected(self):
        if len(self.ui.avatar_listWidget.selectedItems()) == 1:
            self.ui.select_avatarParameter_lineedit.setText(
                self.config["oscSettings"][self.ui.avatar_listWidget.currentRow()]["avatarParameter"].split("/")[-1])
            self.judge_reset()        
        
    def judge_reset(self):
        self.ui.judge_listWidget.clear()   
        for value in self.config["oscSettings"][self.ui.avatar_listWidget.currentRow()]["judgeSettings"]:
            self.ui.judge_listWidget.addItem(str(value["value"]))
        self.ui.judge_listWidget.setCurrentRow(0)
    
               
    def judge_selected(self):
        if len(self.ui.judge_listWidget.selectedItems()) == 1:
            self.ui.select_judge_lineedit.setText(self.ui.judge_listWidget.currentItem().text())
            self.ui.judgemode_comboBox.setCurrentIndex(
                self.config["oscSettings"][self.ui.avatar_listWidget.currentRow()]["mode"])
            self.ui.pattem_comboBox.setCurrentText(
                self.config["oscSettings"][self.ui.avatar_listWidget.currentRow()]
                ["judgeSettings"][self.ui.judge_listWidget.currentRow()]["pattern"])
            self.ui.channel_comboBox.setCurrentText(
                self.config["oscSettings"][self.ui.avatar_listWidget.currentRow()]
                ["judgeSettings"][self.ui.judge_listWidget.currentRow()]["channel"])        
            self.ui.intensity.setText(
                str(self.config["oscSettings"][self.ui.avatar_listWidget.currentRow()]
                ["judgeSettings"][self.ui.judge_listWidget.currentRow()]["intensity"]))
            if  round(float(self.config["oscSettings"][self.ui.avatar_listWidget.currentRow()]["judgeSettings"]
                [self.ui.judge_listWidget.currentRow()]["ticks"])/10,1) == int(float(self.config["oscSettings"][self.ui.avatar_listWidget.currentRow()]["judgeSettings"]
                [self.ui.judge_listWidget.currentRow()]["ticks"])/10):         
                self.ui.Ticks.setText(
                str(int(float(self.config["oscSettings"][self.ui.avatar_listWidget.currentRow()]["judgeSettings"]
                                [self.ui.judge_listWidget.currentRow()]["ticks"])/10)))
            else:
                self.ui.Ticks.setText(
                str(round(float(self.config["oscSettings"][self.ui.avatar_listWidget.currentRow()]["judgeSettings"]
                                [self.ui.judge_listWidget.currentRow()]["ticks"])/10,1)))                
            self.ui.intensity_slider.setValue(int(self.ui.intensity.text()))      
            self.ui.Ticks_slider.setValue(int(float(self.ui.Ticks.text())*10))

    def change_avater_btn(self):
        self.ui.avatar_listWidget.selectedItems()[0].setText(self.ui.select_avatarParameter_lineedit.text()+'('+str(self.ui.avatar_listWidget.currentRow())+')')
        self.config["oscSettings"][self.ui.avatar_listWidget.currentRow()]["avatarParameter"]="/avatar/parameters/"+self.ui.select_avatarParameter_lineedit.text()
        self.save_config()
        
    def add_avatar_btn(self):
        new_avatar_param_dict = {
            "avatarParameter": "/avatar/parameters/"+self.ui.select_avatarParameter_lineedit.text(),
            "mode": 0,
            "judgeSettings": [
                {
                    "value": 1,
                    "pattern": "呼吸",
                    "channel": "A",
                    "intensity": 0,
                    "ticks": 30
                },
                {
                    "value": 0,
                    "pattern": "呼吸",
                    "channel": "A",
                    "intensity": 100,
                    "ticks": 30
                }
            ]
        }
        self.ui.avatar_listWidget.addItem(self.ui.select_avatarParameter_lineedit.text()+'('+str(self.ui.avatar_listWidget.count())+')')
        self.config["oscSettings"].append(new_avatar_param_dict)
        self.save_config()

    def delete_avatar_btn(self):
        del self.config["oscSettings"][self.ui.avatar_listWidget.currentRow()]
        self.save_config()
        i = self.ui.avatar_listWidget.currentRow()
        while i < self.ui.avatar_listWidget.count()-1:
            self.ui.avatar_listWidget.item(i+1).setText(self.ui.avatar_listWidget.item(i+1).text().replace('('+str(i+1)+')', '('+str(i)+')'))
            i += 1
        self.ui.avatar_listWidget.takeItem(self.ui.avatar_listWidget.currentRow())
        self.ui.avatar_listWidget.setCurrentRow(i-1)
        
    def change_judge_btn(self):
        self.ui.judge_listWidget.selectedItems()[0].setText(self.ui.select_judge_lineedit.text())
        self.config["oscSettings"][self.ui.avatar_listWidget.currentRow()]["judgeSettings"][self.ui.judge_listWidget.currentRow()]["value"] = float(self.ui.select_judge_lineedit.text())  
        self.save_config()
        
    def add_judge_btn(self):
        new_judge_dict = {
            "value": float(self.ui.select_judge_lineedit.text()),
            "pattern": "呼吸",
            "channel": "A",
            "intensity": 0,
            "ticks": 30
        }
        self.ui.judge_listWidget.addItem(self.ui.select_judge_lineedit.text())
        self.config["oscSettings"][self.ui.avatar_listWidget.currentRow()]["judgeSettings"].append(new_judge_dict)
        self.save_config()

    def delete_judge_btn(self):
        del self.config["oscSettings"][self.ui.avatar_listWidget.currentRow()]["judgeSettings"][self.ui.judge_listWidget.currentRow()]
        self.save_config()
        self.ui.judge_listWidget.takeItem(self.ui.judge_listWidget.currentRow())
        self.ui.judge_listWidget.setCurrentRow(self.ui.judge_listWidget.currentRow()-1)
        
    def judgemode_change(self):
        self.config["oscSettings"][self.ui.avatar_listWidget.currentRow()]["mode"] = self.ui.judgemode_comboBox.currentIndex()
        self.save_config()
        
    def pattern_change(self):
        self.config["oscSettings"][self.ui.avatar_listWidget.currentRow()]["judgeSettings"][self.ui.judge_listWidget.currentRow()]["pattern"] = self.ui.pattem_comboBox.currentText()
        self.save_config()    
            
    def channel_change(self):
        self.config["oscSettings"][self.ui.avatar_listWidget.currentRow()]["judgeSettings"][self.ui.judge_listWidget.currentRow()]["channel"] = self.ui.channel_comboBox.currentText()
        self.save_config()
        
    def intensity_change(self):
        if  0 <= int(self.ui.intensity.text()) <= 100:
            self.config["oscSettings"][self.ui.avatar_listWidget.currentRow()]["judgeSettings"][self.ui.judge_listWidget.currentRow()]["intensity"] = int(self.ui.intensity.text())
            self.ui.intensity_slider.setValue(int(self.ui.intensity.text()))
            self.ui.intensity.setText(str(int(self.ui.intensity.text())))          
            self.save_config()
        else:
            self.ui.intensity.setText(str(self.config["oscSettings"][self.ui.avatar_listWidget.currentRow()]["judgeSettings"][self.ui.judge_listWidget.currentRow()]["intensity"]))

    def intensity_slider_change(self):
        self.config["oscSettings"][self.ui.avatar_listWidget.currentRow()]["judgeSettings"][self.ui.judge_listWidget.currentRow()]["intensity"] = self.ui.intensity_slider.value()
        self.ui.intensity.setText(str(self.ui.intensity_slider.value()))
        self.save_config()
   
    def Ticks_change(self):
        if  0 <= int(float(self.ui.Ticks.text())*10) <= 1000:
            self.config["oscSettings"][self.ui.avatar_listWidget.currentRow()]["judgeSettings"][self.ui.judge_listWidget.currentRow()]["Ticks"] = int(float(self.ui.Ticks.text())*10)
            self.ui.Ticks_slider.setValue(int(float(self.ui.Ticks.text())*10))
            self.save_config()
        else:
            if round(float(self.config["oscSettings"][self.ui.avatar_listWidget.currentRow()]["judgeSettings"][self.ui.judge_listWidget.currentRow()]["Ticks"])/10,1) == int(float(self.config["oscSettings"][self.ui.avatar_listWidget.currentRow()]["judgeSettings"][self.ui.judge_listWidget.currentRow()]["Ticks"])/10):
                self.ui.Ticks.setText(str(int(float(self.config["oscSettings"][self.ui.avatar_listWidget.currentRow()]["judgeSettings"][self.ui.judge_listWidget.currentRow()]["Ticks"])/10)))
            else:
                self.ui.Ticks.setText(str(round(float(self.config["oscSettings"][self.ui.avatar_listWidget.currentRow()]["judgeSettings"][self.ui.judge_listWidget.currentRow()]["Ticks"])/10,1)))
    
    def Ticks_slider_change(self):
        self.config["oscSettings"][self.ui.avatar_listWidget.currentRow()]["judgeSettings"][self.ui.judge_listWidget.currentRow()]["Ticks"] = self.ui.Ticks_slider.value()
        if round(float(self.ui.Ticks_slider.value()/10),1) == int(float(self.ui.Ticks_slider.value()/10)):
            self.ui.Ticks.setText(str(int(float(self.ui.Ticks_slider.value()/10))))
        else:
            self.ui.Ticks.setText(str(round(float(self.ui.Ticks_slider.value()/10),1)))
        self.save_config()
              
    def server_ip_change(self):
        self.config["server_ip"] = self.ui.server_ip.text()
        self.save_config()
    
    def sleep_time(self):
        if  1 <= int(float(self.ui.sleep_time.text())*10) <= 100:
            self.config["sleep_time"] = round(float(self.ui.sleep_time.text()),1)
            if round(float(self.ui.sleep_time.text()),1) == int(float(self.ui.sleep_time.text())):
                self.config["sleep_time"] = int(float(self.ui.sleep_time.text()))
                self.ui.sleep_time.setText(str(int(float(self.ui.sleep_time.text()))))
            else:
                self.config["sleep_time"] = round(float(self.ui.sleep_time.text()),1)
                self.ui.sleep_time.setText(str(round(float(self.ui.sleep_time.text()),1)))
            self.save_config()
        else:
            self.ui.sleep_time.setText(str(self.config["sleep_time"]))
   
        
    def save_config(self):
        with open('config.json', 'w+', encoding="utf8") as f:
            f.write(json.dumps(self.config,ensure_ascii=False))
    
    def write_local_log(self,text:str):
        windowLog.info(text)
        self.write(text)        


    def closeEvent(self,event:QEvent):
        pass  
        #if not self.deserver_end:
            #self.de_exit_event.set()
            #while not self.deserver_end:
                #time.sleep(0.1)              
        #if not self.server_end:
            #self.osc_exit_event.set()
            #while not self.server_end:
                #time.sleep(0.1)
    #background-color: rgb(212, 148, 249);
    
    
    
        
    def eventFilter(self, obj:QObject, event:QMouseEvent):
        if obj == self.ui.console:
            if event.type() == QEvent.Type.MouseButtonPress and event.buttons() == Qt.MouseButton.RightButton:
                selected_text = self.ui.console.textCursor().selectedText()
                if selected_text:
                    #clipboard = QApplication.clipboard()
                    #clipboard.setText(selected_text)
                    pass
                return True
        return super().eventFilter(obj, event)                
     
    
    def ui_init(self):
        layout1 = QHBoxLayout()
        self.timeline = Timeline(self.ui.timeline_widget)
        layout1.addWidget(self.timeline)
        #layout1.setContentsMargins(0, 10, 0, 10)
        layout2 = QHBoxLayout()
        self.rangeslider = RangeSilder(self.ui.range_widget)
        layout2.addWidget(self.rangeslider)
        #layout2.setContentsMargins(0, 0, 0, 0)
        self.ui.timeline_widget.setLayout(layout1)
        self.ui.range_widget.setLayout(layout2)

        layout = self.ui.avatar_scrollAreaWidgetContents.layout()
        
        for index,setting in enumerate(self.config["oscSettings"]):
            btn = Avatar_btn(setting["avatarParameter"].split("/")[-1]+'('+str(index)+')')
            btn.setStyleSheet(btn.sty2)
            layout.addWidget(btn)
            btn.clicked.connect(self.avatar_btn_clicked)
            btn.delete.connect(self.avatar_remove)
            
        self.avatar_index = 0
        item = layout.itemAt(0)
        if item.widget() is not None and isinstance(item.widget(), QPushButton):
            btn = item.widget()
            btn.setStyleSheet(Avatar_btn.sty1)
            
        self.timeline_reset()
        self.timeline.value_signal.connect(self.timeline_valuechanged)


        
        
        self.ui.avatars_add_btn.clicked.connect(self.avatars_add_btn_clicked)
        self.get_value_ui()
        self.range_slider_init()
           
    
    
    def avatars_add_btn_clicked(self):        
        dialog = EditDialog(self)
        dialog.setTextToEdit('')
        if dialog.exec():
            text = dialog.getEditedText()
            new_avatar_param_dict = {
                "avatarParameter": "/avatar/parameters/"+text,
                "mode": 0,
                "judgeSettings": [
                    {
                        "value": 1,
                        "pattern": "呼吸",
                        "channel": "A",
                        "intensity": 0,
                        "ticks": 30
                    },
                    {
                        "value": 0,
                        "pattern": "呼吸",
                        "channel": "A",
                        "intensity": 100,
                        "ticks": 30
                    }
                ]
            }            
            layout = self.ui.avatar_scrollAreaWidgetContents.layout()
            num = layout.count()+1
            btn = Avatar_btn(text+'('+str(num)+')')
            btn.setStyleSheet(btn.sty2)
            layout.addWidget(btn)
            btn.clicked.connect(self.avatar_btn_clicked)
            btn.delete.connect(self.avatar_remove)
            self.config["oscSettings"].append(new_avatar_param_dict)
    
    
    def avatar_btn_clicked(self):
        obj = self.sender()
        self.avatar_btn_off()
        if isinstance(obj, QPushButton):
            btn = obj
            text = btn.text()
            pattern = r'\((\d+)\)$'
            match = re.search(pattern, text)
            self.avatar_index = int(match.group(1))
            btn.setStyleSheet(Avatar_btn.sty1)
            self.timeline_reset()
            
    def avatar_remove(self):
        if self.ui.avatar_scrollAreaWidgetContents.layout().count() <= 1:
            return
        obj = self.sender()
        if isinstance(obj, QPushButton):
            btn = obj
            text = btn.text()
            pattern = r'\((\d+)\)$'
            match = re.search(pattern, text)
            del self.config["oscSettings"][int(match.group(1))-1]            
        layout = self.ui.avatar_scrollAreaWidgetContents.layout()
        layout.removeWidget(btn)
        self.avatar_index = 0
        item = layout.itemAt(0)
        if item.widget() is not None and isinstance(item.widget(), QPushButton):
            btn = item.widget()
            btn.setStyleSheet(Avatar_btn.sty1)

            
    def avatar_btn_off(self):
        layout = self.ui.avatar_scrollAreaWidgetContents.layout()
        for i in range(layout.count()):
            item = layout.itemAt(i)
            if item.widget() is not None and isinstance(item.widget(), QPushButton):
                btn = item.widget()
                btn.setStyleSheet(Avatar_btn.sty2)
        
    def timeline_reset(self):
        self.timeline.line_points_value = []
        for t in self.config["oscSettings"][self.avatar_index]["judgeSettings"]:
            self.timeline.addpoint(t["value"])
        self.timeline.update()        
        self.selected_value = 0
        
        
                
    
    def timeline_valuechanged(self,singal:int,index:int,value:float):
        if singal == -1:
            del self.config["oscSettings"][self.avatar_index]["judgeSettings"][index]
            self.selected_value = 0
        elif singal == 1:
            self.selected_value = index
            self.selected_value_on()
        elif singal == 0:
            self.config["oscSettings"][self.avatar_index]["judgeSettings"][index]["value"] = value
        elif singal == 2:
            new_judge_dict = {
                "value": value,
                "pattern": "呼吸",
                "channel": "A",
                "intensity": 0,
                "ticks": 30
            }
            self.config["oscSettings"][self.avatar_index]["judgeSettings"].append(new_judge_dict)        
    

    def selected_value_on(self):
        self.pattem_btn_off()
        self.pattem_btn_on()
        self.channel_btn_on()
        self.ui.mode_combox.setCurrentIndex(self.config["oscSettings"][self.avatar_index]["mode"])
        self.ui.tick_label.setText(str(self.config["oscSettings"][self.avatar_index]["judgeSettings"][self.selected_value]["ticks"]/10))
        self.ui.intensity_Slider.setValue(self.config["oscSettings"][self.avatar_index]["judgeSettings"][self.selected_value]["intensity"])
                       


    def get_value_ui(self):
        self.pattem_btn_off()
        self.pattem_btn_on()
        self.ui.btn1.clicked.connect(self.pattem_btn_clicked)
        self.ui.btn2.clicked.connect(self.pattem_btn_clicked)
        self.ui.btn3.clicked.connect(self.pattem_btn_clicked)
        self.ui.btn4.clicked.connect(self.pattem_btn_clicked)
        self.ui.btn5.clicked.connect(self.pattem_btn_clicked)
        self.ui.btn6.clicked.connect(self.pattem_btn_clicked)
        self.ui.btn7.clicked.connect(self.pattem_btn_clicked)
        self.ui.btn8.clicked.connect(self.pattem_btn_clicked)
        self.ui.btn9.clicked.connect(self.pattem_btn_clicked)
        self.ui.btn10.clicked.connect(self.pattem_btn_clicked)
        self.ui.btn11.clicked.connect(self.pattem_btn_clicked)
        self.ui.btn12.clicked.connect(self.pattem_btn_clicked)
        self.ui.btn13.clicked.connect(self.pattem_btn_clicked)
        self.ui.btn14.clicked.connect(self.pattem_btn_clicked)
        self.ui.btn15.clicked.connect(self.pattem_btn_clicked)
        self.ui.btn16.clicked.connect(self.pattem_btn_clicked)        
        self.ui.intensity_label.setText(str(self.config["oscSettings"][self.avatar_index]["judgeSettings"][self.selected_value]["intensity"]))
        self.ui.intensity_Slider.setValue(self.config["oscSettings"][self.avatar_index]["judgeSettings"][self.selected_value]["intensity"])
        self.ui.intensity_Slider.valueChanged.connect(self.intensity_valuechanged)
        self.channel_btn_on()
        self.ui.A_btn.clicked.connect(self.channel_btn_clicked)
        self.ui.B_btn.clicked.connect(self.channel_btn_clicked)
        self.mode_init()
        self.tick_init()
        self.ui.save_btn.clicked.connect(self.save_config)

    
    def pattem_btn_on(self):
        if self.config["oscSettings"][self.avatar_index]["judgeSettings"][self.selected_value]["pattern"] == "呼吸":
            self.ui.btn1.setStyleSheet(self.pattem_on_sty)
        elif self.config["oscSettings"][self.avatar_index]["judgeSettings"][self.selected_value]["pattern"] == "潮汐":
            self.ui.btn2.setStyleSheet(self.pattem_on_sty)
        elif self.config["oscSettings"][self.avatar_index]["judgeSettings"][self.selected_value]["pattern"] == "连击":
            self.ui.btn3.setStyleSheet(self.pattem_on_sty)
        elif self.config["oscSettings"][self.avatar_index]["judgeSettings"][self.selected_value]["pattern"] == "快速按捏":
            self.ui.btn4.setStyleSheet(self.pattem_on_sty)
        elif self.config["oscSettings"][self.avatar_index]["judgeSettings"][self.selected_value]["pattern"] == "按捏渐强":
            self.ui.btn5.setStyleSheet(self.pattem_on_sty)
        elif self.config["oscSettings"][self.avatar_index]["judgeSettings"][self.selected_value]["pattern"] == "心跳节奏":
            self.ui.btn6.setStyleSheet(self.pattem_on_sty)
        elif self.config["oscSettings"][self.avatar_index]["judgeSettings"][self.selected_value]["pattern"] == "压缩":
            self.ui.btn7.setStyleSheet(self.pattem_on_sty)
        elif self.config["oscSettings"][self.avatar_index]["judgeSettings"][self.selected_value]["pattern"] == "节奏步伐":
            self.ui.btn8.setStyleSheet(self.pattem_on_sty)
        elif self.config["oscSettings"][self.avatar_index]["judgeSettings"][self.selected_value]["pattern"] == "颗粒摩擦":
            self.ui.btn9.setStyleSheet(self.pattem_on_sty)
        elif self.config["oscSettings"][self.avatar_index]["judgeSettings"][self.selected_value]["pattern"] == "渐变弹跳":
            self.ui.btn10.setStyleSheet(self.pattem_on_sty)
        elif self.config["oscSettings"][self.avatar_index]["judgeSettings"][self.selected_value]["pattern"] == "波浪涟漪":
            self.ui.btn11.setStyleSheet(self.pattem_on_sty)
        elif self.config["oscSettings"][self.avatar_index]["judgeSettings"][self.selected_value]["pattern"] == "雨水冲刷":
            self.ui.btn12.setStyleSheet(self.pattem_on_sty)
        elif self.config["oscSettings"][self.avatar_index]["judgeSettings"][self.selected_value]["pattern"] == "变速敲击":
            self.ui.btn13.setStyleSheet(self.pattem_on_sty)
        elif self.config["oscSettings"][self.avatar_index]["judgeSettings"][self.selected_value]["pattern"] == "信号灯":
            self.ui.btn14.setStyleSheet(self.pattem_on_sty)
        elif self.config["oscSettings"][self.avatar_index]["judgeSettings"][self.selected_value]["pattern"] == "挑逗1":
            self.ui.btn15.setStyleSheet(self.pattem_on_sty)
        elif self.config["oscSettings"][self.avatar_index]["judgeSettings"][self.selected_value]["pattern"] == "挑逗2":
            self.ui.btn16.setStyleSheet(self.pattem_on_sty)
                                                           
    def pattem_btn_clicked(self):
        btn = self.sender()
        if btn == self.ui.btn1:
            self.pattem_btn_off()
            self.ui.btn1.setStyleSheet(self.pattem_on_sty)
            self.config["oscSettings"][self.avatar_index]["judgeSettings"][self.avatar_index]["pattern"] = "呼吸"
        elif btn == self.ui.btn2:
            self.pattem_btn_off()
            self.ui.btn2.setStyleSheet(self.pattem_on_sty)
            self.config["oscSettings"][self.avatar_index]["judgeSettings"][self.avatar_index]["pattern"] = "潮汐"            
        elif btn == self.ui.btn3:
            self.pattem_btn_off()
            self.ui.btn3.setStyleSheet(self.pattem_on_sty)
            self.config["oscSettings"][self.avatar_index]["judgeSettings"][self.avatar_index]["pattern"] = "连击"          
        elif btn == self.ui.btn4:
            self.pattem_btn_off()
            self.ui.btn4.setStyleSheet(self.pattem_on_sty)
            self.config["oscSettings"][self.avatar_index]["judgeSettings"][self.avatar_index]["pattern"] = "快速按捏"
        elif btn == self.ui.btn5:
            self.pattem_btn_off()
            self.ui.btn5.setStyleSheet(self.pattem_on_sty)
            self.config["oscSettings"][self.avatar_index]["judgeSettings"][self.avatar_index]["pattern"] = "按捏渐强"
        elif btn == self.ui.btn6:
            self.pattem_btn_off()
            self.ui.btn6.setStyleSheet(self.pattem_on_sty)
            self.config["oscSettings"][self.avatar_index]["judgeSettings"][self.avatar_index]["pattern"] = "心跳节奏"            
        elif btn == self.ui.btn7:
            self.pattem_btn_off()
            self.ui.btn7.setStyleSheet(self.pattem_on_sty)
            self.config["oscSettings"][self.avatar_index]["judgeSettings"][self.avatar_index]["pattern"] = "压缩"               
        elif btn == self.ui.btn8:
            self.pattem_btn_off()
            self.ui.btn8.setStyleSheet(self.pattem_on_sty)
            self.config["oscSettings"][self.avatar_index]["judgeSettings"][self.avatar_index]["pattern"] = "节奏步伐" 
        elif btn == self.ui.btn9:
            self.pattem_btn_off()
            self.ui.btn9.setStyleSheet(self.pattem_on_sty)
            self.config["oscSettings"][self.avatar_index]["judgeSettings"][self.avatar_index]["pattern"] = "颗粒摩擦"                                                 
        elif btn == self.ui.btn10:
            self.pattem_btn_off()
            self.ui.btn10.setStyleSheet(self.pattem_on_sty)
            self.config["oscSettings"][self.avatar_index]["judgeSettings"][self.avatar_index]["pattern"] = "渐变弹跳" 
        elif btn == self.ui.btn11:
            self.pattem_btn_off()
            self.ui.btn11.setStyleSheet(self.pattem_on_sty)
            self.config["oscSettings"][self.avatar_index]["judgeSettings"][self.avatar_index]["pattern"] = "波浪涟漪"             
        elif btn == self.ui.btn12:
            self.pattem_btn_off()
            self.ui.btn12.setStyleSheet(self.pattem_on_sty)
            self.config["oscSettings"][self.avatar_index]["judgeSettings"][self.avatar_index]["pattern"] = "雨水冲刷"             
        elif btn == self.ui.btn13:
            self.pattem_btn_off()
            self.ui.btn13.setStyleSheet(self.pattem_on_sty)
            self.config["oscSettings"][self.avatar_index]["judgeSettings"][self.avatar_index]["pattern"] = "变速敲击"             
        elif btn == self.ui.btn14:
            self.pattem_btn_off()
            self.ui.btn14.setStyleSheet(self.pattem_on_sty)
            self.config["oscSettings"][self.avatar_index]["judgeSettings"][self.avatar_index]["pattern"] = "信号灯"
        elif btn == self.ui.btn15:
            self.pattem_btn_off()
            self.ui.btn15.setStyleSheet(self.pattem_on_sty)
            self.config["oscSettings"][self.avatar_index]["judgeSettings"][self.avatar_index]["pattern"] = "挑逗1" 
        elif btn == self.ui.btn16:
            self.pattem_btn_off()
            self.ui.btn16.setStyleSheet(self.pattem_on_sty)
            self.config["oscSettings"][self.avatar_index]["judgeSettings"][self.avatar_index]["pattern"] = "挑逗2" 

    def pattem_btn_off(self):
        self.ui.btn1.setStyleSheet(self.pattem_off_sty)
        self.ui.btn2.setStyleSheet(self.pattem_off_sty)
        self.ui.btn3.setStyleSheet(self.pattem_off_sty)
        self.ui.btn4.setStyleSheet(self.pattem_off_sty)
        self.ui.btn5.setStyleSheet(self.pattem_off_sty)
        self.ui.btn6.setStyleSheet(self.pattem_off_sty)
        self.ui.btn7.setStyleSheet(self.pattem_off_sty)
        self.ui.btn8.setStyleSheet(self.pattem_off_sty)
        self.ui.btn9.setStyleSheet(self.pattem_off_sty) 
        self.ui.btn10.setStyleSheet(self.pattem_off_sty)
        self.ui.btn11.setStyleSheet(self.pattem_off_sty)
        self.ui.btn12.setStyleSheet(self.pattem_off_sty)
        self.ui.btn13.setStyleSheet(self.pattem_off_sty)
        self.ui.btn14.setStyleSheet(self.pattem_off_sty)
        self.ui.btn15.setStyleSheet(self.pattem_off_sty)
        self.ui.btn16.setStyleSheet(self.pattem_off_sty)


                    
    def intensity_valuechanged(self):
        self.config["oscSettings"][self.avatar_index]["judgeSettings"][self.selected_value]["intensity"] = self.ui.intensity_Slider.value()
        self.ui.intensity_label.setText(str(self.ui.intensity_Slider.value()))

    def channel_btn_on(self):
        self.ui.A_btn.setStyleSheet(self.channel_off_sty)
        self.ui.B_btn.setStyleSheet(self.channel_off_sty)
        if self.config["oscSettings"][self.avatar_index]["judgeSettings"][self.selected_value]["channel"] == "A":
            self.ui.A_btn.setStyleSheet(self.channel_on_sty)
        else:
            self.ui.B_btn.setStyleSheet(self.channel_on_sty)
    
    
    def channel_btn_clicked(self):
        btn = self.sender()
        if btn == self.ui.A_btn:
            self.ui.A_btn.setStyleSheet(self.channel_on_sty)
            self.ui.B_btn.setStyleSheet(self.channel_off_sty)
            self.config["oscSettings"][self.avatar_index]["judgeSettings"][self.selected_value]["channel"] = "A"
        else:
            self.ui.A_btn.setStyleSheet(self.channel_off_sty)
            self.ui.B_btn.setStyleSheet(self.channel_on_sty)
            self.config["oscSettings"][self.avatar_index]["judgeSettings"][self.selected_value]["channel"] = "B"
            

    def mode_init(self):
        self.ui.mode_combox.setCurrentIndex(self.config["oscSettings"][self.avatar_index]["mode"])
        self.ui.mode_combox.currentIndexChanged.connect(self.mode_change)  

    def mode_change(self):                                       
        self.config["oscSettings"][self.avatar_index]["mode"] = self.ui.mode_combox.currentIndex()
        
    
    def tick_init(self):
        self.ui.tick_label.setText(str(self.config["oscSettings"][self.avatar_index]["judgeSettings"][self.selected_value]["ticks"]/10))
        self.ui.ticks_add_btn.clicked.connect(self.tick_change)
        self.ui.ticks_decrease_btn.clicked.connect(self.tick_change)
        
    
    def tick_change(self):
        btn = self.sender()
        if btn == self.ui.ticks_add_btn:
            self.config["oscSettings"][self.avatar_index]["judgeSettings"][self.selected_value]["ticks"] += 1
            self.ui.tick_label.setText(str(self.config["oscSettings"][self.avatar_index]["judgeSettings"][self.selected_value]["ticks"]/10))
        else:
            if self.config["oscSettings"][self.avatar_index]["judgeSettings"][self.selected_value]["ticks"] - 1 > 1:
               self.config["oscSettings"][self.avatar_index]["judgeSettings"][self.selected_value]["ticks"] -= 1
               self.ui.tick_label.setText(str(self.config["oscSettings"][self.avatar_index]["judgeSettings"][self.selected_value]["ticks"]/10))
               
    
    def range_slider_init(self):
        self.rangeslider.setmaxvalue(self.config["valuemax"])
        self.rangeslider.setminvalue(self.config["valuemin"])
     
     
               

class Timeline(QWidget):
    
    value_signal = Signal(int,int,float)
    
    def __init__(self, parent:QWidget=None):
        super().__init__(parent)
         
        self.setMinimumSize(100, 50)
        self.maxvalue = 2
        self.minvalue = 0        
        self.line_vacant = 10
        self.point_edge = 5
        self.point_min = self.line_vacant + self.point_edge
        self.point_max = self.width() - self.line_vacant*2 - self.point_edge
        point_1_value = 0       
        value_intervals = 0
        self.get_point_x(point_1_value)
        point_2_value = point_1_value + value_intervals
        self.line_points_value:list[float] = [point_1_value,point_2_value] 
        self.selected_point_index :int = -1  
        self.get_point_index:int = -1
        

        
        self.mousex2 = False
        
        self.point_color = QColor(189, 147, 249)
        self.selected_point_color = QColor(255, 121, 198)
        self.text_color = QColor(221, 221, 221)
        

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
       
        line_path = QPainterPath()
        line_path.addRoundedRect(QRect(self.line_vacant, self.height() / 2 - 5, self.width() - self.line_vacant*2-self.point_edge*2, 10), 5, 5)
        line_color = QColor(52, 59, 72) 
        painter.setPen(QPen(line_color, 0)) 
        painter.fillPath(line_path, QBrush(line_color))


        
        point_color = self.point_color
        selected_point_color = self.selected_point_color
        point_brush = QBrush(point_color)
        painter.setBrush(point_brush)  

       
        text_color = self.text_color
        painter.setFont(QFont("Microsoft YaHei", 8))
        

        for value in self.line_points_value:
            if self.selected_point_index != -1:
                if value == self.line_points_value[self.selected_point_index]:
                    painter.setPen(selected_point_color)
                    painter.setBrush(selected_point_color)
                else:
                    painter.setPen(point_color)
                    painter.setBrush(point_color)                    
            else:
                painter.setPen(point_color)
                painter.setBrush(point_color)
            point_x = self.get_point_x(value)
            painter.drawEllipse(point_x - self.point_edge, self.height()/2 - self.point_edge, self.point_edge*2, self.point_edge*2)     
            text_rect = painter.boundingRect(QRect(), Qt.AlignmentFlag.AlignCenter, str(value))
            text_rect.moveCenter(QPoint(point_x, self.height()/2 + 10))
            painter.setPen(text_color)
            painter.drawText(text_rect, Qt.AlignmentFlag.AlignCenter, str(value))
    
    def get_point_x(self, value:float):
        self.point_min = self.line_vacant + self.point_edge
        self.point_max = self.width() - self.line_vacant*2 - self.point_edge
        k = (self.point_max - self.point_min) / (self.maxvalue - self.minvalue)
        b = self.point_min - k * self.minvalue
        y = k * value + b
        point_intervals = self.point_edge*2
        self.value_intervals = (point_intervals - b)/k
        return y


    def get_point_value(self, point_x:float):
        self.point_min = self.line_vacant + self.point_edge
        self.point_max = self.width() - self.line_vacant*2 - self.point_edge
        k = (self.point_max - self.point_min) / (self.maxvalue - self.minvalue)
        b = self.point_min - k * self.minvalue
        value = (point_x - b) / k
        value = self.get_fit_value(value)
        return value


        

    def get_fit_value(self, value:float):
        if float(value) == int(value):
            value_str = str(int(value))
            value = int(value)
        elif float(value*10) == int(value*10) :
            value_str = f"{value:.1f}"
            value = float(value_str)
        else:
            value_str = f"{value:.2f}"
            value = float(value_str)
        return value        



    def mousePressEvent(self, event:QMouseEvent):
        signal = self.query_Selected(event)       
        if event.buttons() == Qt.MouseButton.MiddleButton:
            if signal == 1:                              
                if len(self.line_points_value) <= 2:
                    return
                value = self.line_points_value[self.get_point_index]
                self.line_points_value.remove(value)  
                self.value_signal.emit(-1,self.get_point_index,value)
                self.get_point_index = self.selected_point_index = -1
        if event.button()  == Qt.MouseButton.LeftButton:
            if signal == 1 :
                self.selected_point_index = self.get_point_index
                self.value_signal.emit(1,self.selected_point_index,0)
            elif signal == -1:
                new_point_value = self.get_point_value(event.position().x())
                self.line_points_value.append(new_point_value)
                self.value_signal.emit(2,0,new_point_value)                                                             
        elif event.button()  == Qt.MouseButton.RightButton:
            self.mousex2 = True   
        self.update()
        

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button()  == Qt.MouseButton.RightButton:
            self.mousex2 = False

    def mouseMoveEvent(self, event: QMouseEvent):   
        if self.mousex2 and self.get_point_index != -1:
            if  self.point_min < event.position().x() < self.point_max:
                for index,value in enumerate(self.line_points_value):
                    if index != self.get_point_index:
                        point_x = self.get_point_x(value)
                        if point_x - self.point_edge*2 < event.position().x() < point_x + self.point_edge*2:
                            return
                set_value = self.get_point_value(event.position().x())
                self.line_points_value[self.get_point_index] = set_value
                self.value_signal.emit(0,self.get_point_index,set_value)                  
                self.query_Selected(event)
                self.update()
                


    def query_Selected(self,event:QMouseEvent):
        click_point = event.position()
        if self.height()/2 - 5 < click_point.y() < self.height()/2 +5 :        
            for index,value in enumerate(self.line_points_value):
                point_x = self.get_point_x(value)
                if point_x - self.point_edge*2 < click_point.x() < point_x + self.point_edge*2 :
                    if not self.mousex2: 
                        self.get_point_index = index
                    return 1       
            return -1
        else:
            self.selected_point_index = -1 
        return 0
                
    def addpoint(self,value):
        new_value = self.get_fit_value(value)
        value_x = self.get_point_x(new_value)
        for value in self.line_points_value:
            point_x = self.get_point_x(value)
            if point_x - self.point_edge*2 < value_x < point_x + self.point_edge*2:
                return False             
        self.line_points_value.append(new_value)
        self.update()
        return True
        
    def movepoint(self,value):
        if self.selected_point_index != -1:
            return
        x = self.get_point_x(value)           
        for index ,value in enumerate(self.line_points_value):
            point_x = self.get_point_x(value)
            if index != self.selected_point_index and point_x - self.point_edge*2 <= x <= point_x + self.point_edge*2:
                return False 
        self.line_points_value[self.selected_point_index] = value
        self.update()
        return True

    
    def deletepoint(self):
        if self.selected_point_index:
            self.line_points_value.remove(self.line_points_value(self.selected_point_index))
            self.selected_point = -1
            self.update()
            return True
    
    def setvaluemax(self,maxvalue):
        maxvalue = self.get_fit_value(maxvalue)
        if maxvalue < self.minvalue + self.value_intervals:
            return
        for value in self.line_points_value:
            if value > maxvalue:
                return
        self.maxvalue = maxvalue
        self.value_signal.emit(3,4,maxvalue)
        self.update()        
    
    def setvaluemin(self,minvalue):
        minvalue = self.get_fit_value(minvalue)
        if minvalue > self.maxvalue - self.value_intervals:
            return
        for value in self.line_points_value:
            if value < minvalue:
                return
        self.minvalue = minvalue
        self.value_signal.emit(3,4,minvalue)
        self.update()       
    
        


class RangeSilder(QWidget):
    
    value_signal = Signal(int,float)
    
    def __init__(self, parent:QWidget=None):
        super().__init__(parent)
        
        self.setMinimumSize(100, 50)
        self.maxvalue = 10
        self.minvalue = 0

        
        self.line_vacant = 10
        self.point_edge = 5
        self.point_min = self.line_vacant + self.point_edge
        self.point_max = self.width() - self.line_vacant*2 - self.point_edge
        self.init_width = self.width()
        self.old_point_max = self.width() - self.line_vacant*2 - self.point_edge

        
        self.point_1 = QPoint()
        self.point_2 = QPoint()
        self.point_1.setX(self.point_min)
        self.point_1.setY(self.height())
        self.point_2.setX(self.point_min+self.point_edge*2)
        self.point_2.setY(self.height())
        self.line_points:list[QPoint] = [self.point_1,self.point_2] 
        self.selected_point :QPoint = None   
        

        
        self.mousex1 = False
        
        self.point_color = QColor(189, 147, 249)
        self.selected_point_color = QColor(255, 121, 198)
        self.text_color = QColor(221, 221, 221)
        

    def paintEvent(self, event):
        self.point_max = self.width() - self.line_vacant*2 - self.point_edge
        if self.init_width != self.width():
            self.init_width = self.width()  
            for i, point in enumerate(self.line_points):
                point_range = self.old_point_max - self.point_min
                value_range = self.maxvalue - self.minvalue
                ratio = (point.x() - self.point_min) / point_range
                value = self.minvalue + ratio * value_range             
                point_range = self.point_max - self.point_min
                value_range = self.maxvalue - self.minvalue
                x = (value - self.minvalue) * point_range /(value_range) + self.point_min
                y = self.height() / 2
                self.line_points[i] = QPoint(x, y)  
        
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)        
        line_path = QPainterPath()
        line_path.addRoundedRect(QRect(self.line_vacant, self.height() / 2 - 5, self.width() - self.line_vacant*2-self.point_edge*2, 10), 5, 5)
        line_color = QColor(52, 59, 72) 
        painter.setPen(QPen(line_color, 0)) 
        painter.fillPath(line_path, QBrush(line_color))


        
        point_color = self.point_color
        selected_point_color = self.selected_point_color
        point_brush = QBrush(point_color)
        painter.setBrush(point_brush)  

        
        text_color = self.text_color
        painter.setFont(QFont("Microsoft YaHei", 9))
        

        for point in self.line_points:   
            if point == self.selected_point:
                painter.setPen(selected_point_color)
                painter.setBrush(selected_point_color)
            else:
                painter.setPen(point_color)
                painter.setBrush(point_color)
            painter.drawEllipse(point.x() - self.point_edge, point.y() - self.point_edge, self.point_edge*2, self.point_edge*2)           
            _ , value = self.get_index_value(point)
            value_str = str(value)

            text_rect = painter.boundingRect(QRect(), Qt.AlignmentFlag.AlignCenter, value_str)
            text_rect.moveCenter(QPoint(point.x(), point.y() + 10))
            painter.setPen(text_color)
            painter.drawText(text_rect, Qt.AlignmentFlag.AlignCenter, value_str)
            
    def mousePressEvent(self, event:QMouseEvent):
        self.query_Selected(event)       
        if event.button()  == Qt.MouseButton.LeftButton:
            self.mousex1 = True                            
        self.update()

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button()  == Qt.MouseButton.RightButton:
            self.selected_point = None 
            self.mousex1 = False

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.mousex1 and self.selected_point:
            if  self.point_min <= event.position().x() <= self.point_max:
                for point in self.line_points:
                    if point != self.selected_point:
                        if point.x() - self.point_edge*2 < event.position().x() < point.x() + self.point_edge*2:
                            return
                self.selected_point.setX(event.position().x())
                _,value = self.get_index_value(self.selected_point)
                if event.position().x() < self.point_2.x():                    
                    self.value_signal.emit(1,value)
                else:
                    self.value_signal.emit(2,value)
                self.update()



    def query_Selected(self,event:QMouseEvent):
        click_point = event.position()
        if self.height()/2 - self.point_edge <= click_point.y() <= self.height()/2 + self.point_edge :        
            for point in self.line_points:
                if point.x() - self.point_edge*2 < click_point.x() < point.x() + self.point_edge*2:
                        self.selected_point = point       
        else:
            self.selected_point = None 


                       

    def get_index_value(self,point:QPoint):
        point_range = self.point_max - self.point_min
        value_range = self.maxvalue - self.minvalue
        ratio = (point.x() - self.point_min) / point_range
        value = self.minvalue + ratio * value_range
        if float(value) == int(value):
            value_str = str(int(value))
            value = int(value)
        elif float(value*10) == int(value*10) :
            value_str = f"{value:.1f}"
            value = float(value_str)
        else:
            value_str = f"{value:.2f}"
            value = float(value_str)       
        index = self.line_points.index(point)
        return index,value

    def setmaxvalue(self,value):
        if self.point_1.x() > self.point_2.x():
            pointmax = self.point_1
            pointmin = self.point_2
        else:
            pointmax = self.point_2
            pointmin = self.point_1
        point_range = self.point_max - self.point_min
        value_range = self.maxvalue - self.minvalue
        x = (value - self.minvalue) * point_range /(value_range) + self.point_min
        _,valuemin = self.get_index_value(pointmin) 
        if valuemin >= value:
            return
        pointmax.setX(x)       
        self.update()

    def setminvalue(self,value):
        if self.point_1.x() < self.point_2.x():
            pointmin = self.point_1
            pointmax = self.point_2
        else:
            pointmin = self.point_2
            pointmax = self.point_1
        point_range = self.point_max - self.point_min
        value_range = self.maxvalue - self.minvalue
        x = (value - self.minvalue) * point_range /(value_range) + self.point_min
        _,valuemax = self.get_index_value(pointmax) 

        if valuemax <= value:
            return
        pointmin.setX(x)      
        self.update()
    
    

class Avatar_btn(QPushButton):

    delete = Signal()
    
    sty1 = ("QPushButton {"
        "border: no;"
        "background-position: center;"
        "background-repeat: no-repeat; "
        "border-radius: 10px;"
        "background-color: rgb(193, 137, 228);"
        "font: 10pt \"微软雅黑\";"
        "color: rgb(225, 225, 225);"
        "}"
        "QMenu{"
        "background:rgb(40,47,56);"
        "}"
        "QMenu::item{"
        "background:rgb(60,67,76);"
        "font: 10pt \"微软雅黑\";"
        "color: rgb(225, 225, 225);" 
        "text-align: center;"     
        "}"
        "QMenu::item:hover{"
        "background:rgb(255, 121, 198);"
        "color: rgb(225, 255, 255);"
        "}"
        "QMenu::item:selected{"
        "background:rgb(255, 121, 198);"
        "color: rgb(225, 255, 255);"        
        "}"                      
        )
    sty2 = (
            "QPushButton {"
            "border: no;"
            "background-position: center;"
            "background-repeat: no-repeat; "
            "border-radius: 10px;"
            "background-color: rgb(33, 37, 43);"
            "font: 10pt \"微软雅黑\";"
            "color: rgb(225, 225, 225);"
        "}"
        "QPushButton:hover {"
            "background-color: rgb(133,137, 143);"
            "border: none;"
        "}"
        "QMenu{"
        "background:rgb(40,47,56);"
        "}"
        "QMenu::item{"
        "background:rgb(60,67,76);"
        "font: 10pt \"微软雅黑\";"
        "color: rgb(225, 225, 225);" 
        "text-align: center;"     
        "}"
        "QMenu::item:hover{"
        "background:rgb(255, 121, 198);"
        "color: rgb(225, 255, 255);"
        "}"
        "QMenu::item:selected{"
        "background:rgb(255, 121, 198);"
        "color: rgb(225, 255, 255);"        
        "}"         
        )
        
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setFixedSize(82,50)
        self.setStyleSheet(self.sty1)
        self.menubar= QMenu(self)     
        self.action1 = QAction("重命名", self)
        self.action2 = QAction("删除", self)
        self.menubar.addAction(self.action1)
        self.menubar.addAction(self.action2)
        self.action1.triggered.connect(self.enterEditMode)
        self.action2.triggered.connect(self.deleteSelf)
        
    def mousePressEvent(self, event:QMouseEvent):     
        if event.button()  == Qt.MouseButton.RightButton:
            self.menubar.popup(event.globalPosition().toPoint())                           
        else:
            super().mousePressEvent(event)

    def enterEditMode(self):
        dialog = EditDialog(self)
        dialog.setTextToEdit(self.text())
        if dialog.exec():
            self.setText(dialog.getEditedText())

    def deleteSelf(self):
        self.delete.emit()
        self.setParent(None)
        self.deleteLater()
        


class EditDialog(QDialog):
        
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("")
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setFixedSize(600, 400)
        self.setStyleSheet("background: rgb(40,47,56);")
        layout1 = QVBoxLayout()
        self.line_edit = QLineEdit()
        self.line_edit.setStyleSheet("color: rgb(255,255,255);font: 10pt \"微软雅黑\"")
        layout1.addWidget(self.line_edit)
        button_layout = QHBoxLayout()
        ok_button = QPushButton("")
        ok_button.setStyleSheet(
        "QPushButton {"
        "border: no;"
        "background-position: center;"
        "background-repeat: no-repeat; "
        "border-radius: 10px;"
        "background-color: rgb(40,47,56);"
        "background-image: url(:/forms/icons/cil-check-alt.png);"                      
        "}"
        "QPushButton:hover {"
            "background-color: rgb(140,147,156);"
            "border: none;}"       
        )
        ok_button.clicked.connect(self.accept)
        ok_button.setFixedSize(100, 40)
        cancel_button = QPushButton("")  
        cancel_button.setStyleSheet(
        "QPushButton {"
        "border: no;"
        "background-position: center;"
        "background-repeat: no-repeat; "
        "border-radius: 10px;"
        "background-color: rgb(40,47,56);"
        "background-image: url(:/forms/icons/cil-x.png);"                      
        "}"
        "QPushButton:hover {"
            "background-color: rgb(140,147,156);"
            "border: none;}"       
        )
        cancel_button.setFixedSize(100, 40)  
        cancel_button.clicked.connect(self.reject)    
        button_layout.addWidget(ok_button)
        button_layout.addWidget(cancel_button)
        layout1.addLayout(button_layout)
        self.setLayout(layout1)
        screen = QApplication.primaryScreen()
        screen_rect = screen.availableGeometry()
        screen_width = screen_rect.width()
        screen_height = screen_rect.height()      
        dialog_width = self.width()
        dialog_height = self.height()
        x = (screen_width - dialog_width) / 2
        y = (screen_height - dialog_height) / 2
        self.move(x,y)
        
    
    def setTextToEdit(self, text):
        self.line_edit.setText(text)

    def getEditedText(self):
        return self.line_edit.text()
    
    
    def mousePressEvent(self, event:QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPosition().toPoint() - self.pos()
            event.accept()
    
    def mouseMoveEvent(self, event:QMouseEvent):
        if Qt.MouseButton.LeftButton == event.buttons() and self.m_drag:
            self.move(event.globalPosition().toPoint() - self.m_DragPosition)
            event.accept()
            
    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        self.m_drag = False


        

class DGLabServerThread(QThread):
    
    console_signal = Signal(str)
    img_signal = Signal(str,str)
    
    def __init__(self,Gui:Loadingwindow,exit_event:Event) -> None:
        super().__init__()
        
        self.gui=Gui
        self.exit_event=exit_event
        self.bind_event=Event()
        self.strengthData:StrengthData=None
        self.task=None

    def run(self):
        self.task=asyncio.run(self.serverStart())
        self.write_log('dglabServer stopped')
        self.gui.deserver_end = True
        
    def create_qrcode(self,data):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        return img
        
    def print_qrcode(self,data: str):
        """输出二维码到终端界面"""
        img = 'qrcode.png'
        image=self.create_qrcode(data)
        image.save('qrcode.png')      
        self.write_log("生成二维码成功！")
        self.img_signal.emit(img,"等待客服端连接") 
        # image.show()

    def write_log(self,text:str):
        dglabLog.info(text)
        self.console_signal.emit(text)
        print("dglabLog:"+text)


    async def serverStart(self):
        async with DGLabWSServer("0.0.0.0", 5678, 60) as server:
            self.client = server.new_local_client()
            if self.gui.config["ipAddress"]=="":ip=str(socket.gethostbyname(socket.getfqdn()))
            else: ip=self.gui.config["ipAddress"]
            url = self.client.get_qrcode(f"ws://{ip}:5678")
            self.print_qrcode(url)
            self.write_log("请用 DG-Lab App 扫描二维码以连接")
            
            # 等待绑定
            while True:
                try:
                    await asyncio.wait_for(self.client.bind(), timeout = 1)
                    break
                except:
                    if self.exit_event.is_set():
                        return
            self.write_log(f"已与 App {self.client.target_id} 成功绑定")
            self.bind_event.set()
            self.img_signal.emit("qrcode.png","连接成功！") 

            async for data in self.client.data_generator(FeedbackButton, RetCode,StrengthData):
                if self.exit_event.is_set():                 
                    return                
                if isinstance(data,StrengthData):
                    self.strengthData=data
                    self.strengthData

                # if isinstance(data, FeedbackButton):
                #     dglabLog.info(f"App 触发了反馈按钮：{data.name}")

                #     if data == FeedbackButton.A1:
                #         # 顺序发送波形
                #         dglabLog.info("对方按下了 A 通道圆圈按钮")

                # 接收 心跳 / App 断开通知
                elif data == RetCode.CLIENT_DISCONNECTED:
                    self.write_log("App 已断开连接，你可以尝试重新扫码进行连接绑定")
                    self.bind_event.clear()
                    await self.client.rebind()
                    self.bind_event.set()
                    self.write_log("重新绑定成功")
                    self.img_signal.emit("qrcode.png","等待客服端连接")

    


class ServerThread(QThread):
    
    console_signal = Signal(str)
    btn_signal = Signal(int)
    
    def __init__(self,Gui:Loadingwindow,exit_event:Event,dgServer:DGLabServerThread=None) -> None:
        super().__init__()
        self.exit_event=exit_event
        self.gui=Gui
        self.dgServer=dgServer
        self.OSCclient=None
        self.config=None
        self.patterns=None
        self.osclink = False
        self.write_log_info("server start")
        self.patterns = self.gui.patterns
        self.config = self.gui.config


    def run(self):
        try:
            browser = OSCQueryBrowser()
            time.sleep(2)
            self.configInit()
            service = browser.find_service_by_name("VRChat-Client")
            self.OSCclient = OSCQueryClient(service)
            self.write_log_info("link vrchat osc successfully")  
            self.osclink = True
            self.btn_signal.emit(1)
        except  Exception as e:
            self.write_log_info("cannot Find OSC please open server after VRCHAT started")
            self.write_log_info("请在当VRCHAT启动以后再运行")
            self.write_log_warning(f"unexcepted error:{e}|type:{type(e)}")    
            self.btn_signal.emit(2)
            self.gui.server_end = True   
            return           
        self.task=asyncio.run(self.webSocketstart())
        self.write_log_info('oscserver closed')
        self.gui.server_end = True
    
                          
    
                
    async def webSocketstart(self):
        last_id=list()
        for i in range(0,len(self.config["oscSettings"])):last_id.append(None)
        while not self.exit_event.is_set():
            try:
                self.dgServer.bind_event.wait(timeout=5)
                if not self.dgServer.bind_event.is_set(): 
                    self.write_log_info("waiting for dgserver bind 等待dglab socket扫码绑定")
                    continue               
                maxtick=0
            except:
                self.write_log_error(f"unexcepted error:{e}|type:{type(e)}")
                continue
            try:
                for i in range(0,len(self.config["oscSettings"])):
                    node = self.OSCclient.query_node(self.config["oscSettings"][i]["avatarParameter"])
                    id=self.judge(i,value=node.value[0])
                    if id is not None :
                        ticks=int(self.config["oscSettings"][i]["judgeSettings"][id]["ticks"])
                        if self.config["oscSettings"][i]["mode"]in[0,1,2]:                            
                            tickstime=await self.sendMessage(i,id,ticks)
                            if maxtick<tickstime:maxtick=tickstime
                        if self.config["oscSettings"][i]["mode"]==3 and id==-1:
                            tickstime=await self.sendMessage(i,id,ticks)
                            if maxtick<tickstime:maxtick=tickstime
                        if self.config["oscSettings"][i]["mode"]==4:
                            if last_id[i]is None:
                                last_id[i]==id
                                time.sleep(1)
                            if last_id[i]is not None and last_id[i]!=id:
                                last_id[i]==id
                                tickstime=await self.sendMessage(i,id,ticks)
                                if maxtick<tickstime:maxtick=tickstime
                time.sleep(self.config["sleepTime"]+maxtick/10)  
            except TimeoutError:  
                self.write_log_warning("Timeout,Sever cannot connect to APP,please check APP||连接超时,无法连接至APP请检查APP是否处于运行状态")
                time.sleep(1)
            except AttributeError:
                self.write_log_warning("Server cannot get value,please check avatar parameters or VRCHAT||无法检测到指定的模型参数,请检查模型参数是否正确")
                time.sleep(1)
            except ConnectionRefusedError:
                self.write_log_warning("ConnectionRefused,Server cannot to APP,please check APP||无法连接致手机APP,请检查手机APP是否开启")
                time.sleep(1) 
            except  Exception as e:
                self.write_log_error(f"unexcepted error:{e}|type:{type(e)}")
                self.btn_signal.emit(2)
                time.sleep(1)
        
    
        
    async def sendMessage(self,i,id,ticks):
            pattern_name=self.config["oscSettings"][i]["judgeSettings"][id]["pattern"]
            pattern=self.patterns[pattern_name]
            channel=self.getChannel(self.config["oscSettings"][i]["judgeSettings"][id]["channel"])

            looptime=self.getPatternLoopTime(pattern_name,ticks)
            inCorrectIntensity,expected_intensity=self.isInCorrectIntensity(i,id,channel)
            if inCorrectIntensity is None:
                self.write_log_error(f"unexcepted intensity error")
                return None
            if not inCorrectIntensity: 
                self.write_log_info(f"SetStrength:{expected_intensity}")
                await self.dgServer.client.set_strength(channel,StrengthOperationType.SET_TO,expected_intensity)
            await self.dgServer.client.add_pulses(channel,*(pattern*looptime))
            self.write_log_info(f"Sent|channel:{channel}|name:{pattern_name}|intensity:{expected_intensity}|strength Data:{self.dgServer.strengthData}|ticks:{ticks}|time:{len(pattern)/10*looptime} s")
            return len(pattern)*looptime
    
    def configInit(self):
        for i in range(0,len(self.config["oscSettings"])): 
            point=self.config["oscSettings"][i]
            if point["mode"]==1 and len(point["judgeSettings"])>1:
                point["judgeSettings"].sort(key=lambda value:value["value"], reverse=True)
            if point["mode"]==2 and len(point["judgeSettings"])>1:
                point["judgeSettings"].sort(key=lambda value:value["value"], reverse=False)
                
    def judge(self,i,value):

        mode=int(self.config["oscSettings"][i]["mode"])
        judgeValue=self.config["oscSettings"][i]["judgeSettings"]
        for index in range(0,len(judgeValue)):
            if mode==0:
                if value==judgeValue[index]["value"]:return index
            elif mode==1:
                if value>=judgeValue[index]["value"]:return index
            elif mode==2:
                if value<=judgeValue[index]["value"]:return index
            elif mode==3:
                return -1
            elif mode==4:
                if value==judgeValue[index]["value"]:return index
            else:
                serverLog.error(f"unexpected json 参数错误 mode{i} error ")
        return None

    def getChannel(self,value):
        if value=='A':return Channel.A
        if value=='B':return Channel.B
        self.write_log_error(f"unexpected json 参数错误 channel error ") 

    def isInCorrectIntensity(self,i,id,channel:Channel):
        intensity=int(self.config["oscSettings"][i]["judgeSettings"][id]["intensity"])
        expected_intensity=None
        current_intensity=None
        if channel==Channel.A:
            expected_intensity=int(intensity/100*self.dgServer.strengthData.a_limit)
            current_intensity=self.dgServer.strengthData.a
        if channel==Channel.B:
            expected_intensity=int(intensity/100*self.dgServer.strengthData.b_limit)  
            current_intensity=self.dgServer.strengthData.b
        if expected_intensity is not None and current_intensity is not None:
            return expected_intensity==current_intensity,expected_intensity
        else:
            return None,None
    
    def getPatternLoopTime(self,pattern_name,ticks)->int:
        one_round_tick=len(self.patterns[pattern_name])
        num=int(ticks/one_round_tick)
        return num+1
    
    def getMessage(self,i,id):
        
        return self.config["patternSettings"][self.config["oscSettings"][i]["judgeSettings"][id]["pattern"]]

    def getParamaterValue(self,message,paramaterstring):
        if paramaterstring in message:return message[paramaterstring]
        if f"A_{paramaterstring}" in message:return message[f"A_{paramaterstring}"]
        if f"B_{paramaterstring}" in message:return message[f"B_{paramaterstring}"]

    def write_log_info(self,text:str):
        serverLog.info(text)
        self.console_signal.emit(text)
        print("serverLog:"+text)
    
    def write_log_warning(self,text:str):
        serverLog.warning(text)
        self.console_signal.emit(text)
        print("serverwarning:"+text)
        
    def write_log_error(self,text:str):
        serverLog.error(text)
        self.console_signal.emit(text)
        print("servererror:"+text)





if __name__ == '__main__':       
    app =   QApplication([])
    window = Loadingwindow()   
    window.show()
    app.exec()