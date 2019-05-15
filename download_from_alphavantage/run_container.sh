#!/bin/bash

docker run -it --rm \
    --name=download_from_alphavantage \
    -v $(pwd -P)/market_data:/market_data \
    finances/download_from_alphavantage $@
