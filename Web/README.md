# AI-Toxic-Content-Classification-in-Django

[![python3.5](https://img.shields.io/badge/python-3.5-blue.svg)](https://www.python.org/downloads/)
[![python3.6](https://img.shields.io/badge/python-3.6-brightgreen.svg)](https://www.python.org/downloads/)
[![python3.7](https://img.shields.io/badge/python-3.7-orange.svg)](https://www.python.org/downloads/)
[![django3.0](https://img.shields.io/badge/django-3.0.0-green.svg)](https://www.djangoproject.com/download/)


## Table of Contents

- [Install](#install)
- [Usage](#usage)
- [Issue](#Issue)
- [Others](#Others)
- [License](#license)

## Install

- GPU required!!!  
I use AWS P2.xlarge with GPU K80 for this application.
You can use either local machine or server.

- Image  
Deep Learning AMI (Ubuntu 16.04) Version 26.0.(Local machine ignore)

- Upload file
You can download files though the [link](https://drive.google.com/open?id=1VNvt9su2-pZ0EN8JsXl24WjgYjqgsKGz).
Then use `scp` upload the file on the server or use local machine on the root dictionary (AI-Toxic-Content-Classification-in-Django/...)
    ```
    en_core_web_lg-2.2.5.zip #unzip this file
    quora_dict.txt
    my_model.h5
    scp -i <amazon_key> <local_file_position> ubuntu@<public_DNS_IPv4>:<local_file_position>
    # public_DNS_IPv4 can find in your AWS instance dashboard
    ```
- Install Keras and Tensorflow GPU   
Please install Keras-gpu and Tensorflow-gpu follow the official instruction.

- Install other package  
I assume you already have your own local virtual environment.  
    ```
    pip install -r requirements.txt
    python manage.py makemigrations  # Option
    python manage.py migrate # Option
    python manage.py collectstatic # Option
    python manage.py runserver 0.0.0.0:8000
    ```

## Usage

- Run application
Access the web page though this link: http://127.0.0.1:8000/

## Issue

If you have questions or issues, please feel free to tell us.

## Others

- Admin Account
``` 
python manage.py createsuperuser

username: ranxiaolang
email: YOUR EMAIL  
password: ranxiaolang  
```
Access the web page though this link: http://127.0.0.1:8000/admin 

## License

[MIT](LICENSE) ©
