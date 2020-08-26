# Copyright 2020 Northern.tech AS
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        https://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from testutils.api.client import ApiClient as _ApiClient

HOST = "mender-tenantadm:8080"
URL_MGMT = "/api/management/v2/tenantadm"

URL_CREATE_ORG_TENANT = "/tenants"
URL_TENANT_STATUS = "/tenants/{id}/status"
URL_TENANT_SECRET = "/secret"


class ManagementApiClient(_ApiClient):
    def __init__(self, host=HOST, scheme="http://"):
        super().__init__(URL_MGMT, host, scheme)
