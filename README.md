# Retool apps

A collection of apps built with [Retool](https://retool.com/) that I want to share with the community. Most of these apps are built for personal use and are not
meant to be production-ready. Feel free to use them as a reference or starting point for your own apps.

## Apps

#### Retool multi space management

[Retool space management](./apps/retool-management/README.md)

This app allows you to manage multiple Retool spaces from a single interface. You can view all your spaces, see and manage space configuration, configure new
spaces. This app is useful if you have multiple Retool spaces and want to manage them from a single interface.

## Setup

In order to run these apps, you will need to run the `app.py` file with the input of the app you want to run. For example, to run the Retool space management
app, you would run:

```bash
python app.py --app retool-management
```

For this to work properly you will need to have the following environment variables set:

- `PG_PASSWORD`: The password for the Retool Postgres database
- `PG_HOST`: The host for the Retool Postgres database

You can set these in a `.env` file in the root of the project.

Example `.env` file:

```shell
PG_PASSWORD=abcd1234
PG_HOST=somethingsomething.retooldb.com
```


