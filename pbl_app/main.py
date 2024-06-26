from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen, CardTransition, FadeTransition
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Line
from check import check_and_install_modules as cim
from pages import *

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

        self.hostel_btn = ToggleButton(text = "Hostel", on_press = self.hostel_func, state = "down")
        self.flat_btn = ToggleButton(text = "Flat", on_press = self.flat_func)
        self.roommate_btn = ToggleButton(text = "Room Mate", on_press = self.roommate_func)
        top2.add_widget(self.hostel_btn)
        top2.add_widget(self.flat_btn)
        top2.add_widget(self.roommate_btn)

        self.textinput = TextInput(hint_text = "search", multiline = False)
        search_btn = Button(text = "search", on_press = self.search, size_hint = (0.1, 1.0))
        top3.add_widget(self.textinput)
        top3.add_widget(search_btn)

        self.scroll = ScrollView(do_scroll_y = True, bar_width = 30, bar_color = (1,1,1,1))
        self.grid = GridLayout(cols = 1, size_hint_y = None)
        self.grid.bind(minimum_height = self.grid.setter('height'))
        self.buttons = []
        for i in range(10):
            btn = Button(text = f"Hostel{i+1} in {self.textinput.text}",size_hint_y = None, height = 150, on_press = self.goto)
            self.grid.add_widget(btn)
            self.buttons.append(btn)
        self.scroll.add_widget(self.grid)
        

        out.add_widget(top1)
        out.add_widget(top2)
        out.add_widget(top3)
        out.add_widget(self.scroll)
        self.add_widget(out)

    def hostel_func(self, instance):
        self.flat_btn.state = "normal"
        self.roommate_btn.state = "normal"
        self.grid.clear_widgets()
        self.scroll.clear_widgets()
        self.buttons = []
        for i in range(10):
            btn = Button(text = f"Hostel{i+1} in {self.textinput.text}",size_hint_y = None, height = 150, on_press = self.goto)
            self.grid.add_widget(btn)
            self.buttons.append(btn)
        self.scroll.add_widget(self.grid)

    def flat_func(self, instance):
        self.hostel_btn.state = "normal"
        self.roommate_btn.state = "normal"
        self.grid.clear_widgets()
        self.scroll.clear_widgets()
        self.buttons = []
        for i in range(10):
            btn = Button(text = f"Flat{i+1} in {self.textinput.text}",size_hint_y = None, height = 150, on_press = self.goto)
            self.grid.add_widget(btn)
            self.buttons.append(btn)
        self.scroll.add_widget(self.grid)

    def roommate_func(self, instance):
        self.flat_btn.state = "normal"
        self.hostel_btn.state = "normal"
        self.grid.clear_widgets()
        self.scroll.clear_widgets()
        self.buttons = []
        for i in range(10):
            btn = Button(text = f"Roommate{i+1} in {self.textinput.text}",size_hint_y = None, height = 150, on_press = self.goto)
            self.grid.add_widget(btn)
            self.buttons.append(btn)
        self.scroll.add_widget(self.grid)

    def search(self, instance):
        area = self.textinput.text
        for button in self.buttons:
            button.text = f"{button.text.split()[0]} in {area}"
    
    def goto(self, instance):
        self.manager.transition = FadeTransition()
        self.manager.current = "blank"       

    def tools(self,instance):
        self.manager.transition = CardTransition(direction = "right", mode = "push")
        self.manager.current = "toolpage"

