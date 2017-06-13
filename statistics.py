import sublime
import sublime_plugin
import re
from bs4 import BeautifulSoup
from markdown import markdown

class TextStatisticsCommand(sublime_plugin.TextCommand):

    def all_characters_incl_ws_count(self):
        return "Characters (including whitespaces): " + str(self.view.size())

    def all_charaters_excl_ws_count(self):
        contents = self.view.substr(sublime.Region(0, self.view.size()))
        # contents = contents.replace(" ", "")
        # return "Characters (no whitespaces): " + str(len(contents))
        return "Characters (no whitespaces): " + str(len("".join(contents.split())))

    def word_count(self):
        contents = self.view.substr(sublime.Region(0, self.view.size()))
        html = markdown(contents)
        text = BeautifulSoup(html).text
        return "Words: " + str(len(text.split()))

    def par_count(self):
        contents = self.view.substr(sublime.Region(0, self.view.size()))

        pars = re.compile("\n|\r\n|\r").split(contents)
        pars = list(filter(None, pars))
        return "Paragraphs: " + str(len(pars))

    def callback(self):
        """Nothing here for now"""
        # print ("foo")

    def run(self, edit):
        stats = [""]
        stats.append(self.all_characters_incl_ws_count())
        stats.append(self.all_charaters_excl_ws_count())
        stats.append(self.word_count())
        stats.append(self.par_count())
        win = sublime.active_window()
        win.show_quick_panel(stats, self.callback)
        # panel = win.create_output_panel("stats")
        # panel.insert(edit, 0, stat)
        # win.run_command("show_panel", {"panel": "output.stats"})
