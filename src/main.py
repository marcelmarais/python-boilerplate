from config.env import get_env


def add(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    add(1, 2)
    print(f"This is an example environment variable: {get_env().ENV_VAR_1}")
