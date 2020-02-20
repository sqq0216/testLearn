import requests
import unittest
from unittest import TestCase

class IasApiTest(TestCase):
    def setUp(self):
        self.baseUrl = "https://api.trustedservices.intel.com/sgx/dev"
        print("开始测试，baseUrl=",self.baseUrl)

    def tearDown(self):
        print("测试结束")

    def test_get(self):
        apiUrl = "/attestation/v3/sigrl/{gid}"
        url = self.baseUrl + apiUrl
        print("当前访问url为",url)
        r = requests.get(url)
        r_json = r.json()
        print(r_json)

if __name__ == "__main__":
    unittest.main(verbosity=2)

