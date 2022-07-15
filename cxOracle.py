

import os
import cx_Oracle
from time import sleep as s


class Execute_sql:
    empty = "поле было пустым"
    """ Блок ввода данных для переменных для sql запроса """
    vN_house_value = '79178'
    vName_street = ""
    """ Конец Блок ввода данных для переменных для sql запроса """

    prefix = {"_kmh": "_kmh", "_cx_oracle": "_cx_oracle"}
    # path   = 'c:\\bin\\bin'
    path = {}
    path["oracle_client"]   = 'C:\\Oracle\\product\\10.1.0\\Client_1\\bin'
    path["results_from_oracle"] = "C:\\results_from_oracle\\" # C:\\results_from_oracle\\
    file = ''
    login = ''

    config = {"config": "config.txt", }
    count_rows_for_print = 3
    sql = {"region":                 "region.sql",
           "LKFL_findAdressLicFIO":  "LKFL_findAdressLicFIO.sql",
           "odpu":                   "control_odpu.sql",
           "ipu":                    "control_ipu.sql",
           "value_ipu":              "value_ipu.sql",
           "terminal":               "terminal.sql",
           "terminal_arch":          "terminal_arch.sql",
           "n_serv":                 "services.sql",
           "column_comment":         "column_comment.sql",
           "contragent":             "contragents.sql",
           "column":                 "find_column_in_objects.sql",
           "find_nLic_nOwner":       "find_lic_from_nOwner.sql",
           "comment":                "comment.sql",
           "find_nOwner_nLic":       "find_nOwner_from_nLic.sql",
           }
    return_res = ''

    def change(self, pref):

        if pref == self.prefix["_cx_oracle"]:
            newName = f'{self.path["oracle_client"]}{self.prefix["_kmh"]}'
            oldName = self.path["oracle_client"]
            os.renames(oldName, newName)
            oldName = f'{self.path["oracle_client"]}{self.prefix["_cx_oracle"]}'
            newName = self.path["oracle_client"]
            os.renames(oldName, newName)
        if pref == self.prefix["_kmh"]:
            newName = f'{self.path["oracle_client"]}{self.prefix["_cx_oracle"]}'
            oldName = self.path["oracle_client"]
            os.renames(oldName, newName)
            oldName = f'{self.path["oracle_client"]}{self.prefix["_kmh"]}'
            newName = self.path["oracle_client"]
            os.renames(oldName, newName)

    def get_sql_from_file(self):
        self.path["sql"] = 'C:\\Раб\\sql_all\\Client\\'
        with open(f"{self.path['sql']}{self.file}", "r") as f:
            sql = f.read()
        return sql

    def get_sql(self, file_sql):
        self.file = self.sql[file_sql]
        sql = self.get_sql_from_file()
        return sql

    def exec_sql(self, nameFuncCall, checkboxes, value_text=''):
        # print(checkboxes)
        if value_text == "":
            return self.empty
        if nameFuncCall == "on_solution_nHouse":
            if checkboxes["n_house"]:
                self.file = "find_n_house_from_adress1.sql"
                sql = self.get_sql_from_file()
                """ Блок ввода данных для переменных для sql запроса """
                sql = sql.replace('vN_house', value_text)
                """ Конец Блок ввода данных для переменных для sql запроса """
            # print(sql)
            if checkboxes["name_street"]:
                self.file = "find_n_house_from_adress2.sql"
                sql = self.get_sql_from_file()
                """ Блок ввода данных для переменных для sql запроса """
                value_text = value_text.split(' ')
                if len(value_text) > 1:
                    sql = sql.replace('&vSt_name_street_num_house', f'{value_text[0]}%{value_text[1]}')
                else:
                    sql = sql.replace('&vSt_name_street_num_house', f'{value_text[0]}')

                """ Конец Блок ввода данных для переменных для sql запроса """

            # print(sql)
            # try:
            #     int(value_text)
            #     self.file = "find_n_house_from_adress1.sql"
            #     sql = self.get_sql_from_file()
            #     """ Блок ввода данных для переменных для sql запроса """
            #     sql = sql.replace('vN_house', value_text)
            #     # sql = sql.replace('vSt.name_street', self.vName_street)
            #     """ Конец Блок ввода данных для переменных для sql запроса """
            # except Exception as e:
            #     if type(value_text) == str and value_text != "":
            #         self.file = "find_n_house_from_adress2.sql"
            #         sql = self.get_sql_from_file()
            #         """ Блок ввода данных для переменных для sql запроса """
            #         value_text = value_text.split(' ')
            #         if len(value_text) > 1:
            #             sql = sql.replace('&vSt_name_street_num_house', f'{value_text[0]}%{value_text[1]}')
            #         else:
            #             sql = sql.replace('&vSt_name_street_num_house', f'{value_text[0]}')
            #
            #         """ Конец Блок ввода данных для переменных для sql запроса """
            #     if value_text == "":
            #         return self.empty
            #
        if nameFuncCall == "on_solution_LKFL_find":
            try:
                if value_text == '':
                    return self.empty
                # int(value_text)
                # self.vN_house_value = value_text
                self.file = self.sql["LKFL_findAdressLicFIO"]

                # читаем sql из файла
                sql = self.get_sql_from_file()
                sql_key = { "w": ["--AND r.id_web_user = &id_web_user", f"  AND r.id_web_user IN ({value_text[:]})"],
                            "l": ["--AND u.n_lic IN (&N_LICs)"        , f"  AND u.n_lic IN ({value_text[:]})"],
                            "e": ["--AND lower(r.user_email) LIKE lower('%fufyrkina@mail.ru%')", f"  AND lower(r.user_email) LIKE lower('%{value_text[:]}%')"],
                            "s": ["--AND lower(r.user_surname) LIKE lower('%%')", f"  AND lower(r.user_surname) LIKE lower('%{value_text[:]}%')"],
                            }
                def value_text_find(key, sql):
                    if value_text.find(key, 0) == 0:
                        """ Блок ввода данных для переменных для sql запроса """
                        # sql = sql.replace('--AND r.id_web_user = &id_web_user', f'AND r.id_web_user IN ({value_text[1:]})')
                        sql = sql.replace(sql_key[key][0], sql_key[key][1])
                        # sql = sql.replace('vSt.name_street', self.vName_street)
                        """ Конец Блок ввода данных для переменных для sql запроса """
                        # print(value_text[1:])
                        return sql


                if checkboxes["n_lic"]:
                    # value_text_find(sql_key["l"], sql)
                    """ Блок ввода данных для переменных для sql запроса """
                    # sql = sql.replace('--AND r.id_web_user = &id_web_user', f'AND r.id_web_user IN ({value_text[1:]})')
                    sql = sql.replace(sql_key["l"][0], sql_key["l"][1])
                    # sql = sql.replace('vSt.name_street', self.vName_street)
                    """ Конец Блок ввода данных для переменных для sql запроса """
                if checkboxes["web_id_user"]:
                    """ Блок ввода данных для переменных для sql запроса """
                    # sql = sql.replace('--AND r.id_web_user = &id_web_user', f'AND r.id_web_user IN ({value_text[1:]})')
                    sql = sql.replace(sql_key["w"][0], sql_key["w"][1])
                    # sql = sql.replace('vSt.name_street', self.vName_street)
                    """ Конец Блок ввода данных для переменных для sql запроса """
                if checkboxes["user_email"]:
                    """ Блок ввода данных для переменных для sql запроса """
                    # sql = sql.replace('--AND r.id_web_user = &id_web_user', f'AND r.id_web_user IN ({value_text[1:]})')
                    sql = sql.replace(sql_key["e"][0], sql_key["e"][1])
                    # sql = sql.replace('vSt.name_street', self.vName_street)
                    """ Конец Блок ввода данных для переменных для sql запроса """
                if checkboxes["user_surname"]:
                    """ Блок ввода данных для переменных для sql запроса """
                    # sql = sql.replace('--AND r.id_web_user = &id_web_user', f'AND r.id_web_user IN ({value_text[1:]})')
                    sql = sql.replace(sql_key["s"][0], sql_key["s"][1])
                    # sql = sql.replace('vSt.name_street', self.vName_street)
                    """ Конец Блок ввода данных для переменных для sql запроса """

                # sql = value_text_find(value_text[0], sql)
                print("2 ---> " + sql)
                # s(100)

                # if value_text.find("w", 0) == 0:
                #     """ Блок ввода данных для переменных для sql запроса """
                #     sql = sql.replace('--AND r.id_web_user = &id_web_user',
                #                        f'AND r.id_web_user IN ({value_text[1:]})')
                #     print(sql)
                #     # sql = sql.replace('vSt.name_street', self.vName_street)
                #     """ Конец Блок ввода данных для переменных для sql запроса """
                #     # print(value_text[1:])
                # if  value_text.find("l", 0) == 0:
                #     """ Блок ввода данных для переменных для sql запроса """
                #     sql = sql.replace('--AND u.n_lic IN (&N_LICs)',
                #                        f'AND u.n_lic IN ({value_text[1:]})')
                #     print(sql)
                #     # sql = sql.replace('vSt.name_street', self.vName_street)
                #     """ Конец Блок ввода данных для переменных для sql запроса """
                # if value_text.find("e", 0) == 0:
                #     """ Блок ввода данных для переменных для sql запроса """
                #     sql = sql.replace("--AND lower(r.user_email) LIKE lower('%fufyrkina@mail.ru%')",
                #                        f"AND lower(r.user_email) LIKE lower('%{value_text[1:]}%')")
                #     print(sql)
                #     # sql = sql.replace('vSt.name_street', self.vName_street)
                #     """ Конец Блок ввода данных для переменных для sql запроса """
                # if value_text.find("s", 0) == 0:
                #     """ Блок ввода данных для переменных для sql запроса """
                #     sql = sql.replace("--AND lower(r.user_surname) LIKE lower('%%')",
                #                        f"AND lower(r.user_surname) LIKE lower('%{value_text[1:]}%')")
                #     print(sql)
                #     # sql = sql.replace('vSt.name_street', self.vName_street)
                #     """ Конец Блок ввода данных для переменных для sql запроса """
            except Exception as e:
                print("Erorr I/O or set parameters ", e)
                # if type(value_text) == str and value_text != "":
                #     self.vName_street = value_text
                #     self.file = "find_n_house_from_adress2.sql"
                # if value_text == "":
                #     return "empty"
        if nameFuncCall == "on_solution_odpu":
            self.file = self.sql["odpu"]
            sql = self.get_sql_from_file()
        if nameFuncCall == "on_solution_ipu":
            self.file = self.sql["ipu"]
            sql = self.get_sql_from_file()
        if nameFuncCall == "on_solution_value_ipu":
            self.file = self.sql["value_ipu"]
            sql = self.get_sql_from_file()
            if checkboxes["arch"]:
                sql = sql.replace("--and cv.date_arch = &date_arch", f" and cv.date_arch = '{value_text.split()[1]}' ") \
                    .replace("from kmh.t_counter_values cv", f"from kmh_arch.t_counter_values cv")
                sql = sql.replace("&n_house", f"{value_text.split()[0]}")
        # else:
        #     sql = sql.replace("&n_house", f"{value_text}")

        if nameFuncCall == "on_solution_terminal":
            if checkboxes["arch"]: # terminal_arch
                self.file = self.sql["terminal_arch"] # terminal_arch
            else:
                self.file = self.sql["terminal"]
            sql = self.get_sql_from_file()
            n_filial = value_text.split()[0]
            start = value_text.split()[1]
            end   = value_text.split()[2]
            sql   = sql.replace("&n_filial", f"{n_filial}").replace("&payment_giud_start", f"{start}").replace("&payment_giud_end", f"{end}")
            # sql = sql.replace("&payment_giud_start", f"{start}")
            # sql = sql.replace("&payment_giud_end", f"{end}")
        if nameFuncCall == "on_solution_nserv":
            self.file = self.sql["n_serv"]
            sql = self.get_sql_from_file()
            if checkboxes["n_serv"]:

                sql = sql.replace("--AND se.n_serv = &n_serv", f"AND se.n_serv = {value_text}").replace("1=2", "1=1")
            else:
                sql = sql.replace("--AND lower( se.name_serv ) LIKE lower( '%&name_serv%')", f"AND lower( se.name_serv ) LIKE lower( '%{value_text}%')").replace("1=2", "1=1")
        if nameFuncCall == "on_solution_contragent":
            self.file = self.sql["contragent"]
            sql = self.get_sql_from_file()
            if checkboxes["id_contragent"]:
                sql = sql.replace("--AND c.id_contragent  = &id_contragent ",
                                  f"AND c.id_contragent  = {value_text}").replace("1=2", "1=1")
            else:
                sql = sql.replace("--AND lower( c.name_contragent ) LIKE lower( '%&name_contragent%')",
                                  f"AND lower( c.name_contragent ) LIKE lower( '%{value_text}%')").replace("1=2", "1=1")
        if nameFuncCall == "on_solution_column_comment":
            if checkboxes["column_comment"] and checkboxes["column"]:
                checkboxes["column_comment"] = False
                checkboxes["column"] = False
                # sql = self.get_sql("")
                sql = """select sysdate "дата" from dual"""
            if checkboxes["column_comment"]:
                sql = self.get_sql("column_comment")
                sql = sql.replace("AND lower( a.column_name ) LIKE lower( '%%')",
                                  f"AND lower( a.column_name ) LIKE lower( '%{value_text}%')").replace("1=2", "1=1")
            if checkboxes["column"]:
                self.file = self.sql["column"]
                sql = self.get_sql_from_file()
                sql = sql.replace("AND lower(ac.COLUMN_NAME)LIKE lower('%test%')",
                                  f"AND lower(ac.COLUMN_NAME)LIKE lower('%{value_text}%')").replace("1=2", "1=1")
            if checkboxes["comment"]:
                sql = self.get_sql("comment")
                sql = sql.replace("AND lower(  comments )  LIKE lower( '%&comment%')",
                                  f"AND lower(  comments )  LIKE lower( '%{value_text}%')")
        if nameFuncCall == "on_solution_btn_find_nLic_nOwner":
            if checkboxes["n_lic"]:
                sql = self.get_sql("find_nOwner_nLic")
                sql = sql.replace("AND st.n_lic = &n_lic", f"AND st.n_lic = {value_text}")
            if checkboxes["id_contragent"]:
                self.file = self.sql["find_nLic_nOwner"]
                sql = self.get_sql_from_file()
                sql = sql.replace("AND cg.id_contragent = &id_contragent",
                                  f"AND cg.id_contragent = {value_text}")

        if nameFuncCall == "":
            pass
        print(sql)
        #--------------------------------------------------------------------------------------------

        #До выполнения запроса

        # --------------------------------------------------------------------------------------------

        self.change(self.prefix["_cx_oracle"]) # pref[0]) #self.prefix["_cx_oracle"])
        with open(self.config["config"], "r") as f:
            line = f.readlines()
            if line[0].split("=")[0] == 'login':
                login = line[0].split("=")[1][:-1]
            if line[1].split("=")[0] == 'password':
                passw = line[1].split("=")[1][:-1]
                # print(passw, )
            if line[2].split("=")[0] == 'ip':
                passw = line[2].split("=")[1][:-1]
                # print(passw, )
        self.path["sql"] = 'C:\\Раб\\sql_all\\'
        # with open(f"{self.path['sql']}{self.file}", "r") as f:
        #     sql = f.read()
        # print(sql)
        # Connect string format: [username]/[password]@//[hostname]:[port]/[DB service name]
        # conn = cx_Oracle.connect(f"{login}/{passw}@//{ip}:{port}/{db}")
        # cur.execute("SELECT 'Hello World!' FROM dual")
        try:
            conn = cx_Oracle.connect(f"{login}/{passw}@//{self.ip}:{self.port}/{self.db}")
            cur = conn.cursor()
            # vn_region = 20
            # cur.execute(f"select name_region from kmh.t_regions where n_region = {vn_region}")
            """ Блок ввода данных для переменных для sql запроса """
            # sql = sql.replace('vN_house', self.vN_house_value)
            # sql = sql.replace('vSt.name_street', self.vName_street)
            """ Конец Блок ввода данных для переменных для sql запроса """
            # print(sql)
            # print("this")
            try:
                cur.execute(f"{sql}")
                res = cur.fetchall()
            except Exception as e:
                print(f"Error or Exception in oracle -> {e}")
                res = f"Error or Exception in oracle -> {e}"
            # print("---> ", res)
        except Exception as e:
            print("Exception --->", e)
        finally:
            print("Finally --->")
            self.change(self.prefix["_kmh"])  # pref[1]) # self.prefix["_kmh"])
        """ Выполнить парсинг результата запроса"""
        # res = str(res)
        self.return_res = ''
        info_res = ''
        if not res == []:
            try:
                # res = str(res[0])
                # res = str(len(res))
                # print(len(res))
                if len(res) > self.count_rows_for_print:
                    for simbol in ['(', ')', '\'', '[', ']', ',', ' ']:
                        value_text = str(value_text).replace(simbol, '')
                    print(value_text)
                    len_res = len(res)
                    info_res = f"\nЗаписей больше, чем одна,\nполный результат тут\n{self.path['results_from_oracle']}{nameFuncCall}_{value_text}.txt\nВсего записей {len_res}\n"
                    if nameFuncCall == "on_solution_nHouse":
                        res = str(res).replace("('", '').replace("),", '\n').replace("',", " n_house ->")
                    if nameFuncCall == "on_solution_odpu":
                        odpu_res = ''
                        for element in res:
                            odpu_res = odpu_res + " " + str(element[1]) + " телефон -> " + str(element[5]) + " количество записей -> " + str(element[6]) + "\n"
                            res = odpu_res
                    if nameFuncCall == "on_solution_ipu":
                        if nameFuncCall == "on_solution_ipu":
                            ipu_res = ''
                            for element in res:
                                ipu_res = ipu_res + " " + str(element[2]) + " телефон -> " + str(
                                    element[4]) + " количество записей " + str(element[7]) + "\n"
                                res = ipu_res
                    if nameFuncCall == "on_solution_value_ipu":
                        value_ipu_res = ''
                        for element in res:
                            ipu_res = value_ipu_res + " " + str(element[2]) + " телефон -> " + str(
                                element[4]) + " количество записей " + str(element[7]) + "\n"
                            res = value_ipu_res
                    if nameFuncCall == "on_solution_terminal":
                        terminal_res = ''
                        for element in res:
                            terminal_res = terminal_res + ' оплата по "' + str(element[0]) + '"' + " лицевой счет -> " + str(
                                element[3]) +" номер чека -> " + str(
                                element[4]) + " сумма " + str(element[13]) + " Статус операции " + str(element[6]) +"\n"
                            res = terminal_res
                        res = str(res).replace("('", '').replace("),", '\n')
                    if nameFuncCall == "on_solution_LKFL_find":
                        lkfl_res = ''
                        for element in res:
                            lkfl_res = lkfl_res + " " + str(element)  + "\n"
                            res = lkfl_res
                        res = str(res).replace("('", '').replace("),", '\n')
                    if nameFuncCall == "on_solution_column_comment":
                        column_comment_res = ''
                        for element in res:
                            column_comment_res = column_comment_res + " " + str(element) + "\n"
                            res = column_comment_res
                        res = str(res).replace("('", '').replace("),", '\n')
                    if nameFuncCall == "on_solution_contragent":
                        contragent = ''
                        for element in res:
                            contragent = contragent + " " + str(element) + "\n"
                            res = contragent
                        res = str(res).replace("('", '').replace("),", '\n')
                    if nameFuncCall == "on_solution_btn_find_nLic_nOwner":
                        nLic = ''
                        for element in res:
                            nLic = nLic + " " + str(element) + "\n"
                            res = nLic
                        res = str(res).replace("('", '').replace("),", '\n')
                    else:
                        res = str(res)
                    # self.return_res = str(res) + f"\nЗаписей больше, чем одна,\nполный результат тут {self.path['results_from_oracle']}{nameFuncCall}_{value_text}.txt\nВсего записей {len_res}"
                    print(res)
                    with open(f'{self.path["results_from_oracle"]}{nameFuncCall}_{value_text}.txt', "w") as f:
                        f.write(f"\nВсего записей {len_res}\n")
                        f.write(res)
                    res = ''
                # res = str(res)
            except Exception as e:
                print("Что то с результатом не то после Oracle -> ", e)
        else:
            res = "empty list response from Oracle: результат sql запроса не выдал ни одной строки"

        return info_res + str(res) # + self.return_res

    # change(self.prefix["_cx_oracle"])

    def exec_sql_test(self):
        self.change(self.prefix["_cx_oracle"])
        self.change(self.prefix["_kmh"])
        print("exec_sql_test()")





if __name__=="__main__":
    # Execute_sql.exec_sql()
    pass