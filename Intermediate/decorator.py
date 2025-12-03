from functools import wraps


def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before executing the function")
        result = func(*args, **kwargs)
        print("After executing the function")
        return result

    return wrapper


@decorator
def say_hello():
    print("Hello")


if __name__ == "__main__":
    say_hello()


def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat(3)
def hi():
    print("Hi")


hi()
