# from kivy.app import App
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.label import Label
# from kivy.uix.textinput import TextInput
#
#
# class LoginScreen(GridLayout):
#
#     def __init__(self, **kwargs):
#         super(LoginScreen, self).__init__(**kwargs)
#         self.cols = 2
#         self.add_widget(Label(text='Variable'))
#         self.username = TextInput(multiline=False)
#         self.add_widget(self.username)
#         # self.add_widget(Label(text='password'))
#         # self.password = TextInput(password=True, multiline=False)
#         # self.add_widget(self.password)
#
#
# class GUInterface(App):
#
#     def build(self):
#         return LoginScreen()
#
#
# if __name__ == '__main__':
#     GUInterface().run()
#______________________________________________________________________________________________
# from kivy.app import App

# from kivy.uix.gridlayout import GridLayout


# class Container(GridLayout):
#     display = ObjectProperty()
#
#     def add_one(self):
#         value = int(self.display.text)
#         self.display.text = str(value+1)
#
#     def subtract_one(self):
#         value = int(self.display.text)
#         self.display.text = str(value-1)
#
# class MainApp(App):
#
#     def build(self):
#         self.title = 'Awesome app!!!'
#         return Container()
#
# if __name__ == "__main__":
#     app = MainApp()
#     app.run()
# #______________________________________________________________________________________________
# from kivy.app import App
# from kivy.lang import Builder
# from kivy.uix.button import Button
# from kivy.properties import ObjectProperty
# from kivy.uix.gridlayout import GridLayout
#
#
# from os import listdir
# # kv_path = ''
# # for kv in listdir(kv_path):
# #     Builder.load_file(kv_path+kv)
#
#
# class AddButton(Button):
#     pass
#
#
# class SubtractButton(Button):
#     pass
#
#
# class Container(GridLayout):
#     display = ObjectProperty()
#
#     def add_one(self):
#         value = int(self.display.text)
#         self.display.text = str(value+1)
#
#     def subtract_one(self):
#         value = int(self.display.text)
#         self.display.text = str(value-1)
#
#
# class MainApp(App):
#     def build(self):
#         self.title = 'Awesome app!!!'
#         return Container()
#
#
# if __name__ == "__main__":
#     app = MainApp()
#     app.run()
# #______________________________________________________________________________________________
# import cxOracle as modelOracle
# from kivy.app import App
# from kivy.uix.button import Button
#
#
# class MainApp(App):
#     def build(self):
#         button = Button(text='Найти адрес по n_house',
#                         size_hint=(.3, .2),
#                         pos_hint={'center_x': .5, 'center_y': .5})
#         button.bind(on_press=self.on_press_button)
#
#         return button
#
#     def on_press_button(self, instance):
#         print('Вы нажали на кнопку!')
#
#         modelOracle.execuite_sql()
#
#
# if __name__ == '__main__':
#     app = MainApp()
#     app.run()
# #______________________________________________________________________________________________
# Python
# from kivy.app import App
# from kivy.uix.button import Button
#
#
# class ButtonApp(App):
#     def build(self):
#         return Button()
#
#     def on_press_button(self):
#         print('Вы нажали на кнопку!')
#
#
# if __name__ == '__main__':
#     app = ButtonApp()
#     app.run()
# #______________________________________________________________________________________________
#
# import cxOracle as modelOracle
# from kivy.app import App
# from kivy.uix.button import Button
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.textinput import TextInput
#
#
# class ClientApp(App):
#
#     def build(self):
#         main_layout = BoxLayout()
#         self.solution = TextInput(
#             # """multiline=True, readonly=True, halign="left, font_size=10 """
#         )
#         main_layout.add_widget(self.solution)
#
#         exc_button = Button(
#             # """text="выполнить", pos_hint={"right_x": 0.1, "right_y": 0.1}"""
#         )
#         # exc_button.bind(on_press=self.on_solution())
#         # exc_button.bind(on_press=self.on_press_button())
#         exc_button.bind(on_press=self.on_press_button())
#         # exc_button.on_press()
#         main_layout.add_widget(exc_button)
#
#         return main_layout # , Button()
#
#     def on_press_button(self):
#         obj = modelOracle.Execute_sql()
#         #result = obj.exec_sql()
#         #self.solution.text = obj.exec_sql()
#         # print(result)
#
#     def on_solution(self):
#         pass
#
# if __name__ == '__main__':
#     app = ClientApp()
#     app.run()
# #______________________________________________________________________________________________
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.sandbox import Sandbox
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

