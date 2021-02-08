# coding: UTF-8
import urllib2
import ssl
import urlparse
import threading

##!!!!##################################################################################################
#### Own written code can be placed above this commentblock . Do not change or delete commentblock! ####
########################################################################################################
##** Code created by generator - DO NOT CHANGE! **##

class Tibber_14108_14108(hsl20_3.BaseModule):

    def __init__(self, homeserver_context):
        hsl20_3.BaseModule.__init__(self, homeserver_context, "hsl20_3_tibber")
        self.FRAMEWORK = self._get_framework()
        self.LOGGER = self._get_logger(hsl20_3.LOGGING_NONE,())
        self.PIN_I_STOKEN=1
        self.PIN_I_NUPDATERATE=2
        self.PIN_O_SRPLY=1
        self.FRAMEWORK._run_in_context_thread(self.on_init)

########################################################################################################
#### Own written code can be placed after this commentblock . Do not change or delete commentblock! ####
###################################################################################################!!!##

    def log_msg(self, text):
        self.DEBUG.add_message("14108: " + str(text))

    def log_data(self, key, value):
        self.DEBUG.set_value("14108 " + str(key), str(value))

    def get_https_data(self, data):
        url = 'https://api.tibber.com/v1-beta/gql'
        url_parsed = urlparse.urlparse(url)

        # Build a SSL Context to disable certificate verification.
        ctx = ssl._create_unverified_context()
        response_data = ""

        try:
            # Build a http request and overwrite host header with the original hostname.
            token = self._get_input_value(self.PIN_I_STOKEN)
            headers = {'Host': url_parsed.hostname,
                       'Content-Type': 'application/json',
                       'Authorization': str('Bearer' + token)}

            request = urllib2.Request(url, data, headers)
            # Open the URL and read the response.
            response = urllib2.urlopen(request, timeout=self.m_nTimeOut, context=ctx)
            response_data = response.read()
        except Exception as e:
            self.logData("Error", "get_https_data: " + str(e))

        return response_data

    def time_out(self):
        interval = float(self._get_input_value(self.PIN_I_NUPDATERATE))
        if interval <= 0:
            return

        # do something

        t = threading.Timer(interval, self.time_out()).start()

    def on_init(self):
        self.DEBUG = self.FRAMEWORK.create_debug_section()

        #self.m_sFBIP = self._get_input_value(self.PIN_I_SFBIP)

        interval = float(self._get_input_value(self.PIN_I_NUPDATERATE))
        if interval > 0:
            t = threading.Timer(interval, self.time_out()).start()

    def on_input_value(self, index, value):
        if index == self.PIN_I_NUPDATERATE:
            interval = float(self._get_input_value(self.PIN_I_NUPDATERATE))
            if interval > 0:
                t = threading.Timer(interval, self.time_out()).start()
