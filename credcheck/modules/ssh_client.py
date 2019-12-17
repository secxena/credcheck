import base64
import paramiko


class SSHClient:
    def __init__(self):
        pass

    def ssh_connect(self):
        key = paramiko.RSAKey(data=base64.b64decode(b"AAA..."))
        client = paramiko.SSHClient()
        client.get_host_keys().add("ssh.example.com", "ssh-rsa", key)
        client.connect("ssh.example.com", username="strongbad", password="thecheat")
