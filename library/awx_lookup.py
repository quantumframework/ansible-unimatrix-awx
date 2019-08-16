from ansible.module_utils.basic import AnsibleModule
from queen.ext.awx.ansible import LookupModule


def main():
    module = LookupModule()
    module.handle()


if __name__ == '__main__':
    main()

