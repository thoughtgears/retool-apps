# Retool Management app

## Prerequisites

To start off you need to create a resource in you admin space that uses the OpenAPI spec of the Retool API. You will need to create an API key as well in
the settings and add it to the configuration variables and call it `self_api_key`. These two resources will be used across the app to manage the Retool spaces.

- **Retool API - Admin:** A OpenAPI resource name `Retool API - Admin` that points to the Retool API.
  - **Specification URL:** `https://api.retool.com/api/v2/spec`
  - **Headers:** `Content-Type: application/json`
  - **Authentication**
    - **Type:** Bearer Token
    - **Bearer Token:** `{{ environment.variables.self_api_key }}`
- **Retool DB:** You will need to create a tabled called `retool_configuration`
  - **Columns:**
    - `id` - autoincrement number primary key
    - `space_id` - Text
    - `space_name` - Text
    - `space_domain` - Text
    - `retool_api_resource_id` - Text

## Installation

* Choose `create` in the app window in Retool
* Choose `From JSON/ZIP` in the dropdown
* Set a name for your application and upload the zip or json file.

