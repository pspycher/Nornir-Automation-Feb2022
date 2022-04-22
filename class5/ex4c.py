from nornir import InitNornir
from nornir_utils.plugins.tasks.data import load_yaml
from nornir_jinja2.plugins.tasks import template_file


ACL_TEMPLATE = """{%- for acl, rules in acls.items() %}
  {%- for entry in rules %}

set firewall family inet filter {{ acl }} term {{ entry['term_name'] }} from protocol {{ entry['protocol'] }}
set firewall family inet filter {{ acl }} term {{ entry['term_name'] }} from destination-port {{ entry['destination_port'] }}
set firewall family inet filter {{ acl }} term {{ entry['term_name'] }} from destination-address {{ entry['destination_address'] }}
set firewall family inet filter {{ acl }} term {{ entry['term_name'] }} then {{ entry['state'] }}
  {%- endfor %}
{%- endfor %}"""  # noqa


def junos_acl(task):
    in_yaml = task.run(task=load_yaml, file="acl.yaml")
    in_yaml = in_yaml[0].result
    multi_result = task.run(task=template_file, template="acl.j2", path=".", acls=in_yaml)

    task.host["acl"] = multi_result.result

    print()
    print("#" * 80, end="")
    print(task.host["acl"])
    print("#" * 80)
    print()


def main():
    nr = InitNornir(config_file="config.yaml")
    nr = nr.filter(name="srx2")
    nr.run(task=junos_acl)


if __name__ == "__main__":
    main()
