# Curtis Server: The public API

![Python application](https://github.com/gantoreno/curtis-api/workflows/Python%20application/badge.svg)

Server files for [Curtis](https://github.com/gantoreno/curtis-engine)' public REST API.

This server will contain a series of endpoints in order to perform ECG-related stuff, mostly analysis and diagnosis over some given patient's info. Built with [tiangolo](https://github.com/tiangolo)'s [FastAPI](https://fastapi.tiangolo.com/) library.

## Usage

First, clone the repo:

```sh
$ git clone https://github.com/gantoreno/curtis-server.git
$ cd curtis-server
```

Next, create a virtual environment named `env` with `venv`, and activate it:

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

### Testing

With the virtual environment active, run the tests with [`pytest`](https://docs.pytest.org/en/stable/):

```sh
(env) $ pytest
```

### Docs

The Curtis server has its own auto-generated documentation since FastAPI uses [Swagger](https://swagger.io/) for this type of tasks. Run the application and head to the application's URL followed by the `/docs` route.

### License

This project is licensed under the [MIT](https://es.wikipedia.org/wiki/Licencia_MIT) license.
