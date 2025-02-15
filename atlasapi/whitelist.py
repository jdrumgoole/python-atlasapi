# Copyright (c) 2019 Matthew Monteleone
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from ipaddress import IPv4Address, IPv4Network
from pprint import pprint


class WhitelistEntry(object):
    def __init__(self, cidrBlock: str = None, comment: str = None, ipAddress: str = None, links: list = None):
        """
        For a single whitelist entry. Contains a bit of helper intelligence for ip addresses.

        :param cidrBlock:
        :param comment:
        :param ipAddress:
        :param links:
        """
        self.links = links
        self.ipAddress = ipAddress
        self.comment = comment
        self.cidrBlock = cidrBlock
        try:
            self.cidrBlockObj: IPv4Network = IPv4Network(self.cidrBlock)
        except Exception:
            self.cidrBlockObj = None
        try:
            self.ipAddressObj: IPv4Address = IPv4Address(self.ipAddress)
        except Exception:
            self.ipAddressObj = None

    @classmethod
    def fill_from_dict(cls, data_dict: dict):
        """
        Fills the object from the standard Atlas API dictionary.
        :param data_dict:
        :return:
        """
        cidrBlock = data_dict.get('cidrBlock', None)
        comment = data_dict.get('comment', None)
        ipAddress = data_dict.get('ipAddress', None)
        links = data_dict.get('links', None)

        return cls(cidrBlock=cidrBlock, comment=comment, ipAddress=ipAddress, links=links)

    def as_dict(self) -> dict:
        """
        Dumps obj as a json valid dict.
        :return:
        """
        orig_dict = self.__dict__
        orig_dict.__delitem__('ipAddressObj')
        orig_dict.__delitem__('cidrBlockObj')
        return orig_dict
