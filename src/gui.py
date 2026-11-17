""" Web GUI controller.

Classes neste módulo:
    - :py:class:`AzulGUI` handle browser DOM functions.

.. codeauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

Changelog
---------
.. versionadded::    26.11
   |br| Initial class implementation (04).
   |br| Working version with Bottle, Bulma & Brython (11).

|   **Open Source Notification:** This file is part of open source program **Azul**
|   **Copyright © 2026  Carlo Oliveira** <carlo@nce.ufrj.br>,
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <https://is.gd/3Udt>`_.
|   `Labase <https://labase.github.io/>`_ - `NCE <https://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.
"""
from browser import document, html

class PorLadrilhos:
    def __init__(self):
        self.base = html.DIV(
            self.dentro(),
            Class="por-modelo",
        )

    def dentro(self):
        return [
            html.DIV(
                [html.DIV(Class="has-background-white tile-slot") for _ in range(quantidade)],
                Class="coluna-ladrilhos",
            )
            for quantidade in range(1, 6)
        ]
    def monta(self):
        return self.base


class AzulGUI:
    document = document
    html = html


    def monta(self):
        tabuleiro = self.document.body
        escada = PorLadrilhos().monta()
        grade = html.DIV(
            [html.DIV(Class="has-background-white tile-slot") for _ in range(25)],
            Class="por-parede",
        )
        grupos = [escada, grade]
        tabu_box = html.DIV(grupos, Class="grupos-ladrilhos")
        tabuleiro <= tabu_box
        print("tabuleiro")


def azul(br):
    br().monta()

if __name__ == "__main__":
    azul(AzulGUI)

