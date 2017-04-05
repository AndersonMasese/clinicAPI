"""
In this program, I have demonstrated the use of GET and POST over the API http://placekitten.com/ 
I obtained this knowledge from codecademy.com 
However, I have modified the program to demonstrate the new skill that I have acquired in using Request,urlopen,urllib2
cheers!!!
"""

from urllib2 import Request, urlopen, URLError

request = Request('http://placekitten.com/')

try:
	response = urlopen(request)#demonstrating GET
	kittens = response.read()
	print (kittens[559:1000])
    print (response.status_code)#prints the status code of the query passed

    """Now trying to post data into the placekitten.com API:"""
    my_data={'name':'anderson','age':'22'}
    new_object=response.post('http://www.placekitten.com/',my_data)#demonstrating POST

except URLError, e:
    print 'No kittez. Got an error code:', e

    
  