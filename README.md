<html>
    <head></head>
    <body>
        <h2># JSONPlaceholder REST API Test Automation</h2>
        <h3>🚀 Overview</h3>
This project provides a modular and reusable test automation framework for validating REST APIs.</br>
It uses:</br>
Python requests for API calls</br>
Pytest for test execution and reporting</br>
Custom API client (Api_Client_Base) for consistent request handling</br>
Config-driven setup for base URLs, headers, and payloads</br>
YAML/JSON data files for test input management</br>

📂 Project Structure</br>
|-- json_placeholder_automation/</br>
    |-- config/</br>
        |-- config.yaml</br>
    |-- tests/</br>
        |-- conftest.py</br>
        |-- test_posts.py</br>
        |-- __init__.py</br>
    |-- test_data/</br>
        |-- json_data.yaml</br>
    |-- utils/</br>
        |-- api_client_base.py</br>
        |-- config_reader.py</br>
        |-- read_json_data.py</br>
        |-- __init__.py</br>
    </body>
</html>
