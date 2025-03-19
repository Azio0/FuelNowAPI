# FuelNowAPI

**FuelNowAPI** is an open-source project that provides access to publicly available data released by the UK's major fuel providers, specifically for Great Britain. The data can be accessed via a URL pull request and is updated daily at midnight. 

Additionally there is a filter framework allowing developers to filter down specific data requests by input critera such as, postcode, city, incode and etc. This framework enables easy modification and addition to allow for custom-built filters to be on your self-hosted FNA server.

## Features

- Access fuel data for the United Kingdom
- Daily updates at midnight
- Self-Updating Environment (Linux)
- Filters Framework
- IP Rate Limited Requests
- Easy to run server

## Requirements

- Python 3
- Redis server

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Azio0/FuelNowAPI.git
   cd FuelNowAPI
   ```
2. Install Python and PIP:
   ```bash
   sudo apt-get install python3
   sudo apt-get install python3-pip
   ```
4. Install the required Python Packages:
   ```bash
   pip install -r requirements.txt
   ```
5. Install the redis-server:
   ```bash
   sudo apt-get install redis-server
   ```

## Usage

1. To start the redis server:
   ```
   cd source/utils/redis
   nohup redis-server &
   ```

3. To start the web server:
   ```
   cd source/webapp
   nohup python3 server.py &
   ```

## Contributing

This is an open-source project, and contributions are welcome. Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the terms of the MIT license.

## Contact

For any questions or suggestions, please open an issue or contact the project maintainers.

## Donations

This project is intended to be open-source and free from cost to use. I love coding, setting a target and accomplishing it, sometimes by using pre-existing technology or creating an original approach to a problem. It excites me and gives me a sense of purpose, but it is not always easy to find the time or motivation to keep pushing forward. Donations are welcome if you wish to give something towards the work I do, but it is completely optional and is certainly not a requirement.

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/azio0)
