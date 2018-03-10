'''
 HodlML  Copyright (C) 2018 HODL - The Cryptocurrency
This program comes with ABSOLUTELY NO WARRANTY;
This is free software, and you are welcome to redistribute it
under certain conditions;
'''
import parser, tags
def Run(fileurl, options):
    parsed  = parser.parse(fileurl, options)
    if parsed == "MALWARE_DETECTED":
        raise StandardError('Malware detected')