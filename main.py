from fastapi import FastAPI, Request, Response
import math

app = FastAPI()

# Declaring both with and without the slash prevents 307 Redirects
@app.get("/christina_kim_1233_gmail_com")
@app.get("/christina_kim_1233_gmail_com/")
async def calculate_lcm(request: Request):
    
    # 1. Extract raw parameters directly from the URL
    x_str = request.query_params.get("x")
    y_str = request.query_params.get("y")

    # 2. Check for missing parameters
    if x_str is None or y_str is None:
        return Response(content="NaN", media_type="text/plain")

    # 3. .isdigit() strictly ensures only numbers 0-9 exist.
    # This automatically fails negative numbers, floats, letters, or hidden spaces.
    if not (x_str.isdigit() and y_str.isdigit()):
        return Response(content="NaN", media_type="text/plain")

    # 4. Calculate LCM
    try:
        x_val = int(x_str)
        y_val = int(y_str)

        if x_val == 0 or y_val == 0:
            ans = 0
        else:
            # Python natively supports arbitrarily large integers. 
            # Using integer floor division (//) prevents it from ever converting to a float.
            ans = (x_val * y_val) // math.gcd(x_val, y_val)
            
        # 5. Return exclusively raw text digits
        return Response(content=str(ans), media_type="text/plain")
        
    except Exception:
        return Response(content="NaN", media_type="text/plain")
