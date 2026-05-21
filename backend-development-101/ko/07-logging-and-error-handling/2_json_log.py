# 2_json_log.py
import json
import logging
import sys


class JsonFmt(logging.Formatter):
    def format(self, r):
        return json.dumps({"level": r.levelname, "msg": r.getMessage()})
h = logging.StreamHandler(sys.stdout)
h.setFormatter(JsonFmt())
logging.basicConfig(handlers=[h], level=logging.INFO)
logging.info("hello")
