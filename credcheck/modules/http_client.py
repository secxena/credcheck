import logging
import warnings

warnings.filterwarnings("ignore")
logger = logging.getLogger(__name__)


class BaseClient:
    def __init__(self, verify_ssl=None, username=None, password=None, api_timeout=None):
        """
        Basic HTTP client to facilitate all kind of requests
        """
        self.method_kwargs = {}
        if verify_ssl is not None:
            self.method_kwargs["verify"] = verify_ssl
        if username is not None and password is not None:
            self.method_kwargs["auth"] = (username, password)
        if api_timeout is not None:
            self.method_kwargs["timeout"] = api_timeout

    def _http_response(self, url, method, **kwargs):
        """
        :params url: - full target url
        :type url: - str
        :param method: - method from requests
        :type method: - function
        :param kwargs: - url formatting args
        :type kwargs: - dict
        :rtype: - Response of the request
        """
        logger.debug("%s %s", method.__name__.upper(), url)
        response = method(url, **self.method_kwargs, **kwargs)
        logger.debug("%s %s", response.status_code, response.reason)
        return response

    def _http_call(self, url, method, **kwargs):
        """
        :param url: - full target url
        :type url: - str
        :param method: - method from requests
        :type method: - function
        :param kwargs: - url formatting args
        :type kwargs: - dict
        :rtype: - response in json format 
        """
        response = self._http_response(url, method, **kwargs)
        if not response.content:
            return {}
        try:
            return response.json()
        except:
            return response.content


class CheckAPI(BaseClient):
    def __init__(self, *args, **kwargs):
        """
        Class to test rest APIs
        """
        super(CheckAPI, self).__init__(*args, **kwargs)

    def _auth(self, url, method, **kwargs):
        """
        This will consume all kind of arguments ie. Headers, data
        etc to test if the service is working fine 
        :param url: - URL of servicefrom API config data 
        :type url: - str
        :param method: - Function of reuqests class 
        :type method: - function
        :param **kwargs: - Header data and all other kind of REST params
        :type **kwargs: - dict
        :rtype : - This will return a json/dict of the response if response
        is of type appliation/json else str
        """
        return self._http_call(url, method, **kwargs)
