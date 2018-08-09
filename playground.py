# list = [3, 'string1', 23, 14.0, 'string2', 49, 64, 70]
# for x in list:
#     if not isinstance(x, int):
#         continue
#     if not x % 7:
#         print('found an integer divisible by seven: %d' % x)
#         break
# 
# Exceptions
# 
# class EmptyFileError(Exception):
#     pass
# 
# filenames = ['myfile1', 'nonExistent', 'emptyFile', 'myfile2']
# for file in filenames:
#     try:
#         f = open(file, 'r')
#         line = f.readline()
#         if line =="":
#             f.close()
#             raise EmptyFileError('%s: is empty:' % file)
#     except IOError as error:
#         print('%s: could not be opened: %s' % (file, error.strerror))
#     except EmptyFileError as error:
#         print(error)
#     else:
#         print('%s: %s' % (file, f.readline()))
#     finally:
#         print('Done processing', file)
# 
# filename = 'myfile.txt'
# with open(filename, 'r') as f:
#     for line in f:
#         print(line)
# 