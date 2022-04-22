from nornir import InitNornir
from nornir.core.filter import F
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_command


def main():
    nr = InitNornir(config_file="config.yaml")
    ios_filt = F(groups__contains="ios")
    eos_filt = F(groups__contains="eos")
    # Test with wrong PW: nr.inventory.hosts["cisco3"].password = 'bogus'
    # nr.inventory.hosts["cisco3"].password = 'bogus'
    nr = nr.filter(ios_filt | eos_filt)
    my_results = nr.run(task=netmiko_send_command, command_string="show ip int brief")
    print_result(my_results)


if __name__ == "__main__":
    main()
