a = 56

# OK version 🤔 - if/else blocks ❌ 
if a > 0:
    sign = "positive"
else:
    sign = "negative"

# Pythonic way 🐍 - Use a ternary operator ✅
sign = "positive" if (a > 0) else "negative" # parentheses are optional

print(sign)