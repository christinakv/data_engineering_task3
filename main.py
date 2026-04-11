from fastapi import FastAPI, Response
from typing import Any
import math

app = FastAPI()

def lcm(x: Any, y: Any) -> str:
    try:
        if not (str(x).isdigit() and str(y).isdigit()):
            return "NaN"

        x, y = int(x), int(y)

        if x == 0 or y == 0:
            return 0

        result = abs(x * y) // math.gcd(x, y)
        return str(result)

    except(ValueError, ZeroDivisionError, TypeError, AttributeError):
        return "NaN"

@app.get("/christina_kim_1233_gmail_com")
async def christina_kim_1233_gmail_com(x: str=None, y: str=None):
    result = lcm(x, y)
    return Response(content=result, media_type="text/plain")

