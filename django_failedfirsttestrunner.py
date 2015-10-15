import pickle

from django.test.runner import DiscoverRunner
from django.utils.unittest import TextTestResult, TextTestRunner


# TODO: should be one per test suite, not one globally
temp_filename = '/tmp/django_test_run.pickle'


class FailedFirstRunner(DiscoverRunner):

    def run_suite(self, suite, **kwargs):
        try:
            with open(temp_filename, 'rb') as temp:
                while True:
                    try:
                        klass, test = pickle.load(temp)
                        tst = klass(test)
                        suite._tests.remove(tst)
                        suite._tests.insert(0, tst)
                    except (EOFError, ValueError, AttributeError):
                        break
        except IOError:
            pass
        return FailedFirstTestRunner(verbosity=self.verbosity, failfast=self.failfast).run(suite)


class FailedFirstTestResult(TextTestResult):
    fp = None

    def startTestRun(self):
        self.fp = open(temp_filename, 'wb')
        super(FailedFirstTestResult, self).startTestRun()

    def addFailure(self, test, err):
        obj = (test.__class__, test._testMethodName)
        pickle.dump(obj, self.fp)
        super(FailedFirstTestResult, self).addFailure(test, err)

    def stopTestRun(self):
        self.fp.close()
        super(FailedFirstTestResult, self).stopTestRun()


class FailedFirstTestRunner(TextTestRunner):
    resultclass = FailedFirstTestResult
