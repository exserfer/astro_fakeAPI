import pika
import redis


def prnt(param_vars, name_vars: str = ''):
    print('-')
    print('-----')
    print('----------')
    print(f'[ INFO ] {name_vars} ==> {param_vars}')
    print('----------')
    print('-----')
    print('-')