def isPalindrome(self, x: int) -> bool:
  ''' Parameters: x, int
      Output: boolean '''
  #converting int to str
        num2str = str(x)
    #creating empty string to be used in conditional
        newStr = ""
      # loop to create new string which will be the x in reverse
        for i in reversed(num2str):
            newStr += i
      #comparing x to reverse of x
        if num2str == newStr:
            return True
        else:
            return False
   
