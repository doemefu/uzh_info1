#!/usr/bin/env python3


def transform_string(s):
    colon = s.find(":")
    return s[:colon].lower() + s[colon:].upper()

