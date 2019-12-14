import os
import json
import re
class staticTest(object):

    def __init__(self):
        """
        """
        self.key_regexes = self.load_regex()


    def load_regex(self,):
        """
        :rtype : returns the api config data for rest calls
        """
        with open(os.path.join(os.path.dirname(__file__), "../data/api_regexes.json"), 'r') as f:
            regexes = json.loads(f.read())
            return regexes

    def find_a_match(self,key_regexes,input_text):
        """
        :param key_regexes: 
        :type dict:
        :param input_text:
        :type str:
        :rtype : Dict of matched service
        """
        result = {}
        for key, value in key_regexes.items():
            if isinstance(value, dict):
                inner_result = self.find_a_match(value, input_text)
                if(inner_result):
                    result[key] = inner_result
            elif isinstance(value, list):
                found_strings = set()
                for regex in value:
                    a = re.findall(regex,input_text)
                    for i in a:
                        found_strings.add(i)
                if(found_strings):
                    result[key] = found_strings
            else:
                regex = value
                found_strings = set(re.findall(regex,input_text))
                if(found_strings):
                    result[key] = found_strings
        return result
    
    def find(self,key_to_find):
        """
        :rtype : returns dict of matched service 
        """
        match = self.find_a_match(self.key_regexes,key_to_find)
        return match