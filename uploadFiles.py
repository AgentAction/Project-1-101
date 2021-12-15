import dropbox
from dropbox.files import WritteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A-P1uJLl4JXI6nyd-rmGMpUQbSRj-1oB4i7xZVbA_AK-BpUe2YBCNn8jRUV_aaXIlMSBO4de1z2-Ec6OcT8Pk_-wxSQm1lNjMXvuBSyWi1__YUcAyXiOd0kQVH6X5HGCMR7IBg0'
    transferData = TransferData(access_token)
    file_from = input("Enter the file path to transfer - ")
    file_to = input("Enter the full path for uploading - ")
    transferData.upload_file(file_from, file_to)
    print("The file has been moved!")


main()
