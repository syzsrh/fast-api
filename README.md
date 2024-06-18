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

3. Run the command: `pytest`

### Running Container

1. While the Docker container is running, access the container's shell using Docker Exec (on the desktop app) or through the terminal using the command `docker exec -it <container-name-or-id> bash`, the container id can be obtained with the command `docker ls`.

2. Run the command `pytest`.

## Answers

1. Add OAuth2 (username/hashed password) and token-based authentication so users receive a JWT, which is included in their requests. The server verifies the token to authenticate the user when making API requests. The analytics pipeline could authenticate itself with its unique token the same way when accessing the API.

2. If the files also need to be connected to the user (for example they can upload multiple files and those files would be associated with their account) I would use a relational database like PostgreSQL. PostgreSQL allows for organization of data into structured tables (for example a User and a Files table, where each file in the Files table has a foreign key from the User table). This makes it easiear to manage the relationship between users and their uploaded files, and you maintain data integrity as each uploaded file stored is associated with a unique account identifier. Also PostgreSQL is robust, reliable and scalable.

3. Text can be stored as TEXT data type and embeddings can be stored as VECTORS by using a vector database extension for PostgreSQL, so we could have a separate Text_Embedding table that, if need be, can be associated with the User table through a foreign key. If the database does not support the data you want to store, in this case embeddings, it might be better to use a separate vector database like Pinecone. But in the case of PostgreSQl, it has a few performant vector extension options that allow for embeddings/vectors to be stored and searchable so you wouldn't have to deal with the overhead of managing multiple databases.

4. When creating a column to store embedding vectors, it's essential to specify the dimensionality of the vectors. This specification allows databases like PostgreSQL to index the table efficiently for search operations. So, when selecting embedding models, it's important to choose those with a consistent vector size.

5. Visual Studio Code, Dark (Visual Studio - C/C++) for the eyes...

6. I've used a lot of Python libraries that have made my work a lot easier but personally, I appreciate BeautifulSoup and Markdownify a lot because I read a lot of blogs and I prefer to scroll rather than click buttons (next post!) plus the formatting of every blog varies. So, I just scrape the tagged posts of a new blog and save it into a formatted .epub file I can read on my e-reader. The increased quality of life is remarkable. (And Selenium for the anti-bot blogs...)

7. GPT-4 can "see" and "hear" with image and audio inputs, so I think GPT-4.5/5 might upgrade its multimodal capabilities by supporting video input, plus Gemini already offers support for video input.