class ToolPage(Screen):
    def __init__(self,**kwargs):
        super(ToolPage,self).__init__(**kwargs)
        layout = BoxLayout(orientation = 'vertical')
        top_box = BoxLayout(orientation = 'horizontal', size_hint = (1.0, 0.2))
        back_btn = Button(text = "Back", on_press = self.back, size_hint = (0.2, 1.0))
        logo_image = Image(source = 'user_logo.png', size_hint = (0.3, 1.0))
        user_name = Label(text="user_name")
        mess_btn = Button(text = "message", on_press = self.mess, size_hint = (0.2, 1.0))
        top_box.add_widget(back_btn)
        top_box.add_widget(logo_image)
        top_box.add_widget(user_name)
        top_box.add_widget(mess_btn)

        btn_box = BoxLayout(orientation = "vertical")
        prof_btn = Button(text = "Profile", on_press = self.prof)
        saved_btn = Button(text = "Saved", on_press = self.save)
        sub_stn = Button(text = "Subscription", on_press = self.sub)
        term_btn = Button(text = "Terms & Policies", on_press = self.term)
        land_btn = Button(text = "Be a Landlord", on_press = self.land)
        btn_box.add_widget(prof_btn)
        btn_box.add_widget(saved_btn)
        btn_box.add_widget(sub_stn)
        btn_box.add_widget(term_btn)
        btn_box.add_widget(land_btn)

        sepa = BoxLayout(size_hint = (1.0, 0.2))
        line = Color(0,0,0,1)
        sepa.canvas.add(Line(points = (0,0, layout.width, 1), color = line))

        bot = BoxLayout(size_hint = (1.0, 0.2))
        faq_btn = Button(text = "FAQs", on_press = self.faq)
        set_btn = Button(text = "Settings", on_press = self.setf)
        call_btn = Button(text = "Call centre", on_press = self.callf)
        bot.add_widget(faq_btn)
        bot.add_widget(set_btn)
        bot.add_widget(call_btn)


        layout.add_widget(top_box)
        layout.add_widget(btn_box)
        layout.add_widget(sepa)
        layout.add_widget(bot)

        self.add_widget(layout)


    def back(self, instance):
        self.manager.transition = CardTransition(direction = "left", mode = "pop")
        self.manager.current = "mainpage"

    def mess(self,instance):
        self.manager.transition = FadeTransition()
        self.manager.current = "messagepage"
    
    def prof(self,instance):
        self.manager.transition = FadeTransition()
        self.manager.current = "profilepage"
    def save(self, instance):
        self.manager.transition = FadeTransition()
        self.manager.current = "savedpage"
    def sub(self, instance):
        self.manager.transition = FadeTransition()
        self.manager.current = "blank"
    def term(self, instance):
        self.manager.transition = FadeTransition()
        self.manager.current = "blank"
    def land(self, instance):
        self.manager.transition = FadeTransition()
        self.manager.current = "blank"
    def faq(self, instance):
        self.manager.transition = FadeTransition()
        self.manager.current = "blank"
    def setf(self, instance):
        self.manager.transition = FadeTransition()
        self.manager.current = "blank"
    def callf(self, instance):
        self.manager.transition = FadeTransition()
        self.manager.current = "blank"

