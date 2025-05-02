# hltv-api

This project offers an easy-to-use interface for extracting [HLTV](https://www.hltv.org/) data through web scraping, providing a RESTful API built with FastAPI. With this tool, developers can easily pull HLTV data into their applications, websites, or data analysis workflows.

Please be aware that the deployed version is intended for testing purposes and includes rate limiting. For more flexibility and customization, it's recommended to host the service on your own cloud infrastructure.

### API Swagger
https://hltv-json-api.fly.dev/

### Running Locally
Install [Poetry](https://python-poetry.org/docs/#installation), if you haven't already.

````bash
# Clone the repository:
$ git clone https://github.com/eupeutro/hltv-api.git

# Navigate to the project folder:
$ cd hltv-api

# Instantiate a Poetry virtual environment:
$ poetry shell

# Install the dependencies:
$ poetry install --no-root

# Start the API server:
$ python app/main.py

# Access the API local page:
$ open http://localhost:8000/
````

### Running via Docker

````bash
# Clone the repository:
$ git clone https://github.com/eupeutro/hltv-api.git

# Navigate to the project folder:
$ cd hltv-api

# Build the Docker image:
$ docker build -t hltv-api . 

# Instantiate the Docker container:
$ docker run -d -p 8000:8000 hltv-api

# Access the API local page
$ open http://localhost:8000/
````

### Environment Variables

| Variable                  | Description                                               | Default      |
|---------------------------|-----------------------------------------------------------|--------------|
| `RATE_LIMITING_ENABLE`    | Enable rate limiting feature for API calls                | `false`      |
| `RATE_LIMITING_FREQUENCY` | Delay allowed between each API call. See [slowapi](https://slowapi.readthedocs.io/en/latest/) for more | `2/3seconds` |

To set the environment variables, create a .env file in the root of your project with the following content:
````python
RATE_LIMITING_ENABLE=false
RATE_LIMITING_FREQUENCY=2/3seconds
````
