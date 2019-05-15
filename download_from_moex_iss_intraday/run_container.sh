#!/bin/bash

docker run -d \
    --name=download_from_moex_iss_intraday \
    --restart unless-stopped \
    -v $(pwd -P)/market_data:/market_data \
    finances/download_from_moex_iss_intraday
