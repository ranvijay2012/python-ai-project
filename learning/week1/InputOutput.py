class MyCustomError(Exception):
    def __init__(self, message, error_code):
        super().__init__(message)
        self.message = message
        self.error_code = error_code

    def __str__(self):
        return f"{self.message} (Error Code: {self.error_code})"

# err = MyCustomError("Invalid operation", 400)
# print(err)

 

def divide(a, b):
    if b == 0:
        raise MyCustomError("Division by zero is not allowed", "NOT_ALLOWED")
    return a / b

divide(10, 0)