from fastapi import FastAPI, Response
from typing import Any
import math

app = FastAPI()

def lcm(x: Any, y: Any) -> str:
    try:
        if x is None or y is None:
            return "NaN"
        
        if not (str(x).isdigit() and str(y).isdigit()):
            return "NaN"

        val_x, val_y = int(x), int(y)

        if val_x == 0 or val_y == 0:
            return "0" 

        result = abs(val_x * val_y) // math.gcd(val_x, val_y)
        return str(result)

    except Exception:
        return "NaN"

@app.get("/christina_kim_1233_gmail_com")
async def christina_kim_1233_gmail_com(x: str = None, y: str = None):
    result_text = lcm(x, y)
    return Response(content=result_text, media_type="text/plain")
