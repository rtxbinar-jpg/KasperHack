import os
import json
from collections import Counter

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.metrics import dp
from kivy.core.window import Window

BG=(0.04,0.04,0.04,1); SURFACE=(0.09,0.09,0.09,1); BUTTON=(0.13,0.13,0.13,1)
PURPLE=(0.42,0.39,1,1); WHITE=(1,1,1,1); GRAY=(0.65,0.65,0.65,1); GREEN=(0.25,0.85,0.45,1)

class HomeScreen(Screen):
    def on_pre_enter(self):
        if not self.children: self.build_ui()
    def build_ui(self):
        root=BoxLayout(orientation='vertical',padding=dp(20),spacing=dp(15))
        root.add_widget(Label(text='KASPER HACK',font_size=dp(32),bold=True,color=PURPLE))
        root.add_widget(Label(text='CYBER ANALYSIS SYSTEM',font_size=dp(14),color=GRAY))
        b=Button(text='APPLE\nANALYSIS',font_size=dp(22),bold=True,background_normal='',background_color=BUTTON)
        b.bind(on_release=lambda x:setattr(self.manager,'current','apple')); root.add_widget(b)
        s=Button(text='SETTINGS',font_size=dp(18),background_normal='',background_color=BUTTON)
        s.bind(on_release=lambda x:setattr(self.manager,'current','settings')); root.add_widget(s)
        self.add_widget(root)

class AppleScreen(Screen):
    def build_ui(self):
        root=BoxLayout(orientation='vertical',padding=dp(15),spacing=dp(10))
        top=BoxLayout(size_hint_y=None,height=dp(50),spacing=dp(8))
        back=Button(text='BACK',background_normal='',background_color=BUTTON); back.bind(on_release=lambda x:setattr(self.manager,'current','home'))
        top.add_widget(back); top.add_widget(Label(text='ONLINE',color=GREEN,font_size=dp(13)))
        st=Button(text='SETTINGS',background_normal='',background_color=BUTTON); st.bind(on_release=lambda x:setattr(self.manager,'current','settings')); top.add_widget(st)
        root.add_widget(top)
        root.add_widget(Label(text='KASPER HACK',font_size=dp(25),bold=True,color=PURPLE,size_hint_y=None,height=dp(55)))
        root.add_widget(Label(text='APPLE',font_size=dp(32),bold=True,color=WHITE,size_hint_y=None,height=dp(55)))
        self.number_label=Label(text='5',font_size=dp(65),bold=True,color=WHITE,size_hint_y=None,height=dp(90)); root.add_widget(self.number_label)
        root.add_widget(Label(text='Haqiqiy natijani tanlang',color=GRAY,font_size=dp(14),size_hint_y=None,height=dp(35)))
        rows=GridLayout(cols=5,spacing=dp(7),size_hint_y=None,height=dp(60))
        for i in range(1,6):
            b=Button(text=str(i),font_size=dp(20),background_normal='',background_color=BUTTON); b.row_number=i; b.bind(on_release=self.row_pressed); rows.add_widget(b)
        root.add_widget(rows)
        scan=Button(text='SCAN',font_size=dp(21),bold=True,background_normal='',background_color=PURPLE,size_hint_y=None,height=dp(60)); scan.bind(on_release=self.scan); root.add_widget(scan)
        self.status=Label(text='STATUS: READY',color=GRAY,font_size=dp(14)); root.add_widget(self.status)
        self.history_label=Label(text='HISTORY: —',color=GRAY,font_size=dp(13)); root.add_widget(self.history_label)
        self.signal_label=Label(text='SIGNAL: —',color=WHITE,font_size=dp(18),bold=True); root.add_widget(self.signal_label)
        restart=Button(text='RESTART',background_normal='',background_color=BUTTON,size_hint_y=None,height=dp(50)); restart.bind(on_release=self.restart); root.add_widget(restart)
        self.add_widget(root)
    def on_pre_enter(self):
        if not self.children: self.build_ui()
        self.update_history()
    def row_pressed(self,b):
        app=App.get_running_app(); app.history.append(b.row_number); self.number_label.text=str(b.row_number); self.status.text=f'SAVED: {b.row_number}-qator'; self.signal_label.text='SIGNAL: —'; self.update_history()
    def update_history(self):
        if hasattr(self,'history_label'):
            h=App.get_running_app().history; self.history_label.text='HISTORY: '+(' '.join(map(str,h[-20:])) if h else '—')
    def scan(self,b):
        h=App.get_running_app().history
        if not h: self.signal_label.text="SIGNAL: MA'LUMOT YO'Q"; self.status.text='Avval haqiqiy natijalarni kiriting'; return
        row,n=Counter(h).most_common(1)[0]; pct=n/len(h)*100
        self.signal_label.text=f'STATISTIK SIGNAL: {row}-QATOR'; self.status.text=f'Tarix: {len(h)} ta | Uchragan: {n} | {pct:.1f}%'
    def restart(self,b):
        App.get_running_app().history.clear(); self.number_label.text='5'; self.signal_label.text='SIGNAL: —'; self.status.text='STATUS: READY'; self.update_history()

class SettingsScreen(Screen):
    def build_ui(self):
        root=BoxLayout(orientation='vertical',padding=dp(20),spacing=dp(12))
        root.add_widget(Label(text='SETTINGS',font_size=dp(28),bold=True,color=PURPLE,size_hint_y=None,height=dp(60)))
        root.add_widget(Label(text='BETWINNER ID',color=WHITE,font_size=dp(15),size_hint_y=None,height=dp(35)))
        self.id_input=TextInput(hint_text='ID raqamingizni kiriting',multiline=False,font_size=dp(18),background_color=SURFACE,foreground_color=WHITE,cursor_color=PURPLE,size_hint_y=None,height=dp(55)); root.add_widget(self.id_input)
        save=Button(text='SAVE ID',font_size=dp(18),background_normal='',background_color=PURPLE,size_hint_y=None,height=dp(55)); save.bind(on_release=self.save_id); root.add_widget(save)
        self.message=Label(text='',color=GREEN,font_size=dp(14)); root.add_widget(self.message)
        for text in ('LANGUAGE','NOTIFICATIONS','SIGNAL SETTINGS'):
            root.add_widget(Button(text=text,background_normal='',background_color=BUTTON,size_hint_y=None,height=dp(50)))
        back=Button(text='BACK',background_normal='',background_color=BUTTON,size_hint_y=None,height=dp(55)); back.bind(on_release=lambda x:setattr(self.manager,'current','home')); root.add_widget(back)
        self.add_widget(root)
    def on_pre_enter(self):
        if not self.children: self.build_ui()
        self.load_id()
    def path(self): return os.path.join(App.get_running_app().user_data_dir,'settings.json')
    def save_id(self,b):
        try:
            with open(self.path(),'w',encoding='utf-8') as f: json.dump({'betwinner_id':self.id_input.text.strip()},f,ensure_ascii=False)
            self.message.text='ID saqlandi.'
        except Exception as e: self.message.text='Saqlashda xato: '+str(e)
    def load_id(self):
        try:
            with open(self.path(),'r',encoding='utf-8') as f: self.id_input.text=json.load(f).get('betwinner_id','')
        except Exception: self.id_input.text=''

class KasperHackApp(App):
    def build(self):
        Window.clearcolor=BG; self.history=[]
        sm=ScreenManager(); sm.add_widget(HomeScreen(name='home')); sm.add_widget(AppleScreen(name='apple')); sm.add_widget(SettingsScreen(name='settings'))
        return sm

if __name__=='__main__': KasperHackApp().run()