class MessagePage(Screen):
    def __init__(self,**kwargs):
        super(MessagePage,self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        top_box = BoxLayout(orientation='horizontal', size_hint_y=0.15)
        back_button = Button(text='Back',size_hint_x = 0.2,  on_press=self.back)
        self.textinput = TextInput(hint_text='Search Messages')
        search_button = Button(text='Search',size_hint_x = 0.2, on_press=self.search)
        top_box.add_widget(back_button)
        top_box.add_widget(self.textinput)
        top_box.add_widget(search_button)

        toggle_box = BoxLayout(orientation='horizontal', size_hint_y=0.25)
        self.focused_button = ToggleButton(text='Focused', on_press=self.focus, state = "down")
        self.other_button = ToggleButton(text='Other', on_press=self.other)
        toggle_box.add_widget(self.focused_button)
        toggle_box.add_widget(self.other_button)

        self.scroll = ScrollView(do_scroll_y = True, bar_width = 30, bar_color = (1,1,1,1))
        self.grid = GridLayout(cols = 1, size_hint_y = None)
        self.grid.bind(minimum_height = self.grid.setter('height'))
        for i in range(10):
            btn = Button(text = f"Focused message{i+1}",size_hint_y = None, height = 150, on_press = self.goto)
            self.grid.add_widget(btn)
        self.scroll.add_widget(self.grid)

        write = Button(text = "Write message", size_hint_y = 0.2, on_press = self.goto)

        layout.add_widget(top_box)
        layout.add_widget(toggle_box)
        layout.add_widget(self.scroll)
        layout.add_widget(write)

        self.add_widget(layout)

    def back(self, instance):
        self.manager.transition = FadeTransition()
        self.manager.current = "toolpage"
    def search(self, instance):
        area = self.textinput.text
        if area:
            self.grid.clear_widgets()
            self.scroll.clear_widgets()
            btn = Button(text = f"{area}",size_hint_y = None, height = 150, on_press = self.goto)
            self.grid.add_widget(btn)
            self.scroll.add_widget(self.grid)

    def goto(self, instance):
        self.manager.transition = FadeTransition()
        self.manager.current = "blank"


    def focus(self, instance):
        self.other_button.state = "normal"
        self.grid.clear_widgets()
        self.scroll.clear_widgets()
        for i in range(10):
            btn = Button(text = f"Focused message{i+1}",size_hint_y = None, height = 150, on_press = self.goto)
            self.grid.add_widget(btn)
        self.scroll.add_widget(self.grid)
    def other(self, instance):
        self.focused_button.state = "normal"
        self.grid.clear_widgets()
        self.scroll.clear_widgets()
        for i in range(10):
            btn = Button(text = f"Other message{i+1}",size_hint_y = None, height = 150, on_press = self.goto)
            self.grid.add_widget(btn)
        self.scroll.add_widget(self.grid)

class ProfilePage(Screen):
    def __init__(self,**kwargs):
        super(ProfilePage,self).__init__(**kwargs)
        grid = BoxLayout(orientation = "vertical")
        grid.bind(minimum_height = grid.setter('height'))

        top = BoxLayout(size_hint_y = 0.15)
        back_btn = Button(text = "Back", size_hint_x = 0.2, on_press = self.back)
        label = Label(text = "Profile      ")
        account_btn = Button(text = "Account", size_hint_x = 0.3, on_press = self.account)
        top.add_widget(back_btn)
        top.add_widget(label)
        top.add_widget(account_btn)
        grid.add_widget(top)

        top2 = BoxLayout(size_hint_y = 0.15)
        logo = Image(source='logo.png', size_hint=(0.3, 1.0))
        right_layout = BoxLayout(orientation='vertical')
        username_label = Label(text='Username')
        area_layout = BoxLayout(size_hint_y = 0.25)
        area_label = Label(text='Area', size_hint=(0.7, 1.0))
        edit_profile_button = Button(text='Edit Profile', size_hint=(0.3, 1.0), on_press = self.edit_prof)
        area_layout.add_widget(area_label)
        area_layout.add_widget(edit_profile_button)
        right_layout.add_widget(username_label)
        right_layout.add_widget(area_layout)
        top2.add_widget(logo)
        top2.add_widget(right_layout)
        grid.add_widget(top2)
        
        sepa1 = BoxLayout(size_hint_y = 0.05)
        line = Color(1,0,0,1)
        sepa1.canvas.add(Line(points = (0,0, grid.width, 1), color = line))
        grid.add_widget(sepa1)

        top3 = BoxLayout(orientation = "vertical", size_hint_y = 0.2)
        base = Label(text = "Basic Details:", size_hint_y = 0.3)
        grid1 = GridLayout(cols = 2, y = 150)
        gender = Label(text = "gender : male", font_size = 30)
        age = Label(text = "age : 20", font_size = 30)
        study = Label(text = "Years of study : FE", font_size = 30)
        branch = Label(text = "Branch : CS", font_size = 30)
        grid1.add_widget(gender)
        grid1.add_widget(age)
        grid1.add_widget(study)
        grid1.add_widget(branch)
        top3.add_widget(base)
        top3.add_widget(grid1)
        grid.add_widget(top3)

        sepa2 = BoxLayout(size_hint_y = 0.05)
        line = Color(1,0,0,1)
        sepa2.canvas.add(Line(points = (0,0, grid.width, 1), color = line))
        grid.add_widget(sepa2)

        bot = BoxLayout(orientation = "vertical")
        bot_top = BoxLayout(size_hint_y = 0.2)
        pre_label = Label(text = "Preference:")
        edit_pre_btn = Button(text = "edit", size_hint_x = 0.2, on_press = self.edit_pre)
        bot_top.add_widget(pre_label)
        bot_top.add_widget(edit_pre_btn)
        bot.add_widget(bot_top)
        bot_grid = GridLayout(cols = 4)
        for i in range(14):
            pre_box = BoxLayout(orientation = "vertical")
            pre_logo = Image(source=f'pre{i+1}.png')
            pre_pre_label = Label(text = f"{i+1}")
            pre_box.add_widget(pre_logo)
            pre_box.add_widget(pre_pre_label)
            bot_grid.add_widget(pre_box)
        bot.add_widget(bot_grid)
        grid.add_widget(bot)

        self.add_widget(grid)


    def back(self,instance):
        self.manager.transition = FadeTransition()
        self.manager.current = "toolpage"
    def account(self, instance):
        self.manager.transition = CardTransition(direction = "left", mode = "push")
        self.manager.current = "loginpage"
    def edit_prof(self, instance):
        self.manager.transition = CardTransition(direction = "left", mode = "push")
        self.manager.current = "editprofpage"
    def edit_pre(self, instance):
        self.manager.transition = CardTransition(direction = "left", mode = "push")
        self.manager.current = "blank"

class EditProfPage(Screen):
    def __init__(self,**kwargs):
        super(EditProfPage, self).__init__(**kwargs)
        layout = BoxLayout(orientation = "vertical")
        top = BoxLayout(size_hint_y = 0.2)
        back_btn = Button(text = "Back", size_hint_x = 0.2, on_press = self.back)
        label= Label(text = "Edit Profile")
        top.add_widget(back_btn)
        top.add_widget(label)
        layout.add_widget(top)

        img_lay = BoxLayout(size_hint_y = 0.3)
        img = Image(source = 'user.png', size = (100,100), size_hint = (None,None))
        img_btn = Button(text = "change", size_hint = (None, None), size = (50,50), on_press = self.change_img)
        img_lay.add_widget(img)
        img_lay.add_widget(img_btn)
        layout.add_widget(img_lay)

        grid = GridLayout(cols = 2)
        name_label = Label(text = "Name:", size_hint_x = 0.25)
        name_text = TextInput(hint_text = "enter your name")
        place_label = Label(text = "Place:", size_hint_x = 0.25)
        place_text = TextInput(hint_text = "enter your place")
        ph_label = Label(text = "Phone no:", size_hint_x = 0.25)
        ph_text = TextInput(hint_text = "enter your phone number")
        email_label = Label(text = "Email:", size_hint_x = 0.25)
        email_text = TextInput(hint_text = "enter your email address")
        gender_label = Label(text = "Gender:", size_hint_x = 0.25)
        gender_text = TextInput(hint_text = "enter your gender")
        age_label = Label(text = "Age:", size_hint_x = 0.25)
        age_text = TextInput(hint_text = "enter your age")
        study_label = Label(text = "Year of study:", size_hint_x = 0.25)
        study_text = TextInput(hint_text = "enter your tear of study")
        branch_label = Label(text = "Branch:", size_hint_x = 0.25)
        branch_text = TextInput(hint_text = "enter your Branch")
        grid.add_widget(name_label)
        grid.add_widget(name_text)
        grid.add_widget(place_label)
        grid.add_widget(place_text)
        grid.add_widget(ph_label)
        grid.add_widget(ph_text)
        grid.add_widget(email_label)
        grid.add_widget(email_text)
        grid.add_widget(gender_label)
        grid.add_widget(gender_text)
        grid.add_widget(age_label)
        grid.add_widget(age_text)
        grid.add_widget(study_label)
        grid.add_widget(study_text)
        grid.add_widget(branch_label)
        grid.add_widget(branch_text)
        layout.add_widget(grid)

        save_btn = Button(text = "save", on_press = self.save, size_hint_y = 0.2)
        layout.add_widget(save_btn)
        self.add_widget(layout)

    def back(self,instance):
        self.manager.transition = CardTransition(direction = "right", mode = "pop")
        self.manager.current = "profilepage"
    def save(self, instance):
        pass
    def change_img(self, instance):
        pass

class LoginPage(Screen):
    def __init__(self,**kwargs):
        super(LoginPage,self).__init__(**kwargs)
        layout = BoxLayout(orientation = "vertical")

        top = BoxLayout(size_hint_y = 0.15)
        back_btn = Button(text = "back", size_hint_x = 0.2, on_press = self.back)
        logo = Image(source = "logo.png")
        top.add_widget(back_btn)
        top.add_widget(logo)
        layout.add_widget(top)

        mid = BoxLayout(orientation = "vertical")
        email_box = BoxLayout()
        email_label = Label(text = "Email", halign = "left", size_hint_x = 0.3)
        email_text = TextInput(hint_text = "Enter email")
        email_box.add_widget(email_label)
        email_box.add_widget(email_text)
        pass_box = BoxLayout()
        pass_label = Label(text = "Password", halign = "left", size_hint_x = 0.3)
        pass_text = TextInput(hint_text = "Enter password", password = True)
        pass_box.add_widget(pass_label)
        pass_box.add_widget(pass_text)
        forgot_btn = Button(text = "Forgot Password?", on_press = self.forgot, size_hint_y = 0.4)
        sepa1 = BoxLayout(size_hint_y = 0.2)
        line = Color(1,0,0,1)
        sepa1.canvas.add(Line(points = (0,0, mid.width, 1), color = line))
        mid.add_widget(sepa1)
        acc_box = BoxLayout(size_hint_y = 0.4)
        log_in = Button(text = "Log In", on_press = self.log)
        sign_in = Button(text = "Sign In", on_press = self.sign)
        acc_box.add_widget(log_in)
        acc_box.add_widget(sign_in)
        mid.add_widget(email_box)
        mid.add_widget(pass_box)
        mid.add_widget(forgot_btn)
        mid.add_widget(acc_box)
        layout.add_widget(mid)

        sepa2 = BoxLayout(size_hint_y = 0.35)
        line = Color(1,0,0,1)
        sepa2.canvas.add(Line(points = (0,0, layout.width, 1), color = line))
        layout.add_widget(sepa2)

        self.add_widget(layout)

    def back(self,instance):
        self.manager.transition = CardTransition(direction = "right", mode = "pop")
        self.manager.current = "profilepage"
    def forgot(self, instance):
        pass
    def log(self, instance):
        pass
    def sign(self, instance):
        pass

class SavedPage(Screen):
    def __init__(self, **kwargs):
        super(SavedPage, self).__init__(**kwargs)
        out = BoxLayout(orientation = "vertical")
        top1 = BoxLayout(size_hint = (1.0, 0.1))
        top2 = BoxLayout(size_hint = (1.0, 0.1))
        top3 = BoxLayout(size_hint = (1.0, 0.1))

        back_btn = Button(text = "Back", on_press = self.back, size_hint = (0.3, 1.0))
        blank = Label(text = "____", size_hint = (0.3, 1.0))
        logo_label = Label(text = "Saved profiles")
        top1.add_widget(back_btn)
        top1.add_widget(logo_label)
        top1.add_widget(blank)

        self.hostel_btn = ToggleButton(text = "Hostel", on_press = self.hostel_func, state = "down")
        self.flat_btn = ToggleButton(text = "Flat", on_press = self.flat_func)
        self.roommate_btn = ToggleButton(text = "Room Mate", on_press = self.roommate_func)
        top2.add_widget(self.hostel_btn)
        top2.add_widget(self.flat_btn)
        top2.add_widget(self.roommate_btn)

        self.textinput = TextInput(hint_text = "search", multiline = False)
        search_btn = Button(text = "search", on_press = self.search, size_hint = (0.1, 1.0))
        top3.add_widget(self.textinput)
        top3.add_widget(search_btn)

        self.scroll = ScrollView(do_scroll_y = True, bar_width = 30, bar_color = (1,1,1,1))
        self.grid = GridLayout(cols = 1, size_hint_y = None)
        self.grid.bind(minimum_height = self.grid.setter('height'))
        self.buttons = []
        for i in range(10):
            btn = Button(text = f"Hostel{i+1} in {self.textinput.text}",size_hint_y = None, height = 150, on_press = self.goto)
            self.grid.add_widget(btn)
            self.buttons.append(btn)
        self.scroll.add_widget(self.grid)
        

        out.add_widget(top1)
        out.add_widget(top2)
        out.add_widget(top3)
        out.add_widget(self.scroll)
        self.add_widget(out)

    def hostel_func(self, instance):
        self.flat_btn.state = "normal"
        self.roommate_btn.state = "normal"
        self.grid.clear_widgets()
        self.scroll.clear_widgets()
        self.buttons = []
        for i in range(10):
            btn = Button(text = f"Hostel{i+1} in {self.textinput.text}",size_hint_y = None, height = 150, on_press = self.goto)
            self.grid.add_widget(btn)
            self.buttons.append(btn)
        self.scroll.add_widget(self.grid)

    def flat_func(self, instance):
        self.hostel_btn.state = "normal"
        self.roommate_btn.state = "normal"
        self.grid.clear_widgets()
        self.scroll.clear_widgets()
        self.buttons = []
        for i in range(10):
            btn = Button(text = f"Flat{i+1} in {self.textinput.text}",size_hint_y = None, height = 150, on_press = self.goto)
            self.grid.add_widget(btn)
            self.buttons.append(btn)
        self.scroll.add_widget(self.grid)

    def roommate_func(self, instance):
        self.flat_btn.state = "normal"
        self.hostel_btn.state = "normal"
        self.grid.clear_widgets()
        self.scroll.clear_widgets()
        self.buttons = []
        for i in range(10):
            btn = Button(text = f"Roommate{i+1} in {self.textinput.text}",size_hint_y = None, height = 150, on_press = self.goto)
            self.grid.add_widget(btn)
            self.buttons.append(btn)
        self.scroll.add_widget(self.grid)

    def search(self, instance):
        area = self.textinput.text
        for button in self.buttons:
            button.text = f"{button.text.split()[0]} in {area}"
    
    def goto(self, instance):
        self.manager.transition = FadeTransition()
        self.manager.current = "blank"       

    def back(self,instance):
        self.manager.transition = FadeTransition()
        self.manager.current = "toolpage"

class Blank(Screen):
    def __init__(self,**kwargs):
        super(Blank,self).__init__(**kwargs)
        button = Button(text = "Nothing to see here for now", on_press = self.next)
        self.add_widget(button)
    def next(self,instance):
        self.manager.transition = FadeTransition()
        self.manager.current = "mainpage"

class ProjectApp(App):
    def build(self):
        screen_manager = ScreenManager()

        screen_manager.add_widget(Start1Page(name='start1page'))
        screen_manager.add_widget(Start2Page(name='start2page'))
        screen_manager.add_widget(Start3Page(name='start3page'))
        screen_manager.add_widget(Start4Page(name='start4page'))
        screen_manager.add_widget(MainPage(name = "mainpage"))
        screen_manager.add_widget(Blank(name = "blank"))
        screen_manager.add_widget(ToolPage(name = "toolpage"))
        screen_manager.add_widget(MessagePage(name = "messagepage"))
        screen_manager.add_widget(ProfilePage(name = "profilepage"))
        screen_manager.add_widget(LoginPage(name = "loginpage")) 
        screen_manager.add_widget(EditProfPage(name = "editprofpage"))
        screen_manager.add_widget(SavedPage(name = "savedpage"))
        

        return screen_manager
    
if __name__ == "__main__":
    cim()
    ProjectApp().run()