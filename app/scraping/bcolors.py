class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @staticmethod
    def info(text):
        return '{}{}{}'.format(bcolors.OKBLUE, text, bcolors.ENDC)

    @staticmethod
    def status(text):
        return '{}{}{}'.format(bcolors.OKCYAN, text, bcolors.ENDC)

    @staticmethod
    def fail(text):
        return '{}{}{}'.format(bcolors.FAIL, text, bcolors.ENDC)

    @staticmethod
    def ok(text):
        return '{}{}{}'.format(bcolors.OKGREEN, text, bcolors.ENDC)

    @staticmethod
    def warning(text):
        return '{}{}{}'.format(bcolors.WARNING, text, bcolors.ENDC)

    @staticmethod
    def header(text):
        return '{}{}{}'.format(bcolors.HEADER, text, bcolors.ENDC)

    @staticmethod
    def bold(text):
        return '{}{}{}'.format(bcolors.BOLD, text, bcolors.ENDC)

    @staticmethod
    def underline(text):
        return '{}{}{}'.format(bcolors.UNDERLINE, text, bcolors.ENDC)
