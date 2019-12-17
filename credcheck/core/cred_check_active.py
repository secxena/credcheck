import json

from credcheck.core.cred_check_utils import CredUtils
from credcheck.modules.http_client import CheckAPI


class DynamicTest:
    def __init__(self):
        """
        
        """
        self.cred_utils = CredUtils()

    def check_it(self, target, input_data):
        """
        :param target: name of the service to test
        :type target: str
        :param input_data: Credential variables ie key, Id, Token, Url
        :rtype : json - returned response from api call
        """
        config_block = self.cred_utils.data[target]
        if config_block:
            # config = self.cred_utils._required(config_block['config'])
            try:
                config = self.cred_utils._format(config_block, input_data)
            except Exception as e:
                print(e)
                return
            method = self.cred_utils._httpmethod[config["request-type"]]
            if config.get("basic"):
                if len(config.get("args")) > 1:
                    respo = CheckAPI(
                        verify_ssl=False,
                        username=config["basic"]["username"],
                        password=config["basic"]["password"],
                    )._auth(config["url"], method, **config["args"])
                else:
                    respo = CheckAPI(
                        verify_ssl=False,
                        username=config["basic"]["username"],
                        password=config["basic"]["password"],
                    )._auth(config["url"], method)
            if config.get("args"):
                respo = CheckAPI(verify_ssl=False)._auth(
                    config["url"], method, **config["args"]
                )
            else:
                respo = CheckAPI(verify_ssl=False)._auth(config["url"], method)
            print(json.dumps(respo, indent=4))

    def run(self):
        """

        """
        for key, value in self.cred_utils.data.items():
            pass  # print(key)


# dt = dynamicTest()
# dt.checkIt('pagerduty')
# print(yolo.find('AIzaIHQ2SLTSHFLUVQQAaaaaaaaaaaaaaaaaaaa'))
