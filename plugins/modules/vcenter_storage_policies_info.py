#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2021, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# template: header.j2
# This module is autogenerated using the ansible.content_builder.
# See: https://github.com/ansible-community/ansible.content_builder


DOCUMENTATION = r"""
module: vcenter_storage_policies_info
short_description: Returns information about at most 1024 visible (subject to permission
    checks) storage solicies availabe in vCenter
description: Returns information about at most 1024 visible (subject to permission
    checks) storage solicies availabe in vCenter. These storage policies can be used
    for provisioning virtual machines or disks.
options:
    policies:
        description:
        - Identifiers of storage policies that can match the filter.
        - If unset or empty, storage policies with any identifiers match the filter.
        - When clients pass a value of this structure as a parameter, the field must
            contain the id of resources returned by M(vmware.vmware_rest.vcenter_storage_policies).
        elements: str
        type: list
    session_timeout:
        description:
        - 'Timeout settings for client session. '
        - 'The maximal number of seconds for the whole operation including connection
            establishment, request sending and response. '
        - The default value is 300s.
        type: float
        version_added: 2.1.0
    vcenter_hostname:
        description:
        - The hostname or IP address of the vSphere vCenter
        - If the value is not specified in the task, the value of environment variable
            C(VMWARE_HOST) will be used instead.
        required: true
        type: str
    vcenter_password:
        description:
        - The vSphere vCenter password
        - If the value is not specified in the task, the value of environment variable
            C(VMWARE_PASSWORD) will be used instead.
        required: true
        type: str
    vcenter_rest_log_file:
        description:
        - 'You can use this optional parameter to set the location of a log file. '
        - 'This file will be used to record the HTTP REST interaction. '
        - 'The file will be stored on the host that run the module. '
        - 'If the value is not specified in the task, the value of '
        - environment variable C(VMWARE_REST_LOG_FILE) will be used instead.
        type: str
    vcenter_username:
        description:
        - The vSphere vCenter username
        - If the value is not specified in the task, the value of environment variable
            C(VMWARE_USER) will be used instead.
        required: true
        type: str
    vcenter_validate_certs:
        default: true
        description:
        - Allows connection when SSL certificates are not valid. Set to C(false) when
            certificates are not trusted.
        - If the value is not specified in the task, the value of environment variable
            C(VMWARE_VALIDATE_CERTS) will be used instead.
        type: bool
author:
- Ansible Cloud Team (@ansible-collections)
version_added: 0.3.0
requirements:
- vSphere 7.0.3 or greater
- python >= 3.6
- aiohttp
notes:
- Tested on vSphere 7.0.3
"""

EXAMPLES = r"""
- name: List existing storage policies
  vmware.vmware_rest.vcenter_storage_policies_info:
  register: storage_policies
"""

RETURN = r"""
# content generated by the update_return_section callback# task: List existing storage policies
value:
  description: List existing storage policies
  returned: On success
  sample:
  - description: Management Storage policy used for VMC large cluster
    name: Management Storage Policy - Large
    policy: cd8f7c94-3e11-67fc-17f5-4e96d91a5beb
  - description: Allow the datastore to determine the best placement strategy for
      storage objects
    name: VVol No Requirements Policy
    policy: f4e5bade-15a2-4805-bf8e-52318c4ce443
  - description: Management Storage policy used for smaller VMC Stretched Cluster
      configuration.
    name: Management Storage Policy - Stretched Lite
    policy: d109de24-c966-428f-8da2-d281e6671e35
  - description: Sample storage policy for VMware's VM and virtual disk encryption
    name: VM Encryption Policy
    policy: 4d5f673c-536f-11e6-beb8-9e71128cae77
  - description: Management Storage policy used for encrypting VM
    name: Management Storage policy - Encryption
    policy: b1263970-8662-69e2-adc6-fa8ae01abecc
  - description: Management Storage policy used for VMC single node cluster
    name: Management Storage Policy - Single Node
    policy: a9423670-7455-11e8-adc0-fa7ae01bbebc
  - description: Storage policy used as default for Host-local PMem datastores
    name: Host-local PMem Default Storage Policy
    policy: c268da1b-b343-49f7-a468-b1deeb7078e0
  - description: Storage policy used as default for vSAN datastores
    name: vSAN Default Storage Policy
    policy: aa6d5a82-1c88-45da-85d3-3d74b91a5bad
  - description: Management Storage policy used for VMC regular cluster
    name: Management Storage Policy - Regular
    policy: bb7e6b13-2d99-46eb-96e4-3d85c91a5bde
  - description: Management Storage policy used for VMC regular cluster which requires
      THIN provisioning
    name: Management Storage policy - Thin
    policy: b6423670-8552-66e8-adc1-fa6ae01abeac
  - description: Management Storage policy used for VMC stretched cluster
    name: Management Storage Policy - Stretched
    policy: f31f2442-8247-4517-87c2-8d69d7a6c696
  type: list
"""

