from fastapi import FastAPI, Response
import math

app = FastAPI()

def get_lcm(a: int, b: int) -> int:
    if hasattr(math, "lcm"):
        return math.lcm(a, b)
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // math.gcd(a, b)

@app.get("/christina_kim_1233_gmail_com")
async def christina_kim_1233_gmail_com(x: str = None, y: str = None):
    # 1. Missing parameters
    if x is None or y is None:
        return Response(content="NaN", media_type="text/plain")
    
    # 2. Strip whitespace and leading '+' signs
    clean_x = x.strip().lstrip("+")
    clean_y = y.strip().lstrip("+")

    # 3. Check for non-negative integers
    if not (clean_x.isdecimal() and clean_y.isdecimal()):
        return Response(content="NaN", media_type="text/plain")

    # 4. Calculate
    try:
        val_x, val_y = int(clean_x), int(clean_y)
        result = get_lcm(val_x, val_y)
        return Response(content=str(result), media_type="text/plain")
    except Exception:
        return Response(content="NaN", media_type="text/plain")
