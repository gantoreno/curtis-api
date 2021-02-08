<div align="center">
    <img src="assets/logo.svg" width="300" height="300"></img>
</div>

# Curtis: The server

![Python application](https://github.com/gantoreno/curtis-api/workflows/Python%20application/badge.svg) ![License](https://img.shields.io/github/license/gantoreno/curtis-server)

Files for [Curtis](https://github.com/gantoreno/curtis-engine)' public REST API.

This server will contain a series of endpoints in order to perform ECG-related stuff, mostly analysis and diagnosis over some given patient's info. Built with [tiangolo](https://github.com/tiangolo)'s [FastAPI](https://fastapi.tiangolo.com/) library.

## Usage

First, clone the repo:

```sh
$ git clone https://github.com/gantoreno/curtis-server.git
$ cd curtis-server
```

Now, follow the steps to run the server in your preferred way.

### With virtual environments

Create a virtual environment named `env` with `venv`, and activate it:

```sh
$ python -m venv env
$ source venv/bin/activate
```

Now, install the required packages listed on `requirements.txt`:

```sh
(env) $ pip install -r requirements.txt
```

Finally, run the app with `uvicorn`:

```sh
(env) $ uvicorn app.main:app
```

### With Docker

In your terminal:

```sh
$ docker-compose up
```

This will create a Docker image and container named `curtis-server`. The container will be available at [http://0.0.0.0:8000](http://0.0.0.0:8000).

### Testing

With the virtual environment active, run the tests with [`pytest`](https://docs.pytest.org/en/stable/):

```sh
(env) $ pytest
```

### Docs

The Curtis server has its own auto-generated documentation since FastAPI uses [Swagger](https://swagger.io/) for this type of tasks. Run the application and head to the application's URL followed by the `/docs` route.

### License

This project is licensed under the [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html) license.
