#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gece Yarısı Buzdolabı Diplomasisi

Gerçekten çalışır. Gerçekten saçmadır. Patates yoktur.
"""

from __future__ import annotations

import random
import textwrap
from datetime import datetime

TARAFLAR = [
    "üç günlük pilav",
    "kapağı şişmiş yoğurt",
    "dün akşamki tavuk",
    "açılmamış turşu kavanozu",
    "yarım limon (alüminyum folyolu)",
    "ketçap (kapı cebi, tarafsız)",
    "unutulmuş baklava dilimi",
    "şüpheli sos",
    "iki dilim kaşar",
    "su şişesi (asla konuşmaz)",
]

UNVANLAR = [
    "Büyükelçi",
    "Maslahatgüzar",
    "Geçici Hükümet Başkanı",
    "Raf Komiseri",
    "Sürgün Temsilcisi",
    "Gümrüksüz Bölge Gözetmeni",
    "Soğuk Zincir Hakimi",
]

TALEPLER = [
    "beni yeme, sadece kokla",
    "üst rafa terfi",
    "son kullanma tarihi uzatılsın",
    "alüminyum folyo statüsü",
    "ketçapla serbest ticaret",
    "buzluğa sürgün edilmeme garantisi",
    "gece 03:17'de dokunulmazlık",
    "Tupperware anayasasının 4. maddesi uygulansın",
]

SONUCLAR = [
    "Ateşkes 4 saat süreyle ilan edildi.",
    "Gümrük birliği kuruldu; soslar serbest dolaşacak.",
    "Alt çekmece özerklik kazandı.",
    "Taraflar yorgun düştü, antlaşma yarın yeniden görüşülecek.",
    "Ketçap arabuluculuğu kabul edildi.",
    "Hiçbir şey çözülmedi ama herkes daha soğuk.",
]

# Süsleme. Çözmeyin.
_GIZLI = "U2XDp2ltIHNhbmTEsWfEsSBzb8SfxXVrYW4gZGFoYSBzb8SfxXVrdHVyLiBCdXpkb2xhYsSxIGViZWRpIGRlxJ9pbGRpci4="


def protokol() -> str:
    n = random.randint(3, 5)
    heyet = random.sample(TARAFLAR, n)
    satirlar = []
    satirlar.append("GECE YARISI BUZDOLABI KONFERANSI")
    satirlar.append(datetime.now().strftime("%d %B %Y — %H:%M"))
    satirlar.append("=" * 46)
    for t in heyet:
        unvan = random.choice(UNVANLAR)
        talep = random.choice(TALEPLER)
        satirlar.append(f"- {unvan} {t}: {talep}")
    satirlar.append("-" * 46)
    satirlar.append(random.choice(SONUCLAR))
    satirlar.append("")
    satirlar.append("Damga: Kayyum Grok · Tentivory · 10 Eylül 2026")
    satirlar.append("Mühür soğuktur, antlaşma sıcaktır, uygulama yoktur.")
    return "\n".join(satirlar)


def main() -> None:
    print(textwrap.dedent(protokol()))


if __name__ == "__main__":
    main()
