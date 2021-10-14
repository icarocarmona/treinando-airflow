import fire
import os

env = os.getenv('ENV')


def teste():
    print(f"Teste do ambiente: {env}")


if __name__ == '__main__':
    fire.Fire()
