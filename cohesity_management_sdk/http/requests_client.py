# -*- coding: utf-8 -*-
# Copyright 2021 Cohesity Inc.

import requests

from cachecontrol import CacheControl
from requests.adapters import HTTPAdapter
from requests.packages import urllib3
from requests.packages.urllib3.util.retry import Retry

from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.http.http_client import HttpClient
from cohesity_management_sdk.http.http_method_enum import HttpMethodEnum
from cohesity_management_sdk.http.http_response import HttpResponse


class RequestsClient(HttpClient):

    """An implementation of HttpClient that uses Requests as its HTTP Client

    Attributes:
        timeout (int): The default timeout for all API requests.

    """

    def __init__(self, timeout=60, cache=False, max_retries=None, retry_interval=None):
        """The constructor.

        Args:
            timeout (float): The default global timeout(seconds).

        """
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.timeout = timeout
        self.session = requests.session()

        if max_retries and retry_interval:
            retries = Retry(total=max_retries, backoff_factor=retry_interval)
            self.session.mount('http://', HTTPAdapter(max_retries=retries))
            self.session.mount('https://', HTTPAdapter(max_retries=retries))

        if cache:
            self.session = CacheControl(self.session)

    def execute_as_string(self, request):
        """Execute a given HttpRequest to get a string response back

        Args:
            request (HttpRequest): The given HttpRequest to execute.

        Returns:
            HttpResponse: The response of the HttpRequest.

        """
        self.session.verify = not Configuration.skip_ssl_verification

        response = self.session.request(HttpMethodEnum.to_string(request.http_method),
                                        request.query_url,
                                        headers=request.headers,
                                        params=request.query_parameters,
                                        data=request.parameters,
                                        files=request.files,
                                        timeout=self.timeout)

        return self.convert_response(response, False)

    def execute_as_binary(self, request):
        """Execute a given HttpRequest to get a binary response back

        Args:
            request (HttpRequest): The given HttpRequest to execute.

        Returns:
            HttpResponse: The response of the HttpRequest.

        """
        self.session.verify = not Configuration.skip_ssl_verification

        response = self.session.request(HttpMethodEnum.to_string(request.http_method),
                                        request.query_url,
                                        headers=request.headers,
                                        params=request.query_parameters,
                                        data=request.parameters,
                                        files=request.files,
                                        timeout=self.timeout)

        return self.convert_response(response, True)

    def convert_response(self, response, binary):
        """Converts the Response object of the HttpClient into an
        HttpResponse object.

        Args:
            response (dynamic): The original response object.

        Returns:
            HttpResponse: The converted HttpResponse object.

        """
        if binary:
            return HttpResponse(response.status_code, response.headers, response.content)
        else:
            return HttpResponse(response.status_code, response.headers, response.text)
