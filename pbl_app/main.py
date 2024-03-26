from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition, CardTransition
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from check import check_and_install_modules as cim

class MainPage(Screen):
    def __init__(self,**kwargs):
        super(MainPage, self).__init__(**kwargs)
        out = BoxLayout(orientation = "vertical")
        top1 = BoxLayout(size_hint = (1.0, 0.1))
        top2 = BoxLayout(size_hint = (1.0, 0.1))
        top3 = BoxLayout(size_hint = (1.0, 0.1))

        tools_btn = Button(text = "Tools", on_press = self.tools, size_hint = (0.3, 1.0))
        blank = Label(text = "____", size_hint = (0.3, 1.0))
        logo_label = Label(text = "#place for logo")
        top1.add_widget(tools_btn)
        top1.add_widget(blank)
        top1.add_widget(logo_label)

        hostel_btn = ToggleButton(text = "Hostel", on_press = self.hostel_func)
        flat_btn = ToggleButton(text = "Flat", on_press = self.flat_func)
        roommate_btn = ToggleButton(text = "Room Mate", on_press = self.roommate_func)
        top2.add_widget(hostel_btn)
        top2.add_widget(flat_btn)
        top2.add_widget(roommate_btn)

        textinput = TextInput(hint_text = "search")
        search_btn = Button(text = "search", on_press = self.search, size_hint = (0.1, 1.0))
        top3.add_widget(textinput)
        top3.add_widget(search_btn)

        scroll = ScrollView(do_scroll_y = True, bar_width = 30, bar_color = (1,1,1,1))
        grid = GridLayout(cols = 1, size_hint_y = None)
        grid.bind(minimum_height = grid.setter('height'))
        for i in range(50):
            btn = Button(text = f"Button {i+1}",size_hint_y = None, height = 150)
            grid.add_widget(btn)
        scroll.add_widget(grid)

        out.add_widget(top1)
        out.add_widget(top2)
        out.add_widget(top3)
        out.add_widget(scroll)
        self.add_widget(out)

    def hostel_func(self, instance):
        pass
    def flat_func(self, instance):
        pass
    def roommate_func(self, instance):
        pass

    def search(self, instance):
        pass

    def tools(self,instance):
        self.manager.transition = CardTransition(direction = "right", mode = "push")
        self.manager.current = "toolpage"

class Start1Page(Screen):
    def __init__(self,**kwargs):
        super(Start1Page,self).__init__(**kwargs)
        pg1 = BoxLayout(orientation = "vertical")
        top1_label = Label(text = "Welcome to", size_hint = (1.0, 0.3), font_size = 50 ,color=(1, 1, 1, 1))
        logo1_label = Label(text = "#1Place holder for project logo",size_hint = (1.0, 0.3))
        text1_label = Label(text = "Before we begin, lets see \nall the features you \ncould get your hands on",size_hint = (1.0, 0.3), font_size = 30)
 
        pg1_1 = BoxLayout(size_hint = (1.0, 0.15))
        btn1_skip = Button(text = "Skip", size_hint = (0.3, 1.0), on_press = self.skip)
        btn1_next = Button(text = "Next", size_hint = (0.3, 1.0), on_press = self.next)
        pg1_1.add_widget(btn1_skip)
        pg1_1.add_widget(btn1_next)

        pg1.add_widget(top1_label)
        pg1.add_widget(logo1_label)
        pg1.add_widget(text1_label)
        pg1.add_widget(pg1_1)

        self.add_widget(pg1)

    def skip(self, instance):
        self.manager.transition = SlideTransition(direction = "up")
        self.manager.current = "mainpage"
    
    def next(self, instance):
        self.manager.transition = SlideTransition()
        self.manager.current = "start2page"

class Start2Page(Screen):
    def __init__(self,**kwargs):
        super(Start2Page,self).__init__(**kwargs)
        pg2 = BoxLayout(orientation = "vertical")
        logo2_label = Label(text = "#2Placeholder for project logo", size_hint = (1.0, 0.3),font_size = 30)
        my_text1 = "In CRoom, you can: \n-Find 1k+ hostels and flats\nin you area \n-Search for hostel/flat in\n20+ areas \n-Save your favourite room\nfor later \n-be a landlord \n-And more..."
        text2_label = Label(text = my_text1, font_size = 30)

        pg2_1 = BoxLayout(size_hint = (1.0, 0.2))
        btn2_skip = Button(text = "Skip", size_hint = (0.3, 1.0), on_press = self.skip)
        btn2_pre = Button(text = "Previous", size_hint = (0.3, 1.0), on_press = self.pre)
        btn2_next = Button(text = "Next", size_hint = (0.3, 1.0), on_press = self.next)
        
        pg2_1.add_widget(btn2_skip)
        pg2_1.add_widget(btn2_pre)
        pg2_1.add_widget(btn2_next)

        pg2.add_widget(logo2_label)
        pg2.add_widget(text2_label)
        pg2.add_widget(pg2_1)
        self.add_widget(pg2)

    def skip(self, instance):
        self.manager.transition = SlideTransition(direction = "up")
        self.manager.current = "mainpage"

    def pre(self, instance):
        self.manager.transition = SlideTransition(direction = "right")
        self.manager.current = "start1page"
    
    def next(self, instance):
        self.manager.transition = SlideTransition()
        self.manager.current = "start3page"

