import paramiko
from paramiko import SSHClient

# Store Variables
localPath = '/Users/germangonzalez/Documents/Repositorios/python-projects/upload-sftp/test.txt'
remotePath = '/sftp/test.txt'

# Configure Client
client = SSHClient()
client.set_missing_host_key_policy(paramiko.client.AutoAddPolicy)
client.connect('localhost', 23, 'demo', 'demo')

# Execute SFTP Commands
sftp = client.open_sftp()
sftp.put(localPath, remotePath)
