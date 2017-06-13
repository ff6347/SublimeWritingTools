"""docstring"""
import re
import sublime
import sublime_plugin


RES = []
# FIG = "foo"
PREFIX = "+@"


class ListFiguresCommand(sublime_plugin.TextCommand):
    """docstrong"""

    def on_done(self, index):
        # global FIG
        if index == -1:
            return
        self.view.run_command("insert", {"characters": PREFIX + RES[index]})
        # self.view.insert(edit, self.view.sel()[0].begin(), RES[index])

    def run(self, edit):
        contents = self.view.substr(sublime.Region(0, self.view.size()))
        # print (self.view.substr(sublime.Region(0, self.view.size())))
        regex = r"(\#)(fig:.*?)(}| )"
        matches = re.findall(regex, contents)
        for match in list(matches):
            # print(r[1])
            RES.append(match[1])
        # print(RES)
        win = sublime.active_window()
        win.show_quick_panel(RES, self.on_done)

        # self.view.insert(edit, 0, "Hello, World!")
