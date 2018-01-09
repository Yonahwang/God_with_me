# -*- coding: utf-8 -*-
# !/usr/bin/python

import numpy
import pandas as pand


fe_id = ['subsections_numObjects', '2version0_Catalog', 'len_URLs', 'version0_Actions_JS', '1version0_Catalog', 'XrefSection', '1version0_obj_10_2', '1version0_obj_10_3', '1version0_Encoded_num', '1version0_obj_10_1', '1version0_obj_10_6', '1version0_obj_10_7', '1version0_obj_10_4', '1version0_obj_10_5', '1version0_obj_10_8', '1version0_obj_10_9', 'version0_Events_AA', 'version0_Catalog', 'Xref_errors', '1version0_Xref Streams', 'Javascript_count', 'Linearized', 'version0_elements', 'version0_Elements_EmbeddedFiles', 'version0_obj_average', 'version0_obj_min', 'JS_count', '2version0_elements', '2version0_Events_num', '2version0_Encoded_num', 'version0_Encoded_num', '1version0_elements', '2version0_obj_10_3', '2version0_obj_10_2', '2version0_obj_10_1', '2version0_obj_10_0', '2version0_obj_10_7', '2version0_obj_10_6', '2version0_obj_10_5', '2version0_obj_10_4', '2version0_obj_10_9', '2version0_obj_10_8', 'comments', 'numEncodedStreams', '1version0_Elements_EmbeddedFiles', 'meta_cration_len', '1version0_Events_num', 'Metadata', '1version0_Events_Names', 'version0_Decoding Errors', '1version0_Vulns', '2version0_Objects_JS_num', '2version0_Events_AA', '1version0_obj_10_0', '1version0_Decoding Errors', '2version0_Actions_JS', '2version0_Events_Names', 'meta_creator_len', 'meta_producer_len', 'version0_Info', '1version0_Compressd_obj', 'stream_num', '2version0_Actions_num', 'Encrypted', 'version0_Actions_num', '2version0_Compressd_obj', 'Binary', 'subsections_size', 'header_offset', 'trailer_num', 'version0_Events_Names', 'version0_Compressd_obj', '1version0_Actions_num', '2version0_obj_min', '1version0_Object Streams', '2version0_Decoding Errors', 'font_count', 'Xref_bytesPerFisId', 'version0_Events_num', '2version0_Info', 'Versions_num', 'subsections_entries', 'version0_stream_min_0', 'version0_stream_min_1', '2version0_Object Streams', 'version0_obj_10_0', '1version0_obj_average', '1version0_Objects_JS_num', '2version0_Xref Streams', '1version0_Streams', '1version0_Events_AA', 'error', 'Xref_offset', 'JS_MODULE', 'version-1', 'version0_obj_10_8', 'version0_obj_10_9', 'version0_obj_10_6', 'version0_obj_10_7', 'version0_obj_10_4', 'version0_obj_10_5', 'version0_obj_10_2', 'version0_obj_10_3', 'subsections_errors', 'version0_obj_10_1', '2version0_Actions_javascript', 'object_num', 'subsections_firstObject', 'file_size', '2version0_Elements_EmbeddedFiles', '2version0_Streams', '1version0_stream_min_0', '1version0_stream_min_1', '1version0_Actions_javascript', 'version0_Vulns', 'version0_Object Streams', '1version0_obj_min', 'subsections_offset', '1version0_Info', 'Xref_stream', '2version0_Vulns', '2version0_obj_average', 'version0_Objects_JS_num', '2version0_stream_min_1', '2version0_stream_min_0', 'meta_author_len', 'update', 'version0_Xref Streams', '1version0_Actions_JS', 'version-2', 'version0_Streams', 'Metadata_len', 'Xref_size', 'version0_Actions_javascript']
num = range(len(fe_id))
table = {'num':num,'fe_name':fe_id}
frame = pand.DataFrame(table)
del frame['num']
frame.to_csv('fe_name.csv')
df = pand.read_csv('fe_name.csv',index_col=0)
#print str(frame)
#numpy.savetxt("fe_name.txt",numpy.array(frame))
print str(df.index)


'''name1= ['a','b','c','d','e','f']
test1 = [0, 0, 0, 1, 1, 1]
predict1 = [0, 1, 0, 1, 0, 0]
name =[]
test = []
predict = []

for i in range(len(predict1)):
    if test1[i] != predict1[i]:
        name.append(name1[i])
        test.append(test1[i])
        predict.append(predict1[i])

table = {'name':name,'test':test,'predint':predict}

frame = pand.DataFrame(table)


print frame'''



