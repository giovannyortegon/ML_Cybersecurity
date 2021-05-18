#!/usr/bin/env python3
import os
import pefile

notepad = pefile.PE("nppx64.exe", fast_load=True)
dbgRVA = notepad.OPTIONAL_HEADER.DATA_DIRECTORY[6].VirtualAddress
imgver = notepad.OPTIONAL_HEADER.MajorImageVersion
expRVA = notepad.OPTIONAL_HEADER.DATA_DIRECTORY[0].VirtualAddress
iat = notepad.OPTIONAL_HEADER.DATA_DIRECTORY[12].VirtualAddress
sections = notepad.FILE_HEADER.NumberOfSections
dll = notepad.OPTIONAL_HEADER.DllCharacteristics

print("Notepad PE info: \n")
print("Image Version: ", imgver)
print("Export RVA: ", expRVA)
print("Import Address Table: ", iat)
print("Number of Sections: ", sections)
print("Dynamic linking libraries: ", dll)
