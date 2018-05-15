import base64
import json
import urllib.request
import hashlib

id_and_key = b'fb5f4050b276:001ba694fafeca4c85124c9f336b3ee026c12ac186'
basic_auth_string = 'Basic ' + str(base64.b64encode(id_and_key),'utf-8')
headers = { 'Authorization': basic_auth_string }

request = urllib.request.Request(
    'https://api.backblazeb2.com/b2api/v1/b2_authorize_account',
    headers = headers
    )
response = urllib.request.urlopen(request)
response_data = json.loads(response.read().decode('utf-8'))
response.close()

# print 'auth token:', response_data['authorizationToken']
# print 'api url:', response_data['apiUrl']
# print 'download url:', response_data['downloadUrl']
# print 'minimum part size:', response_data['minimumPartSize']

'''
auth token: 2_20150812013854_a01f0090bb8e38e6c332e1cd_40106700acdf06d4fd4053d4ff4072da4e71c154_acct
api url: https://api001.backblaze.com
download url: https://f700.backblazeb2.com
minimum part size: 100000000
'''

api_url = response_data['apiUrl']
account_authorization_token = response_data['authorizationToken']
bucket_id = 'ff5b75ffc41025106b120716'
print(json.dumps({                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               'bucketId' : bucket_id }))
request = urllib.request.Request(
	str('%s/b2api/v1/b2_get_upload_url' % api_url),
    json.dumps({ 'bucketId' : bucket_id }).encode('utf-8'),
	headers = { 'Authorization': account_authorization_token }
	)
response = urllib.request.urlopen(request)
response_data = json.loads(response.read().decode('utf-8'))
response.close()

'''
{
    "bucketId" : "4a48fe8875c6214145260818",
    "uploadUrl" : "https://pod-000-1005-03.backblaze.com/b2api/v1/b2_upload_file?cvt=c001_v0001005_t0027&bucket=4a48fe8875c6214145260818",
    "authorizationToken" : "2_20151009170037_f504a0f39a0f4e657337e624_9754dde94359bd7b8f1445c8f4cc1a231a33f714_upld"
}
'''

upload_url = response_data['uploadUrl']
upload_authorization_token = response_data['authorizationToken']

import os
import time
filedir = 'F:/PDFdata/VirusShare_PDF_20170404'
for parent, dirnames, filenames in os.walk(filedir):
    for filename in filenames:
        if filename.find('ok_') == -1:
            old_filepath = os.path.join(parent, filename)

            f = open(old_filepath,'rb')
            file_data = f.read()
            f.close()
            file_name = filename
            content_type = "text/plain"

            sha1_of_file_data = hashlib.sha1(file_data).hexdigest()

            headers = {
                'Authorization' : upload_authorization_token,
                'X-Bz-File-Name' :  file_name,
                'Content-Type' : content_type,
                'X-Bz-Content-Sha1' : sha1_of_file_data
                }
            request = urllib.request.Request(upload_url, file_data, headers)

            try:
                response = urllib.request.urlopen(request)
            except:
                print("error")
                time.sleep(50)
                continue
            response_data = json.loads(response.read().decode('utf-8'))
            response.close()
            print(old_filepath,'success')

            new_filename = 'ok_' + filename
            new_filepath = os.path.join(parent, new_filename)
            os.rename(old_filepath, new_filepath)
'''
{
    "fileId" : "4_h4a48fe8875c6214145260818_f000000000000472a_d20140104_m032022_c001_v0000123_t0104",
    "fileName" : "typing_test.txt",
    "accountId" : "d522aa47a10f",
    "bucketId" : "4a48fe8875c6214145260818",
    "contentLength" : 46,
    "contentSha1" : "bae5ed658ab3546aee12f23f36392f35dba1ebdd",
    "contentType" : "text/plain",
    "fileInfo" : {
       "author" : "unknown"
    }
}
'''
