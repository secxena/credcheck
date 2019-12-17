import argparse
from credcheck.core.cred_check_utils import CredUtils
from credcheck.core.cred_check_active import DynamicTest
import logging

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    choices = CredUtils()._services
    # subparsers = parser.add_subparsers(help='commands', dest="category")
    # dump_parser = subparsers.add_parser('dump_by_service', help='Data Dump Mgmt Commands')
    parser.add_argument(
        "-s",
        "--service",
        default="all",
        nargs="?",
        choices=choices,
        help="Allowed values are " + ", ".join(choices),
        type=str,
        metavar="",
    )
    parser.add_argument("-i", "--id", help="Please provide a key to test it out")
    parser.add_argument("-k", "--key", help="Please provide a key to test it out")
    parser.add_argument("-t", "--token", help="Please provide a key to test it out")
    parser.add_argument("-u", "--url", help="Provide complete URL if needed")
    parser.add_argument(
        "-f", "--file", action="store_true", help="Provide credential file path"
    )
    # parser.add_argument("-l", '--list', action="store_true", help="list supported formats")
    # parser.add_argument('-j', '--json', action="store_true", help="outputs everything in json format")

    # args = parser.parse_args()
    # key = args.key
    # secret = args.secret
    # url = args.url
    # file_path = args.file
    # list_dork = args.list
    # out_json = args.json
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
    dt = DynamicTest()
    dt.check_it(args.service, credDict)
