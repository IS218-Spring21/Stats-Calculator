class BasicOperations:
    @staticmethod
    def addition(x, y):
        result = float(x) + float(y)
        return result

    @staticmethod
    def subtraction(x, y):
        result = float(y) - float(x)
        return result

    @staticmethod
    def multiplication(x, y):
        result = y * x
        return result

    @staticmethod
    def division(x, y):
        result = float(y) / float(x)
        return result

    @staticmethod
    def square(x):
        result = x ** 2
        return result

    @staticmethod
    def squareRoot(x):
        if x < 0:
            print("Cannot output imaginary result, please enter a positive number for x")
        else:
            result = x ** .5
            return result
