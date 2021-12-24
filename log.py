import os


class Log:
    def executionLog(toLog):
        Log.__checkDir("Logs")
        with open("Logs/execution_log.txt", "a", encoding="UTF8") as log:
            log.write(f"{toLog}\n")

    def __checkDir(directory):
        if directory not in os.listdir():
            os.mkdir(directory)
