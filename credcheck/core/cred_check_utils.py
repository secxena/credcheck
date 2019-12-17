import json
import logging
import os
import re

from requests import get, put, post

from credcheck.exceptions import ParametersRequiredError

# sys.tracebacklimit=0
from credcheck.modules import ssh_client, http_client

logging.basicConfig(
    format="%(asctime)s - %(name)s (%(lineno)s) - %(levelname)s: %(message)s",
    datefmt="%Y.%m.%d %H:%M:%S",
)


class CredUtils:
    def __init__(self):
        """
        """
        self.rootdir = os.path.abspath(os.path.dirname(__file__))
        self.data = self.load_data()

    @property
    def _services(self):
        """
        All available services for Credentials testing
        :rtype: dict of available target blocks 
        """
        return list(self.data.keys())

    @property
    def _protocol(self):
        """
        HTTP and SSH client to test over different protocols 
        :rtype: protocol handler clients to check credentials over different protocol
        """
        return {"http_client": http_client, "ssh_client": ssh_client}

    @property
    def _httpmethod(self):
        """
        :rtype
        """
        return {"get": get, "post": post, "put": put}

    def load_data(self):
        """
        :rtype
        """
        with open(self.rootdir + "/../data/api_key_meta.json", "r") as f:
            data = json.loads(f.read())
        return data

    def check_validity(self):
        """
        :rtype
        """
        for target, target_data in self.data.items():
            self.data[target]["config"]
            # print(target_data)

    def _format(self, data_block, data):
        """
        :param data_block: -
        :type data_block : -
        :param data: -
        :type data: -
        :rtype: -
        """
        # logging.debug("data to format %s", data_block)
        _helper = data_block.get("helper")
        if not data_block.get("config").get("request-type"):
            data_block["config"]["request-type"] = "get"
        try:
            data_block = self._filler(data_block["config"], data)
        except KeyError:
            logging.debug("Fatal Exception")
            raise ParametersRequiredError(_helper.get("help"), _helper) from None
        # logging.debug("formatted data %s", data_block)
        if not data_block.get("args"):
            data_block["args"] = {"timeout": 10}
            logging.debug("Arguments are not present")
        else:
            data_block["args"]["timeout"] = 10
        return data_block

    def _filler(self, config_block, cred_data):
        """
        :param config_block: - 
        :type config_block: -
        :param cred_data: -
        :type cred_data: - 
        :rtype: - 
        """
        result = {}
        for key, value in config_block.items():
            if isinstance(value, dict):
                try:
                    d = self._filler(value, cred_data)
                    result[key] = d
                except KeyError:
                    logging.debug("Fuck it")
                    raise
            else:
                result[key] = value.format(**cred_data)

        return result

    def _handler(self, helper_block):
        """
        :param helper_block: -
        :type helper_block: -
        :rtype: -
        """
        if not helper_block["_verification_protocol"]:
            # noinspection PyUnresolvedReferences
            helper_block[_helper_function] = "http"  # TODO: Fix..?
        return helper_block

    def _required(self, data_block):
        """
        :param data_block: -
        :type data_block: -
        :rtype: -
        """
        _required_params = list()
        for key, value in data_block.items():
            if isinstance(value, dict):
                _required_params.extend(self._required(value))
            else:
                _params = re.findall(r"{(.*?)}", value)
                if len(_params) > 0:
                    _required_params.extend(_params)
        return set(_required_params)
