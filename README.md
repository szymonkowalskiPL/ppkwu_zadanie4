# PPKWU zadanie 4
## API string

Api to count chars in given string using external API and convert types of response type.

## Required packages:
1. Flask (```pip install flask```)
2. requests (``` pip install requests ```)
3. json (built-in python)
4. re (built-in python)

## Endpoints:

**1. /checkstring (POST)**
	
Endpoint accepts 3 arguments and return response in one of file formats 

## Arguments: 
1. "string" (type: string)
2. "returnType" (type: string)
3. "downloadType" (type: string)

## Response types:
1. "txt"
2. "json"
3. "xml"
4. "csv" (delimiter ;)

## Example of usage
**txt**

	http://127.0.0.1:8001/checkstring?string=Szymon&returnType=txt&downloadType=txt

response 
```
Upper case: 1
Lower case: 5
Numbers: 0
Special characters: 0
```

**csv**

	http://127.0.0.1:5001/checkstring?string=Szymon&returnType=txt&downloadType=csv

response 
```
1;5;0;0
```



**2. /convertstring (POST)**
	
Endpoint accepts 2 arguments and return response in one of file formats 
