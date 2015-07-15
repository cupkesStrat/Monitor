__author__ = 'christopherupkes'

import nagiosplugin


class NagiosPluginTest(nagiosplugin.Resource):

    def probe(self):
        return [nagiosplugin.Metric('Plugin Test', True, context='null')]


def main():
    check = nagiosplugin.Check(NagiosPluginTest())
    check.main()

if __name__ == '__main__':
    main()