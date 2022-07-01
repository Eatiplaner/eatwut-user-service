"""
 Password Regex:
    at least one uppercase letter
    one lowercase letter
    one number
    one special character include: @$!%*?&
"""
passwordRegex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]*$"
