"""docstring"""
import re
import sublime
import sublime_plugin

from SublimeWritingTools.conf import settings

RES = []
# FIG = "foo"
PREFIX = settings().get("prefix", "+@")

class ListFiguresCommand(sublime_plugin.TextCommand):
    """docstrong"""

    def on_done(self, index):
        if index == -1:
            return
        self.view.run_command("insert", {"characters": PREFIX + RES[index]})

    def run(self, edit):
        global RES
        contents = self.view.substr(sublime.Region(0, self.view.size()))
        regex = r"(\#)(fig:.*?)(}| )"
        matches = re.findall(regex, contents)
        for match in list(matches):
            RES.append(match[1])
        RES = list(set(RES))
        win = sublime.active_window()
        win.show_quick_panel(RES, self.on_done)
