#!/bin/bash

docker run -d \
    --name=download_from_alphavantage_daily \
    --restart unless-stopped \
    -v $(pwd -P)/market_data:/market_data \
    finances/download_from_alphavantage_daily
