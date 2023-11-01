# -*- coding:utf-8 -*-
'''
@Project  : lb_toolkits

@File     : ftppro.py

@Modify Time : 2022/8/11 15:34

@Author : Lee

@Version : 1.0

@Description :
通过ftplib进行ftp文件上传和下载
'''
import ftplib 
import os
import datetime
import re

class ftppro():

    def __init__(self, ip, user=None, password=None, remotepath=None, localpath=None):

        self.host = ip
        self.user = user
        self.pwd = str(password)
        self.remotePath = remotepath
        self.localPath = localpath
        self.ftp = None

        self.connect()

    def connect(self, timeout=5*60):

        connflag = False
        try:
            self.ftp.voidcmd("NOOP")
            connflag = True
        #     print("Connection already open.")
        except BaseException as e:
            connflag = False
            # errorInfo = str(e).split(None, 1)[0]
        #     print(e)
        #     print("Connection already closed.")

        try:
            if connflag :
                return self.ftp
            else:
                ftp = ftplib.FTP(self.host, timeout=timeout)
                ftp.encoding = 'utf'

                if self.user is None or self.pwd is None :
                    ftp.login('anonymous', '')
                else:
                    ftp.login(self.user, self.pwd)
                self.ftp = ftp

                return ftp
        except BaseException as e:
            raise Exception('connect error"%s"' % self.host)
            # ftp.quit()
            return None

    def downloadFile(self, remoteFile, localPath, blocksize = 1 * 1024, skip=False, cover=False):
        '''
        通过ftp下载文件

        Parameters
        ----------
        remoteFile: str
        localPath : str
        blocksize
        skip : bool
            是否跳过下载文件，TRUE则不下载文件，直接返回文件名，否则，下载该文件

        cover : bool
            文件存在，
            如果cover为TRUE，则删除原文件后重新下载,
            如果cover为FALSE，就跳过该文件下载

        Returns
        -------

        '''

        localFile = os.path.join(localPath, os.path.basename(remoteFile))

        if skip :
            return localFile

        # 文件存在，如果skip为TRUE，就跳过该文件下载，
        # 如果skip为FALSE，则删除原文件后重新下载
        if os.path.isfile(localFile):
            if cover :
                os.remove(localFile)
                print('文件已存在，删除该文件后重新下载【%s】' %(localFile))
            else:
                print('文件已存在，跳过下载该文件【%s】' %(localFile))
                return localFile


        tempfile = localFile + '.download'

        self.__makedir(localPath)

        try:
            ftp = self.connect()
            if ftp is None :
                return None
            self._download(ftp, tempfile, remoteFile, blocksize=blocksize)

            # with open(tempfile, "wb") as fp:
            #     ftp.retrbinary('RETR %s' % remoteFile, fp.write, blocksize=block_size)
            if os.path.isfile(localFile):
                os.remove(localFile)

            if os.path.isfile(tempfile) :
                os.rename(tempfile, localFile)
            return localFile
        except BaseException as e:
            print(e)
            print('下载文件失败【%s】' %(localFile))
            print('再尝试一次下载文件【%s】' %(localFile))
            try:
                ftp = self.connect()
                if ftp is None :
                    return None
                self._download(ftp, tempfile, remoteFile, blocksize=blocksize)
                if os.path.isfile(tempfile) :
                    os.rename(tempfile, localFile)
                return localFile
            except BaseException as e:
                print(e)
                print('再次下载文件失败【%s】' %(localFile))
            return None

    def uploadFile(self, localfile, remotePath, blocksize = 1 * 1024):
        '''
        上传文件
        【注意】：本功能未经过测试验证可行性

        Parameters
        ----------
        localfile: str
            本地存储路径
        remotePath: str
            远程上传路径
        remoteFile: str
            远程文件
        block_size: int
            上传块大小，单位：byte

        Returns
        -------

        '''

        ftp = self.connect()
        if ftp is None :
            return False

        ftp.voidcmd('TYPE I')
        basename = os.path.basename(localfile)
        remoteFile = os.path.join(remotePath, basename)

        remotePath = remotePath.replace('\\','/')
        self.__makeRemoteDir(remotePath)

        self._upload(ftp, localfile, remoteFile, blocksize)


    def _upload(self, ftp, localfile, remotefile, blocksize):

        basename = os.path.basename(localfile)

        localsize = os.path.getsize(localfile)
        if self._judge_remotefile_exist(self, ftp, remotefile):
            remotesize = ftp.size(remotefile)
        else:
            remotesize = 0

        try:

            with open(localfile, 'rb') as fp:
                from tqdm import tqdm
                with tqdm(
                        total=localsize, unit="B", unit_scale=True, desc=f"正在上传【{basename}】",
                        unit_divisor=blocksize, initial=remotesize
                ) as pbar:
                    datasock, esize = ftp.ntransfercmd("STOR %s" % remotefile, remotesize)
                    fp.seek(remotesize)

                    def callback(block):
                        datasock.sendall(block)
                        pbar.update(len(block))

                    while True:
                        data = fp.read(blocksize)
                        if not data:
                            break

                        callback(data)
                        remotesize += len(data)

                    if remotesize != localsize :
                        print('上传文件失败【%s】' %(remotefile))
                try:
                    import ssl
                except ImportError:
                    _SSLSocket = None
                else:
                    _SSLSocket = ssl.SSLSocket

                datasock.close()
                # shutdown ssl layer
                # if _SSLSocket is not None and isinstance(conn, _SSLSocket):
                #     conn.unwrap()

            # with open(localfile, "rb") as fp:
            #     fp.seek(remotesize)
            #     ftp.storbinary("STOR %s" % remotePath, fp, block_size)
        except BaseException as e:
            print(e)
        ftp.voidresp()

    def setRemotePath(self,remotePath):
        self.remotePath = remotePath

    def setLocalPath(self,localPath):
        self.localPath = localPath

    def __makedir(self,dirname):
        if not os.path.isdir(dirname):
            os.makedirs(dirname)

    def list_dir_regex(self, regexStr):
        ftp = self.connect()
        try:
            ftp.cwd(self.remotePath)
            fileList = ftp.nlst()

            p = re.compile(regexStr)
            matchedFiles = []
            for file in fileList:
                match = p.search(file)
                if match:
                    matchedFiles.append(match.string)

            return matchedFiles
        except BaseException as e:
            print(e)


    def listdir(self, dirname, pattern=None):
        ftp = self.connect()
        try:
            ftp.cwd(dirname)
            if pattern is None :
                fileList = ftp.nlst()
            else:
                fileList = ftp.nlst(pattern)
            return fileList

        except BaseException as e:
            # print(e)
            return []

    def __makeRemoteDir(self, dirPath):
        ftp = self.connect()

        dirs = dirPath.split('/')

        for dirName in dirs:
            if dirName:
                try:
                    if dirName == 'home':
                        ftp.cwd( '/' + dirName)
                    else:
                        ftp.cwd(dirName)
                except Exception as e:
                    ftp.mkd(dirName)
                    ftp.cwd(dirName)


    def _download(self, ftp, tempfile, remoteFile, blocksize=1024, rest=None):
        ''' 下载文件 '''
        ftp.voidcmd('TYPE I')
        basename = os.path.basename(remoteFile)
        def callback(block):
            fp.write(block)
            pbar.update(len(block))

        continuing = os.path.isfile(tempfile)
        if continuing:
            already_downloaded_bytes = os.path.getsize(tempfile)
        else:
            already_downloaded_bytes = 0

        remotesize = ftp.size(remoteFile)

        mode = "ab" if continuing else "wb"

        with open(tempfile, mode) as fp:
            from tqdm import tqdm
            with tqdm(
                    total=remotesize, unit="B", unit_scale=True, desc=f"正在下载【{basename}】",
                    unit_divisor=blocksize, initial=already_downloaded_bytes
            ) as pbar:

                with ftp.transfercmd('RETR %s' % (remoteFile), already_downloaded_bytes) as conn:
                    while 1:
                        data = conn.recv(blocksize)
                        if not data:
                            break
                        callback(data)

            try:
                import ssl
            except ImportError:
                _SSLSocket = None
            else:
                _SSLSocket = ssl.SSLSocket
            # shutdown ssl layer
            if _SSLSocket is not None and isinstance(conn, _SSLSocket):
                conn.unwrap()

        return ftp.voidresp()


    def _judge_remotefile_exist(self, ftp, remotefile):

        try:
            if remotefile in ftp.nlst(os.path.dirname(remotefile)):
                return True
            else:
                return False
        except BaseException as e:
            return False


    def close(self, ftp):
        if ftp is not None:
            ftp.quit()
            ftp = None


    def __del__(self):
        if self.ftp is not None:
            self.ftp.quit()
            self.ftp = None
