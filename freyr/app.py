"""
Freyr - A Free stock API
"""
import time
from fastapi import FastAPI, Request
from freyr.services.requests import req_data, req_yfinance_data
from freyr.utils.exception import UnicornException
from fastapi.responses import JSONResponse
from freyr.utils.logging import create_logger

# Start FastAPI
app = FastAPI()

# Register log system
logger = create_logger("requests", "INFO")


@app.get("/")
async def main():
    return "Hiho! Visit https://github.com/gutogirardon!"


@app.get("/major-indexes")
async def major(request: Request):
    logger.info(F"NewApiRequest: /major-indexes - Client: {request.client.host}")
    result = req_data()
    return result


@app.get("/stocks/{ticker}/{period}/{interval}")
async def stocks(request: Request, ticker, period="1d", interval="1d"):
    """
    Get ticker finance information

    :param request:
    :param ticker:
    :param period: 1d, 5d , 7d, 1mo
    :param interval: 1m, 2m, 5m, 15m, 30m, 60m, 1d, 5d, 1wk, 1mo
    :return: result
    """
    logger.info(F"NewApiRequest: /stocks/{ticker} - Client: {request.client.host}")
    result = req_yfinance_data(ticker, period, interval)
    return result


@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={
            "message": f"Oops! {exc.name}! or we did something wrong."
        },
    )


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    """
    Middleware put request time in headers
    :param request:
    :param call_next:
    :return:
    """
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