import cxOracle as modelOracle


class ClientApp(App):
    def build(self):
        self.cols = 2
        self.btn_clear = "Очистить все поля"
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None
        main_layout = BoxLayout(orientation="vertical")
        self.solution = TextInput(
            multiline=True, readonly=True, halign="right", font_size=15, # height=200
        )
        main_layout.add_widget(self.solution)
        buttons = [

            [self.btn_clear]
        ]
        #  Создаем checkboxы
        """ Create checkboxs """
        conteiner = BoxLayout()
        checkbox_lable = Label(text="n_lic")
        self.checkbox_n_lic = CheckBox()
        conteiner.add_widget(checkbox_lable)
        conteiner.add_widget(self.checkbox_n_lic)

        checkbox_lable = Label(text="n_house")
        self.checkbox_n_house = CheckBox()
        conteiner.add_widget(checkbox_lable)
        conteiner.add_widget(self.checkbox_n_house)

        checkbox_lable = Label(text="n_serv")
        self.checkbox_n_serv = CheckBox()
        conteiner.add_widget(checkbox_lable)
        conteiner.add_widget(self.checkbox_n_serv)

        checkbox_lable = Label(text="name_street")
        self.checkbox_name_street = CheckBox()
        conteiner.add_widget(checkbox_lable)
        conteiner.add_widget(self.checkbox_name_street)

        checkbox_lable = Label(text="web_id_user")
        self.checkbox_web_id_user = CheckBox()
        conteiner.add_widget(checkbox_lable)
        conteiner.add_widget(self.checkbox_web_id_user)

        checkbox_lable = Label(text="user_email")
        self.checkbox_user_email = CheckBox()
        conteiner.add_widget(checkbox_lable)
        conteiner.add_widget(self.checkbox_user_email)

        checkbox_lable = Label(text="user_surname")
        self.checkbox_user_surname = CheckBox()
        conteiner.add_widget(checkbox_lable)
        conteiner.add_widget(self.checkbox_user_surname)

        checkbox_lable = Label(text="arch")
        self.checkbox_arch = CheckBox()
        conteiner.add_widget(checkbox_lable)
        conteiner.add_widget(self.checkbox_arch)

        checkbox_lable = Label(text="id_contragent")
        self.checkbox_id_contragent = CheckBox()
        conteiner.add_widget(checkbox_lable)
        conteiner.add_widget(self.checkbox_id_contragent)

        checkbox_lable = Label(text="column_comment")
        self.checkbox_column_comment = CheckBox()
        conteiner.add_widget(checkbox_lable)
        conteiner.add_widget(self.checkbox_column_comment)

        checkbox_lable = Label(text="column")
        self.checkbox_column = CheckBox()
        conteiner.add_widget(checkbox_lable)
        conteiner.add_widget(self.checkbox_column)

        checkbox_lable = Label(text="comment")
        self.checkbox_comment = CheckBox()
        conteiner.add_widget(checkbox_lable)
        conteiner.add_widget(self.checkbox_comment)

        main_layout.add_widget(conteiner)
        """ Create checkboxs """
        # print(self.lab.active)
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text=label,
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)
        # Создаем кнопки
        equals_button        = Button(text="Найти n_house(по адресу) или адрес(по n_house)", pos_hint={"center_x": 0.5, "center_y": 0.5})
        btn_LKFL_find        = Button(text="личный кабинет ФизЛиц поиск адреса ФИО ЛС", pos_hint={"center_x": 0.5, "center_y": 0.5})
        btn_odpu             = Button(text="Проверить остаток по ОДПУ", pos_hint={"center_x": 0.5, "center_y": 0.5})
        btn_ipu              = Button(text="Проверить остаток по ИПУ", pos_hint={"center_x": 0.5, "center_y": 0.5})
        btn_value_ipu        = Button(text="Показания по ИПУ n_house + date_arch", pos_hint={"center_x": 0.5, "center_y": 0.5})
        btn_value_odpu       = Button(text="Показания по ОДПУ n_house + date_arch", pos_hint={"center_x": 0.5, "center_y": 0.5})
        btn_serv             = Button(text="либо n_serv либо название услуги ", pos_hint={"center_x": 0.5, "center_y": 0.5})
        # conteiner_termminal = BoxLayout()
        btn_terminal         = Button(text="терминал № начало конец периода", pos_hint={"center_x": 0.5, "center_y": 0.5})
        btn_column_comment   = Button(text="Поиск колонки, комментария, таблицы", pos_hint={"center_x": 0.5, "center_y": 0.5})
        btn_contragent       = Button(text="Поиск id_contragent, имя контрагента", pos_hint={"center_x": 0.5, "center_y": 0.5})
        btn_find_nLic_nOwner = Button(text="Поиск n_lic, от КА n_owner и наоборот", pos_hint={"center_x": 0.5, "center_y": 0.5})

        self.textInput_total = TextInput(text="")
        # ----------------------------------------------------------------------------------------------------------------------
        # Связываем кнопку с действием
        # equals_button.bind(on_press=self.on_solution)
        btn_serv.bind(on_press=self.on_solution_nserv)
        equals_button.bind(on_press=self.on_solution_nHouse)
        btn_LKFL_find.bind(on_press=self.on_solution_LKFL_find)
        btn_terminal.bind(on_press=self.on_solution_terminal)
        btn_odpu.bind(on_press=self.on_solution_odpu)
        btn_ipu.bind(on_press=self.on_solution_ipu)
        btn_value_ipu.bind(on_press=self.on_solution_value_ipu)
        btn_value_odpu.bind(on_press=self.on_solution_value_odpu)
        btn_contragent.bind(on_press=self.on_solution_contragent)
        btn_column_comment.bind(on_press=self.on_solution_column_comment)
        btn_find_nLic_nOwner.bind(on_press=self.on_solution_btn_find_nLic_nOwner)



        # ------------------------------------------------------------------------------------------------
        # Добавляем виджет
        main_layout.add_widget(self.textInput_total)
        main_layout.add_widget(equals_button)
        main_layout.add_widget(btn_LKFL_find)
        main_layout.add_widget(btn_terminal)
        # main_layout.add_widget(conteiner_termminal)
        main_layout.add_widget(btn_odpu)
        main_layout.add_widget(btn_ipu)
        main_layout.add_widget(btn_value_ipu)
        main_layout.add_widget(btn_value_odpu)
        main_layout.add_widget(btn_serv)
        main_layout.add_widget(btn_column_comment)
        main_layout.add_widget(btn_contragent)
        main_layout.add_widget(btn_find_nLic_nOwner)

        # self.check = CheckBox()
        # main_layout.add_widget(self.check)
        # self.sanbox = Sandbox()
        # main_layout.add_widget(self.sanbox)


        return main_layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == self.btn_clear:
            # Очистка виджета с решением
            self.solution.text = ""
            self.textInput_total.text = ""
            self.checkbox_user_email.active= False
            self.checkbox_user_surname.active = False
            self.checkbox_n_lic.active = False
            self.checkbox_web_id_user.active = False
            self.checkbox_n_house.active = False
            self.checkbox_name_street.active = False
            self.checkbox_arch.active = False
            self.checkbox_n_serv.active = False
            self.checkbox_id_contragent.active = False
            self.checkbox_column_comment.active = False
            self.checkbox_column.active = False
            self.checkbox_comment.active = False
        else:
            if current and (
                    self.last_was_operator and button_text in self.operators):
                # Не добавляйте два оператора подряд, рядом друг с другом
                return
            elif current == "" and button_text in self.operators:
                # Первый символ не может быть оператором
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators

    def on_solution(self, instance):

        obj = modelOracle.Execute_sql()
        solution = obj.exec_sql(self.textInput_total.text)
        self.solution.text = str(solution)

    def on_solution_nHouse(self, instance):

        self.checkboxes = {"n_house": self.checkbox_n_house.active,
                      "name_street": self.checkbox_name_street.active,
                      "n_lic": self.checkbox_n_lic.active,
                      "web_id_user": self.checkbox_web_id_user.active,
                      "user_email": self.checkbox_user_email.active,
                      "user_surname": self.checkbox_user_surname.active,
                      }
        obj = modelOracle.Execute_sql()
        solution = obj.exec_sql(nameFuncCall="on_solution_nHouse", checkboxes=self.checkboxes, value_text=self.textInput_total.text)
        self.solution.text = str(solution)
        self.textInput_total.text = ""

    def on_solution_LKFL_find(self, instance):
        self.checkboxes = {"n_house": self.checkbox_n_house.active,
                           "name_street": self.checkbox_name_street.active,
                           "n_lic": self.checkbox_n_lic.active,
                           "web_id_user": self.checkbox_web_id_user.active,
                           "user_email": self.checkbox_user_email.active,
                           "user_surname": self.checkbox_user_surname.active,
                           }
        obj = modelOracle.Execute_sql()
        solution = obj.exec_sql(nameFuncCall="on_solution_LKFL_find", checkboxes=self.checkboxes, value_text=self.textInput_total.text)
        self.solution.text = str(solution)
        self.textInput_total.text = ""

    def on_solution_odpu(self, instasnce):
        self.checkboxes = {"n_house": self.checkbox_n_house.active,
                           "name_street": self.checkbox_name_street.active,
                           "n_lic": self.checkbox_n_lic.active,
                           "web_id_user": self.checkbox_web_id_user.active,
                           "user_email": self.checkbox_user_email.active,
                           "user_surname": self.checkbox_user_surname.active,
                           }
        obj = modelOracle.Execute_sql()
        solution = obj.exec_sql(nameFuncCall="on_solution_odpu", checkboxes=self.checkboxes, value_text='ОДПУ')
        self.solution.text = str(solution)
        self.textInput_total.text = ""

    def on_solution_ipu(self, instance):
        self.checkboxes = {"n_house": self.checkbox_n_house.active,
                           "name_street": self.checkbox_name_street.active,
                           "n_lic": self.checkbox_n_lic.active,
                           "web_id_user": self.checkbox_web_id_user.active,
                           "user_email": self.checkbox_user_email.active,
                           "user_surname": self.checkbox_user_surname.active,
                           }
        obj = modelOracle.Execute_sql()
        solution = obj.exec_sql(nameFuncCall="on_solution_ipu", checkboxes=self.checkboxes, value_text='ИПУ')
        self.solution.text = str(solution)
        self.textInput_total.text = ""

    def on_solution_value_ipu(self, instance):
        self.on_solution_get("on_solution_value_ipu")

    def on_solution_value_odpu(self, instance):
        self.on_solution_get("on_solution_value_odpu")

    def on_solution_terminal(self, instance):
        self.checkboxes = {"n_house": self.checkbox_n_house.active,
                           "name_street": self.checkbox_name_street.active,
                           "n_lic": self.checkbox_n_lic.active,
                           "web_id_user": self.checkbox_web_id_user.active,
                           "user_email": self.checkbox_user_email.active,
                           "user_surname": self.checkbox_user_surname.active,
                           "arch": self.checkbox_arch.active,
                           }
        obj = modelOracle.Execute_sql()
        solution = obj.exec_sql(nameFuncCall="on_solution_terminal", checkboxes=self.checkboxes, value_text=self.textInput_total.text)
        self.solution.text = str(solution)
        self.textInput_total.text = ""

    def on_solution_nserv(self, instance):
        self.checkboxes = {"n_house": self.checkbox_n_house.active,
                           "name_street": self.checkbox_name_street.active,
                           "n_lic": self.checkbox_n_lic.active,
                           "web_id_user": self.checkbox_web_id_user.active,
                           "user_email": self.checkbox_user_email.active,
                           "user_surname": self.checkbox_user_surname.active,
                           "arch": self.checkbox_arch.active,
                           "n_serv": self.checkbox_n_serv.active,
                           }
        obj = modelOracle.Execute_sql()
        solution = obj.exec_sql(nameFuncCall="on_solution_nserv", checkboxes=self.checkboxes, value_text=self.textInput_total.text)
        self.solution.text = str(solution)
        self.textInput_total.text = ""

    def on_solution_column_comment(self, instance):
        self.checkboxes = {"n_house": self.checkbox_n_house.active,
                           "name_street": self.checkbox_name_street.active,
                           "n_lic": self.checkbox_n_lic.active,
                           "web_id_user": self.checkbox_web_id_user.active,
                           "user_email": self.checkbox_user_email.active,
                           "user_surname": self.checkbox_user_surname.active,
                           "arch": self.checkbox_arch.active,
                           "n_serv": self.checkbox_n_serv.active,
                           "id_contragent": self.checkbox_id_contragent.active,
                           "column_comment": self.checkbox_column_comment.active,
                           "column": self.checkbox_column.active,
                           "comment": self.checkbox_comment.active,
                           }
        obj = modelOracle.Execute_sql()
        solution = obj.exec_sql(nameFuncCall="on_solution_column_comment", checkboxes=self.checkboxes,
                                value_text=self.textInput_total.text)
        self.solution.text = str(solution)
        self.textInput_total.text = ""

    def on_solution_contragent(self, instance):
            self.checkboxes = {"n_house": self.checkbox_n_house.active,
                               "name_street": self.checkbox_name_street.active,
                               "n_lic": self.checkbox_n_lic.active,
                               "web_id_user": self.checkbox_web_id_user.active,
                               "user_email": self.checkbox_user_email.active,
                               "user_surname": self.checkbox_user_surname.active,
                               "arch": self.checkbox_arch.active,
                               "n_serv": self.checkbox_n_serv.active,
                               "id_contragent": self.checkbox_id_contragent.active,
                               "column_comment": self.checkbox_column_comment.active,
                               }
            obj = modelOracle.Execute_sql()
            solution = obj.exec_sql(nameFuncCall="on_solution_contragent", checkboxes=self.checkboxes,
                                    value_text=self.textInput_total.text)
            self.solution.text = str(solution)
            self.textInput_total.text = ""

    def on_solution_find_column_in_objects(self, instance):
        self.checkboxes = {"n_house": self.checkbox_n_house.active,
                           "name_street": self.checkbox_name_street.active,
                           "n_lic": self.checkbox_n_lic.active,
                           "web_id_user": self.checkbox_web_id_user.active,
                           "user_email": self.checkbox_user_email.active,
                           "user_surname": self.checkbox_user_surname.active,
                           "arch": self.checkbox_arch.active,
                           "n_serv": self.checkbox_n_serv.active,
                           "id_contragent": self.checkbox_id_contragent.active,
                           "column_comment": self.checkbox_column_comment.active,
                           "column": self.checkbox_column.active,
                           }
        obj = modelOracle.Execute_sql()
        solution = obj.exec_sql(nameFuncCall="on_solution_contragent", checkboxes=self.checkboxes,
                                value_text=self.textInput_total.text)
        self.solution.text = str(solution)
        self.textInput_total.text = ""

    def on_solution_btn_find_nLic_nOwner(self, instance):
        self.on_solution_get("on_solution_btn_find_nLic_nOwner")

    def on_solution_get(self, nameFuncCall, ):
        self.checkboxes = {"n_house": self.checkbox_n_house.active,
                           "name_street": self.checkbox_name_street.active,
                           "n_lic": self.checkbox_n_lic.active,
                           "web_id_user": self.checkbox_web_id_user.active,
                           "user_email": self.checkbox_user_email.active,
                           "user_surname": self.checkbox_user_surname.active,
                           "arch": self.checkbox_arch.active,
                           "n_serv": self.checkbox_n_serv.active,
                           "id_contragent": self.checkbox_id_contragent.active,
                           "column_comment": self.checkbox_column_comment.active,
                           "column": self.checkbox_column.active,
                           "comment": self.checkbox_comment.active,

                           }
        obj = modelOracle.Execute_sql()
        solution = obj.exec_sql(nameFuncCall=nameFuncCall, checkboxes=self.checkboxes,
                                value_text=self.textInput_total.text)
        self.solution.text = str(solution)
        self.textInput_total.text = ""

if __name__ == "__main__":
    app = ClientApp()
    app.run()