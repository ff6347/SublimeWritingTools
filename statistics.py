import sublime
import sublime_plugin
import re

stats = ["Insert all"]
from SublimeWritingTools.cleaner import Cleaner

cleaner = Cleaner()

class TextStatisticsCommand(sublime_plugin.TextCommand):

    def remove_formatting(self):
        contents = self.view.substr(sublime.Region(0, self.view.size()))
        return cleaner.plain_text(contents)

    def all_characters_incl_ws_count(self):
        text = self.remove_formatting()
        return "Characters (including whitespaces): " + str(len(text))

    def all_charaters_excl_ws_count(self):
        text = self.remove_formatting()
        prefix = "Characters (no whitespaces): "
        return prefix + str(len("".join(text.split())))

    def word_count(self):
        text = self.remove_formatting()
        return "Words: " + str(len(text.split()))

    def par_count(self):
        text = self.remove_formatting()
        pars = re.compile("\n|\r\n|\r").split(text)
        pars = list(filter(None, pars))
        return "Paragraphs: " + str(len(pars))

    def on_done(self, index):
        if index == -1:
            return
        elif index == 0:
            stats.pop(0)
            self.view.run_command("insert", {"characters": "\n".join(stats)})
        else:
            self.view.run_command(
                "insert", {"characters": stats[index]})

        """Nothing here for now"""
        # print ("foo")

    def run(self, edit):
        global stats
        stats = ["Insert all"]
        stats.append(self.all_characters_incl_ws_count())
        stats.append(self.all_charaters_excl_ws_count())
        stats.append(self.word_count())
        stats.append(self.par_count())
        win = sublime.active_window()
        win.show_quick_panel(stats, self.on_done)
        # panel = win.create_output_panel("stats")
        # panel.insert(edit, 0, stat)
        # win.run_command("show_panel", {"panel": "output.stats"})