# This structure describes the format of the data expected by the end-points
PAYLOAD_FORMAT = {
    "list": {"query": {"policies": "policies"}, "body": {}, "path": {}}
}  # pylint: disable=line-too-long

from ansible.module_utils.basic import env_fallback

try:
    from ansible_collections.cloud.common.plugins.module_utils.turbo.exceptions import (
        EmbeddedModuleFailure,
    )
    from ansible_collections.cloud.common.plugins.module_utils.turbo.module import (
        AnsibleTurboModule as AnsibleModule,
    )

    AnsibleModule.collection_name = "vmware.vmware_rest"
except ImportError:
    from ansible.module_utils.basic import AnsibleModule
from ansible_collections.vmware.vmware_rest.plugins.module_utils.vmware_rest import (
    gen_args,
    open_session,
    session_timeout,
    update_changed_flag,
)


def prepare_argument_spec():
    argument_spec = {
        "vcenter_hostname": dict(
            type="str",
            required=True,
            fallback=(env_fallback, ["VMWARE_HOST"]),
        ),
        "vcenter_username": dict(
            type="str",
            required=True,
            fallback=(env_fallback, ["VMWARE_USER"]),
        ),
        "vcenter_password": dict(
            type="str",
            required=True,
            no_log=True,
            fallback=(env_fallback, ["VMWARE_PASSWORD"]),
        ),
        "vcenter_validate_certs": dict(
            type="bool",
            required=False,
            default=True,
            fallback=(env_fallback, ["VMWARE_VALIDATE_CERTS"]),
        ),
        "vcenter_rest_log_file": dict(
            type="str",
            required=False,
            fallback=(env_fallback, ["VMWARE_REST_LOG_FILE"]),
        ),
        "session_timeout": dict(
            type="float",
            required=False,
            fallback=(env_fallback, ["VMWARE_SESSION_TIMEOUT"]),
        ),
    }

    argument_spec["policies"] = {"type": "list", "elements": "str"}

    return argument_spec


async def main():
    required_if = list([])

    module_args = prepare_argument_spec()
    module = AnsibleModule(
        argument_spec=module_args, required_if=required_if, supports_check_mode=True
    )
    if not module.params["vcenter_hostname"]:
        module.fail_json("vcenter_hostname cannot be empty")
    if not module.params["vcenter_username"]:
        module.fail_json("vcenter_username cannot be empty")
    if not module.params["vcenter_password"]:
        module.fail_json("vcenter_password cannot be empty")
    try:
        session = await open_session(
            vcenter_hostname=module.params["vcenter_hostname"],
            vcenter_username=module.params["vcenter_username"],
            vcenter_password=module.params["vcenter_password"],
            validate_certs=module.params["vcenter_validate_certs"],
            log_file=module.params["vcenter_rest_log_file"],
        )
    except EmbeddedModuleFailure as err:
        module.fail_json(err.get_message())
    result = await entry_point(module, session)
    module.exit_json(**result)


# template: info_list_and_get_module.j2
def build_url(params):
    import yarl

    _in_query_parameters = PAYLOAD_FORMAT["list"]["query"].keys()
    return yarl.URL(
        ("https://{vcenter_hostname}" "/api/vcenter/storage/policies").format(**params)
        + gen_args(params, _in_query_parameters),
        encoded=True,
    )


async def entry_point(module, session):
    url = build_url(module.params)
    async with session.get(url, **session_timeout(module.params)) as resp:
        _json = await resp.json()

        if "value" not in _json:  # 7.0.2+
            _json = {"value": _json}

        return await update_changed_flag(_json, resp.status, "get")


if __name__ == "__main__":
    import asyncio

    current_loop = asyncio.get_event_loop_policy().get_event_loop()
    current_loop.run_until_complete(main())
