import pandas as pd
import requests


def lambda_handler(event, context):
    print(f"Looks like pandas is installed, version {pd.__version__}")
    print(f"Looks like requests is installed, version {requests.__version__}")

    return "Hello World"
