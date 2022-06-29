"""
 Password Regex:
    at least one uppercase letter
    one lowercase letter
    one number
    and one special character
"""
passwordRegex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]$"
