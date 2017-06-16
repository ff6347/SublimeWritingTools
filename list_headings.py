"""docstring"""
import re
import sublime
import sublime_plugin

from SublimeWritingTools.conf import settings
from SublimeWritingTools.cleaner import Cleaner

cleaner = Cleaner()

# RES = []
# FIG = "foo"
PREFIX = settings().get("prefix-headings", "#")

class ListHeadingsCommand(sublime_plugin.TextCommand):
    """docstrong"""

    def on_done(self, index):
        if index == -1:
            return
        self.view.run_command("insert", {"characters": PREFIX + RES[index]})

    def run(self, edit):
        global RES
        result = []
        contents = self.view.substr(sublime.Region(0, self.view.size()))
        regex = r"(^\#{1,6})(.*?)\n"
        matches = re.findall(regex, contents, re.MULTILINE)
        # print(matches)
        # these are the rules
        # https://pandoc.org/MANUAL.html#header-identifiers
        for match in list(matches):
            mdown = match[1]
            txt = cleaner.plain_text(mdown)
            txt_no_pun = cleaner.punctuation(txt)
            txt_no_nums = cleaner.leading_numbers(txt_no_pun)
            txt_lower = cleaner.lower_case(txt_no_nums)
            txt_stripped = cleaner.strip(txt_lower)
            txt_hyp = cleaner.hypens(txt_stripped)
            print(txt_hyp)
            if txt_hyp == "":
                res = "section"
            else:
                res = txt_hyp
            result.append(res)

        #     RES.append(match[1])
        # RES = list(set(RES))
        # print(RES)
        win = sublime.active_window()
        RES = result
        win.show_quick_panel(result, self.on_done)
