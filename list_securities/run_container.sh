#!/bin/bash

docker run -it --rm \
    --name=list_securities \
    finances/list_securities $@
