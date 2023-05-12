"""for some reason v1 wasnt working so i had to remake it and turn it into a function"""

def formatter(symbol,text):
    sides = symbol * 3
    formatted_text = f"{sides}{text}{sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}{text}{top_bottom}"