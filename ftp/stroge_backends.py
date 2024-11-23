import os
from ftplib import FTP, error_perm
from django.conf import settings
from django.core.files.storage import Storage
from django.utils.deconstruct import deconstructible
import logging
from django.apps import apps


@deconstructible
class FtpStorage(Storage):

    def __init__(self, *args, **kwargs):
        self.ftp_host = settings.FTP_HOST
        self.ftp_user = settings.FTP_USER
        self.ftp_password = settings.FTP_PASSWORD
        self.ftp_directory = settings.FTP_DIRECTORY
    
    def _open(self, name, mode="rb"):
         raise NotImplementedError("This storage backend does not support file reading.")
    
    def _save(self, name, content):
        logger = logging.getLogger("TESTING")

        ftp = FTP(self.ftp_host)
        ftp.login(self.ftp_user, self.ftp_password)

        logger.debug('Ftp connected successfully')
        ftp.cwd(self.ftp_directory)

        # try:
        #     ImageUpload = apps.get_model('ftp', 'Ftp')
        #     image_instance = ImageUpload.objects.first()
        #     if image_instance:
        #         local_image_path = image_instance.get_local_image_path()
        #         if local_image_path:
        #             local_image_path = settings.MEDIA_URL
        #             file_name = os.path.basename(local_image_path)
        # except AttributeError as a:
        #     logger.debug(f'--------------------------error : {a}')
                
        # with open(local_image_path, 'rb') as f:
        #     ftp.storbinary(f'STOR {file_name}', f)


        with ftp.storbinary(f"STOR {name}", content, 1024):
            pass

        ftp.quit()
        # os.remove(local_image_path)
        return name

    def exists(self, name):
        return False
    
    def url(self, name):
        return f"ftp://{self.ftp_host}/{self.ftp_derectory}/{name}"