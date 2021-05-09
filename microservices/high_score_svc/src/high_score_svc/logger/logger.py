from datetime import datetime


class PrintLogger:
    def __init__(self, component):
        self.component = component

    def log(self, msg):
        PrintLogger.s_log(self.component, msg)

    @staticmethod
    def s_log(component, msg):
        print(
            f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}][{component:>12}] {msg}\n',
            end="",
        )
