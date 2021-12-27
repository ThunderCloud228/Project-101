import os
import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):
            relative_path = os.path.relpath("./", file_from)
            dropbox_path = os.path.join(file_to, relative_path)
            with open(relative_path, 'rb') as f:
                dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))


def main():
    access_token = 'sl.A--YDHkLsBeqs8h5gYPG--QmngaTysG50_L2WsbANGTnTI--ar_CRJOKglBHKnVBitP7rz0c6J1m14kMCXHSRXcEUJMgQNpSUxNf02pKK1dmrx-iDKOMHGQSX6IeipZE_RY3Ii4'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer: ")
    file_to = input("Enter the full path to upload the file to the dropbox: ")

    transferData.upload_file(file_from, file_to)
    print("The file has been uploaded")


main()

