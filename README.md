String API 3
Api to count chars in srting using external API and save result in one of three types of fies (json, csv, xml or response as simple text).

required packages:
1. Flask (pip install flask)
2. requests (pip install requests)

Endpoints:

1. /checkstring (POST)
	
	Endpoint accepts string and return or save response in file 

	Arguments: 
		1. "string" (type: string)
		2. "responseType" (type: int)
	
	Example of usage

	request -> http://127.0.0.1:5001/checkstring?string=Szymon&responseType=1
	
	response -> "upper_case: 1, lower_case: 5, numbers: 0, special_characters: 0}