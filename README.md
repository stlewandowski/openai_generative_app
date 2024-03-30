# OpenAI Generative App

This application uses the OpenAI API to connect with DallE and generate images. It retrieves the content from OpenAI and stores them in Azure. It also uses the Azure API to retrieve the images and display them in the app.
- Additional modules beyond DallE are planned.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
- Gunicorn is used to run the application in the Docker container.
- Waitress is used to run the application in the development environment.
- Both of these are included in the requirements.txt file.

### Prerequisites

- Python 3.10
- Docker

### Installation

1. Clone the repository
```bash
git clone https://github.com/stlewandowski/openai_generative_app.git
```

2. Navigate to the project directory
```bash
cd openai_generative_app
```

3. Build the Docker image
```bash
docker build -t openai_generative_app:latest .
```

4. Run the Docker container, also specifying the environment variables.
```bash
docker run -p 8000:8000 --env-file dev.env -d openai_generative_app:latest
```

The application should now be running at `http://localhost:8000`.

## Usage

The application uses a Postgres database. The 'dev.env.example' file contains the environment variables needed to connect to the database. Rename the file to 'dev.env' and update the values as needed. This can then be used when starting the container. 
- Azure blob storage is presently used, but AWS and GCP (whose relevant environment variables are in the dev.env.example) can also be used.

## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details


