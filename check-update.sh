#!/bin/sh
curl "https://github.com/midori-browser/core/releases" 2>/dev/null |grep "tag/v" |sed -e 's,.*tag/v,,;s,\".*,,;' |head -n1


