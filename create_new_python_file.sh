#!/bin/bash
echo "#!/usr/bin/env python" > new_file.py
echo "# -*- coding:utf-8 -*-" >> new_file.py
echo "#-----------------------------------------------------------------------------" >> new_file.py
echo "# Purpose: " >> new_file.py
#echo -n "// Date: " >> new_file.py; date "+%Y/%m/%d %a" >> new_file.py
echo "# Date: `date '+%Y/%m/%d %a'`" >> new_file.py
echo "#-----------------------------------------------------------------------------" >> new_file.py
echo " " >> new_file.py