class Start3Page(Screen):
    def __init__(self,**kwargs):
        super(Start3Page,self).__init__(**kwargs)
        pg3 = BoxLayout(orientation = "vertical")
        logo3_label = Label(text = "#3Placeholder for project logo", size_hint = (1.0, 0.2), font_size = 30)
        my_text2 = "We also provide:\n  Zer0 paper work,\n  Zer0 brokerage,\n  Zer0 Installment,\n  Reasonable price for\ncall and subscription!"
        text3_label = Label(text = my_text2, font_size = 30)

        pg3_1 = BoxLayout(size_hint = (1.0, 0.2))
        btn3_skip = Button(text = "Skip", size_hint = (0.3, 1.0), on_press = self.skip)
        btn3_pre = Button(text = "Previous", size_hint = (0.3, 1.0), on_press = self.pre)
        btn3_next = Button(text = "Next", size_hint = (0.3, 1.0), on_press = self.next)
        pg3_1.add_widget(btn3_skip)
        pg3_1.add_widget(btn3_pre)
        pg3_1.add_widget(btn3_next)


        pg3.add_widget(logo3_label)
        pg3.add_widget(text3_label)
        pg3.add_widget(pg3_1)
        self.add_widget(pg3)

    def skip(self, instance):
        self.manager.transition = SlideTransition(direction = "up")
        self.manager.current = "mainpage"
    
    def pre(self, instance):
        self.manager.transition = SlideTransition(direction = "right")
        self.manager.current = "start2page"
    
    def next(self, instance):
        self.manager.transition = SlideTransition()
        self.manager.current = "start4page"

class Start4Page(Screen):
    def __init__(self,**kwargs):
        super(Start4Page,self).__init__(**kwargs)
        pg4 = BoxLayout(orientation = "vertical")
        logo4_label = Label(text = "#4Placeholder for project logo", size_hint = (1.0, 0.3), font_size = 30)
        text4_label = Label(text = "So what are you \nwaiting for?", size_hint = (1.0,0.3), font_size = 30)
        text4_1_label = Label(text = "Put on your shoes\nand lets get\nstarted", size_hint = (1.0,0.3), font_size = 30)
        text4_2_label = Label(text = "#Placeholder for image", size_hint = (1.0, 0.3), font_size = 30)

        pg4_1 = BoxLayout(size_hint = (1.0, 0.2))
        btn4_start = Button(text = "Start", size_hint = (0.3, 1.0), on_press = self.start)
        btn4_pre = Button(text = "Previous", size_hint = (0.3, 1.0), on_press = self.pre)
        pg4_1.add_widget(btn4_pre)
        pg4_1.add_widget(btn4_start)
        

        pg4.add_widget(logo4_label)
        pg4.add_widget(text4_label)
        pg4.add_widget(text4_1_label)
        pg4.add_widget(text4_2_label)
        pg4.add_widget(pg4_1)
        self.add_widget(pg4)

    def start(self, instance):
        self.manager.transition = SlideTransition(direction = "up")
        self.manager.current = "mainpage"
    
    def pre(self, instance):
        self.manager.transition = SlideTransition(direction = "right")
        self.manager.current = "start3page"

    
class ToolPage(Screen):
    def __init__(self,**kwargs):
        super(ToolPage,self).__init__(**kwargs)
        button = Button(text = "Welcome to tools page\nOops, you are a bit early!\nWork under progress", on_press = self.start)
        self.add_widget(button)

    def start(self, instance):
        self.manager.transition = CardTransition(direction = "left", mode = "pop")
        self.manager.current = "mainpage"

    def next(self,instance):
        pass

class MessagePage(Screen):
    def __init__(self,**kwargs):
        super(MessagePage,self).__init__(**kwargs)
        #add layouts
    def next(self,instance):
        pass

class ProfilePage(Screen):
    def __init__(self,**kwargs):
        super(ProfilePage,self).__init__(**kwargs)
        #add layouts
    def next(self,instance):
        pass

class EditProfPage(Screen):
    def __init__(self,**kwargs):
        super(EditProfPage,self).__init__(**kwargs)
        #add layouts
    def next(self,instance):
        pass

class MyApp(App):
    def build(self):
        screen_manager = ScreenManager()
        
        screen_manager.add_widget(Start1Page(name = "start1page"))
        screen_manager.add_widget(Start2Page(name = "start2page"))
        screen_manager.add_widget(Start3Page(name = "start3page"))
        screen_manager.add_widget(Start4Page(name = "start4page"))
        screen_manager.add_widget(MainPage(name = "mainpage"))
        screen_manager.add_widget(ToolPage(name = "toolpage"))
        screen_manager.add_widget(MessagePage(name = "messagepage"))
        screen_manager.add_widget(ProfilePage(name = "profilepage"))
        screen_manager.add_widget(EditProfPage(name = "editprofpage"))
        

        return screen_manager
    
if __name__ == "__main__":
    cim()
    MyApp().run()