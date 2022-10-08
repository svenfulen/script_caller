
# script_caller

This is a Flask application that can be used to execute Python scripts from an API endpoint.
Once this is running on a server, you can put your Python scripts in the "callable_scripts" folder to make them available from the API.

API Usage:

To make calls to this API, you will need to do the following:

1. Build a URL in the following format: `http://<hostname>/runscript/<script name>`

	`<hostname>` will be the IP address or DNS name of your API server
	`<script name>` will be the full filename of your script, including the file extension

2. Include the header to allow JSON data: 
	`{"Content-Type" : "application/json"}`

3. To pass arguments to the script, send the arguments as JSON data in the request body, in the following format:
```
	{
	  "--filename": "test",
	  "--text": "Hello World",
	  "single_arg": ""
	}
```
