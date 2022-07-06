import os
from audioop import tostereo
from multiprocessing.sharedctypes import RawValue

import kivy
from kivy.config import Config
from kivy.properties import StringProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivymd.toast.kivytoast.kivytoast import toast
from typing_extensions import Self

import automail
import Capture_Image
import check_camera
import Recognize
import Train_Image

Config.set('input', 'mouse', 'mouse,multitouch_on_demand')


class AuttendoApp(MDApp):

    def build(self):
        return


class WindowManager(ScreenManager):
    pass


class MainWindow(Screen):

    data = {
        "About Us": "account-box",
        "Suggestions": "lightbulb"
    }


input_cam = 0


class SysReq(Screen):

    def checkCamera(self):
        icam = self.ids['"inputcam"'].text

        if (len(icam) != 0):
            global input_cam
            input_cam = int(icam)

        check_camera.camer(input_cam)


class Setup(Screen):
    def trainImages(self):
        Train_Image.TrainImages()
        toast("All Images Trained")


class addUser(Screen):

    input_id = 0
    input_name = StringProperty("1")
    input_sem = StringProperty("1")
    input_mno = StringProperty("1")

    def submitInfo(self, Widget):

        in_id = self.ids['"inputid"'].text
        name = self.ids['"inputname"'].text
        sem = self.ids['"inputsem"'].text
        mno = self.ids['"inputmno"'].text

        self.input_id = in_id
        self.input_name = name
        self.input_sem = sem
        self.input_mno = mno

        Capture_Image.takeImages(
            self.input_id, self.input_name, self.input_sem, self.input_mno, input_cam)


class Auttendo(Screen):

    def recognize(self):
        Recognize.recognize_attendance(input_cam)
        toast("Atttendance Successful")


class Attendance(Screen):
    r_mail = "test Ttext"

    def checkAttendance(self):
        Recognize.check_attendance()


class Automail(Screen):
    rmail = StringProperty("None")

    def r_mail(self):
        mail = self.ids['"rmail"'].text
        self.rmail = mail
        automail.automail(self.rmail)
        toast("Attendance Mailed Successfully")


AuttendoApp().run()
