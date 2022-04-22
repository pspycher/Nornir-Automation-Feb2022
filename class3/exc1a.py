from nornir import InitNornir
from pprint import pprint
 

def main():
    nr = InitNornir()
    # nr = InitNornir(config_file ="config.yaml") 
    print()
    print(nr.inventory.hosts["arista3"].data)
    # Cast as a dict() to make output more readable
    pprint(dict(nr.inventory.hosts["arista3"].items()))
    print()


if __name__ == "__main__":
    main()

