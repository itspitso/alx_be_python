def safe_divide(numerator, denominator):
    try:
        float(numerator) / float(denominator)
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please use numeric values only."
    else:
        return float(numerator) / float(denominator)
        
    
    
