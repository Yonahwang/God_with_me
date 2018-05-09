#!/usr/bin/python
# -*- coding: utf-8 -*-

print "The story begins..."

import base64

import json

import urllib2



# id_and_key = 'hexAccountId_value:accountKey_value'

id_and_key = '' # NEED to fill

basic_auth_string = 'Basic ' + base64.b64encode(id_and_key)

headers = { 'Authorization': basic_auth_string }



request = urllib2.Request(

        'https://api.backblazeb2.com/b2api/v1/b2_authorize_account',

        headers = headers

)

response = urllib2.urlopen(request)

response_data = json.loads(response.read())

response.close()



print 'auth token:', response_data['authorizationToken']

print 'api url:', response_data['apiUrl']

print 'download url:', response_data['downloadUrl']

print 'minimum part size:', response_data['minimumPartSize']



api_url = response_data['apiUrl']  # Provided by b2_authorize_account

account_authorization_token = response_data['authorizationToken']  # Provided by b2_authorize_account



while start_file_name != "":
    print "request_num:", request_num
    print "start_file_name:", start_file_name
    bucket_id = "" # The ID of the bucket you are querying
    request = urllib2.Request(
        '%s/b2api/v1/b2_list_file_names' % api_url,
        json.dumps({ 'bucketId':bucket_id, 'startFileName':start_file_name, 'maxFileCount':1000}),
        headers = { 'Authorization': account_authorization_token }
        )
    response = urllib2.urlopen(request)
    response_data = json.loads(response.read())

    for response_data['file'] in response_data['files']:
        print "sampleFile",file_num,response_data['file']['fileName']
        file_num += 1
    start_file_name = response_data['nextFileName']
    print
    request_num += 1
response.close()
print "The story ends."