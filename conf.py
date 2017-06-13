import sublime

base_name = "SublimeWritingTools.sublime-settings"

class Loader(object):

    def load(self):
        return sublime.load_settings(base_name)
    def get_setting(key):
        print("Hello Settings")
        value = sublime.load_settings(base_name).get(key)
        return value

settings = Loader().load
