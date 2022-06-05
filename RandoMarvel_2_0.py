import kivy
from kivy.app import App
from kivy.uix.widget import Widget

from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition


from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView
from kivy.effects.scroll import ScrollEffect

import random
import os


schemes_file = open(os.path.join(os.path.dirname(__file__),'lists/list_schemes.txt'), 'r', encoding="utf8")
schemes_clean = schemes_file.read().replace("\n\n>> ","").replace(">> ","")
schemes_list = schemes_clean.split("///")
schemes_dict_desc = {}
schemes_dict_keys = {}
schemes_names = []
schemes_keywords = []
for scheme in schemes_list:
    titleSCH,descSCH = scheme.split(":::\n")
    if "[-]" in titleSCH :
        nameSCH,keySCHM = titleSCH.split("[-]")
        schemes_dict_keys[nameSCH] = keySCHM.split(" , ")
    else:
        nameSCH = titleSCH
        schemes_dict_keys[nameSCH] = []
    schemes_names.append(nameSCH)
    schemes_dict_desc[nameSCH] = descSCH
    

masterminds_file = open(os.path.join(os.path.dirname(__file__),'lists/list_masterminds.txt'), 'r')
masterminds_list = masterminds_file.read().splitlines()
masterminds_dict = {}
masterminds_names = []
for line in masterminds_list:
    namesMM,keysMM = line.split(" : ")
    masterminds_names.append(namesMM)
    keysMM_list = keysMM.split(" , ")
    if keysMM_list[0] == "":
        keysMM_list = []
    masterminds_dict[namesMM] = keysMM_list

villains_file = open(os.path.join(os.path.dirname(__file__),'lists/list_villains.txt'), 'r')
villains_list = villains_file.read().splitlines()
villains_dict = {}
villains_names = []
for line in villains_list:
    namesVi,keysVi = line.split(" : ")
    villains_names.append(namesVi)
    keysVi_list = keysVi.split(" , ")
    if keysVi_list[0] == "":
        keysVi_list = []
    villains_dict[namesVi] = keysVi_list

henchmen_file = open(os.path.join(os.path.dirname(__file__),'lists/list_henchmen.txt'), 'r')
henchmen_list = henchmen_file.read().splitlines()
henchmen_dict = {}
henchmen_names = []
for line in henchmen_list:
    namesHeN,keysHeN = line.split(" : ")
    henchmen_names.append(namesHeN)
    keysHeN_list = keysHeN.split(" , ")
    if keysHeN_list[0] == "":
        keysHeN_list = []
    henchmen_dict[namesHeN] = keysHeN_list

heroes_file = open(os.path.join(os.path.dirname(__file__),'lists/list_heroes.txt'), 'r')
heroes_list = heroes_file.read().splitlines()
heroes_dict = {}
heroes_names = []
for line in heroes_list:
    namesHeR,keysHeR = line.split(" : ")
    heroes_names.append(namesHeR)
    keysHeR_list = keysHeR.split(" , ")
    if keysHeR_list[0] == "":
        keysHeR_list = []
    heroes_dict[namesHeR] = keysHeR_list

keywords_file = open(os.path.join(os.path.dirname(__file__),'lists/list_keywords.txt'), 'r', encoding="utf8")
keywords_clean = keywords_file.read().replace("\n\n>> ","").replace(">> ","")
keywords_list = keywords_clean.split("///")
keywords_dict = {}
keywords_names = set()
for keyword in keywords_list:
    nameKW,descKW = keyword.split(":::\n")
    keywords_dict[nameKW] = descKW
    keywords_names.add(nameKW)

vilnum = 1
hennum = 1
hernum = 1


