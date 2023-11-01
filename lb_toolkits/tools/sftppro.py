# -*- coding:utf-8 -*-
'''
@Project  : lb_toolkits
@File     : sftppro.py
@Modify Time      @Author    @Version
--------------    -------    --------
2022/7/21 17:09      Lee       1.0
@Description
------------------------------------
利用paramiko库，通过sftp方式上传或者下载文件
或者路径下的所有文件
'''
import os
import sys
import datetime
import time
import paramiko
import stat


class sftppro(object):

    def __init__(self, ip=None, port=22,
                 username=None, password=None,
                 PKEY=None, timeout=5*60):
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password
        self.PKEY = PKEY
        self.sftp = None
        self.trans = None
        self.timeout = timeout

        self.connect(timeout)

    def connect(self, timeout=5*60):
        try:
            if self.password is None and self.PKEY is not None:  # 如果没有传入密码，则以秘钥方式登录
                # 指定本地的RSA私钥文件,如果建立密钥对时设置的有密码，password为设定的密码，如无不用指定password参数
                pkey = paramiko.RSAKey.from_private_key_file(self.PKEY)
                # 建立连接
                self.trans = paramiko.Transport((self.ip, self.port))
                self.trans.connect(username=self.username, pkey=pkey)
                # 将sshclient的对象的transport指定为以上的trans
                self.ssh = paramiko.SSHClient()
                self.ssh._transport = self.trans
                # 实例化一个 sftp对象,指定连接的通道
                self.sftp = paramiko.SFTPClient.from_transport(self.trans)
            else:
                # 连接到IP地址
                self.trans = paramiko.Transport((self.ip, self.port))
                # 登录
                self.trans.connect(username=self.username, password=self.password)
                # 建立FTP通道
                self.sftp = paramiko.SFTPClient.from_transport(self.trans)
        except Exception as e:
            raise Exception('连接【%s】失败' %(self.ip))

        if self.sftp is not None :
            self.sftp.sock.settimeout(timeout)

    def close(self):
        '''
        关闭sftp通道
        '''
        if self.sftp is not None :
            self.sftp.close()

        if self.trans is not None :
            self.trans.close()

    def download(self, remotepath, localpath,
                 retry=3,
                 redownload=False,
                 pathdownload=False,
                 okstatus=False):
        '''
        递归方式下载目录下的所有文件
        :param remotepath:
        :param localpath:
        :param retry:
        :param redownload:
        :param pathdownload:
        :param okstatus:
        :return:
        '''



        remotefile = remotepath
        # 判断是否为文件，是文件则下载，否则递归该目录
        if stat.S_ISREG(self.sftp.stat(remotefile).st_mode):
            self._download(remotefile, localpath,
                           retry=retry,
                           okstatus=okstatus,
                           redownload=redownload)
        else:
            # 开始对远程目录进行list，列出所有文件和目录
            fils = self.sftp.listdir_attr(remotepath)

            filecount = len(fils)
            for f in fils:
                try:
                    remotefile = os.path.join(remotepath, f.filename)
                    remotefile = remotefile.replace('\\', '/')
                    if stat.S_ISREG(self.sftp.stat(remotefile).st_mode):
                        self._download(remotefile, localpath,
                                       retry=retry,
                                       okstatus=okstatus,
                                       redownload=redownload,
                                       id = filecount)
                    else:
                        if pathdownload :
                            localpath = os.path.join(localpath, f.filename)
                            if not os.path.isdir(localpath):
                                os.makedirs(localpath)
                            # 暂不轮循下载目录下载的所有文件夹
                            self.DownloadPath(remotefile, localpath,
                                              retry=retry,
                                              okstatus=okstatus,
                                              redownload=redownload,
                                              pathdownload=pathdownload)
                        else:
                            print('%s is file folder, will continue it...' % (remotefile))

                    filecount -= 1
                except BaseException as e :
                    print('下载文件失败【%s】' %(os.path.basename(remotefile)))
                    if os.path.isfile(localpath) :
                        os.remove(localpath)

    def upload(self, localpath, remotepath,
               retry=3,
               reupload=False,
               pathupload=False,
               okstatus=False):
        '''
        通过sftp, 上传文件或者路径下的所有文件
        :param localpath:
        :param remotepath:
        :param retry:
        :param reupload:
        :param pathupload:
        :param okstatus:
        :return:
        '''
        # print('Now, star to upload %s' % (localpath))

        if os.path.isfile(localpath) :
            self._upload(localpath, remotepath,
                         retry=retry,
                         okstatus=okstatus,
                         reupload=reupload)
        else:
            fils = os.listdir(localpath)
            for item in fils :
                localfile = os.path.join(localpath, item)
                remotefile = os.path.join(remotepath, item)

                # 如果是文件，则上传该文件，否则，进入该路径后再次循环搜索文件上传
                if os.path.isfile(localfile):
                    self._upload(localfile, remotepath, okstatus=okstatus, reupload=reupload)
                elif os.path.isdir(localfile):
                    # 推送文件夹，判断远程文件目录是否存在，不存在，则需创建文件夹
                    if pathupload :
                        # 暂不轮循下载目录下载的所有文件夹
                        self.UploadPath(localfile, remotepath, okstatus=okstatus, reupload=reupload, pathupload=pathupload)
                    else:
                        print('%s is file folder, will continue it...' %(localfile))
                else:
                    print('%s is error name...' %(localfile))


    def Exec_cmd(self, command):
        # 执行命令，和传统方法一样
        stdin, stdout, stderr = self.ssh.exec_command(command)
        print(stdout.read().decode())

    def makedirs(self, path):
        '''
        创建远程路径下的文件夹，如果不存在则直接创建，存在则跳过
        :param path:
        :return:
        '''
        try:
            self.sftp.stat(path)
        except BaseException as e:

            filename = os.path.basename(path)
            path = os.path.dirname(path)

            self.makedirs(path)
            try:
                self.sftp.mkdir(os.path.join(path, filename))
                print('创建远程文件夹【%s】成功' %())
            except BaseException as e:
                raise Exception('create remote path ==>> %s error!!!' %(os.path.join(path, filename)))

    def _upload(self, local_filename, remote_path, retry=3, okstatus=False, reupload=False):
        # 判断远程端目录是否存在，如果不存在，则创建
        filename = os.path.basename(local_filename)
        remote_filename = os.path.join(remote_path, filename)
        PathFlag = False
        try:
            self.sftp.stat(remote_path)
        except BaseException as e:
            PathFlag = True
        if PathFlag:  # 远程路径不存在
            try:
                print(self.GetStrTime(), '文件路径不存在，将创建【%s】' % (remote_path))

                # 远程路径不存在，则创建多级目录
                self.makedirs(remote_path)
            except Exception as e:
                print(e)
                print('创建路径失败【%s】' %(remote_path))
                return False

        if os.path.isfile(local_filename):
            try:
                # 将本地文件写入到远程文件
                self.sftp.put(local_filename, remote_filename)
                print('成功上传【%s】' %(remote_filename))
            except Exception as e:
                print('上传失败【%s】' % (remote_filename))
                print(e)

        else:
            print('文件不存在【%s】' %(local_filename))
            return False

        return True

    def UploadPath(self, local_path, remote_path, retry=3, okstatus=False, reupload=False, pathupload=False):
        print('正在上传【%s】' %(local_path))

        fils = os.listdir(local_path)
        for item in fils :
            local_filname = os.path.join(local_path, item)
            remote_filename = os.path.join(remote_path, item)

            # 如果是文件，则上传该文件，否则，进入该路径后再次循环搜索文件上传
            if os.path.isfile(local_filname):
                self._upload(local_filname, remote_path, okstatus=okstatus, reupload=reupload)
            elif os.path.isdir(local_filname):
                # 推送文件夹，判断远程文件目录是否存在，不存在，则需创建文件夹
                if pathupload :
                    # 暂不轮循下载目录下载的所有文件夹
                    self.UploadPath(local_filname, remote_path, okstatus=okstatus, reupload=reupload, pathupload=pathupload)
                else:
                    print('%s is file folder, will continue it...' %(local_filname))
            else:
                print('%s is error name...' %(local_filname))

    def get(self, remotepath, localpath, callback=None, chucksize=1024, prefetch=True):
        '''
        从远程下载数据文件
        :param remotepath:
        :param localpath:
        :param callback:
        :param chucksize:
        :param prefetch:
        :return:
        '''


        continuing = os.path.isfile(localpath)
        if continuing:
            already_downloaded_bytes = os.path.getsize(localpath)
        else:
            already_downloaded_bytes = 0

        file_size = self.sftp.stat(remotepath).st_size

        mode = "ab" if continuing else "wb"

        basename = os.path.basename(localpath).replace('.download','')
        with open(localpath, mode) as writer:
            # 进度条
            from tqdm import tqdm
            with tqdm(
                    total=file_size, unit_scale=True, unit="B", desc=f"正在下载【{basename}】",
                    unit_divisor=chucksize, initial=already_downloaded_bytes
            ) as pbar:
                with self.sftp.open(remotepath, "rb") as reader:
                    if prefetch:
                        reader.prefetch(file_size)

                    size = already_downloaded_bytes
                    reader.seek(size)

                    while True:
                        data = reader.read(chucksize)
                        writer.write(data)
                        size += len(data)
                        if len(data) == 0:
                            break
                        if callback is not None:
                            callback(size, file_size)

                        pbar.update(len(data))

        localsize = os.path.getsize(localpath)
        if localsize != file_size:
            return False
        else:
            return True

    def _download(self, remotefile, localpath, retry=3, okstatus=False, redownload=False, id=1):
        '''
        下载文件，成功下载并生成OK，否则生成ERROR
        :param remotefile: 远程路径 + 文件名
        :param localpath:  本地路径
        :param okstatus: 是否输出OK文件，default：False，不输出OK文件，
                         如果为True，将在文件同级目录下输出《文件名.OK》文件
        :param redownload：如果下载目标已存在，是否重新下载该文件
                            default：False，本地文件已存在，不在重复下载该文件
                            如果为True，将下载并覆盖该文件
        :return:
        '''

        if not os.path.isdir(localpath):
            print('路径不存在，将创建【%s】' % (localpath))
            os.makedirs(localpath)

        filename = os.path.basename(remotefile)
        localfile = os.path.join(localpath, filename)
        tempfile = localfile + '.download'

        # if os.path.isfile(tempfile) and not redownload :
        #     print('[%d]文件已存在，跳过下载【%s】'  %(id, localfile))
        #     return False

        if os.path.isfile(localfile) and not redownload :
            print('[%d]文件已存在，跳过下载【%s】'  %(id, localfile))
            return False
        print('[%d]开始下载【%s】' %(id, localfile))
        for i in range(retry) :

            # 判断远程文件是否是一个文件，是文件则下载该文件，否则返回
            if stat.S_ISREG(self.sftp.stat(remotefile).st_mode):  # remote is file
                try:
                    # 调用get下载远程文件
                    if self.get(remotefile, tempfile) :
                        os.rename(tempfile, localfile)
                    # print('[%d]success to download %s ...' %(id, localfile))

                    if okstatus :
                        okname = localfile + '.OK'
                        self.WriteOK(localfile, okname)

                    return True
                except BaseException as e:
                    print(e)
            else:
                print('远程文件不存在，将跳过下载【%s】' % (remotefile))
                return False

    def DownloadPath(self, remote_path, local_path, retry=3, okstatus=False, redownload=False, pathdownload=False):
        '''
        # 递归方式下载目录下的所有文件
        :param remote_path:
        :param local_path:
        :return:
        '''

        # 开始对远程目录进行list，列出所有文件和目录
        for f in self.sftp.listdir_attr(remote_path):
            remote_filename = os.path.join(remote_path, f.filename)
            # 判断是否为文件，是文件则下载，否则递归该目录
            if stat.S_ISREG(self.sftp.stat(remote_filename).st_mode):

                self._download(remote_filename, local_path,
                               retry = retry,
                               okstatus=okstatus,
                               redownload=redownload)
            else:

                if pathdownload :
                    local_path = os.path.join(local_path, f.filename)
                    if not os.path.isdir(local_path):
                        os.makedirs(local_path)
                    # 暂不轮循下载目录下载的所有文件夹
                    self.DownloadPath(remote_filename, local_path, okstatus=okstatus,
                                      redownload=redownload, pathdownload=pathdownload)
                else:
                    print('%s is file folder, will continue it...' % (remote_filename))

    def JudgeLocalFileExist(self, filename):
        '''
        # 判断文件是否存在,存在则返回True，否则返回False
        :param filename:
        :return:
        '''
        if os.path.isfile(filename):
            print(self.GetStrTime(), '%s is exist, will return True' %(filename))
            return True
        else:
            print(self.GetStrTime(), '%s is not exist, will return False' % (filename))
            return False

    def JudgeRemoteExist(self, remote):
        try:
            self.sftp.stat(remote)

            if stat.S_ISREG(self.sftp.stat(remote).st_mode):
                return 1
            else:
                return 2

        except BaseException as e:
            print('JudgeRemoteExist:%s is not exist, will be return ...' % (remote))
            # print(e)
            return 0

    def JudgeRemotePathExist(self, remote_path):
        # 判断远程目录是否存在，不存在则退出
        try:
            self.sftp.stat(remote_path)
            return True
        except BaseException as e:
            print('JudgeRemotePathExist:%s is not exist, will be return ...' % (remote_path))
            # print(e)
            return False

    def WriteOK(self, s, okname):
        '''
        写OK文件，标识文件下载状态
        :param s: 输出文件内容
        :param okname: OK文件名
        :return:
        '''
        try:
            fp = open(okname, 'w')
            fp.write(self.GetStrTime() + s)
            fp.write('\n')
            fp.close()
        except BaseException as e:
            print('create %s error...' %(okname))
            print(e)

    # 获取实时时间，并做格式化处理
    def GetStrTime(self, s=None):
        if not s is None :
            print(time.strftime('[%Y-%m-%d %H:%M:%S]:',
                                time.localtime(time.time())) + s)

        return time.strftime('[%Y-%m-%d %H:%M:%S]:',
                             time.localtime(time.time()))

    def __del__(self):
        self.close()



