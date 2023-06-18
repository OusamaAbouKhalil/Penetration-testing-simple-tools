
import paramiko
import sys
import getpass
import logging

class SSH_Connect(object):
    def __init__(self,ip,port,username,password):
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password
        self.ssh = None
        self.sftp = None
        self.chan = None
        self.transport = None
        self.timeout = 10
        self.bufsize = 1024
        self.logfile = 'ssh.log'
        self.logger = logging.getLogger('SSH_Connect')
        self.logger.setLevel(logging.DEBUG)
        self.fh = logging.FileHandler(self.logfile)
        self.fh.setLevel(logging.DEBUG)
        self.ch = logging.StreamHandler()
        self.ch.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.fh.setFormatter(self.formatter)
        self.ch.setFormatter(self.formatter)
        self.logger.addHandler(self.fh)
        self.logger.addHandler(self.ch)

    def connect(self):
        try:
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh.connect(self.ip,self.port,self.username,self.password,timeout=self.timeout)
            self.logger.info('SSH connect to %s:%s success' % (self.ip,self.port))
        except Exception as e:
            self.logger.error('SSH connect to %s:%s failed' % (self.ip,self.port))
            self.logger.error(e)
            sys.exit(1)

    def sftp_connect(self):
        try:
            self.transport = paramiko.Transport((self.ip,self.port))
            self.transport.connect(username=self.username,password=self.password)
            self.sftp = paramiko.SFTPClient.from_transport(self.transport)
            self.logger.info('SFTP connect to %s:%s success' % (self.ip,self.port))
        except Exception as e:
            self.logger.error('SFTP connect to %s:%s failed' % (self.ip,self.port))
            self.logger.error(e)
            sys.exit(1)

    def ssh_exec_cmd(self,cmd):
        try:
            stdin,stdout,stderr = self.ssh.exec_command(cmd)
            self.logger.info('Exec command: %s' % cmd)
            self.logger.info('Exec result: %s' % stdout.read())
        except Exception as e:
            self.logger.error('Exec command: %s failed' % cmd)
            self.logger.error(e)
            sys.exit(1)

def ssh_exec_cmd_timeout(self,cmd,timeout):
    try:
        stdin,stdout,stderr = self.ssh.exec_command(cmd)
        self.logger.info('Exec command: %s' % cmd)
        self.logger.info('Exec result: %s' % stdout.read())
    except Exception as e:
        self.logger.error('Exec command: %s failed' % cmd)
        self.logger.error(e)
        sys.exit(1)

def ssh_exec_cmd_get_result(self,cmd):
    try:
        stdin,stdout,stderr = self.ssh.exec_command(cmd)
        self.logger.info('Exec command: %s' % cmd)
        self.logger.info('Exec result: %s' % stdout.read())
        return stdout.read()
    except Exception as e:
        self.logger.error('Exec command: %s failed' % cmd)
        self.logger.error(e)
        sys.exit(1)

def ssh_exec_cmd_get_result_timeout(self,cmd,timeout):
    try:
        stdin,stdout,stderr = self.ssh.exec_command(cmd,timeout=timeout)
        self.logger.info('Exec command: %s' % cmd)
        self.logger.info('Exec result: %s' % stdout.read())
        return stdout.read()
    except Exception as e:
        self.logger.error('Exec command: %s failed' % cmd)
        self.logger.error(e)
        sys.exit(1)




if __name__ == '__main__':
   #take ip port username password from user input
    ip = raw_input('Please input the ip address: ')
    port = raw_input('Please input the port: ')
    username = raw_input('Please input the username: ')
    password = getpass.getpass('Please input the password: ')
    ssh = SSH_Connect(ip,port,username,password)
    ssh.connect()
    ssh.ssh_exec_cmd('ls -l')
    ssh.sftp_connect()
    ssh.ssh.close()
    ssh.sftp.close()
    ssh.transport.close()