class Main_Window(Screen):

           
    def Player1(self):
        global vilnum
        global hennum
        global hernum
        vilnum = 1
        hennum = 1
        hernum = 3

    def Player2(self):
        global vilnum
        global hennum
        global hernum
        vilnum = 1
        hennum = 1
        hernum = 5

    def Player3(self):
        global vilnum
        global hennum
        global hernum
        vilnum = 2
        hennum = 1
        hernum = 5

    def Player4(self):
        global vilnum
        global hennum
        global hernum
        vilnum = 2
        hennum = 2
        hernum = 5

    def Randomize(self, tipo):
        random_item = tipo[random.randint(0,len(tipo)-1)]
        return random_item

    def Randomize_lista(self, tipo, num):
        self.ChangeInstructions()
        lista = set()
        while len(lista) < num:
            lista.add(tipo[random.randint(0,len(tipo)-1)])
        listaprint = " / ".join(lista)
        if tipo == masterminds_names:
            third = random.randint(1,3)
            if third == 3:
                listaprint = "Epic {}".format(listaprint)
        return listaprint

    def Show_Schemes(self,num):
        self.ids.scheme_lab.text = "{}".format(self.Randomize_lista(schemes_names,num))
        while "|" in self.ids.scheme_lab.text:
            self.ids.scheme_lab.text = "{}".format(self.Randomize_lista(schemes_names,num))
        
    def Show_Mastermind(self, num):
        self.ids.mastermind_lab.text = "{}".format(self.Randomize_lista(masterminds_names,num))

    def Show_Villains(self, num):
        self.ids.villains_lab.text = "{}".format(self.Randomize_lista(villains_names,num))

    def Show_Henchmen(self, num):
        if hernum != 3:
            self.ids.henchmen_lab.text = "{}".format(self.Randomize_lista(henchmen_names,num))
            
        else:
            self.ids.henchmen_lab.text = "{} (only 3 cards)".format(self.Randomize_lista(henchmen_names,num))

    def Show_Heroes(self,num):
        self.ids.heroes_lab.text = "{}".format(self.Randomize_lista(heroes_names,num))
                    
    def Show_Bystanders(self,num):
        self.ids.bystanders_lab.text = "{}".format(num)
 

    def Show1Scheme(self):
        self.Show_Schemes(1)

    def Show1Mastermind(self):
        self.Show_Mastermind(1)

    def Show1Villain(self):
        self.Show_Villains(vilnum)

    def Show1Henchman(self):
        self.Show_Henchmen(hennum)

    def Show1Heroe(self):
        self.Show_Heroes(hernum)

    def Randomize_1P(self):
        self.Player1()
        self.Show_Schemes(1)
        self.Show_Mastermind(1)
        self.Show_Villains(vilnum)
        self.Show_Henchmen(hennum)
        self.Show_Heroes(hernum)
        self.Show_Bystanders(1)

    def Randomize_2P(self):
        self.Player2()
        self.Show_Schemes(1)
        self.Show_Mastermind(1)
        self.Show_Villains(vilnum)
        self.Show_Henchmen(hennum)
        self.Show_Heroes(hernum)
        self.Show_Bystanders(2)

    def Randomize_3P(self):
        self.Player3()
        self.Show_Schemes(1)
        self.Show_Mastermind(1)
        self.Show_Villains(vilnum)
        self.Show_Henchmen(hennum)
        self.Show_Heroes(hernum)
        self.Show_Bystanders(8)

    def Randomize_4P(self):
        self.Player4()
        self.Show_Schemes(1)
        self.Show_Mastermind(1)
        self.Show_Villains(vilnum)
        self.Show_Henchmen(hennum)
        self.Show_Heroes(hernum)
        self.Show_Bystanders(8)

            
    def Reset(self):
        global vilnum
        global hennum
        global hernum
        vilnum = 1
        hennum = 1
        hernum = 1        

        self.ids.instructions.text="Select Number of Players\nor Categories to be Randomized"
        self.ids.scheme_lab.text=''
        self.ids.mastermind_lab.text=''
        self.ids.villains_lab.text=''
        self.ids.henchmen_lab.text=''
        self.ids.heroes_lab.text=''
        self.ids.bystanders_lab.text=''

    def ChangeInstructions(self):
        self.ids.instructions.text="Press on the Results\nto see Descriptions or Keywords"

    def SwitchToKeywords(self):
        app = App.get_running_app()
        app.root.get_screen("main_window").manager.transition.direction = "left"
        app.root.get_screen("main_window").manager.current = "keywords_window"

               
    def ShowKeywords(self,carrier,dict,title):
                        
        if carrier == "":
            pass
        else:
            app = App.get_running_app()
                        
            app.root.get_screen("keywords_window").ids.accordion_container.clear_widgets()

            TempCarriers_text_clean = carrier.replace("Epic ","").replace(" (only 3 cards)","")

            if title == "Mastermind" or title in masterminds_names:
                app.root.get_screen("keywords_window").ids.keywords_title.text = "{}'s Keywords".format(title)
                app.root.get_screen("keywords_window").ids.keywords_title.background_color=(119/255.0, 50/255.0, 168/255.0,1)
                #app.root.get_screen("keywords_window").ids.emptylabel.background_color=(119/255.0, 50/255.0, 168/255.0,1)
            elif title == "Villains" or title in villains_names:
                app.root.get_screen("keywords_window").ids.keywords_title.text = "{}' Keywords".format(title)
                app.root.get_screen("keywords_window").ids.keywords_title.background_color=(1,0,0,1)
                #app.root.get_screen("keywords_window").ids.emptylabel.background_color=(1,0,0,1)
            elif title == "Henchmen" or title in henchmen_names:
                app.root.get_screen("keywords_window").ids.keywords_title.text = "{}'s Keywords".format(title)
                app.root.get_screen("keywords_window").ids.keywords_title.background_color=(235/255.0, 156/255.0, 38/255.0,1)
                #app.root.get_screen("keywords_window").ids.emptylabel.background_color=(235/255.0, 156/255.0, 38/255.0,1)
            else:
                app.root.get_screen("keywords_window").ids.keywords_title.text = "{}' Keywords".format(title)
                app.root.get_screen("keywords_window").ids.keywords_title.background_color=(48/255.0,99/255.0,194/255.0,1)
                #app.root.get_screen("keywords_window").ids.emptylabel.background_color=(48/255.0,99/255.0,194/255.0,1)

            TempCarriers = TempCarriers_text_clean.split(" / ")
            
            AllKeywords = []
            for Carrier in TempCarriers:
                AllKeywords.append(dict[Carrier])
            KeywordsList = [item for sublist in AllKeywords for item in sublist]
            TempKeywords_set = sorted(set(KeywordsList))

            if len(TempKeywords_set) == 0:
                if title == "Villains" or title == "Henchmen" or title == "Heroes":
                    empty = Label(text="These {} have no Keywords".format(title), valign = 'center', halign = 'center')
                else:
                    empty = Label(text="{} has no Keywords".format(TempCarriers_text_clean), valign = 'center', halign = 'center')
                app.root.get_screen("keywords_window").ids.accordion_container.add_widget(empty)

            else:

                KeysAccordion = Accordion(orientation = "vertical")
                app.root.get_screen("keywords_window").ids.accordion_container.add_widget(KeysAccordion)
                                        
                for kw in TempKeywords_set:
                    
                    item = AccordionItem(title="{}".format(kw))
                    KeysAccordion.add_widget(item)

                    if kw == TempKeywords_set[0]:
                        item.collapse=False
                    
                    scroll = ScrollView()
                    item.add_widget(scroll)
                    
                    label = Label_Scroll()
                    label.text = "{}".format(keywords_dict[kw])
                    scroll.add_widget(label)

            self.SwitchToKeywords()


    def MastermindsKeywords(self):
        TempCarriers_text = self.ids.mastermind_lab.text
        Dict = masterminds_dict
        Title = "Mastermind"
        self.ShowKeywords(TempCarriers_text,Dict,Title)

    def VillainsKeywords(self):
        TempCarriers_text = self.ids.villains_lab.text
        Dict = villains_dict
        Title = "Villains"
        self.ShowKeywords(TempCarriers_text,Dict,Title)

    def HenchmenKeywords(self):
        TempCarriers_text = self.ids.henchmen_lab.text
        Dict = henchmen_dict
        Title = "Henchmen"
        self.ShowKeywords(TempCarriers_text,Dict,Title)

    def HeroesKeywords(self):
        TempCarriers_text = self.ids.heroes_lab.text
        Dict = heroes_dict
        Title = "Heroes"
        self.ShowKeywords(TempCarriers_text,Dict,Title)


    def SchemeDescriptThis(self,Scheme):
        
        if Scheme == "":
            pass
        else:
            app = App.get_running_app()
                        
            app.root.get_screen("scheme_window").ids.scheme_container.clear_widgets()

            app.root.get_screen("scheme_window").ids.scheme_title.text="{}".format(Scheme.replace("|",""))
            app.root.get_screen("scheme_window").ids.scheme_title.background_color=(45/255.0, 145/255.0, 73/255.0, 1)

            ItemsAccordion = Accordion(orientation = "vertical")
            app.root.get_screen("scheme_window").ids.scheme_container.add_widget(ItemsAccordion)

            try:
                content = schemes_dict_desc[Scheme].split("\n---\n")

            except KeyError:
                
                Scheme = "".join(["|", Scheme])
                content = schemes_dict_desc[Scheme].split("\n---\n")

            for item in content:
                title,description = item.split("\n--\n")
                
                accordionitem = AccordionItem(title="{}".format(title))
                ItemsAccordion.add_widget(accordionitem)

                scroll = ScrollView()
                accordionitem.add_widget(scroll)
                if item == content[0]:
                    accordionitem.collapse=False
                
                label = Label_Scroll()
                label.text = "{}".format(description)
                scroll.add_widget(label)

            keywords = schemes_dict_keys[Scheme]

            if len(keywords) != []:
                for kw in keywords:
                    if "Scheme Transforms" in kw:
                        SchTranTitle, SchTranTarget = kw.split(":")
                        button = Button(size_hint_y = .15)
                        button.text="{}".format(kw.replace("|","").replace(":",":\n"))
                        button.background_color= (45/255, 145/255, 73/255, 1)
                        schemetransform = lambda : self.SchemeDescriptThis(SchTranTarget)
                        button.on_release = schemetransform
                        app.root.get_screen("scheme_window").ids.scheme_container.add_widget(button)

                    elif "Veiled Scheme" in kw:
                        unveiled_schemes = [item for item in schemes_names if "|..." in item]

                        #[ expression for item in iterable if condition ]

                        randomizer = random.randint(0,len(unveiled_schemes)-1)
                        chosen_scheme = unveiled_schemes[randomizer]

                        button = Button(size_hint_y = .15)
                        button.text="Unveil Scheme"
                        button.background_color= (45/255, 145/255, 73/255, 1)
                        schemetransform = lambda : self.SchemeDescriptThis(chosen_scheme)
                        button.on_release = schemetransform
                        app.root.get_screen("scheme_window").ids.scheme_container.add_widget(button)


                    else:

                        item = AccordionItem(title="{}".format(kw))
                        ItemsAccordion.add_widget(item)

                        scroll = ScrollView()
                        item.add_widget(scroll)

                        label = Label_Scroll()
                        label.text = "{}".format(keywords_dict[kw])
                        
                                        
                        scroll.add_widget(label)



            app = App.get_running_app()
            app.root.get_screen("main_window").manager.transition.direction = "left"
            app.root.get_screen("main_window").manager.current = "scheme_window"
            self.ids.scheme_lab.text = "{}".format(Scheme.replace("|",""))

    def SchemeDescription(self):
        
        scheme = self.ids.scheme_lab.text
        self.SchemeDescriptThis(scheme)

    def Search_input(self):

        app = App.get_running_app()
        input = (app.root.get_screen("search_window").ids.textinput.text)
        
        app.root.get_screen("search_window").ids.search_container.clear_widgets()

        if len(input) <= 3:
            pass

        else:

            button = {}
            button_list = []
            content_list = {}
            show_desc = {}
            show_keys = {}
            
            for name in schemes_names:
                if (input in name) or (input.capitalize() in name) or (input.upper() in name) or (input.lower() in name) or (input.title() in name) :
                    
                    button[name] = Button()
                    app.root.get_screen("search_window").ids.search_container.add_widget(button[name])
                    button_list.append(button[name])
                    content_list[button[name]] = name
                    
                    button[name].text="{}".format(name.replace("|",""))
                    button[name].background_color= (45/255, 145/255, 73/255, 1)


            for item in button_list:
                show_desc[item] = lambda item : self.SchemeDescriptThis(content_list[item])
                item.bind(on_release = show_desc[item])

            button_list = []

            for name in masterminds_names:
                if (input in name) or (input.capitalize() in name) or (input.upper() in name) or (input.lower() in name) or (input.title() in name) :
                    
                    button[name] = Button()
                    app.root.get_screen("search_window").ids.search_container.add_widget(button[name])
                    button_list.append(button[name])
                    content_list[button[name]] = name
                    
                    button[name].text="{}".format(name)
                    button[name].background_color= (119/255.0, 50/255.0, 168/255.0,1)
                    
            for item in button_list:
                show_keys[item] = lambda item : self.ShowKeywords(content_list[item],masterminds_dict,content_list[item])
                item.bind(on_release = show_keys[item])

            button_list = []        

            for name in villains_names:
                if (input in name) or (input.capitalize() in name) or (input.upper() in name) or (input.lower() in name) or (input.title() in name) :
                    
                    button[name] = Button()
                    app.root.get_screen("search_window").ids.search_container.add_widget(button[name])
                    button_list.append(button[name])
                    content_list[button[name]] = name
                    
                    button[name].text="{}".format(name)
                    button[name].background_color= (1,0,0,1)
                    
            for item in button_list:
                show_keys[item] = lambda item : self.ShowKeywords(content_list[item],villains_dict,content_list[item])
                item.bind(on_release = show_keys[item])

            button_list = []    


            for name in henchmen_names:
                if (input in name) or (input.capitalize() in name) or (input.upper() in name) or (input.lower() in name) or (input.title() in name) :
                    
                    button[name] = Button()
                    app.root.get_screen("search_window").ids.search_container.add_widget(button[name])
                    button_list.append(button[name])
                    content_list[button[name]] = name
                    
                    button[name].text="{}".format(name)
                    button[name].background_color= (235/255.0, 156/255.0, 38/255.0,1)
                    
            for item in button_list:
                show_keys[item] = lambda item : self.ShowKeywords(content_list[item],henchmen_dict,content_list[item])
                item.bind(on_release = show_keys[item])

            button_list = []

            for name in heroes_names:
                if (input in name) or (input.capitalize() in name) or (input.upper() in name) or (input.lower() in name) or (input.title() in name) :
                    
                    button[name] = Button()
                    app.root.get_screen("search_window").ids.search_container.add_widget(button[name])
                    button_list.append(button[name])
                    content_list[button[name]] = name
                    
                    button[name].text="{}".format(name)
                    button[name].background_color= (48/255.0,99/255.0,194/255.0,1)
                    
            for item in button_list:
                show_keys[item] = lambda item : self.ShowKeywords(content_list[item],heroes_dict,content_list[item])
                item.bind(on_release = show_keys[item])

            button_list = []


            def KeywordDescriptThis(Keyword):
                app = App.get_running_app()
                app.root.get_screen("scheme_window").ids.scheme_container.clear_widgets()

                app.root.get_screen("scheme_window").ids.scheme_title.text="{}".format(Keyword)
                app.root.get_screen("scheme_window").ids.scheme_title.background_color=(0,0,8/10.0,1)

                scroll = ScrollView()
                app.root.get_screen("scheme_window").ids.scheme_container.add_widget(scroll)

                label = Label_Scroll()
                label.text = "{}".format(keywords_dict[Keyword])
                scroll.add_widget(label)

                app = App.get_running_app()
                app.root.get_screen("main_window").manager.transition.direction = "left"
                app.root.get_screen("main_window").manager.current = "scheme_window" 


            for name in keywords_names:
                if "Scheme Transforms" in name:
                    pass
                elif (input in name) or (input.capitalize() in name) or (input.upper() in name) or (input.lower() in name) or (input.title() in name):
                    
                    button[name] = Button()
                    app.root.get_screen("search_window").ids.search_container.add_widget(button[name])
                    button_list.append(button[name])
                    content_list[button[name]] = name
                    
                    button[name].text="{}".format(name)
                    button[name].background_color= (0,0,8/10.0,1)
                    
            for item in button_list:
                show_keys[item] = lambda item : KeywordDescriptThis(content_list[item])
                item.bind(on_release = show_keys[item])

            button_list = []                           


        
    def Go_To_Search(self):
        app = App.get_running_app()
        app.root.get_screen("main_window").manager.transition.direction = "left"
        app.root.get_screen("main_window").manager.current = "search_window"
        app.root.get_screen("search_window").ids.textinput.focus=True

    def Save_Game(self):
        scheme_save = self.ids.scheme_lab.text
        mastermind_save = self.ids.mastermind_lab.text
        villains_save = self.ids.villains_lab.text
        henchmen_save = self.ids.henchmen_lab.text
        heroes_save = self.ids.heroes_lab.text
        bystanders_save = self.ids.bystanders_lab.text
        lines = [str(vilnum),str(hennum),str(hernum),scheme_save,mastermind_save,villains_save,henchmen_save,heroes_save,bystanders_save]
        with open(os.path.join(os.path.dirname(__file__),'lists/saved_game.txt'), 'w') as save:
            save.write('\n'.join(lines))

    def Load_Game(self):
        global vilnum
        global hennum
        global hernum
        load_game = open(os.path.join(os.path.dirname(__file__),'lists/saved_game.txt'), 'r')
        if len(load_game.read().splitlines()) != 9:
            pass
        else:
            load_game = open(os.path.join(os.path.dirname(__file__),'lists/saved_game.txt'), 'r')
            vilnum,hennum,hernum,scheme_load,mastermind_load,villains_load,henchmen_load,heroes_load,bystanders_load = load_game.read().splitlines()
            vilnum = int(vilnum)
            hennum = int(hennum)
            hernum = int(hernum)
            self.ids.scheme_lab.text = '{}'.format(scheme_load)
            self.ids.mastermind_lab.text = '{}'.format(mastermind_load)
            self.ids.villains_lab.text = '{}'.format(villains_load)
            self.ids.henchmen_lab.text = '{}'.format(henchmen_load)
            self.ids.heroes_lab.text = '{}'.format(heroes_load)
            self.ids.bystanders_lab.text = '{}'.format(bystanders_load)
            self.ChangeInstructions()

        


class Label_Scroll(Label):
    pass

class Keywords_Window(Screen):
    def Go_Search(self):
        proxy = Main_Window()
        proxy.Go_To_Search()

class Scheme_Window(Screen):
    def Go_Search(self):
        proxy = Main_Window()
        proxy.Go_To_Search()

class Search_Window(Screen):
    def Search_Button(self):
        proxy = Main_Window()
        proxy.Search_input()
        


class WindowManager(ScreenManager):
    pass

ux = Builder.load_file("RandoMarvel_2_0.kv")    

class RandoMarvel(App):
    def build(self):

        root_folder = self.user_data_dir
        

        return ux

            

if __name__ == "__main__":
    RandoMarvel().run()

