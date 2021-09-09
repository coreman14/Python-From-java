class SomethingWentWrong(Exception):
    def __init__(self):
        super().__init__("A custom message would go here")
        
    #You could customize the error message sent back by overriding the default string method
    def __str__(self):
        return "This exception will return this instead of anything useful"


class SomethingWentWrong2(Exception):
    def __init__(self,number,message="Optional parameter containing the default message"):
        #You could pass in a custom error message now and store the variable that caused the error
        self.number = number
        super().__init__(message)
        
    #You could customize the error message sent back by overriding the default string method
    def __str__(self) :
        return f"{self.number} is too small."