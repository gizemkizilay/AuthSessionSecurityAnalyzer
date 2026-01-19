#!/bin/bash
echo "--- Auth Session Security Analyzer Başlatılıyor ---"
# Önce testleri çalıştır
python3 src/test_main.py
# Sonra ana programı başlat
python3 src/main.py
