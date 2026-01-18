<html>
    <head></head>
    <body>
        <h2># JSONPlaceholder REST API Test Automation</h2>
        <h3>🚀 Overview</h3>
This project provides a modular and reusable test automation framework for validating REST APIs.<br\>
It uses:
Python requests for API calls
Pytest for test execution and reporting
Custom API client (Api_Client_Base) for consistent request handling
Config-driven setup for base URLs, headers, and payloads
YAML/JSON data files for test input management

📂 Project Structure
|-- json_placeholder_automation/
    |-- config/
        |-- config.yaml
    |-- tests/
        |-- conftest.py
        |-- test_posts.py
        |-- __init__.py
    |-- test_data/
        |-- json_data.yaml
    |-- utils/
        |-- api_client_base.py
        |-- config_reader.py
        |-- read_json_data.py
        |-- __init__.py

    </body>
</html>
