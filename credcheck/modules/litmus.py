import requests


class Litmus:
    def __init__(self, key, secret, url, file_out):
        self.url = url
        self.key = key
        self.secret = secret
        self.file = file_out

    def check_slack_webhook(self):
        header = {"Content-type: application/json"}
        data = {"text": ""}
        url = self.url
        response = requests.post(url, headers=header, data=data)
        if response.text == "":
            return True, {}
        else:
            return False, {}

    def check_slack_api_token(self):
        slack_test = "https://slack.com/api/auth.test?token=xoxp-{}&pretty=1"
        response = requests.post(slack_test.format(self.key))
        if response.text == "":
            return True, {}
        else:
            return False, {}

    def sauce_labs_username_secret_check(self):
        sauce_lab_test = "https://saucelabs.com/rest/v1/users/USERNAME"
        response = requests.post()
        pass

    def check_facebook_app_secrets(self):
        pass

    def check_facebook_access_token(self):
        pass

    def check_firebase_custom_token_and_api(self):
        """
        Obtain ID token and refresh token from custom token and API key:
            curl -s -XPOST -H 'content-type: application/json' -d '{"custom_token":":custom_token"}' \
            'https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyCustomToken?key=:api_key'
        Exchange ID token for auth token:
            curl -s -XPOST -H 'content-type: application/json' -d '{"idToken":":id_token"}' \
            https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyCustomToken?key=:api_key'
        """
        pass

    def check_github_token(self):
        pass

    def github_client_id_and_secret(self):
        pass

    def check_google_cloud_messaging(self):
        pass

    def check_private_ssh_key(self):
        pass

    def check_twilio_account_token_and_sid(self):
        pass

    def check_twitter_api_secret(self):
        pass

    def check_twitter_bearer_token(self):
        pass

    def deviant_art_secret(self):
        pass

    def check_devient_art_access_token(self):
        pass

    def check_pendo_integration_key(self):
        pass

    def check_sendgrid_api_token(self):
        pass
