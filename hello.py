#!/usr/bin/env python3

import os
import json


# PRINT OUT ALL ENV VARIABLES AS PLAIN TEXT
'''
print("Content-Type: text/plain")
print()
print(os.environ)
'''
'''
# PRINT OUT ALL ENV VARIABLES AS JSON
print("Content-Type: application/json")
print()
print(json.dumps(dict(os.environ), indent=2))
'''
'''
# PRINT QUERY PARAMETER DATA IN HTML
print("Content-Type: text/html")
print()
print(f"<p>QUERY_STRING={os.environ['QUERY_STRING']}</p>")
'''

# PRINT USER DATA INFO 
print("Content-Type: text/html")
print()
print(f"<p>USER BROWSER={os.environ['HTTP_USER_AGENT']}</p>")