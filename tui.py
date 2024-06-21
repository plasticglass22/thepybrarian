#!/usr/bin/env python3

import sys
import utils
import aesth
import os
import npyscreen as nps

# class PybrarianForm(nps.Form):
#     def create(self):
#         self.title = self.add(nps.FixedText, name = 'Pybrarian')
#         self.searchterm = self.add(nps.TitleText, name = 'Search For: ', value = 'Enter Search Term')
#         tb_cwd = self.add(nps.TitleFixedText, name = "Current Working Directory: ", value = str(os.getcwd()))

#     def afterEditing(self):
#         self.parentApp.setNextForm(None)

# class Pybrarian(nps.NPSAppManaged):
#     def onStart(self):
#         self.addForm('MAIN', PybrarianForm, name = 'Pybrarian') ## title at top of form

def search(*args) -> list[str, list[tuple[str, list[str]]]]:
     results = []
     form = nps.Form(name = "Test Form")
     search_input = form.add(nps.TitleText, name = "Search Term: ", value = '')
     form.edit()
     results.append(str(search_input.value))
     results.append(utils.fullContents('.', search_input.value, False))
     return results
