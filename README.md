## Updating the OpenAI API Key

To utilize the OpenAI services in this project, you must provide your own API key.

1. Obtain an API key from OpenAI by registering or logging into your account on their platform.

2. Open the `constants.py` file located in `/app/` folder of this project.

3. Find the line that reads `API_KEY = 'YOUR_KEY'`.

4. Replace `'YOUR_KEY'` with your actual OpenAI API key. Ensure that the key is enclosed in single quotes.

5. Save your changes to the `constants.py` file.

## Build

1. Navigate to the folder where the Dockerfile is located, it should be in `/fast-api`.

2. Run the following command to build and start the container `docker-compose up --build`.

3. Once the build process completes successfully, navigate to the provided link to access the FastAPI application.

## Running Tests



### Locally

1. (Optional) [Set](https://python.land/virtual-environments/virtualenv) up and activate your virtual environment.

2. Run the following command to install necessary packages: `pip install -r requirements.txt`

3. (Optional) Run the command: `pytest`

### Running Container

1. While the Docker container is running, access the container's shell using Docker Exec (on the desktop app) or through the terminal using the command `docker exec -it <container-name-or-id> bash`, the container id can be obtained with the command `docker ls`.

2. (Optional) Run the command `pytest`.