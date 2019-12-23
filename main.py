import argparse
from credcheck.core.cred_check_utils import CredUtils
from credcheck.core.cred_check_active import DynamicTest
from pyfiglet import figlet_format
import logging

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    choices = CredUtils()._services
    parser.add_argument(
        "-s",
        "--service",
        nargs="?",
        choices=choices,
        help="Allowed values are " + ", ".join(choices),
        type=str,
        metavar="",
        required=True
    )
    parser.add_argument("-i", "--id", help="Please provide a key to test it out")
    parser.add_argument("-k", "--key", help="Please provide a key to test it out")
    parser.add_argument("-t", "--token", help="Please provide a key to test it out")
    parser.add_argument("-u", "--url", help="Provide complete URL if needed")
    parser.add_argument(
        "-f", "--file", action="store_true", help="Provide credential file path"
    )
  
    args = parser.parse_args()
    credDict = dict()
    if args.id:
        credDict["ID"] = args.id
    if args.key:
        credDict["KEY"] = args.key
    if args.token:
        credDict["TOKEN"] = args.token
    if args.url:
        credDict["URL"] = args.token
    if args.file:
        credDict["FILE"] = args.file
    logging.info("Options Provided: \n\t %s", credDict)
    print('\n\n')
    print(figlet_format('CredCheck', font='basic'))
    dt = DynamicTest()
    dt.check_it(args.service, credDict)
